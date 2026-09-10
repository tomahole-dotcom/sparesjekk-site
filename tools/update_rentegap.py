#!/usr/bin/env python3
"""Update Sparesjekk's rate data from official Norwegian sources.

Safety defaults:
- Dry-run unless --write is supplied.
- Refuses to overwrite data if expected source values cannot be identified.
- No scheduler is configured here.

Sources:
- Norges Bank policy-rate page (official public page; current decision).
- SSB PxWeb API v2 tables 10729, 10745 and 11018.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "rentegap.json"
UA = "Sparesjekk-rate-updater/1.0 (+https://sparesjekk.no/)"
SSB_BASE = "https://data.ssb.no/api/pxwebapi/v2/tables"
NB_POLICY_URL = "https://www.norges-bank.no/tema/pengepolitikk/Styringsrenten/"


def get_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json;q=0.9,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8")


def get_json(url: str):
    return json.loads(get_text(url))


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"\s+", " ", s).strip()


def first_float(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, list):
        for item in value:
            if isinstance(item, (int, float)):
                return float(item)
    raise ValueError("No numeric value returned")


def policy_rate() -> float:
    html = get_text(NB_POLICY_URL)
    plain = re.sub(r"<[^>]+>", " ", html)
    plain = re.sub(r"\s+", " ", plain)
    # Search close to the Norwegian label so unrelated percentages are ignored.
    m = re.search(r"styringsrente.{0,220}?([0-9]{1,2}[,.][0-9]{1,3})\s*%", plain, flags=re.I)
    if not m:
        # English label is retained as a fallback if the page template changes language.
        m = re.search(r"policy rate.{0,220}?([0-9]{1,2}[,.][0-9]{1,3})\s*%", plain, flags=re.I)
    if not m:
        raise RuntimeError("Could not identify policy rate on Norges Bank's official page")
    v = float(m.group(1).replace(",", "."))
    if not 0 <= v <= 20:
        raise RuntimeError(f"Implausible policy rate: {v}")
    return v


def category_map(meta, dim_id):
    dim = meta["dimension"][dim_id]
    labels = dim.get("category", {}).get("label", {})
    return {str(code): str(label) for code, label in labels.items()}


def match_code(labels: dict[str, str], required: list[str], forbidden: list[str] | None = None) -> str:
    forbidden = forbidden or []
    candidates = []
    for code, label in labels.items():
        n = norm(label)
        if all(norm(x) in n for x in required) and not any(norm(x) in n for x in forbidden):
            candidates.append((code, label))
    if len(candidates) != 1:
        raise RuntimeError(f"Expected one category for {required}; found {candidates}")
    return candidates[0][0]


def find_dim(meta, words: list[str]) -> str:
    for dim_id in meta.get("id", []):
        label = norm(meta["dimension"][dim_id].get("label", dim_id))
        if any(norm(w) in label for w in words):
            return dim_id
    raise RuntimeError(f"Could not find dimension matching {words} in table metadata")


def ssb_latest(table: str, value_requirements: dict[str, tuple[list[str], list[str]]]):
    meta_url = f"{SSB_BASE}/{table}/metadata?lang=no"
    meta = get_json(meta_url)
    time_dim = find_dim(meta, ["tid", "maaned", "month"])
    params = []
    for dim_id in meta.get("id", []):
        if dim_id == time_dim:
            params.append((f"valueCodes[{dim_id}]", "top(1)"))
            continue
        label = norm(meta["dimension"][dim_id].get("label", dim_id))
        matched = False
        for key, (required, forbidden) in value_requirements.items():
            if norm(key) in label:
                code = match_code(category_map(meta, dim_id), required, forbidden)
                params.append((f"valueCodes[{dim_id}]", code))
                matched = True
                break
        if not matched:
            # Contents/statistics dimensions normally contain one value; select all safely.
            labels = category_map(meta, dim_id)
            if len(labels) == 1:
                params.append((f"valueCodes[{dim_id}]", next(iter(labels))))
            else:
                raise RuntimeError(f"Unhandled dimension {dim_id!r} ({label!r}) in table {table}")
    params.append(("outputFormat", "json-stat2"))
    data_url = f"{SSB_BASE}/{table}/data?" + urllib.parse.urlencode(params)
    data = get_json(data_url)
    period_codes = list(data["dimension"][time_dim]["category"]["index"].keys())
    if len(period_codes) != 1:
        raise RuntimeError(f"Expected one period from SSB table {table}, got {period_codes}")
    return first_float(data.get("value")), period_codes[0], data_url


def fetch_all():
    # 10729: new loans secured on dwellings, households.
    new_rate, p1, u1 = ssb_latest("10729", {
        "lanetype": (["pant i bolig"], []),
        "type of loan": (["secured on dwellings"], []),
        "sektor": (["hushold"], []),
        "sector": (["household"], []),
    })
    # 10745: outstanding loans secured on dwellings, households.
    outstanding_rate, p2, u2 = ssb_latest("10745", {
        "lanetype": (["pant i bolig"], []),
        "type of loan": (["secured on dwellings"], []),
        "sektor": (["hushold"], []),
        "sector": (["household"], []),
    })
    # 11018: total household deposits.
    deposit_rate, p3, u3 = ssb_latest("11018", {
        "innskuddstype": (["totale innskudd"], []),
        "type of deposit": (["total deposits"], []),
        "sektor": (["hushold"], []),
        "sector": (["household"], []),
    })
    periods = {p1, p2, p3}
    if len(periods) != 1:
        raise RuntimeError(f"SSB tables do not share the same latest period: {sorted(periods)}")
    return {
        "policy_rate": policy_rate(),
        "new_mortgage_rate": new_rate,
        "outstanding_mortgage_rate": outstanding_rate,
        "deposit_rate": deposit_rate,
        "reference_period": p1.replace("M", "-") if "M" in p1 else p1,
        "api_urls": [u1, u2, u3],
    }


def build_payload(old, live):
    p = dict(old)
    p.update({k: live[k] for k in ("policy_rate", "new_mortgage_rate", "outstanding_mortgage_rate", "deposit_rate", "reference_period")})
    p["checked_date"] = date.today().isoformat()
    p["metrics"] = {
        "new_mortgage_minus_policy_pp": round(live["new_mortgage_rate"] - live["policy_rate"], 2),
        "outstanding_mortgage_minus_policy_pp": round(live["outstanding_mortgage_rate"] - live["policy_rate"], 2),
        "outstanding_minus_new_mortgage_pp": round(live["outstanding_mortgage_rate"] - live["new_mortgage_rate"], 2),
        "policy_minus_deposit_pp": round(live["policy_rate"] - live["deposit_rate"], 2),
    }
    p["machine_sources"] = {
        "norges_bank": NB_POLICY_URL,
        "ssb_api": live["api_urls"],
    }
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="write validated values to data/rentegap.json")
    ap.add_argument("--json", action="store_true", help="print candidate payload as JSON")
    args = ap.parse_args()

    old = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    live = fetch_all()
    candidate = build_payload(old, live)
    changed = any(candidate.get(k) != old.get(k) for k in ("policy_rate", "new_mortgage_rate", "outstanding_mortgage_rate", "deposit_rate", "reference_period"))

    print("Official rate source check: PASS")
    print(f"Policy rate: {candidate['policy_rate']:.2f}%")
    print(f"New mortgages: {candidate['new_mortgage_rate']:.2f}% ({candidate['reference_period']})")
    print(f"Outstanding mortgages: {candidate['outstanding_mortgage_rate']:.2f}%")
    print(f"Household deposits: {candidate['deposit_rate']:.2f}%")
    print(f"Changed vs stored data: {'YES' if changed else 'NO'}")

    if args.json:
        print(json.dumps(candidate, ensure_ascii=False, indent=2))
    if args.write:
        DATA_FILE.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE {DATA_FILE.relative_to(ROOT)}")
    else:
        print("DRY RUN only. Use --write after validation to update the stored dataset.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"RATE UPDATE FAILED: {e}", file=sys.stderr)
        raise SystemExit(1)
