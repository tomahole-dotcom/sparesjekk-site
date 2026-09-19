from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'rentemote-hva-betyr-det.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-rate-meeting-bridge="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-rate-meeting-bridge']='v1'
h=s.new_tag('h2');h.string='Hva betyr rentebeslutningen for ditt boliglån?';sec.append(h)
para=s.new_tag('p');para.string='Et rentemøte avgjør ikke automatisk hvilken boliglånsrente du får. Bankenes priser og din egen situasjon kan avvike. Bruk derfor rentebeslutningen som et signal til å kontrollere hva du faktisk betaler.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('boliglansrente-komplett-guide.html','Forstå og vurder boliglånsrenten din →','problem_route'),
 ('bor-jeg-bytte-bank.html','Sjekk om bankbytte kan være relevant →','problem_route'),
 ('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='rate_meeting_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Rate meeting conversion bridge applied')
