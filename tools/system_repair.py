from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
NAV = [('/boliglan.html','Boliglån'),('/forbrukslan.html','Forbrukslån'),('/omstartslan.html','Omstartslån'),('/kredittkort.html','Kredittkort'),('/problemloser.html','Problemløser'),('/tilbudssjekk-refinansiering.html','Tilbudssjekken'),('/guider.html','Guider'),('/om.html','Om oss')]
RATE_ID='2026-09-24'
RATE_HTML='''<section class="current-rate-event" data-current-rate-event="2026-09-24"><div><p class="eyebrow">RENTEBESLUTNING 24. SEPTEMBER</p><h2>Norges Bank hever styringsrenten til 4,50 %</h2><p>Styringsrenten er satt opp fra 4,25 til 4,50 prosent. Har du lån, er dette et naturlig tidspunkt å sjekke renten du faktisk betaler og sammenligne alternativer.</p></div><div class="rate-event-actions"><a class="cta" href="/min-rente-vs-markedet.html">Sjekk renten min →</a><a class="secondary-cta" href="/boliglanskalkulator-renteforskjell.html">Se hva renteforskjellen betyr →</a></div><p class="rate-event-source">Kilde: Norges Bank, rentebeslutning 24.09.2026.</p></section>'''
CARD_BRIDGE_HTML='''<section class="conversion-bridge card-conversion-bridge" data-conversion-bridge="kredittkort-v1"><div><p class="eyebrow">KLAR FOR NESTE STEG?</p><h2>Finn riktig vei før du velger kort</h2><p>Du trenger ikke lese hele guiden først. Velg det som passer situasjonen din nå – eller fortsett nedover hvis du vil forstå detaljene.</p></div><div class="conversion-bridge-actions"><a class="cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_match_v1" href="/kredittkort-match.html">Finn kort som passer bruken min →</a><a class="secondary-cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_compare_v1" href="/sjekk/kredittkort/">Se kort og samarbeidspartnere →</a></div><p class="conversion-bridge-note">Har du kredittkortgjeld som blir stående? <a href="/gjeldssjekk.html?src=kredittkort-bridge">Start heller med Gjeldssjekken.</a></p></section>'''
CONSUMER_BRIDGE_HTML='''<section class="conversion-bridge consumer-conversion-bridge" data-conversion-bridge="forbrukslan-v1"><div><p class="eyebrow">KLAR FOR NESTE STEG?</p><h2>Velg nytt lån eller start med gjelden du allerede har</h2><p>Skal du låne nytt, kan du gå direkte til sammenligning. Har du lån eller kredittkortgjeld fra før, er det mer nyttig å starte med samlet kostnad og rente.</p></div><div class="conversion-bridge-actions"><a class="cta" data-revenue-event="commercial_route" data-revenue-context="consumer_bridge_new_v1" href="/sjekk/forbrukslan/?intent=nytt-lan&amp;origin=forbrukslan-bridge">Se alternativer for nytt lån →</a><a class="secondary-cta" data-revenue-event="problem_route" data-revenue-context="consumer_bridge_debt_v1" href="/gjeldssjekk.html?src=forbrukslan-bridge">Sjekk gjelden min →</a></div><p class="conversion-bridge-note">Usikker på hva som er riktig? Fortsett til guiden under og se effektiv rente, gebyrer, løpetid og total kostnad før du bestemmer deg.</p></section>'''
OFFER_ROUTE_HTML='''<div class="gs-offer-route" data-offer-route="gjeldssjekk-v1"><span>Har du allerede fått et refinansieringstilbud?</span><a data-revenue-event="tool_route" data-revenue-context="gjeldssjekk_offercheck_v1" href="/tilbudssjekk-refinansiering.html?src=gjeldssjekk">Sjekk om tilbudet faktisk er bedre →</a></div>'''

def ensure_css(soup):
    if soup.head and not soup.find('link', href=lambda x:isinstance(x,str) and 'design-v45.css' in x): soup.head.append(soup.new_tag('link', rel='stylesheet', href='/design-v45.css?v=20260924-system'))

def canonical_nav(soup):
    nav=soup.select_one('header.header .topnav')
    if not nav:return
    nav.clear()
    for href,label in NAV:
        a=soup.new_tag('a',href=href);a.string=label;nav.append(a)

def add_rate_notice(path,soup):
    if path.name not in ('index.html','boliglan.html') or path.parent!=ROOT:return
    for old in soup.select('[data-current-rate-event]'):old.decompose()
    frag=BeautifulSoup(RATE_HTML,'html.parser').section;anchor=soup.select_one('.visual-hero') if path.name=='index.html' else soup.select_one('.premium-hero')
    if anchor:anchor.insert_after(frag)

