from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n;return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s):p.write_text(str(s),encoding='utf-8')
def add(n,m,title,text,links):
 p,s=load(n);old=s.select_one(f'[data-rate-authority="{m}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main');x=s.new_tag('section');x['data-rate-authority']=m
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=text;x.append(q);ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);first=root.find('section');first.insert_before(x) if first else root.append(x);save(p,s)
add('boliglansrente-komplett-guide.html','mortgage-rate-v1','Boliglånsrente: fra rentetall til konkret handling','Boliglånsrenten må vurderes sammen med restgjeld, gebyrer og vilkår. Når du kjenner renten din, er neste spørsmål hva en forskjell betyr i kroner og om det er grunnlag for å forhandle eller sammenligne andre tilbud.',[('min-rente-vs-markedet.html','Sjekk renten din mot et sammenligningspunkt'),('boliglanskalkulator-renteforskjell.html','Regn renteforskjellen i kroner'),('sjekk/boliglan/','Se boliglånsalternativer')])
add('guide-effektiv-nominell-rente.html','nominal-effective-v1','Nominell rente vs. effektiv rente – kort svar','Nominell rente er selve rentesatsen. Effektiv rente inkluderer relevante kostnader i beregningen og er derfor normalt det bedre sammenligningstallet når du vurderer konkrete lånetilbud med like forutsetninger.',[('hva-er-effektiv-rente.html','Les mer om effektiv rente'),('boliglanskalkulator-renteforskjell.html','Gjør en renteforskjell om til kroner'),('guide-sammenligne-boliglan.html','Sammenlign boliglån på like vilkår'),('sjekk/boliglan/','Se boliglånsalternativer')])
add('nedbetalingstid-boliglan.html','term-v1','Løpetid på boliglån: se mer enn månedsbeløpet','Google viser allerede denne siden høyt på søk om løpetid. Behold derfor rollen tydelig: lengre løpetid kan redusere terminbeløpet, men gjelden står lenger. Sammenlign både månedsbeløp, løpetid og samlet kostnad.',[('boliglan-terminbelop.html','Forstå terminbeløpet'),('boliglanskalkulator-renteforskjell.html','Regn på renteforskjellen'),('sjekk/boliglan/','Se boliglånsalternativer')])
for n in ['boliglan.html','boliglan-guider.html','guider.html']:
 p,s=load(n);old=s.select_one('[data-rate-authority-link="v1"]')
 if old:old.decompose()
 root=s.select_one('main') or s.body;x=s.new_tag('section');x['class']=['seo-related'];x['data-rate-authority-link']='v1'
 h=s.new_tag('h2');h.string='Rente: forstå, regn og sammenlign';x.append(h);ul=s.new_tag('ul')
 for href,label in [('boliglansrente-komplett-guide.html','Boliglånsrente – komplett guide'),('guide-effektiv-nominell-rente.html','Nominell og effektiv rente – forskjellen'),('nedbetalingstid-boliglan.html','Løpetid på boliglån'),('rentemote-hva-betyr-det.html','Rentemøte og styringsrente')]:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);root.append(x);save(p,s)
print('Rate authority batch applied: 6 pages')
