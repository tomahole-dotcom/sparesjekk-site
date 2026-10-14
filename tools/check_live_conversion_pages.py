#!/usr/bin/env python3
"""Check public conversion URLs after deployment; no third-party affiliate requests."""
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys

BASE = "https://sparesjekk.no"
PATHS = [
    "/",
    "/ta-sparesjekken.html",
    "/gjeldssjekk.html",
    "/sjekk/forbrukslan/",
    "/sjekk/refinansiering/",
    "/sjekk/kredittkort/",
    "/sjekk/omstartslan/",
]
failures = []
for path in PATHS:
    url = BASE + path
    try:
        request = Request(url, headers={"User-Agent": "Sparesjekk-Deployment-QA/1.0"})
        with urlopen(request, timeout=15) as response:
            status = response.status
            destination = response.geturl()
            ok = status == 200 and destination.startswith(BASE)
            print(f"{'PASS' if ok else 'FAIL'} {status} {url} -> {destination}")
            if not ok:
                failures.append(url)
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"FAIL {url}: {exc}")
        failures.append(url)

if failures:
    print(f"Deployment QA failed: {len(failures)} unavailable conversion URLs.", file=sys.stderr)
    sys.exit(1)
print("Deployment QA passed.")
