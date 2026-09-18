from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');old=s.select_one(f'[data-refi-intent-ranking="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-refi-intent-ranking']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h);q=s.new_tag('p');q.string=body;sec.append(q);ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='refi_intent_gsc_v2';li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
add('guide-refinansiering.html','hub-v2','Hva vil du refinansiere? Velg riktig vei','Refinansiering kan bety ulike ting. Skill mellom boliglån, usikret forbruksgjeld og gjeld som vurderes refinansiert med sikkerhet, slik at du sammenligner relevante alternativer.',[('refinansiere-forbruksgjeld.html','Refinansiere forbruksgjeld →','problem_route'),('refinansiering-med-sikkerhet.html','Refinansiering med sikkerhet i bolig →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('refinansiere-forbruksgjeld.html','consumer-v3','Refinansiere forbrukslån eller kredittkortgjeld?','Når problemet er dyr usikret gjeld, bør du sammenligne dagens samlede kostnad med et mulig refinansieringsalternativ før du går videre.',[('refinansiering-kalkulator.html','Regn på refinansieringen først →','problem_route'),('sjekk/forbrukslan/?intent=refinansiere','Undersøk refinansieringsalternativer →','commercial_route'),('samle-smalan-kredittkortgjeld.html','Har du flere smålån eller kredittkort? →','problem_route')])
add('refinansiering-med-sikkerhet.html','secured-v3','Når refinansieringen gjelder sikkerhet i bolig','Refinansiering med sikkerhet er en annen situasjon enn vanlig refinansiering av usikret gjeld. Gå derfor videre i sporet som faktisk passer situasjonen din.',[('sjekk/omstartslan/?intent=sikkerhet','Undersøk alternativer med sikkerhet →','commercial_route'),('refinansiere-forbruksgjeld.html','Se refinansiering uten dette sporet →','problem_route')])
add('samle-smalan-kredittkortgjeld.html','consolidate-v2','Samle smålån og kredittkortgjeld: regn før du søker','Hvis målet er å samle flere dyre gjeldsposter, start med å få oversikt og regn på om et samlet alternativ faktisk forbedrer kostnaden.',[('refinansiering-kalkulator.html','Regn på mulig refinansiering →','problem_route'),('sjekk/forbrukslan/?intent=refinansiere','Undersøk alternativer for å samle gjeld →','commercial_route')])
print('Refinance intent ranking batch applied: 4 pages')