def repair_boliglan(path,soup):
    if path.name!='boliglan.html' or path.parent!=ROOT:return
    hub=soup.select_one('.hub-editorial');first=soup.select_one('.decision-grid > article:first-child')
    if not hub or not first:return
    nested=list(first.find_all('section',recursive=False))
    if nested:
        wrap=soup.new_tag('section');wrap['class']=['hub-followups'];wrap['data-layout-repair']='20260924'
        for sec in nested:wrap.append(sec.extract())
        hub.insert_after(wrap)

def repair_offer(path,soup):
    if path.name!='tilbudssjekk-refinansiering.html' or path.parent!=ROOT:return
    main=soup.select_one('.offer-check')
    if main:main['data-layout-repair']='20260924'
    info=next((sec for sec in soup.select('.offer-check > section.info') if 'Har du ikke fått et konkret tilbud ennå?' in sec.get_text(' ',strip=True)),None)
    if info and info.find('p'):
        p=info.find('p');p.clear();p.append('Start med ');a=soup.new_tag('a',href='/gjeldssjekk.html?src=tilbudssjekk-no-offer');a.string='Gjeldssjekken';p.append(a);p.append(' for å få oversikt over gjeld og rente, eller bruk ');b=soup.new_tag('a',href='/refinansiering-kalkulator.html');b.string='før/etter-kalkulatoren';p.append(b);p.append(' dersom du vil sammenligne flere gjeldsposter mot et mulig nytt lån.')

def ensure_conversion_bridge(path,soup):
    bridges={'kredittkort.html':('kredittkort-v1',CARD_BRIDGE_HTML),'forbrukslan.html':('forbrukslan-v1',CONSUMER_BRIDGE_HTML)}
    if path.parent!=ROOT or path.name not in bridges:return
    bridge_id,html=bridges[path.name]
    for old in soup.select(f'[data-conversion-bridge="{bridge_id}"]'):old.decompose()
    anchor=soup.select_one('.premium-benefits')
    if anchor:anchor.insert_after(BeautifulSoup(html,'html.parser').section)

def ensure_debt_offer_route(path,soup):
    if path.name!='gjeldssjekk.html' or path.parent!=ROOT:return
    for old in soup.select('[data-offer-route="gjeldssjekk-v1"]'):old.decompose()
    ad=soup.select_one('#gsAd')
    if ad:ad.insert_after(BeautifulSoup(OFFER_ROUTE_HTML,'html.parser').div)

def expose_partner_brands(path,soup):
    matcher=soup.select_one('.revenue-matcher');cards=soup.select('.partner-card[data-partner]')
    if not matcher or not cards:return
    for old in soup.select('[data-partner-visibility="v1"]'):old.decompose()
    names=[]
    for card in cards:
        name=card.get('data-partner')
        if name and name not in names:names.append(name)
    if not names:return
    box=soup.new_tag('div');box['class']=['partner-visibility-strip'];box['data-partner-visibility']='v1'
    eye=soup.new_tag('p');eye['class']=['eyebrow'];eye.string='SAMARBEIDSPARTNERE PÅ DENNE SIDEN';box.append(eye)
    strong=soup.new_tag('strong');strong.string='Du ser hvem du kan gå videre til før du velger spor.';box.append(strong)
    p=soup.new_tag('p');p.string='Valget under sorterer bare rekkefølgen. Du sendes ikke videre før du selv trykker på en partner.';box.append(p)
    brands=soup.new_tag('div');brands['class']=['partner-brand-list']
    for name in names:
        span=soup.new_tag('span');span.string=name;brands.append(span)
    box.append(brands);matcher.insert_before(box)

changed=0
for path in ROOT.rglob('*.html'):
    if any(x in path.parts for x in ('.git','release')):continue
    original=path.read_text(encoding='utf-8');soup=BeautifulSoup(original,'html.parser')
    ensure_css(soup);canonical_nav(soup);add_rate_notice(path,soup);repair_boliglan(path,soup);repair_offer(path,soup);ensure_conversion_bridge(path,soup);ensure_debt_offer_route(path,soup);expose_partner_brands(path,soup)
    new=str(soup)
    if new!=original:path.write_text(new,encoding='utf-8');changed+=1
print(f'SYSTEM REPAIR PASS: {changed} HTML files normalized; rate event {RATE_ID}; partner visibility protected')
