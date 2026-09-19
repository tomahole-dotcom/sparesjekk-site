from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
blocks={
'boliglan.html':[('boliglansrente-komplett-guide.html','Forstå boliglånsrenten før du sammenligner'),('oke-boliglanet.html','Vurderer du å øke boliglånet?')],
'boliglan-guider.html':[('boliglansrente-komplett-guide.html','Boliglånsrente – komplett guide'),('nedbetalingstid-boliglan.html','Nedbetalingstid på boliglån'),('oke-boliglanet.html','Øke boliglånet')],
'forbrukslan.html':[('refinansiere-forbruksgjeld.html','Har du allerede dyr forbruksgjeld? Se refinansiering'),('gjeldsregisteret-forbrukslan.html','Få oversikt over usikret gjeld')],
'forbrukslan-komplett-guide.html':[('refinansiere-forbruksgjeld.html','Refinansiere forbruksgjeld'),('gjeldsregisteret-forbrukslan.html','Gjeldsregisteret og usikret gjeld')],
'guide-refinansiering.html':[('refinansiere-forbruksgjeld.html','Refinansiering av forbruksgjeld'),('gjeldsregisteret-forbrukslan.html','Start med oversikt over usikret gjeld')]
}
for name,links in blocks.items():
 p=R/name
 if not p.exists(): continue
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-commercial-ranking-links="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-commercial-ranking-links']='v1'
 h=s.new_tag('h2');h.string='Relaterte neste steg';sec.append(h)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Commercial ranking internal-link batch applied')
