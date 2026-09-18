from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n;return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s):p.write_text(str(s),encoding='utf-8')
def section(n,marker,title,text,links):
 p,s=load(n);old=s.select_one(f'[data-debt-search-revenue="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main');x=s.new_tag('section');x['data-debt-search-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=text;x.append(q);ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']=marker
  li.append(a);ul.append(li)
 x.append(ul);root.append(x);save(p,s)
section('gjeldsregisteret-forbrukslan.html','overview-v1','Fra gjeldsoversikt til riktig handling','Søket etter gjeldsregister eller usikret gjeld kan bety alt fra ren kontroll av opplysninger til et konkret behov for å redusere dyr gjeld. Ikke gå til ny finansiering bare fordi du har hentet oversikten; velg neste steg ut fra hva oversikten faktisk viser.',[
 ('gjeldsmiks-sjekk.html','Se hvilke deler av gjelden som koster mest','problem_route'),
 ('hva-bor-jeg-gjore-med-dyr-gjeld.html','Dyr gjeld? Finn riktig refinansieringsspor','problem_route'),
 ('betalingsproblemer-hva-gjor-jeg.html','Har du betalingsproblemer? Start her','problem_route')])
section('refinansiere-forbruksgjeld.html','refi-credit-v1','Kredittkortgjeld er et tydelig refinansieringssignal','Har du flere kredittkort eller annen usikret gjeld, er målet ikke bare én faktura. Sammenlign om et nytt tilbud faktisk gir bedre effektiv rente og total kostnad. Når du har før-bildet klart kan du gå direkte til relevante refinansieringsalternativer.',[
 ('gjeldsmiks-sjekk.html','Få før-bildet av gjelden','problem_route'),
 ('sjekk/forbrukslan/?intent=refinansiere','Sammenlign refinansieringsalternativer','commercial_route')])
section('samle-smalan-kredittkortgjeld.html','consolidate-v1','Vil du faktisk samle kredittkortgjeld og smålån?','Når du kjenner saldo, rente og månedskostnad på gjelden, kan du sammenligne refinansieringsalternativer mot dagens situasjon. Gå bare videre hvis målet er å undersøke en reell samleløsning.',[
 ('refinansiering-kalkulator.html','Regn før og etter','problem_route'),
 ('sjekk/forbrukslan/?intent=refinansiere','Undersøk alternativer for å samle gjelden','commercial_route')])
for n in ['forbrukslan.html','forbrukslan-guider.html','kredittkort.html','kredittkort-guider.html']:
 p,s=load(n);old=s.select_one('[data-debt-search-revenue-link="v1"]')
 if old:old.decompose()
 root=s.select_one('main') or s.body;x=s.new_tag('section');x['class']=['seo-related'];x['data-debt-search-revenue-link']='v1'
 h=s.new_tag('h2');h.string='Fra gjeldsoversikt til handling';x.append(h);ul=s.new_tag('ul')
 for href,label in [('gjeldsregisteret-forbrukslan.html','Gjeldsregisteret og usikret gjeld'),('samle-smalan-kredittkortgjeld.html','Samle smålån og kredittkortgjeld'),('refinansiere-forbruksgjeld.html','Vurder refinansiering av forbruksgjeld')]:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 x.append(ul);root.append(x);save(p,s)
print('Debt search-to-revenue batch applied: 7 pages')
