from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('cashback-bonus-kredittkort.html','bonus_card'),
 ('kredittkort-utlandet-dyrt.html','travel_card'),
 ('kredittkort-komplett-guide.html','card_guide')
]
for rel,ctx in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for a in s.find_all('a',href='sjekk/kredittkort/'):
  a['href']='sjekk/kredittkort/?intent=match'
  a['data-revenue-event']='commercial_route';a['data-revenue-context']=ctx
 # Add debt safety beside commercial card routes once.
 marker=s.select_one(f'[data-card-debt-safety="{ctx}"]')
 if marker: marker.decompose()
 first=s.find('a',href='sjekk/kredittkort/?intent=match')
 if first:
  note=s.new_tag('p');note['data-card-debt-safety']=ctx;note['class']=['small']
  note.string='Har du en saldo som allerede løper renter, bør du prioritere nedbetaling eller refinansiering av eksisterende dyr gjeld fremfor å velge et nytt kredittkort.'
  first.parent.insert_after(note)
 p.write_text(str(s),encoding='utf-8');print('Safe card handoff:',rel)
# Cost calculator needs result-dependent routing, so leave its existing dynamic logic untouched.
