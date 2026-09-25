from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SYSTEM_CSS = '/design-v45.css?v=20260925-r82'

ROUTES = {
    'forbrukslan.html': {
        'section': '[data-consumer-hub-intent="v1"]',
        'href': '/sjekk/forbrukslan/?intent=nytt-lan&origin=forbrukslan-hub',
        'title': 'Jeg vurderer et nytt forbrukslån',
        'cta': 'Se alternativer og samarbeidspartnere →',
        'context': 'consumer_hub_new_v2',
    },
    'omstartslan.html': {
        'section': '[data-restart-hub-intent="v1"]',
        'href': '/sjekk/omstartslan/?intent=sikkerhet&origin=omstartslan-hub',
        'title': 'Jeg eier bolig og vurderer sikkerhet i boligen',
        'cta': 'Se alternativer og samarbeidspartnere →',
        'context': 'restart_hub_security_v2',
    },
    'kredittkort.html': {
        'section': '[data-card-hub-intent="v1"]',
        'href': '/sjekk/kredittkort/#samarbeidspartnere',
        'title': 'Jeg skal velge eller bytte kredittkort',
        'cta': 'Se kort og samarbeidspartnere →',
        'context': 'card_hub_choose_v2',
    },
}

for filename, cfg in ROUTES.items():
    path = ROOT / filename
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    section = soup.select_one(cfg['section'])
    if not section:
        raise SystemExit(f'Missing canonical intent section: {filename}')
    cards = section.select('.decision-actions > a')
    if len(cards) < 2:
        raise SystemExit(f'Missing decision cards: {filename}')
    primary = cards[0]
    primary['href'] = cfg['href']
    primary['data-revenue-event'] = 'commercial_route'
    primary['data-revenue-context'] = cfg['context']
    primary['data-direct-conversion'] = 'v2'
    strong = primary.find('strong')
    span = primary.find('span')
    if not strong or not span:
        raise SystemExit(f'Malformed primary decision card: {filename}')
    strong.string = cfg['title']
    span.string = cfg['cta']
    # The category choice itself is now the short conversion route. Remove any
    # duplicate bridge accidentally introduced by older release logic.
    for duplicate in soup.select('[data-conversion-bridge]'):
        duplicate.decompose()
    csslinks = soup.find_all('link', href=lambda x: isinstance(x,str) and 'design-v45.css' in x)
    if csslinks:
        csslinks[0]['href'] = SYSTEM_CSS
        for extra in csslinks[1:]: extra.decompose()
    elif soup.head:
        soup.head.append(soup.new_tag('link', rel='stylesheet', href=SYSTEM_CSS))
    path.write_text(str(soup), encoding='utf-8')

print('CATEGORY CONVERSION ROUTES PASS: 3 category hubs have one-click commercial routes and no duplicate bridge')
