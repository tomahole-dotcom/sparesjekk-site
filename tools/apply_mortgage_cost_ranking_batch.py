from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-mortgage-cost-ranking="{marker}"]')
 if old: old.decompose()
 root=s.select_one('article') or s.select_one('main'); sec=s.new_tag('section');sec['data-mortgage-cost-ranking']=marker
 h=s.new_tag('h2');h.string=title;sec.append(h);q=s.new_tag('p');q.string=body;sec.append(q)
 ul=s.new_tag('ul')
 for href,label,event in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']='mortgage_cost_gsc_v1';li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
add('boliglansrente-komplett-guide.html','rate-rank-v1','Boliglånsrente: fra renteinformasjon til et konkret valg','Når du kjenner renten din, er neste nyttige steg å måle hva en renteforskjell betyr i kroner og deretter vurdere om du bør forhandle, sammenligne eller bytte.',[('boliglanskalkulator-renteforskjell.html','Regn ut renteforskjellen i kroner →','problem_route'),('guide-forhandle-rente.html','Forhandle med banken →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('nedbetalingstid-boliglan.html','term-rank-v1','Nedbetalingstid på boliglån: se månedskostnad og total kostnad sammen','Kortere og lengre nedbetalingstid påvirker både månedsbeløpet og hvor lenge du betaler renter. Vurder derfor løpetid sammen med rente og total kostnad før du endrer lånet.',[('boliglanskalkulator-renteforskjell.html','Se hva en renteforskjell betyr →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('annuitetslan-serielan.html','repayment-rank-v1','Annuitetslån eller serielån: sammenlign mer enn lånetypen','Forskjellen i nedbetalingsprofil er nyttig å forstå, men rente og løpetid påvirker også kostnaden. Hvis du vurderer nytt eller flyttet boliglån, sammenlign hele finansieringen.',[('nedbetalingstid-boliglan.html','Se hvordan nedbetalingstid påvirker lånet →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
print('Mortgage cost ranking batch applied: 3 pages')
