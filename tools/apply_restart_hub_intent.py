from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'omstartslan.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-restart-hub-intent="v1"]')
if old: old.extract()
sec=BeautifulSoup('''<section class="tool-card restart-hub-intent" data-restart-hub-intent="v1" id="restart-hub-intent"><p class="eyebrow">FINN RIKTIG REFINANSIERINGSSPOR</p><h2>Hva beskriver situasjonen din best?</h2><p>Omstartslån innebærer normalt sikkerhet i bolig. Velg situasjonen før du går videre.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="restart_hub_security_v1" href="sjekk/omstartslan/?intent=sikkerhet"><strong>Jeg eier bolig og vurderer sikkerhet i boligen</strong><span>Undersøk relevante omstartslån-alternativer →</span></a><a data-revenue-event="problem_route" data-revenue-context="restart_hub_unsecured_v1" href="refinansiere-forbruksgjeld.html"><strong>Jeg har dyr gjeld, men dette gjelder ikke sikkerhet i bolig</strong><span>Gå til refinansiering av forbruksgjeld →</span></a><a data-revenue-event="content_route" data-revenue-context="restart_hub_learn_v1" href="#omstartslan-hub-guide"><strong>Jeg vil forstå risiko og kostnader først</strong><span>Fortsett til den uavhengige guiden →</span></a></div></section>''','html.parser').section
hero=s.select_one('.premium-hero'); hero.insert_after(sec)
actions=hero.select_one('.hero-actions') if hero else None
if actions:
    actions.clear()
    a=s.new_tag('a',href='#restart-hub-intent'); a['class']=['cta']; a.string='Finn riktig refinansieringsspor'
    b=s.new_tag('a',href='refinansiering-kalkulator.html'); b['class']=['secondary-cta']; b.string='Regn før og etter'
    actions.append(a); actions.append(b)
article=s.select_one('article.article')
if article: article['id']='omstartslan-hub-guide'
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Restart hub intent applied')
