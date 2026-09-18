from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n;return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s):p.write_text(str(s),encoding='utf-8')
p,s=load('hvor-mye-kan-jeg-lane-bolig.html');old=s.select_one('[data-borrowing-capacity="v1"]')
if old:old.decompose()
root=s.select_one('article');x=s.new_tag('section');x['data-borrowing-capacity']='v1'
h=s.new_tag('h2');h.string='Fra «hvor mye kan jeg låne?» til et konkret neste steg';x.append(h)
q=s.new_tag('p');q.string='En teoretisk låneramme er bare første filter. Samlet gjeld kan som hovedregel ikke overstige fem ganger brutto årsinntekt, men banken må også vurdere egenkapital, sikkerhet og om økonomien tåler rentestress. Derfor bør du avklare hva som faktisk begrenser deg før du sammenligner boliglån.';x.append(q)
ul=s.new_tag('ul')
for href,label,event in [
 ('gjeldsgrad-forklart.html','Forstå gjeldsgrad og inntektsgrensen',''),
 ('mangler-egenkapital-bolig.html','Mangler du egenkapital? Finn riktig spor','problem_route'),
 ('belaningsgrad-sjekk.html','Har du bolig? Sjekk belåningsgraden','problem_route'),
 ('sjekk/boliglan/','Klar til å undersøke boliglånsalternativer','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label
 if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='borrowing_capacity_v1'
 li.append(a);ul.append(li)
x.append(ul);root.append(x);save(p,s)
for n in ['boliglan.html','boliglan-guider.html','guider.html']:
 p,s=load(n);old=s.select_one('[data-borrowing-capacity-link="v1"]')
 if old:old.decompose()
 root=s.select_one('main') or s.body;x=s.new_tag('section');x['class']=['seo-related'];x['data-borrowing-capacity-link']='v1'
 h=s.new_tag('h2');h.string='Hvor mye kan du låne?';x.append(h)
 q=s.new_tag('p');q.string='Start med lånerammen, finn deretter om inntekt, eksisterende gjeld eller egenkapital er den reelle begrensningen.';x.append(q)
 a=s.new_tag('a',href='hvor-mye-kan-jeg-lane-bolig.html');a.string='Se hva som påvirker hvor mye du kan låne til bolig →';x.append(a);root.append(x);save(p,s)
print('Borrowing capacity conversion batch applied: 4 pages')
