from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
NAV = [('/boliglan.html','Boliglån'),('/forbrukslan.html','Forbrukslån'),('/omstartslan.html','Omstartslån'),('/kredittkort.html','Kredittkort'),('/problemloser.html','Problemløser'),('/tilbudssjekk-refinansiering.html','Tilbudssjekken'),('/guider.html','Guider'),('/om.html','Om oss')]
RATE_ID='2026-09-24'
SYSTEM_CSS='/design-v45.css?v=20260925-r80'
RATE_HTML='''<section class="current-rate-event" data-current-rate-event="2026-09-24"><div><p class="eyebrow">RENTEBESLUTNING 24. SEPTEMBER</p><h2>Norges Bank hever styringsrenten til 4,50 %</h2><p>Styringsrenten er satt opp fra 4,25 til 4,50 prosent. Har du lån, er dette et naturlig tidspunkt å sjekke renten du faktisk betaler og sammenligne alternativer.</p></div><div class="rate-event-actions"><a class="cta" href="/min-rente-vs-markedet.html">Sjekk renten min →</a><a class="secondary-cta" href="/boliglanskalkulator-renteforskjell.html">Se hva renteforskjellen betyr →</a></div><p class="rate-event-source">Kilde: Norges Bank, rentebeslutning 24.09.2026.</p></section>'''
HOME_FAST_HTML='''<section class="home-fast-routes" data-home-fast-routes="v1"><div class="section-head"><p class="eyebrow">VET DU ALLEREDE HVA DU VIL SJEKKE?</p><h2>Gå raskt til alternativer og samarbeidspartnere</h2><p>Velg område og gå direkte til siden der du kan se relevante alternativer. Du bestemmer selv om du vil gå videre til en samarbeidspartner.</p></div><div class="home-fast-grid"><a class="home-fast-card" data-revenue-event="home_fast_route" data-revenue-context="home_fast_mortgage" href="/boliglan.html#sammenlign"><small>BOLIGLÅN</small><strong>Sjekk rente og alternativer</strong><span>Gå til boliglån →</span></a><a class="home-fast-card" data-revenue-event="home_fast_route" data-revenue-context="home_fast_refi" href="/sjekk/forbrukslan/?intent=refinansiering&amp;origin=homepage-fast"><small>REFINANSIERING</small><strong>Se alternativer for dyr gjeld</strong><span>Se refinansiering →</span></a><a class="home-fast-card" data-revenue-event="home_fast_route" data-revenue-context="home_fast_consumer" href="/sjekk/forbrukslan/?intent=nytt-lan&amp;origin=homepage-fast"><small>FORBRUKSLÅN</small><strong>Se aktuelle samarbeidspartnere</strong><span>Se forbrukslån →</span></a><a class="home-fast-card" data-revenue-event="home_fast_route" data-revenue-context="home_fast_credit" href="/sjekk/kredittkort/#samarbeidspartnere"><small>KREDITTKORT</small><strong>Se kort og sammenligningstjenester</strong><span>Se kredittkort →</span></a></div><div class="home-fast-help"><span>Usikker på hva som passer situasjonen din?</span><a href="/ta-sparesjekken.html?src=homepage-fast-help">Ta Sparesjekken →</a></div><p class="home-fast-disclosure">ANNONSE / REKLAME – enkelte sider inneholder samarbeidspartnere. Sparesjekk kan motta provisjon dersom du går videre.</p></section>'''
CARD_BRIDGE_HTML='''<section class="conversion-bridge card-conversion-bridge" data-conversion-bridge="kredittkort-v1"><div><p class="eyebrow">KLAR FOR NESTE STEG?</p><h2>Finn riktig vei før du velger kort</h2><p>Du trenger ikke lese hele guiden først. Velg det som passer situasjonen din nå – eller fortsett nedover hvis du vil forstå detaljene.</p></div><div class="conversion-bridge-actions"><a class="cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_match_v1" href="/kredittkort-match.html">Finn kort som passer bruken min →</a><a class="secondary-cta" data-revenue-event="commercial_route" data-revenue-context="card_bridge_compare_v1" href="/sjekk/kredittkort/">Se kort og samarbeidspartnere →</a></div><p class="conversion-bridge-note">Har du kredittkortgjeld som blir stående? <a href="/gjeldssjekk.html?src=kredittkort-bridge">Start heller med Gjeldssjekken.</a></p></section>'''
CONSUMER_BRIDGE_HTML='''<section class="conversion-bridge consumer-conversion-bridge" data-conversion-bridge="forbrukslan-v1"><div><p class="eyebrow">KLAR FOR NESTE STEG?</p><h2>Velg nytt lån eller start med gjelden du allerede har</h2><p>Skal du låne nytt, kan du gå direkte til sammenligning. Har du lån eller kredittkortgjeld fra før, er det mer nyttig å starte med samlet kostnad og rente.</p></div><div class="conversion-bridge-actions"><a class="cta" data-revenue-event="commercial_route" data-revenue-context="consumer_bridge_new_v1" href="/sjekk/forbrukslan/?intent=nytt-lan&amp;origin=forbrukslan-bridge">Se alternativer for nytt lån →</a><a class="secondary-cta" data-revenue-event="problem_route" data-revenue-context="consumer_bridge_debt_v1" href="/gjeldssjekk.html?src=forbrukslan-bridge">Sjekk gjelden min →</a></div><p class="conversion-bridge-note">Usikker på hva som er riktig? Fortsett til guiden under og se effektiv rente, gebyrer, løpetid og total kostnad før du bestemmer deg.</p></section>'''
OFFER_ROUTE_HTML='''<div class="gs-offer-route" data-offer-route="gjeldssjekk-v1"><span>Har du allerede fått et refinansieringstilbud?</span><a data-revenue-event="tool_route" data-revenue-context="gjeldssjekk_offercheck_v1" href="/tilbudssjekk-refinansiering.html?src=gjeldssjekk">Sjekk om tilbudet faktisk er bedre →</a></div>'''
RESTART_END_HTML='''<section class="revenue-next-step restart-next-step" data-restart-end-flow="v1"><p class="eyebrow">NESTE STEG</p><h2>Klar til å vurdere omstartslån?</h2><p>Har du kontroll på dagens gjeld, risikoen ved pant og samlet kostnad, kan du gå videre. Hvis ikke, start med før/etter-regnestykket.</p><div class="conversion-bridge-actions"><a class="cta" data-revenue-context="restart_end_commercial_v1" data-revenue-event="commercial_route" href="sjekk/omstartslan/?intent=sikkerhet&amp;origin=omstartslan-end">Se relevante alternativer →</a><a class="secondary-cta" data-revenue-context="restart_end_calc_v1" data-revenue-event="tool_route" href="refinansiering-kalkulator.html">Regn før og etter →</a></div><p class="partner-note">ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.</p></section>'''

