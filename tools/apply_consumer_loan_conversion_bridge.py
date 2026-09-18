from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select(f'[data-consumer-conversion="{marker}"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-consumer-conversion']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h);q=s.new_tag('p');q.string=body;sec.append(q);ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='consumer_loan_gsc_v2';li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
add('forbrukslan-komplett-guide.html','guide-v2','Fra guide til faktiske alternativer','Hvis du vurderer et nytt forbrukslån, er neste nyttige steg å sammenligne faktiske alternativer. Hvis du allerede har dyr gjeld, bør du gå til refinansieringssporet i stedet.',[('sjekk/forbrukslan/?intent=nytt-lan','Jeg vurderer et nytt lån – undersøk alternativer →','commercial_route'),('refinansiere-forbruksgjeld.html','Jeg har allerede dyr gjeld – se refinansiering →','problem_route')])
add('sammenligne-forbrukslan.html','compare-v2','Klar til å gå fra sammenligning til alternativer?','Når du vet hvilke kostnader og vilkår du skal sammenligne, kan du gå videre til matcher og undersøke relevante alternativer. Har du eksisterende gjeld, velg refinansieringssporet.',[('sjekk/forbrukslan/?intent=nytt-lan','Undersøk alternativer for nytt lån →','commercial_route'),('sjekk/forbrukslan/?intent=refinansiere','Undersøk alternativer for refinansiering →','commercial_route')])
print('Consumer loan conversion bridge applied')
