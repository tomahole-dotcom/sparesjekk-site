from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
TARGETS=[
 ('boliglan-uten-egenkapital.html','mortgage_equity','Vil du sjekke hele økonomien før du går videre?'),
 ('hvor-mye-kan-jeg-lane-bolig.html','mortgage_capacity','Har du oversikt over mer enn lånerammen?'),
 ('guide-avdragsfrihet.html','mortgage_relief','Er avdragsfrihet bare én del av bildet?'),
 ('guide-bytte-bank-steg.html','bank_switch','Før du bytter bank: sjekk hva som bør prioriteres'),
 ('bytte-bank-boliglan-komplett.html','mortgage_switch','Vil du sjekke mer enn selve bankbyttet?'),
 ('guide-refinansiering.html','refinance','Usikker på hvilket refinansieringsspor som passer?'),
 ('kausjonist-boliglan.html','guarantor','Vil du sjekke resten av lånebildet også?'),
 ('flytte-boliglan.html','mortgage_move','Før du flytter boliglånet: sjekk helheten'),
 ('rammelan-bolig.html','credit_line','Er rammelån riktig sted å starte?')
]
for rel,ctx,title in TARGETS:
 p=ROOT/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if s.select_one('[data-savings-check-gsc-entry="v1"]'): continue
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-savings-check-gsc-entry']='v1';sec['class']=['savings-check-entry']
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string='Ta Sparesjekken på ca. 2 minutter. Du får en prioritert vei videre på tvers av boliglån, dyr gjeld, omstartslån og kredittkort – uten registrering.';sec.append(q)
 a=s.new_tag('a',href='ta-sparesjekken.html');a['class']=['cta'];a['data-revenue-event']='savings_check_entry';a['data-revenue-context']='gsc_'+ctx;a.string='Ta Sparesjekken →';sec.append(a)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('GSC entry:',rel)
