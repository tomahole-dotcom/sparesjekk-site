from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Make guide-sammenligne the owner for direct comparison intent.
p=R/'guide-sammenligne-boliglan.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-mortgage-compare-owner-v2="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-mortgage-compare-owner-v2']='v1'
h=s.new_tag('h2');h.string='Klar til å sammenligne boliglån?';sec.append(h)
para=s.new_tag('p');para.string='Når du sammenligner boliglån bør du se på mer enn den annonserte renten: effektiv rente, gebyrer, belåningsgrad og vilkår kan påvirke totalen. Hvis du allerede vet at du vil undersøke alternativer, kan du gå direkte videre.';sec.append(para)
a=s.new_tag('a',href='sjekk/boliglan/');a.string='Undersøk boliglånsalternativer →';a['data-event']='commercial_route';a['data-context']='mortgage_compare_gsc_v2';sec.append(a);root.append(sec);p.write_text(str(s),encoding='utf-8')
# Supporting complete article should point direct comparison intent to owner instead of competing.
p=R/'sammenligne-boliglan-komplett.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-mortgage-compare-support-v2="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-mortgage-compare-support-v2']='v1'
h=s.new_tag('h2');h.string='Vil du sammenligne boliglån nå?';sec.append(h)
para=s.new_tag('p');para.append('For en kortere sammenligningsvei, gå til ');a=s.new_tag('a',href='guide-sammenligne-boliglan.html');a.string='guiden for å sammenligne boliglån';a['data-event']='problem_route';a['data-context']='mortgage_compare_gsc_v2';para.append(a);para.append('.');sec.append(para);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Mortgage compare intent consolidation v2 applied')
