from pathlib import Path
from bs4 import BeautifulSoup

p=Path('gjeldsmiks-sjekk.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
result=soup.select_one('#result')
if not result:
    raise SystemExit('Missing #result')
box=result.select_one('.ad-next')
if not box:
    raise SystemExit('Missing result .ad-next')
cta=box.select_one('#commercialCta')
if not cta:
    raise SystemExit('Missing #commercialCta')
cta['data-revenue-event']='commercial_route'
cta['data-revenue-context']='debt_mix_result'
cta['href']='sjekk/forbrukslan/'
print('Debt mix result Revenue tracking applied')
p.write_text(str(soup),encoding='utf-8')
