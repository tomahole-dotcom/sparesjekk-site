from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');old=s.select_one(f'[data-bank-switch-ranking="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-bank-switch-ranking']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h);q=s.new_tag('p');q.string=body;sec.append(q);ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='bank_switch_gsc_v2';li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
add('bytte-bank-boliglan-komplett.html','decision-v2','Bytte bank med boliglån: start med om flytting faktisk er poenget','Hvis målet er bedre boliglånsvilkår, trenger du ikke begynne med å flytte alle banktjenestene. Sammenlign først boliglånet og vurder deretter om selve lånet eller hele bankforholdet bør flyttes.',[('guide-sammenligne-boliglan.html','Sammenlign boliglån på samme grunnlag →','problem_route'),('flytte-boliglan.html','Se hvordan du flytter selve boliglånet →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('flytte-boliglan.html','transfer-v2','Flytte boliglån til annen bank: sammenlign før du flytter','Når du vurderer å flytte boliglånet, er den kommersielle beslutningen først om et annet tilbud faktisk er bedre. Se på rente, vilkår og relevante kostnader før du bestemmer deg for selve flyttingen.',[('guide-sammenligne-boliglan.html','Slik sammenligner du boliglån →','problem_route'),('boliglanskalkulator-renteforskjell.html','Regn renteforskjellen i kroner →','problem_route'),('sjekk/boliglan/','Undersøk alternativer før flytting →','commercial_route')])
add('guide-sammenligne-boliglan.html','compare-v2','Sammenligne boliglån med mål om å bytte eller flytte','Hvis sammenligningen viser at dagens boliglån ikke er konkurransedyktig, er neste steg å undersøke faktiske alternativer. Deretter kan du bruke flytteguiden hvis et nytt tilbud er aktuelt.',[('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route'),('flytte-boliglan.html','Se selve flytteprosessen →','problem_route')])
print('Bank switch ranking batch applied: 3 pages')
