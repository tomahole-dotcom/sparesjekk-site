from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
p=R/'nedbetaling-kredittkortgjeld.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-card-debt-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-card-debt-conversion']='v1'
h=s.new_tag('h2');h.string='Har du kredittkortgjeld på flere kort eller lån?';sec.append(h)
para=s.new_tag('p');para.string='Hvis du kan betale ned saldoen direkte, er det ofte den enkleste veien. Har du derimot flere dyre kreditter eller lån, kan det være relevant å undersøke om gjelden kan samles eller refinansieres. Sammenlign total kostnad og vilkår før du velger.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('samle-smalan-kredittkortgjeld.html','Se hvordan samling av smålån og kredittkortgjeld fungerer →','problem_route'),
 ('refinansiere-forbruksgjeld.html','Se når refinansiering av forbruksgjeld kan være relevant →','problem_route'),
 ('sjekk/forbrukslan/?intent=refinansiere','Undersøk alternativer for refinansiering →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='card_debt_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Credit-card debt conversion bridge applied')
