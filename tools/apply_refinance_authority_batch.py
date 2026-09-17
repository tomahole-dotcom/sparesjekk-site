from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]

def load(name):
    p=ROOT/name
    return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')

def save(p,soup):
    p.write_text(str(soup),encoding='utf-8')

# GSC authority batch: strengthen existing pages instead of creating overlapping pages.
# 1) Definition/umbrella intent -> guide-refinansiering.html
p,s=load('guide-refinansiering.html')
old=s.select_one('[data-refi-authority="definition-v1"]')
if old: old.decompose()
article=s.select_one('article')
sec=s.new_tag('section'); sec['data-refi-authority']='definition-v1'
h=s.new_tag('h2'); h.string='Hva er refinansiering? Kort forklart'
lead=s.new_tag('p'); lead.string='Refinansiering betyr at du endrer eksisterende gjeld ved å erstatte, flytte eller samle ett eller flere lån. Målet kan være lavere rente, færre gebyrer, bedre oversikt eller en annen nedbetalingsplan.'
p2=s.new_tag('p'); p2.string='Det er nyttig å skille mellom tre hovedspor: å flytte et boliglån, å samle usikret forbruksgjeld, og å refinansiere med sikkerhet i bolig. De har ulik risiko og bør vurderes hver for seg.'
links=s.new_tag('ul')
for href,label in [
 ('flytte-boliglan.html','Flytte eller refinansiere boliglån'),
 ('refinansiere-forbruksgjeld.html','Refinansiere forbruksgjeld'),
 ('refinansiering-med-sikkerhet.html','Refinansiering med sikkerhet i bolig')]:
    li=s.new_tag('li'); a=s.new_tag('a',href=href); a.string=label; li.append(a); links.append(li)
sec.extend([h,lead,p2,links])
first=article.find('section')
if first: first.insert_before(sec)
else: article.append(sec)
save(p,s)

# 2) Secured refinance intent -> make answer immediate and route qualified intent.
p,s=load('refinansiering-med-sikkerhet.html')
old=s.select_one('[data-refi-authority="secured-v1"]')
if old: old.decompose()
article=s.select_one('article')
sec=s.new_tag('section'); sec['data-refi-authority']='secured-v1'
h=s.new_tag('h2'); h.string='Refinansiering med sikkerhet i bolig – kort forklart'
p1=s.new_tag('p'); p1.string='Du tar opp eller endrer et lån der boligen brukes som pant, og bruker finansieringen til å erstatte eksisterende gjeld. Pant kan gi andre vilkår enn usikret gjeld, men boligen blir samtidig sikkerhet for lånet.'
p2=s.new_tag('p'); p2.string='Har du dyr gjeld og bolig som kan være relevant som sikkerhet, bør du sammenligne effektiv rente, gebyrer, løpetid, samlet tilbakebetaling og konsekvensen av pant – ikke bare månedsbeløpet.'
a=s.new_tag('a',href='hva-bor-jeg-gjore-med-dyr-gjeld.html'); a['class']=['cta']; a.string='Finn riktig refinansieringsspor →'
sec.extend([h,p1,p2,a])
first=article.find('section')
if first: first.insert_before(sec)
else: article.append(sec)
save(p,s)

# 3) Consumer debt page -> reciprocal authority links.
p,s=load('refinansiere-forbruksgjeld.html')
old=s.select_one('[data-refi-authority="consumer-v1"]')
if old: old.decompose()
article=s.select_one('article')
sec=s.new_tag('section'); sec['data-refi-authority']='consumer-v1'
h=s.new_tag('h2'); h.string='Hvilken type refinansiering gjelder situasjonen din?'
p1=s.new_tag('p'); p1.string='Denne siden gjelder først og fremst forbruksgjeld som kredittkort, forbrukslån og smålån. For en generell forklaring av begrepet eller refinansiering med pant bør du bruke de egne guidene.'
links=s.new_tag('ul')
for href,label in [
 ('guide-refinansiering.html','Hva betyr refinansiering?'),
 ('refinansiering-med-sikkerhet.html','Refinansiering med sikkerhet i bolig'),
 ('hva-bor-jeg-gjore-med-dyr-gjeld.html','Usikker? Finn riktig neste steg')]:
    li=s.new_tag('li'); a=s.new_tag('a',href=href); a.string=label; li.append(a); links.append(li)
sec.extend([h,p1,links])
first=article.find('section')
if first: first.insert_before(sec)
else: article.append(sec)
save(p,s)

# 4) Strengthen links from relevant hubs without creating duplicate pages.
for name in ['forbrukslan.html','omstartslan.html','guider.html']:
    p,s=load(name)
    if s.select_one('[data-refi-authority-link="v1"]'): continue
    container=s.select_one('main') or s.body
    box=s.new_tag('section'); box['class']=['seo-related']; box['data-refi-authority-link']='v1'
    h=s.new_tag('h2'); h.string='Refinansiering: velg riktig guide'
    ul=s.new_tag('ul')
    for href,label in [
      ('guide-refinansiering.html','Hva er refinansiering?'),
      ('refinansiere-forbruksgjeld.html','Refinansiering av forbruksgjeld'),
      ('refinansiering-med-sikkerhet.html','Refinansiering med sikkerhet i bolig')]:
        li=s.new_tag('li'); a=s.new_tag('a',href=href); a.string=label; li.append(a); ul.append(li)
    box.extend([h,ul])
    container.append(box)
    save(p,s)

print('Refinance authority batch applied: 6 pages')
