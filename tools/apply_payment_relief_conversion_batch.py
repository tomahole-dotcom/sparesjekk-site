from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'guide-avdragsfrihet.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-payment-relief-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-payment-relief-conversion']='v1'
h=s.new_tag('h2');h.string='Hvorfor vurderer du avdragsfrihet?';sec.append(h)
q=s.new_tag('p');q.string='Neste steg avhenger av problemet du prøver å løse. Hvis boliglånet i seg selv er blitt dyrt, kan det være mer relevant å undersøke boliglånsalternativer. Hvis flere dyre lån eller betalingsproblemer ligger bak behovet, bør du undersøke refinansiering i stedet for å behandle avdragsfrihet som hele løsningen.';sec.append(q)
ul=s.new_tag('ul')
for href,label,event in [
 ('sjekk/boliglan/','Boliglånet er blitt dyrt – undersøk alternativer →','commercial_route'),
 ('refinansiere-forbruksgjeld.html','Flere dyre lån/kreditter – se refinansieringssporet →','problem_route'),
 ('sjekk/omstartslan/?intent=utfordringer','Betalingsproblemer og bolig som sikkerhet – undersøk relevant matcher →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='payment_relief_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Payment relief conversion batch applied')
