from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Owner: make LTV a useful decision bridge, preserving existing title/H1/factual copy.
p=R/'guide-belaningsgrad.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-ltv-rate-decision-v2="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-ltv-rate-decision-v2']='v1'
h=s.new_tag('h2');h.string='Bruk belåningsgraden når du vurderer boliglånsrenten';sec.append(h)
para=s.new_tag('p');para.string='Belåningsgrad sier hvor stor del av boligverdien som er finansiert med lån. Når boligverdien eller lånesaldoen har endret seg, kan det derfor være nyttig å kontrollere belåningsgraden før du vurderer renteforhandling eller bankbytte.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('guide-forhandle-rente.html','Se hvordan du kan forhandle boliglånsrenten →','problem_route'),
 ('bor-jeg-bytte-bank.html','Sjekk om bankbytte kan være relevant →','problem_route'),
 ('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='ltv_rate_decision_v2';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
# Strengthen contextual authority from bank-switch decision page.
p=R/'bor-jeg-bytte-bank.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-ltv-authority-v2="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-ltv-authority-v2']='v1'
h=s.new_tag('h2');h.string='Har boligverdien eller lånesaldoen endret seg?';sec.append(h)
para=s.new_tag('p');para.append('Før du vurderer et bankbytte kan du kontrollere ');a=s.new_tag('a',href='guide-belaningsgrad.html');a.string='belåningsgraden på boligen';para.append(a);para.append(', siden forholdet mellom lån og boligverdi er relevant når du vurderer finansieringen din.');sec.append(para);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('LTV rate decision cluster v2 applied')
