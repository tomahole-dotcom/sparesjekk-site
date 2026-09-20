from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'guide-bytte-bank.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
# Upgrade the existing contextual comparison link; do not add duplicate sales sections.
links=[a for a in s.find_all('a') if a.get('href') in ('sjekk/boliglan/','sjekk/boliglan/?intent=sammenligne') and ('Sammenlign boliglån' in a.get_text() or 'Innhent og sammenlign boliglånstilbud' in a.get_text())]
if not links: raise SystemExit('Expected bank-switch comparison link missing')
for a in links:
 a['href']='sjekk/boliglan/?intent=sammenligne'
 a['data-revenue-event']='commercial_route'
 a['data-revenue-context']='bank_switch_decision'
 a['class']=list(dict.fromkeys((a.get('class') or [])+['cta']))
 # Clear destination expectation without changing the surrounding SEO copy.
 a.string='Innhent og sammenlign boliglånstilbud →'
p.write_text(str(s),encoding='utf-8')
print('Bank-switch intent handoff applied')
