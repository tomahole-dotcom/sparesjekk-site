from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('gjeldsgrad-forklart.html','ta-sparesjekken.html','debt_ratio','Usikker på hva gjeldsbildet betyr for neste steg?','Ta Sparesjekken →'),
 ('kredittkort-valutapaslag.html','sjekk/kredittkort/?intent=match','card_fx','Betaler du hele fakturaen og vil sammenligne kort?','Se kredittkortalternativer →'),
 ('kredittkort-faktura-minstebelop.html','sjekk/forbrukslan/?intent=refinansiere','card_minimum','Blir kredittkortsaldoen stående med renter?','Undersøk refinansieringsalternativer →'),
 ('boligverdi-og-boliglansrente.html','sjekk/boliglan/?intent=sammenligne','home_value_rate','Kan bedre boligverdi gi grunn til å sammenligne?','Undersøk boliglånsalternativer →'),
 ('guide-rentekutt.html','sjekk/boliglan/?intent=sammenligne','rate_cut','Vil du se om faktiske alternativer er bedre?','Undersøk boliglånsalternativer →')
]
for rel,href,ctx,title,label in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-remaining-intent-route="v1"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-remaining-intent-route']='v1'
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string='Bruk forklaringen over som grunnlag. Gå videre bare hvis neste steg passer situasjonen din; sammenlign alltid faktiske renter, gebyrer, vilkår og total kostnad.';sec.append(q)
 a=s.new_tag('a',href=href);a['class']=['cta'];a['data-revenue-event']='savings_check_entry' if href.startswith('ta-') else 'commercial_route';a['data-revenue-context']=ctx;a.string=label;sec.append(a)
 if ctx=='card_minimum':
  n=s.new_tag('p');n['class']=['small'];n.string='Dette sporet gjelder eksisterende dyr gjeld – ikke nytt kredittkort.';sec.append(n)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('Remaining intent route:',rel)
