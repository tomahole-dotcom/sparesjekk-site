from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-refi-ranking-revenue="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-refi-ranking-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=body;x.append(q)
 for href,label,event in links:
  q=s.new_tag('p');a=s.new_tag('a',href=href);a.string=label;a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='refi_ranking_gsc_v1';q.append(a);x.append(q)
 root.append(x);p.write_text(str(s),encoding='utf-8')
add('refinansiere-forbruksgjeld.html','refi-v2','Vil du gå fra informasjon til faktiske refinansieringsalternativer?','Når du har oversikt over dagens forbruksgjeld, er det mer nyttig å hente reelle alternativer enn å lese enda en generell refinansieringsguide. Sammenlign tilbudene mot før-bildet ditt og se på effektiv rente, løpetid og total kostnad.',[('refinansiering-kalkulator.html','Regn før og etter →','problem_route'),('sjekk/forbrukslan/?intent=refinansiere','Undersøk faktiske refinansieringsalternativer →','commercial_route')])
add('effektiv-rente-forbrukslan.html','compare-v2','Har du forstått effektiv rente? Neste steg er faktiske alternativer','Denne siden hjelper deg å lese kostnadene riktig. Hvis du nå vil undersøke markedet, hent alternativer først og sammenlign konkrete tilbud på samme grunnlag.',[('sjekk/forbrukslan/','Undersøk forbrukslånsalternativer →','commercial_route'),('sammenligne-forbrukslan.html','Sammenlign tilbudene når du har dem →','problem_route')])
print('Refi ranking conversion batch applied: 2 pages')
