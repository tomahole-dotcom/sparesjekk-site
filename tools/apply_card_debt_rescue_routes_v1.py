from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('kredittkort-minstebelop-fellen.html','minimum_trap'),
 ('minimumsbetaling-kredittkort.html','minimum_payment')
]
for rel,ctx in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-card-debt-rescue="v1"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-card-debt-rescue']='v1';sec['class']=['card-debt-rescue']
 h=s.new_tag('h2');h.string='Betaler du renter på kredittkortsaldoen?';sec.append(h)
 q=s.new_tag('p');q.string='Da er målet å få kontroll på gjelden – ikke å finne et nytt kredittkort. Start med nedbetalingssporet. Hvis du har flere dyre usikrede lån eller kortsaldoer, kan du deretter undersøke om refinansiering faktisk gir lavere effektiv rente og total kostnad.';sec.append(q)
 p1=s.new_tag('p');a1=s.new_tag('a',href='nedbetaling-kredittkortgjeld.html');a1.string='Se nedbetalingssporet →';a1['data-revenue-event']='problem_route';a1['data-revenue-context']='card_debt_'+ctx;p1.append(a1);sec.append(p1)
 p2=s.new_tag('p');a2=s.new_tag('a',href='sjekk/forbrukslan/?intent=refinansiere');a2['class']=['cta'];a2['data-revenue-event']='commercial_route';a2['data-revenue-context']='card_debt_'+ctx;a2.string='Undersøk refinansieringsalternativer →';p2.append(a2);sec.append(p2)
 n=s.new_tag('p');n['class']=['small'];n.string='Gå bare videre hvis målet er å samle eller refinansiere eksisterende dyr gjeld. Sammenlign effektiv rente, gebyrer, løpetid og total kostnad.';sec.append(n)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('Card debt rescue:',rel)
