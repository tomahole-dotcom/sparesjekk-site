from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('boliglan-terminbelop.html','mortgage_payment','Vil du sammenligne terminbeløpet med faktiske alternativer?'),
 ('guide-fastrente-flytende.html','fixed_float','Vil du sammenligne faktiske boliglånstilbud før du velger?')
]
for rel,ctx,title in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-mortgage-decision-route="v1"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-mortgage-decision-route']='v1'
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string='Bruk beregningene og forklaringene på siden som beslutningsgrunnlag. Hvis du vil undersøke markedet videre, kan matcheren sende deg til kommersielle alternativer der du kontrollerer faktisk effektiv rente, gebyrer og vilkår.';sec.append(q)
 a=s.new_tag('a',href='sjekk/boliglan/?intent=sammenligne');a['class']=['cta'];a['data-revenue-event']='commercial_route';a['data-revenue-context']=ctx;a.string='Sammenlign boliglånsalternativer →';sec.append(a)
 n=s.new_tag('p');n['class']=['small'];n.string='Sparesjekk kan motta provisjon dersom du går videre via en partnerlenke. Ingen besparelse eller godkjenning er garantert.';sec.append(n)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('Mortgage decision route:',rel)
