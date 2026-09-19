from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'forbrukslan.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-consumer-hub-intent="v1"]')
if old: old.extract()
sec=BeautifulSoup('''<section class="tool-card consumer-hub-intent" data-consumer-hub-intent="v1"><p class="eyebrow">VELG RIKTIG SPOR</p><h2>Hva gjelder det for deg?</h2><p>Et nytt lån og refinansiering er to forskjellige behov. Velg situasjonen før du går videre.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="consumer_hub_new_v1" href="sjekk/forbrukslan/?intent=nytt-lan"><strong>Jeg vurderer et nytt forbrukslån</strong><span>Se aktuelle sammenligningsalternativer →</span></a><a data-revenue-event="problem_route" data-revenue-context="consumer_hub_refi_v1" href="refinansiere-forbruksgjeld.html"><strong>Jeg har lån eller kredittgjeld fra før</strong><span>Start med refinansiering og før/etter-regnestykket →</span></a><a data-revenue-event="content_route" data-revenue-context="consumer_hub_learn_v1" href="#forbrukslan-hub-guide"><strong>Jeg vil forstå kostnadene først</strong><span>Fortsett til den uavhengige guiden →</span></a></div></section>''','html.parser').section
hero=s.select_one('.premium-hero')
hero.insert_after(sec)
actions=hero.select_one('.hero-actions') if hero else None
if actions:
    actions.clear()
    jump=s.new_tag('a',href='#consumer-hub-intent')
    jump['class']=['cta']
    jump.string='Velg riktig spor'
    guides=s.new_tag('a',href='forbrukslan-guider.html')
    guides['class']=['secondary-cta']
    guides.string='Se guidene'
    actions.append(jump); actions.append(guides)
sec['id']='consumer-hub-intent'
article=s.select_one('article.article')
if article: article['id']='forbrukslan-hub-guide'
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Consumer hub intent applied')
