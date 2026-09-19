from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Dedicated page owns early-repayment intent
p=R/'nedbetalingstid-forbrukslan.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-consumer-early-repayment="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-consumer-early-repayment']='v1'
h=s.new_tag('h2');h.string='Vil du betale ned forbrukslånet før tiden?';sec.append(h)
para=s.new_tag('p');para.string='Ekstra nedbetaling kan redusere rentekostnaden og løpetiden. Før du velger neste steg, se på effektiv rente, gjenstående gjeld og om du har flere dyre lån eller kreditter.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('refinansiere-forbruksgjeld.html','Har du flere dyre lån eller kreditter? Se når refinansiering kan være relevant →','problem_route'),
 ('sjekk/forbrukslan/?intent=refinansiere','Undersøk alternativer for refinansiering →','commercial_route'),
 ('forbrukslan-komplett-guide.html','Les mer om kostnader og nedbetalingstid →','problem_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='consumer_early_repayment_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
# Supporting guide points exact intent to dedicated page
p=R/'forbrukslan-komplett-guide.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-consumer-early-repayment-support="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-consumer-early-repayment-support']='v1'
h=s.new_tag('h2');h.string='Betale ned forbrukslån før tiden?';sec.append(h)
para=s.new_tag('p');para.append('Hvis spørsmålet ditt er hva som skjer når du vil betale ekstra eller avslutte lånet tidligere, se ');a=s.new_tag('a',href='nedbetalingstid-forbrukslan.html');a.string='guiden om nedbetalingstid og tidlig nedbetaling';para.append(a);para.append('.');sec.append(para);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Consumer-loan early repayment cluster applied')
