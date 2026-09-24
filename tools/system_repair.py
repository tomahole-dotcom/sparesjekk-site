from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
NAV = [
    ('/boliglan.html','Boliglån'),('/forbrukslan.html','Forbrukslån'),('/omstartslan.html','Omstartslån'),
    ('/kredittkort.html','Kredittkort'),('/problemloser.html','Problemløser'),
    ('/tilbudssjekk-refinansiering.html','Tilbudssjekken'),('/guider.html','Guider'),('/om.html','Om oss')
]
RATE_ID='2026-09-24'
RATE_HTML='''<section class="current-rate-event" data-current-rate-event="2026-09-24"><div><p class="eyebrow">RENTEBESLUTNING 24. SEPTEMBER</p><h2>Norges Bank hever styringsrenten til 4,50 %</h2><p>Styringsrenten er satt opp fra 4,25 til 4,50 prosent. Har du lån, er dette et naturlig tidspunkt å sjekke renten du faktisk betaler og sammenligne alternativer.</p></div><div class="rate-event-actions"><a class="cta" href="/min-rente-vs-markedet.html">Sjekk renten min →</a><a class="secondary-cta" href="/boliglanskalkulator-renteforskjell.html">Se hva renteforskjellen betyr →</a></div><p class="rate-event-source">Kilde: Norges Bank, rentebeslutning 24.09.2026.</p></section>'''
CARD_BRIDGE_HTML='''<section class="conversion-bridge card-conversion-bridge" data-conversion-bridge="kredittkort-v1"><div><p class="eyebrow">KLAR FOR NESTE STEG?</p><h2>Finn riktig vei før du velger kort</h2><p>Du trenger ikke lese hele guiden først. Velg det som passer situasjonen din nå – eller fortsett nedover hvis du vil forstå detaljene.</p></div><div class="conversion-bridge-actions"><a class="cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_match_v1" href="/kredittkort-match.html">Finn kort som passer bruken min →</a><a class="secondary-cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_compare_v1" href="/sjekk/kredittkort/">Se kort og samarbeidspartnere →</a></div><p class="conversion-bridge-note">Har du kredittkortgjeld som blir stående? <a href="/gjeldssjekk.html?src=kredittkort-bridge">Start heller med Gjeldssjekken.</a></p></section>'''

def ensure_css(soup):
    if soup.head and not soup.find('link', href=lambda x:isinstance(x,str) and 'design-v45.css' in x):
        soup.head.append(soup.new_tag('link', rel='stylesheet', href='/design-v45.css?v=20260924-system'))

def canonical_nav(soup):
    nav=soup.select_one('header.header .topnav')
    if not nav: return False
    nav.clear()
    for href,label in NAV:
        a=soup.new_tag('a', href=href); a.string=label; nav.append(a)
    return True

def add_rate_notice(path,soup):
    if path.name not in ('index.html','boliglan.html') or path.parent != ROOT: return
    for old in soup.select('[data-current-rate-event]'): old.decompose()
    frag=BeautifulSoup(RATE_HTML,'html.parser').section
    anchor=soup.select_one('.visual-hero') if path.name=='index.html' else soup.select_one('.premium-hero')
    if anchor: anchor.insert_after(frag)
    else:
        main=soup.select_one('main')
        if main: main.insert(0,frag)

def repair_boliglan(path,soup):
    if path.name!='boliglan.html' or path.parent != ROOT: return
    hub=soup.select_one('.hub-editorial')
    first=soup.select_one('.decision-grid > article:first-child')
    if not hub or not first: return
    nested=list(first.find_all('section', recursive=False))
    if not nested: return
    wrap=soup.new_tag('section'); wrap['class']=['hub-followups']; wrap['data-layout-repair']='20260924'
    for sec in nested: wrap.append(sec.extract())
    hub.insert_after(wrap)

def repair_offer(path,soup):
    if path.name!='tilbudssjekk-refinansiering.html' or path.parent != ROOT: return
    main=soup.select_one('.offer-check')
    if main: main['data-layout-repair']='20260924'

def ensure_card_conversion_bridge(path,soup):
    if path.name!='kredittkort.html' or path.parent != ROOT: return
    for old in soup.select('[data-conversion-bridge="kredittkort-v1"]'): old.decompose()
    anchor=soup.select_one('.premium-benefits') or soup.select_one('#card-hub-intent')
    if not anchor: return
    frag=BeautifulSoup(CARD_BRIDGE_HTML,'html.parser').section
    anchor.insert_after(frag)

changed=0
for path in ROOT.rglob('*.html'):
    if any(x in path.parts for x in ('.git','release')): continue
    original=path.read_text(encoding='utf-8')
    soup=BeautifulSoup(original,'html.parser')
    ensure_css(soup); canonical_nav(soup); add_rate_notice(path,soup); repair_boliglan(path,soup); repair_offer(path,soup); ensure_card_conversion_bridge(path,soup)
    new=str(soup)
    if new!=original:
        path.write_text(new,encoding='utf-8'); changed+=1
print(f'SYSTEM REPAIR PASS: {changed} HTML files normalized; rate event {RATE_ID}; card conversion bridge protected')
