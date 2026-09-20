from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Add a non-sensitive source token to internal Sparesjekken entry links.
for p in R.rglob('*.html'):
 if '/sjekk/' in p.as_posix() or p.name=='ta-sparesjekken.html': continue
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');changed=False
 for a in s.select('a[href^="ta-sparesjekken.html"][data-revenue-context]'):
  ctx=a.get('data-revenue-context','').strip()
  if ctx:
   a['href']='ta-sparesjekken.html?src='+ctx;changed=True
 if changed:p.write_text(str(s),encoding='utf-8')
# Enhance Ta Sparesjekken event attribution without sending financial answers.
p=R/'ta-sparesjekken.html';t=p.read_text(encoding='utf-8')
old="var state={},step=1,steps=5;"
new="var state={},step=1,steps=5;var entrySource=(new URLSearchParams(location.search).get('src')||'direct').slice(0,80);"
if old not in t and new not in t: raise SystemExit('Ta Sparesjekken state marker missing')
t=t.replace(old,new)
old2="function event(n,p){if(typeof gtag==='function')gtag('event',n,Object.assign({source_path:location.pathname},p||{}))}"
new2="function event(n,p){if(typeof gtag==='function')gtag('event',n,Object.assign({source_path:location.pathname,entry_source:entrySource},p||{}))}"
if old2 not in t and new2 not in t: raise SystemExit('Event marker missing')
t=t.replace(old2,new2)
p.write_text(t,encoding='utf-8')
print('Savings Check attribution applied')
