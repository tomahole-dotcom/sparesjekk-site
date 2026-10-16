#!/usr/bin/env python3
"""Read-only checks for conversion event instrumentation. Run from repo root."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
checks = {
    "index.html": [
        'data-home-revenue-tracking="v1"',
        'data-revenue-event="home_primary"',
        'data-revenue-event="home_debt_route"',
        'data-revenue-event="home_mortgage_route"',
        'data-revenue-event="home_card_route"',
        'data-revenue-event="home_secured_debt_route"',
        'data-revenue-event="home_rate_tool_route"',
        'data-revenue-event="home_ltv_tool_route"',
    ],
    "ta-sparesjekken.html": [
        "savings_check_start",
        "savings_check_step",
        "savings_check_result",
        "commercial_route",
        "savings_check_restart",
    ],
    "kredittkort-match.html": [
        "credit_card_match_complete",
        "gtag('event','credit_card_match_complete'",
        "gjeldssjekk.html?src=kredittkort-match",
        'data-revenue-event="credit_card_match_debt_check"',
    ],
    "gjeldssjekk.html": [
        "debt_check_start",
        "debt_check_complete",
        "debt_check_commercial_click",
    ],
}
failed = []
for name, needles in checks.items():
    path = ROOT / name
    if not path.is_file():
        failed.append(f"Missing file: {name}")
        continue
    content = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in content:
            failed.append(f"{name}: missing {needle}")
if failed:
    for message in failed:
        print("FAIL", message, file=sys.stderr)
    sys.exit(1)
print("PASS: homepage and tool funnel event markers are present.")
