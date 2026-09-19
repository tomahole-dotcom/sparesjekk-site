from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
pages={
'oke-boliglanet.html':[('rammelan-bolig.html','Rammelån som alternativ'),('nedbetalingstid-boliglan.html','Endre nedbetalingstid'),('boliglan-terminbelop.html','Forstå terminbeløpet')],
'rammelan-bolig.html':[('oke-boliglanet.html','Øke eksisterende boliglån'),('nedbetalingstid-boliglan.html','Nedbetalingstid på boliglån'),('boliglan-terminbelop.html','Hva består terminbeløpet av?')],
'nedbetalingstid-boliglan.html':[('oke-boliglanet.html','Vurderer du å øke boliglånet?'),('boliglan-terminbelop.html','Se hvordan terminbeløpet henger sammen'),('ekstra-nedbetaling-boliglan.html','Ekstra nedbetaling på boliglån')],
'boliglan-terminbelop.html':[('nedbetalingstid-boliglan.html','Kort eller lang nedbetalingstid?'),('oke-boliglanet.html','Øke boliglånet'),('guide-avdragsfrihet.html','Avdragsfrihet – hva betyr det?')],
'ekstra-nedbetaling-boliglan.html':[('nedbetalingstid-boliglan.html','Vurder nedbetalingstiden'),('boliglan-terminbelop.html','Forstå terminbeløpet')],
'guide-avdragsfrihet.html':[('nedbetalingstid-boliglan.html','Se alternativer i nedbetalingstiden'),('boliglan-terminbelop.html','Forstå terminbeløpet')]
}
for name,links in pages.items():
 p=R/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-existing-mortgage-change="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-existing-mortgage-change']='v1'
 h=s.new_tag('h2');h.string='Andre måter å endre boliglånet på';sec.append(h)
 para=s.new_tag('p');para.string='Hvis du allerede har boliglån, kan størrelse, lånetype, nedbetalingstid og terminbeløp påvirke hvilke grep som er relevante.';sec.append(para)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Existing mortgage change cluster applied')
