from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
p=R/'guide-forstehjemslan.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-first-home-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-first-home-conversion']='v1'
h=s.new_tag('h2');h.string='Skal du faktisk kjøpe din første bolig?';sec.append(h)
q=s.new_tag('p');q.string='Da er neste spørsmål vanligvis ikke bare hva et førstehjemslån er, men om økonomien din passer et boligkjøp og hvilke finansieringsalternativer du kan undersøke. Velg sporet som passer situasjonen din.';sec.append(q)
ul=s.new_tag('ul')
for href,label,event in [
 ('hvor-mye-kan-jeg-lane-bolig.html','Finn ut hva som påvirker hvor mye du kan låne →','problem_route'),
 ('mangler-egenkapital-bolig.html','Mangler du egenkapital? Se mulige neste steg →','problem_route'),
 ('sjekk/boliglan/','Klar for å undersøke boliglånsalternativer? →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='first_home_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('First-home conversion batch applied')
