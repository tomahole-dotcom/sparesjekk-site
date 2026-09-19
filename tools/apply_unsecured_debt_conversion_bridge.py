from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'gjeldsregisteret-forbrukslan.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-unsecured-debt-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-unsecured-debt-conversion']='v1'
h=s.new_tag('h2');h.string='Har du fått oversikt over den usikrede gjelden?';sec.append(h)
p1=s.new_tag('p');p1.string='En gjeldsoversikt er først nyttig når du bruker den til å vurdere neste steg. Har du flere dyre usikrede lån eller kreditter, kan det være relevant å undersøke om de kan samles eller refinansieres. Hvis du bare trenger oversikten, trenger du ikke gå videre til en lånesøknad.';sec.append(p1)
ul=s.new_tag('ul')
for href,label,event in [
 ('refinansiere-forbruksgjeld.html','Jeg har dyr usikret gjeld – se refinansieringssporet →','problem_route'),
 ('sjekk/forbrukslan/?intent=refinansiere','Jeg vil undersøke faktiske refinansieringsalternativer →','commercial_route'),
 ('samle-smalan-kredittkortgjeld.html','Jeg vil forstå hva det innebærer å samle smålån og kredittgjeld →','problem_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='unsecured_debt_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Unsecured debt conversion bridge applied')
