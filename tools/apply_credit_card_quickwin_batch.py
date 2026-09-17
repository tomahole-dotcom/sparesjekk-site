from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n; return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s): p.write_text(str(s),encoding='utf-8')
def block(s,marker,title,text,links):
 x=s.new_tag('section');x['data-credit-quickwin']=marker
 h=s.new_tag('h2');h.string=title;x.append(h)
 p=s.new_tag('p');p.string=text;x.append(p)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);return x
def add(n,marker,title,text,links):
 p,s=load(n);old=s.select_one(f'[data-credit-quickwin="{marker}"]')
 if old:old.decompose()
 art=s.select_one('article') or s.select_one('main');first=art.find('section');x=block(s,marker,title,text,links)
 first.insert_before(x) if first else art.append(x);save(p,s)
add('cashback-bonus-kredittkort.html','bonus-v1','Kredittkort med bonus: velg etter nettoverdi, ikke bare bonusprosent','Google viser allerede denne siden høyt på flere konkrete bonussøk. Behold derfor bonussporet tydelig: vurder bonus eller cashback mot årsgebyr, valutakostnader, renter og om du faktisk bruker fordelene.',[('kredittkort-match.html','Finn hvilke kortegenskaper som passer bruken din'),('sjekk/kredittkort/','Se aktuelle kredittkortalternativer'),('valutapaslag-kredittkort.html','Sjekk valutapåslag før reisekort velges')])
add('minimumsbetaling-kredittkort.html','paydown-v1','Vil du betale ned kredittkortet raskere?','Når målet er raskere nedbetaling, er minimumsbeløpet bare nedre betalingskrav. Finn saldo, rente og et realistisk høyere månedsbeløp. Har du flere dyre gjeldsposter, bør du vurdere dem samlet før du velger neste steg.',[('nedbetaling-kredittkortgjeld.html','Lag en plan for kredittkortgjelden'),('hva-bor-jeg-gjore-med-dyr-gjeld.html','Finn riktig neste steg for dyr gjeld'),('refinansiere-forbruksgjeld.html','Les når refinansiering kan være relevant')])
add('valutapaslag-kredittkort.html','fx-v1','Valutapåslag på kredittkort: kostnaden som er lett å overse','Ved kortbruk i utenlandsk valuta kan valutapåslaget påvirke den reelle kostnaden. Sammenlign derfor ikke reisekort bare på bonus eller andre fordeler; se kostnadene i sammenheng med hvordan du faktisk bruker kortet.',[('cashback-bonus-kredittkort.html','Sammenlign bonus mot faktiske kostnader'),('kredittkort-match.html','Finn hva du bør prioritere i et kredittkort'),('sjekk/kredittkort/','Se aktuelle kredittkortalternativer')])
for n in ['kredittkort.html','kredittkort-komplett-guide.html','kredittkort-guider.html']:
 p,s=load(n);old=s.select_one('[data-credit-quickwin-link="v1"]')
 if old:old.decompose()
 c=s.select_one('main') or s.body;x=s.new_tag('section');x['class']=['seo-related'];x['data-credit-quickwin-link']='v1'
 h=s.new_tag('h2');h.string='Kredittkort: tre spørsmål med tydelig søkeinteresse';x.append(h)
 ul=s.new_tag('ul')
 for href,label in [('cashback-bonus-kredittkort.html','Bonus og cashback: regn på nettoverdien'),('valutapaslag-kredittkort.html','Valutapåslag ved bruk i utlandet'),('minimumsbetaling-kredittkort.html','Betale ned kredittkort raskere')]:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);c.append(x);save(p,s)
print('Credit-card quick-win batch applied: 6 pages')
