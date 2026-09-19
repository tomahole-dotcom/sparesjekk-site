from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
TARGETS=[
 ('banken-vil-ikke-senke-renten.html','mortgage','Usikker på om dette bare gjelder renten?','Ta hele Sparesjekken på ca. 2 minutter og se om boliglån, dyr gjeld eller kredittkort også bør sjekkes.'),
 ('refinansiere-forbruksgjeld.html','debt','Er dette den eneste delen av økonomien du bør sjekke?','Ta hele Sparesjekken og få en prioritert vei videre for boliglån, dyr gjeld, omstartslån og kredittkort.'),
 ('omstartslan.html','restart','Usikker på hvilket spor som passer situasjonen?','Ta Sparesjekken før du går videre. Den skiller mellom vanlig refinansiering, omstartslån med sikkerhet og andre relevante neste steg.'),
 ('kredittkort.html','card','Vil du sjekke mer enn bare kredittkortet?','Ta hele Sparesjekken og se om boliglån eller dyr gjeld bør prioriteres før du vurderer et nytt kort.')
]
for rel,ctx,title,body in TARGETS:
 p=ROOT/rel
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-savings-check-entry="v1"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-savings-check-entry']='v1';sec['class']=['savings-check-entry']
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string=body;sec.append(q)
 a=s.new_tag('a',href='ta-sparesjekken.html');a['class']=['cta'];a['data-revenue-event']='savings_check_entry';a['data-revenue-context']='traffic_'+ctx;a.string='Ta Sparesjekken →';sec.append(a)
 n=s.new_tag('p');n['class']=['small'];n.string='Gratis · ingen registrering · ca. 2 minutter';sec.append(n)
 root.append(sec)
 p.write_text(str(s),encoding='utf-8')
 print('Ta Sparesjekken traffic entry:',rel)
