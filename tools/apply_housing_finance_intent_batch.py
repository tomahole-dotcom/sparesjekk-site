from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n;return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s):p.write_text(str(s),encoding='utf-8')
def add(n,m,title,text,links,commercial=True):
 p,s=load(n);old=s.select_one(f'[data-housing-intent="{m}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main');x=s.new_tag('section');x['data-housing-intent']=m
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=text;x.append(q);ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label
  if href.startswith('sjekk/'): a['class']=['cta'];a['data-revenue-event']='commercial_route';a['data-revenue-context']=m
  li.append(a);ul.append(li)
 x.append(ul);root.append(x);save(p,s)
add('guide-mellomfinansiering.html','bridge-v1','Skal du kjøpe før du har solgt?','Mellomfinansiering er et konkret finansieringsbehov, ikke bare et rentebegrep. Når tidspunktet for kjøp og salg er avklart, bør du sammenligne total finansiering, kostnader og hvor lenge økonomien tåler en dobbeltperiode.',[('boliglanskalkulator-renteforskjell.html','Regn på renteforskjellen'),('sjekk/boliglan/','Se boliglånsalternativer')])
add('oke-boliglanet.html','increase-v1','Vil du faktisk øke boliglånet?','Når behovet er konkret, bør neste steg være å avklare hvor mye ekstra gjeld økonomien tåler, hvordan belåningsgraden endres og hvilke boliglånsalternativer som finnes. Hvis formålet er å samle dyr gjeld, bør refinansieringssporet vurderes separat.',[('belaningsgrad-sjekk.html','Sjekk belåningsgraden'),('sjekk/boliglan/','Se boliglånsalternativer'),('hva-bor-jeg-gjore-med-dyr-gjeld.html','Skal du samle dyr gjeld? Finn riktig spor')])
add('rammelan-bolig.html','creditline-v1','Vurderer du rammelån eller vanlig boliglån?','Rammelån handler om fleksibilitet med sikkerhet i bolig. Før du velger bør du sammenligne kostnad, nedbetalingsdisiplin og om et ordinært boliglån dekker behovet bedre.',[('guide-belaningsgrad.html','Forstå belåningsgraden'),('sjekk/boliglan/','Se boliglånsalternativer')])
add('guide-avdragsfrihet.html','payment-relief-v1','Er problemet midlertidig eller varig?','Avdragsfrihet kan gi midlertidig lavere betaling, men er ikke i seg selv en billigere finansiering. Hvis problemet er varig eller du har flere dyre gjeldsposter, bør du kartlegge hele gjeldssituasjonen før du søker mer kreditt.',[('boliglan-terminbelop.html','Forstå terminbeløpet'),('betalingsproblemer-hva-gjor-jeg.html','Har du betalingsproblemer? Finn riktig neste steg'),('hva-bor-jeg-gjore-med-dyr-gjeld.html','Vurder dyr gjeld samlet')],False)
for n in ['boliglan.html','boliglan-guider.html','guider.html']:
 p,s=load(n);old=s.select_one('[data-housing-intent-link="v1"]')
 if old:old.decompose()
 root=s.select_one('main') or s.body;x=s.new_tag('section');x['class']=['seo-related'];x['data-housing-intent-link']='v1'
 h=s.new_tag('h2');h.string='Når boliglånsbehovet endrer seg';x.append(h);ul=s.new_tag('ul')
 for href,label in [('guide-mellomfinansiering.html','Mellomfinansiering ved kjøp før salg'),('oke-boliglanet.html','Øke boliglånet'),('rammelan-bolig.html','Rammelån eller vanlig boliglån'),('guide-avdragsfrihet.html','Avdragsfrihet ved midlertidig behov')]:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);root.append(x);save(p,s)
print('Housing finance intent batch applied: 7 pages')
