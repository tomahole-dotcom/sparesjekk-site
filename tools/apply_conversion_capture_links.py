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

# GSC 2026-09-17 showed the bank-switch cluster competing for the same queries.
# Keep four useful pages, but give each one a single, explicit search/job intent.
BANK_INTENTS={
 'bytte-bank-boliglan-komplett.html':{
   'role':'decision',
   'title':'Bytte bank med boliglån – bør du bytte? | Sparesjekk',
   'description':'Vurder om det lønner seg å bytte bank med boliglån. Sammenlign rente, kostnader og break-even før du bestemmer deg.',
   'h1':'Bytte bank med boliglån – bør du bytte?',
   'lead':'Hovedsiden for beslutningen: sammenlign dagens boliglån med et konkret alternativ og se om rentegevinsten forsvarer kostnaden ved å bytte.'
 },
 'flytte-boliglan.html':{
   'role':'mortgage-transfer',
   'title':'Flytte boliglån til annen bank – selve låneflyttingen | Sparesjekk',
   'description':'Har du bestemt deg? Se den praktiske prosessen for å flytte selve boliglånet til en annen bank, uten å gjøre siden til en generell bankbytteguide.',
   'h1':'Flytte boliglån til en annen bank – selve låneflyttingen',
   'lead':'Denne guiden starter etter at du har bestemt deg: dokumenter lånet, kontroller tilbudet og gjennomfør flyttingen av selve boliglånet.'
 },
 'guide-bytte-bank-steg.html':{
   'role':'full-bank-move',
   'title':'Bytte bank steg for steg – konto, kort og betalinger | Sparesjekk',
   'description':'Sjekkliste for å flytte hele bankforholdet: kontoer, kort, lønn, AvtaleGiro, eFaktura og andre betalinger når du bytter bank.',
   'h1':'Bytte bank steg for steg – konto, kort og betalinger',
   'lead':'Denne sjekklisten gjelder hele bankbyttet rundt lånet: kontoer, kort, lønnsinngang og faste betalinger. For bare boliglånet bruker du låneflytteguiden.'
 },
 'guide-bytte-bank.html':{
   'role':'trigger',
   'title':'Når bør du vurdere å bytte bank? 5 tegn | Sparesjekk',
   'description':'Fem situasjoner der det kan være naturlig å undersøke banken og boliglånsrenten på nytt – før du bestemmer deg for et bankbytte.',
   'h1':'Når bør du vurdere å bytte bank? 5 tegn',
   'lead':'Denne siden handler bare om når det er verdt å undersøke et bytte. Den dekker ikke selve flytteprosessen.'
 },
}
intent_changed=0
for rel,cfg in BANK_INTENTS.items():
 p=ROOT/rel
 if not p.exists(): continue
 soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if not soup.body: continue
 soup.body['data-search-intent']=cfg['role']
 if soup.title: soup.title.string=cfg['title']
 meta=soup.find('meta',attrs={'name':'description'})
 if meta: meta['content']=cfg['description']
 for attr in ['og:title','twitter:title']:
  tag=soup.find('meta',attrs={'property':attr}) or soup.find('meta',attrs={'name':attr})
  if tag: tag['content']=cfg['title']
 for attr in ['og:description','twitter:description']:
  tag=soup.find('meta',attrs={'property':attr}) or soup.find('meta',attrs={'name':attr})
  if tag: tag['content']=cfg['description']
 h1=soup.find('h1')
 if h1: h1.string=cfg['h1']
 lead=soup.select_one('.lead')
 if lead: lead.string=cfg['lead']
 p.write_text(str(soup),encoding='utf-8'); intent_changed+=1

print(f'Conversion capture internal routes applied: {changed}')
print(f'Bank-switch intents separated: {intent_changed}')
