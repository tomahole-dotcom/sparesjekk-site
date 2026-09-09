from pathlib import Path
from bs4 import BeautifulSoup
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'site-config.json').read_text(encoding='utf-8'))
errors=[]; htmls=list(ROOT.rglob('*.html'))
for p in htmls:
    s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    # internal link integrity
    for a in s.find_all('a',href=True):
        h=a['href'].split('#')[0].split('?')[0]
        if not h or h.startswith(('http://','https://','mailto:','tel:','javascript:','#')): continue
        target=(p.parent/h).resolve()
        if h.endswith('/'): target=target/'index.html'
        if not target.exists(): errors.append(f'BROKEN LINK {p.relative_to(ROOT)} -> {h}')
    # affiliate safety
    for a in s.select('a[rel]'):
        rel=' '.join(a.get('rel',[])) if isinstance(a.get('rel'),list) else str(a.get('rel',''))
        if 'sponsored' in rel and not a.get('href','').startswith(('https://','http://')): errors.append(f'BAD AFFILIATE URL {p.relative_to(ROOT)}')
# config safety
for p in CFG.get('partners',[]):
    if p.get('status')=='active':
        for k in ('name','url','categories'):
            if not p.get(k): errors.append(f'ACTIVE PARTNER MISSING {k}: {p.get("name","?")}')
        if not p.get('approved',False): errors.append(f'ACTIVE BUT NOT APPROVED: {p.get("name","?")}')
        if not p.get('url','').startswith('https://'): errors.append(f'ACTIVE PARTNER URL NOT HTTPS: {p.get("name","?")}')
# SEO hard gate
r=subprocess.run([sys.executable,str(ROOT/'tools/seo_guard.py'),'check'],cwd=ROOT,text=True,capture_output=True)
print(r.stdout.strip())
if r.returncode: errors.append(r.stdout+r.stderr)
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'FULL QA PASS: {len(htmls)} HTML pages; links + partner rules + SEO guard')
