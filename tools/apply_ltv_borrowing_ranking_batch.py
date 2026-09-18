from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');old=s.select_one(f'[data-ltv-borrow-ranking="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-ltv-borrow-ranking']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h);q=s.new_tag('p');q.string=body;sec.append(q);ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='ltv_borrow_gsc_v1';li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
add('guide-belaningsgrad.html','ltv-v1','Belåningsgrad eller låneevne? Det er to forskjellige spørsmål','Belåningsgrad handler om forholdet mellom lån og boligverdi. Hvis spørsmålet ditt egentlig er hvor mye du kan låne, bør du gå videre til låneevne i stedet for å blande de to vurderingene.',[('hvor-mye-kan-jeg-lane-bolig.html','Se hva som påvirker hvor mye du kan låne →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('hvor-mye-kan-jeg-lane-bolig.html','capacity-v2','Fra «hvor mye kan jeg låne?» til et konkret neste steg','Når du har oversikt over hva som påvirker låneevnen, kan du skille mellom egenkapital, boligverdi og selve finansieringen. Det gjør det enklere å velge riktig neste steg.',[('guide-belaningsgrad.html','Forstå belåningsgrad og boligverdi →','problem_route'),('mangler-egenkapital-bolig.html','Mangler du egenkapital? →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('boliglan.html','hub-v1','Leter du etter belåningsgrad eller hvor mye du kan låne?','Bruk den spesifikke guiden for spørsmålet ditt. Da får du et mer presist svar og en kortere vei videre dersom du vil undersøke boliglån.',[('guide-belaningsgrad.html','Belåningsgrad →','problem_route'),('hvor-mye-kan-jeg-lane-bolig.html','Hvor mye kan jeg låne? →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
print('LTV and borrowing capacity ranking batch applied: 3 pages')
