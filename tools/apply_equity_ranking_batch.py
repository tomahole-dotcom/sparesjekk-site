from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-equity-ranking="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-equity-ranking']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h)
 q=s.new_tag('p');q.string=body;sec.append(q)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul); root.append(sec); p.write_text(str(s),encoding='utf-8')
add('boliglan-uten-egenkapital.html','gap-rank-v1','Mangler egenkapital til bolig? Skill mellom tre ulike problemer','Søk etter boliglån uten egenkapital kan bety at du mangler oppspart kapital, trenger ekstra sikkerhet eller at lånerammen er for lav. De tre situasjonene bør vurderes forskjellig før du undersøker boliglånsalternativer.',[('mangler-egenkapital-bolig.html','Finn ut hva som faktisk mangler →'),('kausjonist-boliglan.html','Les om kausjonist ved boliglån →'),('medlantaker-boliglan.html','Les om medlåntaker ved boliglån →')])
add('kausjonist-boliglan.html','guarantor-rank-v1','Kausjonist ved boliglån når egenkapitalen ikke strekker til','Hvis utfordringen er manglende egenkapital eller sikkerhet, er kausjonist ett av sporene mange undersøker. Det er noe annet enn å ha en medlåntaker, og ansvar og risiko bør forstås før en søknad.',[('boliglan-uten-egenkapital.html','Se muligheter når egenkapitalen ikke er nok →'),('medlantaker-boliglan.html','Forskjellen på kausjonist og medlåntaker →')])
add('medlantaker-boliglan.html','coborrower-rank-v1','Medlåntaker eller kausjonist ved boliglån?','En medlåntaker er relevant når låneevnen og det felles ansvaret er sentralt, mens kausjonist typisk undersøkes når sikkerhet er problemet. Start med å identifisere hva som faktisk stopper boligkjøpet.',[('mangler-egenkapital-bolig.html','Finn flaskehalsen først →'),('kausjonist-boliglan.html','Les om kausjonist →')])
add('egenkapital-bolig.html','capital-rank-v1','Egenkapital til boliglån: gå videre etter hva du mangler','Når du har oversikt over egenkapitalen, er neste spørsmål om utfordringen er selve kapitalen, sikkerheten eller hvor mye du kan låne. Bruk riktig spor i stedet for å starte en ny generell søknad.',[('boliglan-uten-egenkapital.html','Muligheter når egenkapitalen ikke er nok →'),('hvor-mye-kan-jeg-lane-bolig.html','Sjekk mulig låneramme →')])
print('Equity ranking batch applied: 4 pages')
