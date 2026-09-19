from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
p=R/'boliglan-guider.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-toploan-housing-intent="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-toploan-housing-intent']='v1'
h=s.new_tag('h2');h.string='Leter du etter topplån til bolig?';sec.append(h)
p1=s.new_tag('p');p1.string='Begrepet «topplån» brukes om finansiering av den øverste delen av et boligkjøp, men hvilke løsninger som faktisk tilbys og hvilke krav som gjelder kan variere. Hvis søket ditt egentlig handler om at du mangler egenkapital, er det mer nyttig å starte med finansieringssituasjonen din enn med selve begrepet.';sec.append(p1)
ul=s.new_tag('ul')
for href,label,etype in [
 ('boliglan-uten-egenkapital.html','Se muligheter når du mangler egenkapital →','problem_route'),
 ('egenkapital-bolig.html','Forstå egenkapital ved boligkjøp →','problem_route'),
 ('kausjonist-boliglan.html','Se hvordan kausjonist kan fungere →','problem_route'),
 ('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='toploan_housing_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Topplaan housing intent applied')
