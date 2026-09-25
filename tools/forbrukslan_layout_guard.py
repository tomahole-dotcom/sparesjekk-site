from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'forbrukslan.html'
soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')

# The top intent chooser is the canonical conversion decision on this page.
# Do not repeat the same new-loan/debt choice immediately after benefits.
for node in soup.select('[data-conversion-bridge="forbrukslan-v1"], .consumer-conversion-bridge'):
    node.decompose()

intent = soup.select_one('#consumer-hub-intent[data-consumer-hub-intent="v1"]')
if not intent:
    raise SystemExit('Canonical forbrukslan intent chooser missing')

choices = intent.select('.decision-actions > a')
if len(choices) != 3:
    raise SystemExit(f'Expected exactly 3 canonical forbrukslan choices, found {len(choices)}')

# Protect the hierarchy: hero -> one decision block -> benefits -> editorial guide.
benefits = soup.select_one('.premium-benefits')
article = soup.select_one('#forbrukslan-hub-guide')
if not benefits or not article:
    raise SystemExit('Forbrukslan hierarchy anchors missing')

path.write_text(str(soup), encoding='utf-8')

# Global header-logo regression guard.
# system_repair.py intentionally inserts the canonical SVG as an <img> inside
# a.logo. Older brand CSS also paints the same SVG as the anchor background.
# Disable that legacy background whenever the canonical <img> is present so
# exactly one logo is rendered on every page.
logo_pages = 0
for html_path in ROOT.rglob('*.html'):
    if any(part in html_path.parts for part in ('.git', 'release')):
        continue
    doc = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    logo = doc.select_one('header.header a.logo')
    if not logo:
        continue
    img = logo.find('img', src=lambda value: isinstance(value, str) and 'sparesjekk-logo-blue.svg' in value)
    if not img:
        continue
    existing = logo.get('style', '').strip()
    guard = 'background:none!important;background-image:none!important;'
    if guard not in existing:
        logo['style'] = (existing + (';' if existing and not existing.endswith(';') else '') + guard)
        html_path.write_text(str(doc), encoding='utf-8')
    logo_pages += 1

print(f'FORBRUKSLAN LAYOUT GUARD PASS: redundant conversion bridge removed; single-logo guard applied to {logo_pages} pages')
