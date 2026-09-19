from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Add relevant authority links from housing pages to the dedicated bridge-financing owner.
sources=[
 ('boliglan.html','Kjøpe før du har solgt?','Hvis du skal kjøpe ny bolig før den gamle er solgt, kan finansieringsbehovet være annerledes enn ved et vanlig boligkjøp.','Les guiden om mellomfinansiering →'),
 ('hvor-mye-kan-jeg-lane-bolig.html','Skal du kjøpe før eksisterende bolig er solgt?','Hvor mye du kan låne er bare én del av bildet når kjøp og salg overlapper. Se også hvordan mellomfinansiering fungerer i perioden mellom boligene.','Se mellomfinansiering ved boligbytte →'),
 ('bytte-bank-boliglan-komplett.html','Boligbytte samtidig med bankbytte?','Hvis du også skal kjøpe ny bolig før den gamle er solgt, bør du skille selve bankbyttet fra behovet for midlertidig finansiering.','Se hva mellomfinansiering innebærer →')
]
for fn,head,body,label in sources:
 p=R/fn;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-bridge-financing-authority="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-bridge-financing-authority']='v1'
 h=s.new_tag('h2');h.string=head;sec.append(h);para=s.new_tag('p');para.string=body;sec.append(para)
 a=s.new_tag('a',href='guide-mellomfinansiering.html');a.string=label;a['data-event']='problem_route';a['data-context']='bridge_financing_gsc_v1';sec.append(a);root.append(sec)
 p.write_text(str(s),encoding='utf-8')
# Reinforce commercial transition on owner without changing title/H1/current factual copy.
p=R/'guide-mellomfinansiering.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-bridge-financing-conversion="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-bridge-financing-conversion']='v1'
h=s.new_tag('h2');h.string='Neste steg når du trenger finansiering mellom to boliger';sec.append(h)
para=s.new_tag('p');para.string='Mellomfinansiering henger sammen med den samlede boligfinansieringen. Når du har oversikt over kjøpesum, forventet salg og eksisterende lån, kan du undersøke hvilke boliglånsalternativer som er relevante for situasjonen din.';sec.append(para)
a=s.new_tag('a',href='sjekk/boliglan/');a.string='Undersøk boliglånsalternativer →';a['data-event']='commercial_route';a['data-context']='bridge_financing_gsc_v1';sec.append(a);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Bridge financing authority cluster applied')