def ensure_css(soup):
    if not soup.head:return
    links=soup.find_all('link',href=lambda x:isinstance(x,str) and 'design-v45.css' in x)
    if links:
        links[0]['href']=SYSTEM_CSS
        for extra in links[1:]:extra.decompose()
    else:soup.head.append(soup.new_tag('link', rel='stylesheet', href=SYSTEM_CSS))

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

def ensure_home_fast_routes(path,soup):
    if path.name!='index.html' or path.parent!=ROOT:return
    for old in soup.select('[data-home-fast-routes]'):old.decompose()
    rate=soup.select_one('[data-current-rate-event="2026-09-24"]');start=soup.select_one('#start');frag=BeautifulSoup(HOME_FAST_HTML,'html.parser').section
    if rate:rate.insert_after(frag)
    elif start:start.insert_before(frag)

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
    box=soup.new_tag('div');box['class']=['partner-visibility-strip'];box['data-partner-visibility']='v1';box['id']='samarbeidspartnere'
    eye=soup.new_tag('p');eye['class']=['eyebrow'];eye.string='SAMARBEIDSPARTNERE PÅ DENNE SIDEN';box.append(eye)
    strong=soup.new_tag('strong');strong.string='Du ser hvem du kan gå videre til før du velger spor.';box.append(strong)
    p=soup.new_tag('p');p.string='Valget under sorterer bare rekkefølgen. Du sendes ikke videre før du selv trykker på en partner.';box.append(p)
    brands=soup.new_tag('div');brands['class']=['partner-brand-list']
    for name in names:
        span=soup.new_tag('span');span.string=name;brands.append(span)
    box.append(brands);matcher.insert_before(box)

