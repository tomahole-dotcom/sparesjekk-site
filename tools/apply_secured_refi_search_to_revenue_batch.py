from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-secured-refi-revenue="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-secured-refi-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=body;x.append(q)
 for href,label,event in links:
  q=s.new_tag('p');a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='secured_refi_gsc_v2'
  q.append(a);x.append(q)
 root.append(x);p.write_text(str(s),encoding='utf-8')
add('refinansiering-med-sikkerhet.html','secured-v2','Har du bolig og dyr gjeld? Skill mellom informasjon og faktisk alternativ','Denne siden forklarer risikoen ved pant. Hvis sikkerhet i bolig faktisk kan være aktuelt og du vil undersøke markedet, gå videre til omstartslånssjekken. Der kan du sortere kommersielle alternativer etter situasjonen din uten at Sparesjekk lover godkjenning.',[('refinansiering-kalkulator.html','Regn før og etter først →','problem_route'),('sjekk/omstartslan/?intent=sikkerhet','Undersøk alternativer med sikkerhet →','commercial_route')])
add('omstartslan.html','omstart-v2','Fra omstartslån-søk til en konkret vurdering','Har du dyr gjeld og bolig som kan være aktuell sikkerhet, kan du først regne på dagens og mulig ny løsning. Når du forstår risiko, løpetid og total kostnad, kan du undersøke relevante partneralternativer.',[('refinansiering-kalkulator.html','Sammenlign før og etter →','problem_route'),('sjekk/omstartslan/?intent=sikkerhet','Undersøk alternativer med sikkerhet →','commercial_route')])
print('Secured refinancing search-to-revenue batch applied: 2 pages')
