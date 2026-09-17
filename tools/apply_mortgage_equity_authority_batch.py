from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
def load(n):
 p=ROOT/n; return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s): p.write_text(str(s),encoding='utf-8')
def insert_first(article,sec):
 first=article.find('section')
 if first:first.insert_before(sec)
 else:article.append(sec)
def section(s,marker,title,text,links):
 sec=s.new_tag('section');sec['data-mortgage-equity']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h)
 p=s.new_tag('p');p.string=text;sec.append(p)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul);return sec

# GSC's largest equity-gap page: make the three solution roles explicit without changing its established intent.
p,s=load('boliglan-uten-egenkapital.html')
old=s.select_one('[data-mortgage-equity="gap-v1"]')
if old:old.decompose()
a=s.select_one('article')
sec=section(s,'gap-v1','Mangler egenkapital? Skill mellom tre forskjellige problemer',
'For lite oppspart egenkapital, for lav betjeningsevne og for høy samlet gjeld er ikke samme problem. Kausjon eller tilleggssikkerhet kan være relevant når sikkerheten er problemet, mens medlåntaker innebærer ansvar for selve lånet. Finn først hva som faktisk stopper finansieringen.',
[('mangler-egenkapital-bolig.html','Ta 3-spørsmåls egenkapitalsjekken'),('kausjonist-boliglan.html','Kausjonist og tilleggssikkerhet'),('medlantaker-boliglan.html','Medlåntaker: ansvar og forskjeller')])
insert_first(a,sec);save(p,s)

# Kausjonist query has the strongest single GSC demand in the cluster.
p,s=load('kausjonist-boliglan.html')
old=s.select_one('[data-mortgage-equity="guarantor-v1"]')
if old:old.decompose()
a=s.select_one('article')
sec=section(s,'guarantor-v1','Kausjonist på boliglån – kort forklart',
'En kausjonist påtar seg et økonomisk ansvar etter kausjonsavtalen. Ved boligkjøp brukes begrepet ofte når familie bidrar med ekstra sikkerhet, men løsningen er ikke det samme som medlåntaker og gir ikke automatisk rett til boliglån.',
[('boliglan-uten-egenkapital.html','Se mulighetene når egenkapitalen ikke strekker til'),('medlantaker-boliglan.html','Forskjellen på kausjonist og medlåntaker'),('mangler-egenkapital-bolig.html','Finn riktig spor med egenkapitalsjekken')])
insert_first(a,sec);save(p,s)

p,s=load('medlantaker-boliglan.html')
old=s.select_one('[data-mortgage-equity="coborrower-v1"]')
if old:old.decompose()
a=s.select_one('article')
sec=section(s,'coborrower-v1','Medlåntaker på boliglån – hva betyr det?',
'En medlåntaker står på lånet og har ansvar etter låneavtalen. Det skiller seg fra en løsning der en annen person bare stiller tilleggssikkerhet eller kausjon. Derfor bør du avklare hvilket problem banken faktisk mener må løses.',
[('kausjonist-boliglan.html','Se hvordan kausjonist skiller seg fra medlåntaker'),('boliglan-uten-egenkapital.html','Mangler egenkapital? Se de ulike sporene'),('mangler-egenkapital-bolig.html','Ta egenkapitalsjekken')])
insert_first(a,sec);save(p,s)

p,s=load('egenkapital-bolig.html')
old=s.select_one('[data-mortgage-equity="capital-v1"]')
if old:old.decompose()
a=s.select_one('article')
sec=section(s,'capital-v1','Har du for lite egenkapital til boligkjøpet?',
'Start med å skille mellom hvor mye egenkapital du faktisk har, kjøpskostnadene og hva banken mener mangler i finansieringen. Da unngår du å lete etter kausjonist eller medlåntaker dersom det egentlig er inntekt, gjeld eller betjeningsevne som stopper kjøpet.',
[('boliglan-uten-egenkapital.html','Se alternativer når egenkapitalen er for lav'),('mangler-egenkapital-bolig.html','Ta den korte egenkapitalsjekken'),('hvor-mye-kan-jeg-lane-bolig.html','Se hva som påvirker lånerammen')])
insert_first(a,sec);save(p,s)

# Reinforce from mortgage hubs without creating new overlapping pages.
for name in ['boliglan.html','boliglan-guider.html','guider.html']:
 p,s=load(name)
 old=s.select_one('[data-mortgage-equity-link="v1"]')
 if old:old.decompose()
 container=s.select_one('main') or s.body
 sec=s.new_tag('section');sec['class']=['seo-related'];sec['data-mortgage-equity-link']='v1'
 h=s.new_tag('h2');h.string='Egenkapital, kausjonist og medlåntaker';sec.append(h)
 ul=s.new_tag('ul')
 for href,label in [('boliglan-uten-egenkapital.html','Boliglån når egenkapitalen ikke strekker til'),('kausjonist-boliglan.html','Kausjonist på boliglån'),('medlantaker-boliglan.html','Medlåntaker på boliglån'),('mangler-egenkapital-bolig.html','Egenkapitalsjekken')]:
  li=s.new_tag('li');x=s.new_tag('a',href=href);x.string=label;li.append(x);ul.append(li)
 sec.append(ul);container.append(sec);save(p,s)
print('Mortgage equity authority batch applied: 7 pages')
