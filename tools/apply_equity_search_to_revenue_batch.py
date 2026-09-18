from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-equity-search-revenue="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-equity-search-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=body;x.append(q)
 for href,label,event in links:
  q=s.new_tag('p');a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='equity_gsc_v1'
  q.append(a);x.append(q)
 root.append(x);p.write_text(str(s),encoding='utf-8')
add('boliglan-uten-egenkapital.html','gap-v2','Hva er det som faktisk stopper boligkjøpet?','Google-søkene viser mange som leter etter boliglån uten egenkapital. Før du går videre bør du skille mellom manglende sikkerhet, for lav inntekt og for høy samlet gjeld. Løsningen er forskjellig for hvert problem.',[('mangler-egenkapital-bolig.html','Finn problemet med 3-spørsmålsjekken →','problem_route'),('sjekk/boliglan/','Har du finansieringen på plass? Undersøk boliglånsalternativer →','commercial_route')])
add('kausjonist-boliglan.html','guarantor-v2','Kausjonist løser ikke alle lånehindre','Hvis banken først og fremst mangler sikkerhet, kan kausjon eller tilleggssikkerhet være relevant. Hvis inntekt eller samlet gjeld stopper søknaden, bør du avklare det før noen påtar seg kausjonsansvar.',[('mangler-egenkapital-bolig.html','Finn hvilket hinder som gjelder →','problem_route'),('sjekk/boliglan/','Når finansieringen er avklart: undersøk alternativer →','commercial_route')])
add('medlantaker-boliglan.html','coborrower-v2','Når medlåntaker faktisk er relevant','Medlåntaker kan være relevant når inntektsgrunnlaget er problemet, men innebærer reelt låneansvar. Skill dette fra tilleggssikkerhet før dere går videre.',[('hvor-mye-kan-jeg-lane-bolig.html','Sjekk hva som begrenser lånerammen →','problem_route'),('sjekk/boliglan/','Når rammen er avklart: undersøk alternativer →','commercial_route')])
add('egenkapital-bolig.html','capital-v2','Fra egenkapital til neste beslutning','Har du nok egenkapital og realistisk buffer, er neste spørsmål hvor mye banken kan finansiere og hvilke boliglånsalternativer som er relevante. Mangler du egenkapital, bruk problemsjekken først.',[('mangler-egenkapital-bolig.html','Mangler du egenkapital? Finn riktig spor →','problem_route'),('hvor-mye-kan-jeg-lane-bolig.html','Se hva som påvirker lånerammen →','problem_route'),('sjekk/boliglan/','Klar til å undersøke boliglånsalternativer →','commercial_route')])
print('Equity search-to-revenue batch applied: 4 pages')
