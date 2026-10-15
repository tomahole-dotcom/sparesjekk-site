#!/usr/bin/env python3
"""Production smoke test for existing Sparesjekk conversion funnels (read-only)."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys

BASE = "https://sparesjekk.no"
PAGES = {
    "/": "Få bedre kontroll på pengene dine",
    "/ta-sparesjekken.html": "Ta Sparesjekken",
    "/gjeldssjekk.html": "Gjeldssjekken",
    "/sjekk/forbrukslan/": "Sjekk om gjelden din kan få bedre vilkår",
    "/sjekk/kredittkort/": "Finn riktig vei til kredittkort",
}
errors = []
for path, marker in PAGES.items():
    url = BASE + path
    try:
        with urlopen(Request(url, headers={"User-Agent": "Sparesjekk-Growth-QA/1.0"}), timeout=15) as response:
            body = response.read().decode("utf-8", errors="replace")
            ok = response.status == 200 and marker.casefold() in body.casefold()
            print(f"{'PASS' if ok else 'FAIL'} {response.status} {url}")
            if not ok:
                errors.append(url)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"FAIL {url}: {exc}")
        errors.append(url)
if errors:
    sys.exit(f"Conversion smoke test failed for {len(errors)} pages.")
print("All existing conversion paths passed.")
