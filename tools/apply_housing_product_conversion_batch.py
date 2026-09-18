from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-housing-product-revenue="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-housing-product-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=body;x.append(q)
 for href,label,event in links:
  q=s.new_tag('p');a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='housing_product_gsc_v1'
  q.append(a);x.append(q)
 root.append(x);p.write_text(str(s),encoding='utf-8')
add('guide-mellomfinansiering.html','bridge-v2','Trenger du mellomfinansiering fordi boligkjøpet er konkret?','Når du både skal kjøpe og selge bolig, er neste steg å få oversikt over finansieringen og hvilke boliglånsalternativer som faktisk er tilgjengelige. Sammenlign helheten, ikke bare kostnaden på mellomperioden.',[('hvor-mye-kan-jeg-lane-bolig.html','Sjekk lånerammen først →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('rammelan-bolig.html','creditline-v2','Vurderer du rammelån fordi du vil bruke ledig verdi i boligen?','Rammelån bør vurderes opp mot vanlig boliglån, rente, fleksibilitet og hvor mye av boligen som allerede er belånt. Hvis behovet er reelt, undersøk alternativer på boliglånssiden.',[('guide-belaningsgrad.html','Forstå belåningsgraden først →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('oke-boliglanet.html','increase-v2','Vil du øke boliglånet? Sjekk alternativene før du bestemmer deg','Et større lån hos dagens bank er ikke nødvendigvis eneste mulighet. Når du kjenner belåningsgrad, låneramme og formålet, kan du undersøke boliglånsalternativer og sammenligne totalbildet.',[('hvor-mye-kan-jeg-lane-bolig.html','Sjekk mulig låneramme →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
print('Housing product conversion batch applied: 3 pages')
