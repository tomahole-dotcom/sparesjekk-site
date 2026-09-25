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
print('FORBRUKSLAN LAYOUT GUARD PASS: redundant conversion bridge removed')
