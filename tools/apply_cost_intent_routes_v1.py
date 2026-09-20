from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('forbrukslan-gebyrer.html','sjekk/forbrukslan/?intent=nytt','consumer_cost','Vil du sammenligne faktiske alternativer?','Se lånealternativer →'),
 ('kredittkort-effektiv-rente.html','sjekk/kredittkort/?intent=match','card_cost','Betaler du normalt hele kortfakturaen?','Se kredittkortalternativer →'),
 ('kredittkort-gebyrer.html','sjekk/kredittkort/?intent=match','card_fees','Skal du velge eller bytte kredittkort?','Se kredittkortalternativer →'),
 ('kredittkort-rentefri-periode.html','sjekk/kredittkort/?intent=match','card_interest_free','Betaler du hele fakturaen og vil sammenligne kort?','Se kredittkortalternativer →')
]
for rel,href,ctx,title,label in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-cost-intent-route="v1"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-cost-intent-route']='v1'
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string='Bruk kostnadsinformasjonen på siden først. Hvis dette beskriver situasjonen din, kan du gå videre til matcheren og sammenligne kommersielle alternativer og faktiske vilkår.';sec.append(q)
 a=s.new_tag('a',href=href);a['class']=['cta'];a['data-revenue-event']='commercial_route';a['data-revenue-context']=ctx;a.string=label;sec.append(a)
 if ctx.startswith('card_'):
  w=s.new_tag('p');w['class']=['small'];w.string='Har du saldo som står og løper renter? Prioriter nedbetaling eller refinansiering fremfor å skaffe et nytt kort.';sec.append(w)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('Cost-intent route:',rel)
