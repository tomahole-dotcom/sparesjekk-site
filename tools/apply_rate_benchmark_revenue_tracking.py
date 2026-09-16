from pathlib import Path
from bs4 import BeautifulSoup

p=Path('min-rente-vs-markedet.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
result=soup.select_one('#result')
if not result:
    raise SystemExit('Missing #result')
box=result.select_one('#commercial')
if not box:
    raise SystemExit('Missing result #commercial')
cta=box.select_one('#commercialCta')
if not cta:
    raise SystemExit('Missing #commercialCta')
cta['data-revenue-event']='commercial_route'
cta['data-revenue-context']='mortgage_rate_benchmark_result'
cta['href']='sjekk/boliglan/'
cta.string='Sjekk aktuelle boliglånstilbud →'
p.write_text(str(soup),encoding='utf-8')
print('Mortgage benchmark result Revenue tracking applied')
