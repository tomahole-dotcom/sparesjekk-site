from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(path, marker, heading, text, links):
 p=R/path;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select(f'[{marker}="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec[marker]='v1'
 h=s.new_tag('h2');h.string=heading;sec.append(h);para=s.new_tag('p');para.string=text;sec.append(para)
 if links:
  ul=s.new_tag('ul')
  for href,label,etype in links:
   li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='payment_relief_authority_v2';li.append(a);ul.append(li)
  sec.append(ul)
 root.append(sec);p.write_text(str(s),encoding='utf-8')
add('guide-avdragsfrihet.html','data-payment-relief-authority-v2','Avdragsfrihet eller lavere månedskostnad?','Avdragsfrihet betyr at du i en periode normalt ikke betaler avdrag, men rentekostnader og andre avtalte kostnader kan fortsatt løpe. Hvis målet først og fremst er å få bedre kontroll på månedskostnaden, bør du også se på løpetid, rente og om lånet fortsatt passer situasjonen din.',[
 ('nedbetalingstid-boliglan.html','Se hvordan nedbetalingstid påvirker lånet →','problem_route'),
 ('boliglan-terminbelop.html','Forstå hva som påvirker terminbeløpet →','problem_route'),
 ('guide-forhandle-rente.html','Se hvordan du kan vurdere boliglånsrenten →','problem_route'),
 ('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('nedbetalingstid-boliglan.html','data-payment-relief-support-v2','Trenger du midlertidig lavere belastning?','Hvis behovet er midlertidig og gjelder avdragene, kan det være relevant å forstå hvordan avdragsfrihet fungerer før du endrer løpetiden.',[
 ('guide-avdragsfrihet.html','Les om avdragsfrihet på boliglån →','problem_route')])
add('betalingsproblemer-hva-gjor-jeg.html','data-payment-relief-problem-v2','Gjelder problemet boliglånet?','Hvis problemet er midlertidig betalingsevne på boliglånet, kan du først lese hva avdragsfrihet innebærer. Ved mer omfattende gjeldsproblemer bør du bruke alternativene som passer situasjonen din på denne siden.',[
 ('guide-avdragsfrihet.html','Forstå avdragsfrihet på boliglån →','problem_route')])
print('Payment relief authority v2 applied')
