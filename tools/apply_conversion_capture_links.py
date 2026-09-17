from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
MARK='traffic-conversion-capture-20260917'
LINKS={
 'boliglan-uten-egenkapital.html':('mangler-egenkapital-bolig.html','Usikker på hvilket spor som passer? Ta 3-spørsmåls egenkapitalsjekken →'),
 'kausjonist-boliglan.html':('mangler-egenkapital-bolig.html','Mangler boligkjøperen egenkapital? Finn riktig neste steg →'),
 'egenkapital-bolig.html':('mangler-egenkapital-bolig.html','Mangler du nok egenkapital? Sjekk situasjonen på 3 spørsmål →'),
 'refinansiere-forbruksgjeld.html':('hva-bor-jeg-gjore-med-dyr-gjeld.html','Dyr gjeld? Finn riktig neste steg før du velger løsning →'),
 'guide-refinansiering.html':('hva-bor-jeg-gjore-med-dyr-gjeld.html','Usikker på hvilket refinansieringsspor som passer? Ta hurtigsjekken →'),
 'gjeldsmiks-sjekk.html':('hva-bor-jeg-gjore-med-dyr-gjeld.html','Har du dyr gjeld? Finn riktig neste steg →'),
 'samle-smalan-kredittkortgjeld.html':('hva-bor-jeg-gjore-med-dyr-gjeld.html','Vil du samle gjelden? Sjekk hvilket spor som passer først →'),
}
changed=0
for rel,(href,label) in LINKS.items():
 p=ROOT/rel
 if not p.exists(): continue
 soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if soup.select_one(f'[data-traffic-route="{MARK}"]') or soup.find('a',href=href): continue
 container=soup.select_one('article') or soup.select_one('main')
 if not container: continue
 box=soup.new_tag('section'); box['class']=['traffic-conversion-route']; box['data-traffic-route']=MARK
 h=soup.new_tag('h2'); h.string='Finn riktig neste steg'
 text=soup.new_tag('p'); text.string='Bruk den korte veiviseren for å sortere situasjonen før du går videre til kalkulator, guide eller kommersiell sammenligning.'
 a=soup.new_tag('a',href=href); a['class']=['cta']; a.string=label
 box.extend([h,text,a])
 first=container.find('section')
 if first: first.insert_before(box)
 else: container.append(box)
 p.write_text(str(soup),encoding='utf-8'); changed+=1
print(f'Conversion capture internal routes applied: {changed}')
