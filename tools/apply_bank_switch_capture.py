from pathlib import Path

PAGE = Path('bor-jeg-bytte-bank.html')
if not PAGE.exists():
    raise SystemExit('Missing bor-jeg-bytte-bank.html')

html = PAGE.read_text(encoding='utf-8')
required = [
    'id="bankSwitchCheck"',
    'id="strongCta"',
    'href="sjekk/boliglan/"',
    'data-revenue-event="commercial_route"',
    'id="softCta"',
    'href="min-rente-vs-markedet.html"',
    'bank_switch_check_complete',
    'strongSignals',
    'softSignals',
    'G-XYRPP78DJ5',
]
missing = [x for x in required if x not in html]
if missing:
    raise SystemExit('Bank switch capture missing markers: ' + ', '.join(missing))

# Idempotent transform marker. The page itself is the source artifact; this tool
# validates it and marks the generated output so production/QA use one stable step.
marker = '<meta content="traffic-bankbytte-capture-v1" name="sparesjekk-transform"/>'
if marker not in html:
    html = html.replace('</head>', marker + '</head>', 1)
    PAGE.write_text(html, encoding='utf-8')

print('Bank switch Traffic Capture applied')
