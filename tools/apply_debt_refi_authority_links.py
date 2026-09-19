from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
blocks={
'refinansiere-forbruksgjeld.html':[('gjeldsregisteret-forbrukslan.html','Start med å få oversikt over usikret gjeld'),('samle-smalan-kredittkortgjeld.html','Har du flere smålån og kredittkort?')],
'samle-smalan-kredittkortgjeld.html':[('gjeldsregisteret-forbrukslan.html','Sjekk først hvilke usikrede lån og kreditter du har'),('refinansiere-forbruksgjeld.html','Se hvordan refinansiering av forbruksgjeld fungerer')],
'effektiv-rente-forbrukslan.html':[('refinansiere-forbruksgjeld.html','Har du allerede dyr forbruksgjeld? Se refinansiering'),('gjeldsregisteret-forbrukslan.html','Få oversikt over usikret gjeld')],
'betalingsproblemer-hva-gjor-jeg.html':[('gjeldsregisteret-forbrukslan.html','Få oversikt over usikret gjeld'),('refinansiere-forbruksgjeld.html','Les om refinansiering av forbruksgjeld')]
}
for name,links in blocks.items():
 p=R/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-debt-refi-authority="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-debt-refi-authority']='v1'
 h=s.new_tag('h2');h.string='Fra gjeldsoversikt til neste steg';sec.append(h)
 para=s.new_tag('p');para.string='Oversikt og refinansiering er to forskjellige steg. Start med oversikt hvis du ikke kjenner gjelden din; vurder refinansiering først når målet er å samle eller redusere kostnaden på eksisterende usikret gjeld.';sec.append(para)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Debt/refinance authority links applied')
