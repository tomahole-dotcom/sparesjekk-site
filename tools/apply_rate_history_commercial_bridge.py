from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'rentehistorikk-boliglan.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-rate-history-bridge="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-rate-history-bridge']='v1'
h=s.new_tag('h2');h.string='Historikken er bakgrunn – dagens boliglånsrente er det du kan påvirke';sec.append(h)
para=s.new_tag('p');para.string='Gamle renter kan gi perspektiv, men de avgjør ikke om boliglånet ditt er konkurransedyktig i dag. Sammenlign derfor det du faktisk betaler med dagens alternativer og vurder om det er grunnlag for å forhandle eller bytte.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('boliglansrente-komplett-guide.html','Se hva som påvirker boliglånsrenten →','problem_route'),
 ('guide-forhandle-rente.html','Se hvordan du kan forhandle renten →','problem_route'),
 ('bor-jeg-bytte-bank.html','Sjekk om bankbytte kan være relevant →','problem_route'),
 ('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='rate_history_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Rate history commercial bridge applied')
