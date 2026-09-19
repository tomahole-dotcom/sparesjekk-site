from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
sources={
'guide-effektiv-nominell-rente.html':('Boliglånsrente i praksis','For boliglån bør du se rentebegrepene sammen med hva som faktisk påvirker boliglånsrenten.'),
'guide-sammenligne-boliglan.html':('Sammenlign renten før du velger','Når du sammenligner boliglån er renten en sentral del av totalkostnaden.'),
'bytte-bank-boliglan-komplett.html':('Er boliglånsrenten grunnen til bankbyttet?','Hvis målet er lavere lånekostnad, start med å forstå og sammenligne boliglånsrenten før du vurderer flytting.'),
'flytte-boliglan.html':('Sjekk renten før du flytter','En låneflytting bør bygge på en reell sammenligning av boliglånsrenten og øvrige kostnader.'),
'bor-jeg-bytte-bank.html':('Er renten hovedproblemet?','Hvis du vurderer bankbytte på grunn av boliglånet, sammenlign først renten og hva som påvirker den.'),
'oke-boliglanet.html':('Renten betyr mer når lånet øker','Et større boliglån gjør rente og totalkostnad viktigere å vurdere før du bestemmer deg.'),
'nedbetalingstid-boliglan.html':('Se rente og nedbetalingstid sammen','Rente og løpetid påvirker kostnaden på ulike måter og bør vurderes samlet.')
}
for name,(head,body) in sources.items():
 p=R/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-mortgage-rate-authority-v2="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-mortgage-rate-authority-v2']='v1'
 h=s.new_tag('h2');h.string=head;sec.append(h)
 para=s.new_tag('p');para.string=body+' ';a=s.new_tag('a',href='boliglansrente-komplett-guide.html');a.string='Se komplett guide til boliglånsrente →';para.append(a);sec.append(para);root.append(sec)
 p.write_text(str(s),encoding='utf-8')
print('Mortgage rate authority v2 applied')
