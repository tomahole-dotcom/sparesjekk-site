from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]

def load(name):
 p=ROOT/name; return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s): p.write_text(str(s),encoding='utf-8')
def before_first(article,sec):
 first=article.find('section')
 if first: first.insert_before(sec)
 else: article.append(sec)

# Main informational intent: GSC maps "hva er et forbrukslån" and "hvordan fungerer forbrukslån" here.
p,s=load('forbrukslan-komplett-guide.html')
old=s.select_one('[data-consumer-authority="definition-v1"]')
if old: old.decompose()
a=s.select_one('article')
sec=s.new_tag('section'); sec['data-consumer-authority']='definition-v1'
h=s.new_tag('h2'); h.string='Hva er et forbrukslån, og hvordan fungerer det?'
p1=s.new_tag('p'); p1.string='Et forbrukslån er et lån uten pant i bolig eller annen eiendel. Du låner et avtalt beløp og betaler det tilbake over tid med renter og eventuelle gebyrer. Fordi lånet normalt er usikret, vurderer långiver økonomien og kredittrisikoen før et eventuelt tilbud gis.'
p2=s.new_tag('p'); p2.string='Det viktigste når du vurderer et konkret tilbud er effektiv rente, løpetid, månedsbeløp og samlet tilbakebetaling. Skal eksisterende dyr gjeld samles, er refinansiering et eget spor og bør sammenlignes mot kostnaden på gjelden du allerede har.'
ul=s.new_tag('ul')
for href,label in [('effektiv-rente-forbrukslan.html','Forstå effektiv rente i tilbudet'),('sammenligne-forbrukslan.html','Sammenlign konkrete tilbud steg for steg'),('refinansiere-forbruksgjeld.html','Har du eksisterende gjeld? Se refinansiering')]:
 li=s.new_tag('li'); x=s.new_tag('a',href=href); x.string=label; li.append(x); ul.append(li)
sec.extend([h,p1,p2,ul]); before_first(a,sec); save(p,s)

# Preserve the page Google already ranks for "sammenligne forbrukslån"; clarify its role rather than retargeting it.
p,s=load('effektiv-rente-forbrukslan.html')
old=s.select_one('[data-consumer-authority="compare-signal-v1"]')
if old: old.decompose()
a=s.select_one('article')
sec=s.new_tag('section'); sec['data-consumer-authority']='compare-signal-v1'
h=s.new_tag('h2'); h.string='Sammenligne forbrukslån? Start med tallene som faktisk kan sammenlignes'
p1=s.new_tag('p'); p1.string='Når tilbudene gjelder omtrent samme lånebeløp og løpetid, er effektiv rente og samlet tilbakebetaling de viktigste kostnadstallene å sette side om side. Har du flere konkrete tilbud, går du deretter videre til selve sammenligningsprosessen.'
x=s.new_tag('a',href='sammenligne-forbrukslan.html'); x['class']=['cta']; x.string='Sammenlign konkrete tilbud steg for steg →'
sec.extend([h,p1,x]); before_first(a,sec); save(p,s)

# Comparison page remains process intent, not definition intent.
p,s=load('sammenligne-forbrukslan.html')
old=s.select_one('[data-consumer-authority="process-v1"]')
if old: old.decompose()
a=s.select_one('article')
sec=s.new_tag('section'); sec['data-consumer-authority']='process-v1'
h=s.new_tag('h2'); h.string='Denne siden er for deg som allerede har tilbud å sammenligne'
p1=s.new_tag('p'); p1.string='Har du ikke konkrete tilbud ennå, start med å forstå kostnadstallene eller se hvilke alternativer som finnes. Har du tilbudene foran deg, fortsetter du med stegene under.'
ul=s.new_tag('ul')
for href,label in [('effektiv-rente-forbrukslan.html','Forstå effektiv rente og totalpris'),('sjekk/forbrukslan/','Se aktuelle sammenligningsalternativer')]:
 li=s.new_tag('li'); x=s.new_tag('a',href=href); x.string=label; li.append(x); ul.append(li)
sec.extend([h,p1,ul]); before_first(a,sec); save(p,s)

# Hub reinforcement: send broad authority to the informational guide and preserve commercial path.
for name in ['forbrukslan.html','forbrukslan-guider.html','guider.html']:
 p,s=load(name)
 if s.select_one('[data-consumer-authority-link="v1"]'): continue
 container=s.select_one('main') or s.body
 sec=s.new_tag('section'); sec['class']=['seo-related']; sec['data-consumer-authority-link']='v1'
 h=s.new_tag('h2'); h.string='Forbrukslån: forstå før du sammenligner'
 ul=s.new_tag('ul')
 for href,label in [('forbrukslan-komplett-guide.html','Hva er forbrukslån og hvordan fungerer det?'),('effektiv-rente-forbrukslan.html','Effektiv rente og kostnader'),('sammenligne-forbrukslan.html','Sammenligne konkrete forbrukslån')]:
  li=s.new_tag('li'); x=s.new_tag('a',href=href); x.string=label; li.append(x); ul.append(li)
 sec.extend([h,ul]); container.append(sec); save(p,s)

print('Consumer-loan authority batch applied: 6 pages')
