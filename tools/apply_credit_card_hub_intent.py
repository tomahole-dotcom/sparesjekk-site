from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'kredittkort.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-card-hub-intent="v1"]')
if old: old.extract()
sec=BeautifulSoup('''<section class="tool-card card-hub-intent" data-card-hub-intent="v1" id="card-hub-intent"><p class="eyebrow">VELG RIKTIG KREDITTKORTSPOR</p><h2>Hva vil du løse?</h2><p>Hvordan du bruker kredittkortet avgjør hvilket neste steg som er mest relevant.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="card_hub_choose_v1" href="kredittkort-match.html"><strong>Jeg skal velge eller bytte kredittkort</strong><span>Finn korttype ut fra hvordan du faktisk bruker kortet →</span></a><a data-revenue-event="problem_route" data-revenue-context="card_hub_debt_v1" href="nedbetaling-kredittkortgjeld.html"><strong>Jeg har kredittkortgjeld som blir stående</strong><span>Start med rente, nedbetaling og gjeldskostnad →</span></a><a data-revenue-event="content_route" data-revenue-context="card_hub_learn_v1" href="#kredittkort-hub-guide"><strong>Jeg vil forstå renter og gebyrer først</strong><span>Fortsett til guiden →</span></a></div></section>''','html.parser').section
hero=s.select_one('.premium-hero'); hero.insert_after(sec)
actions=hero.select_one('.hero-actions') if hero else None
if actions:
    actions.clear()
    a=s.new_tag('a',href='#card-hub-intent'); a['class']=['cta']; a.string='Velg riktig kredittkortspor'
    b=s.new_tag('a',href='sammenligne-kredittkort.html'); b['class']=['secondary-cta']; b.string='Lær å sammenligne kort'
    actions.append(a); actions.append(b)
article=s.select_one('article.article')
if article: article['id']='kredittkort-hub-guide'
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Credit card hub intent applied')