def make_partner_route_obvious(path,soup):
    rel=path.relative_to(ROOT).as_posix()
    if rel not in ('sjekk/forbrukslan/index.html','sjekk/omstartslan/index.html'):return
    actions=soup.select_one('.campaign-hero .hero-actions')
    if not actions:return
    links=actions.find_all('a',recursive=False)
    if rel=='sjekk/forbrukslan/index.html' and len(links)>=2:
        links[1]['href']='#samarbeidspartnere';links[1].string='Se samarbeidspartnere'
    if rel=='sjekk/omstartslan/index.html' and links:
        links[0]['href']='#samarbeidspartnere';links[0].string='Se samarbeidspartnere'
        if len(links)>=2:links[1]['href']='../../omstartslan.html';links[1].string='Forstå omstartslån først'

def protect_credit_partner_clarity(path,soup):
    if path.relative_to(ROOT).as_posix()!='sjekk/kredittkort/index.html':return
    zone=soup.select_one('[data-credit-card-partners]')
    if not zone:return
    zone['id']='samarbeidspartnere';hero=soup.select_one('.campaign-hero .hero-actions a.cta')
    if hero:hero['href']='#samarbeidspartnere';hero.string='Se kort og samarbeidspartnere'
    disclosure=zone.select_one('.partner-disclosure')
    if disclosure:disclosure.string='ANNONSE / REKLAME – Sparesjekk kan motta provisjon dersom du går videre'
    direct=zone.find('h2',id='direkte')
    if direct:direct.string='Konkrete kredittkort fra re:member'
    multi=zone.select_one('#flere h2')
    if multi:multi.string='Sammenligningstjenester for flere kredittkortalternativer'

def consolidate_restart_end(path,soup):
    if path.name!='omstartslan.html' or path.parent!=ROOT:return
    article=soup.select_one('article#omstartslan-hub-guide')
    if not article:return
    for old in article.select('[data-restart-end-flow], .revenue-next-step, [data-secured-refi-revenue]'):old.decompose()
    note=article.select_one('.article-note');frag=BeautifulSoup(RESTART_END_HTML,'html.parser').section
    if note:note.insert_before(frag)
    else:article.append(frag)

changed=0
for path in ROOT.rglob('*.html'):
    if any(x in path.parts for x in ('.git','release')):continue
    original=path.read_text(encoding='utf-8');soup=BeautifulSoup(original,'html.parser')
    ensure_css(soup);canonical_nav(soup);add_rate_notice(path,soup);ensure_home_fast_routes(path,soup);repair_boliglan(path,soup);repair_offer(path,soup);ensure_conversion_bridge(path,soup);ensure_debt_offer_route(path,soup);expose_partner_brands(path,soup);make_partner_route_obvious(path,soup);protect_credit_partner_clarity(path,soup);consolidate_restart_end(path,soup)
    new=str(soup)
    if new!=original:path.write_text(new,encoding='utf-8');changed+=1
print(f'SYSTEM REPAIR PASS: {changed} HTML files normalized; cache-safe stylesheet and homepage fast routes applied')
