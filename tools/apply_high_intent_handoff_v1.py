from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('avslag-refinansiering-hva-na.html','sjekk/forbrukslan/?intent=refinansiere','refi_rejected','Undersøk andre refinansieringsalternativer →'),
 ('refinansiering-tilbudssjekk.html','sjekk/forbrukslan/?intent=refinansiere','refi_offer','Se refinansieringsalternativer →'),
 ('tilbudssjekk-refinansiering.html','sjekk/forbrukslan/?intent=refinansiere','refi_offer_check','Undersøk refinansieringsalternativer →'),
 ('sammenligne-forbrukslan.html','sjekk/forbrukslan/?intent=nytt','consumer_compare','Se aktuelle lånealternativer →'),
 ('sammenligne-kredittkort.html','sjekk/kredittkort/?intent=match','card_compare','Se kredittkortalternativer →'),
 ('boliglansrente-for-hoy.html','sjekk/boliglan/?intent=sammenligne','mortgage_rate_high','Sammenlign boliglånsalternativer →'),
 ('banken-satte-ikke-ned-renten.html','sjekk/boliglan/?intent=sammenligne','mortgage_rate_no_cut','Undersøk boliglånsalternativer →')
]
for rel,href,ctx,label in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-high-intent-handoff="v1"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-high-intent-handoff']='v1';sec['class']=['high-intent-handoff']
 h=s.new_tag('h2');h.string='Klar for neste steg?';sec.append(h)
 q=s.new_tag('p');q.string='Bruk informasjonen over som beslutningsgrunnlag. Hvis du vil undersøke faktiske alternativer, kan du gå videre til Sparesjekks matcher. Du velger selv om du vil følge en kommersiell partnerlenke.';sec.append(q)
 a=s.new_tag('a',href=href);a['class']=['cta'];a['data-revenue-event']='commercial_route';a['data-revenue-context']=ctx;a.string=label;sec.append(a)
 n=s.new_tag('p');n['class']=['small'];n.string='Matcher-siden viser kommersielle partnere og merker partnerlenker som annonse/reklame.';sec.append(n)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('High-intent handoff:',rel)
