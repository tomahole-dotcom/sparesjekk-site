from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SYSTEM_CSS = '/design-v45.css?v=20260925-r82'

ROUTES = {
    'forbrukslan.html': {'section':'[data-consumer-hub-intent="v1"]','href':'/sjekk/forbrukslan/?intent=nytt-lan&origin=forbrukslan-hub','title':'Jeg vurderer et nytt forbrukslån','cta':'Se alternativer og samarbeidspartnere →','context':'consumer_hub_new_v2'},
    'omstartslan.html': {'section':'[data-restart-hub-intent="v1"]','href':'/sjekk/omstartslan/?intent=sikkerhet&origin=omstartslan-hub','title':'Jeg eier bolig og vurderer sikkerhet i boligen','cta':'Se alternativer og samarbeidspartnere →','context':'restart_hub_security_v2'},
    'kredittkort.html': {'section':'[data-card-hub-intent="v1"]','href':'/sjekk/kredittkort/#samarbeidspartnere','title':'Jeg skal velge eller bytte kredittkort','cta':'Se kort og samarbeidspartnere →','context':'card_hub_choose_v2'},
}

def version_css(soup):
    if not soup.head: return
    links=soup.find_all('link',href=lambda x:isinstance(x,str) and 'design-v45.css' in x)
    if links:
        links[0]['href']=SYSTEM_CSS
        for extra in links[1:]: extra.decompose()
    else:
        soup.head.append(soup.new_tag('link',rel='stylesheet',href=SYSTEM_CSS))

for filename,cfg in ROUTES.items():
    path=ROOT/filename
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    section=soup.select_one(cfg['section'])
    if not section: raise SystemExit(f'Missing canonical intent section: {filename}')
    cards=section.select('.decision-actions > a')
    if len(cards)!=3: raise SystemExit(f'Expected exactly 3 decision cards: {filename}')
    primary=cards[0]
    primary['href']=cfg['href']; primary['data-revenue-event']='commercial_route'; primary['data-revenue-context']=cfg['context']; primary['data-direct-conversion']='v2'
    strong=primary.find('strong'); span=primary.find('span')
    if not strong or not span: raise SystemExit(f'Malformed primary decision card: {filename}')
    strong.string=cfg['title']; span.string=cfg['cta']
    for duplicate in soup.select('[data-conversion-bridge]'): duplicate.decompose()
    version_css(soup)
    path.write_text(str(soup),encoding='utf-8')

# The contrast fix lives in design-v45.css. Version it on every HTML page so
# production cannot mix new markup with a stale cached stylesheet.
for path in ROOT.rglob('*.html'):
    if any(x in path.parts for x in ('.git','release')): continue
    text=path.read_text(encoding='utf-8'); soup=BeautifulSoup(text,'html.parser'); version_css(soup)
    new=str(soup)
    if new!=text: path.write_text(new,encoding='utf-8')

print('CATEGORY CONVERSION ROUTES PASS: one-click commercial routes on forbrukslan, omstartslan and kredittkort; duplicate bridges removed; r82 CSS versioned sitewide')
