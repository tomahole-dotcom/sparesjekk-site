from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
p=R/'valutapaslag-kredittkort.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-fx-card-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-fx-card-conversion']='v1'
h=s.new_tag('h2');h.string='Bruker du kortet mye i utlandet?';sec.append(h)
para=s.new_tag('p');para.string='Valutapåslag er én av flere kostnader som kan ha betydning når du velger kredittkort. Se også på gebyrer, renter og hvordan du faktisk bruker kortet før du vurderer et alternativ.';sec.append(para)
ul=s.new_tag('ul')
for href,label,etype in [
 ('kredittkort-komplett-guide.html','Se hva du bør sammenligne på kredittkort →','problem_route'),
 ('sjekk/kredittkort/','Undersøk kredittkortalternativer →','commercial_route'),
 ('kontantuttak-kredittkort.html','Bruker du kontanter i utlandet? Se kostnader ved kontantuttak →','problem_route')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-event']=etype;a['data-context']='fx_fee_card_gsc_v1';li.append(a);ul.append(li)
sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
# Strengthen contextual authority from the general card guide only; deliberately do not touch cashback/bonus page.
p=R/'kredittkort-komplett-guide.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-fx-card-authority="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-fx-card-authority']='v1'
h=s.new_tag('h2');h.string='Kortbruk i utlandet';sec.append(h)
para=s.new_tag('p');para.append('Skal kortet brukes i utenlandsk valuta, bør du også se på ');a=s.new_tag('a',href='valutapaslag-kredittkort.html');a.string='valutapåslag og kostnaden ved kortbruk i utlandet';para.append(a);para.append('.');sec.append(para);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('FX fee credit-card conversion applied')
