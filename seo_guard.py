from pathlib import Path
from bs4 import BeautifulSoup
import json, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]
SNAP=ROOT/'seo-baseline.json'

def norm(v): return ' '.join((v or '').split())
def extract(p):
    s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    def meta(**kw):
        x=s.find('meta',attrs=kw); return norm(x.get('content')) if x else ''
    can=s.find('link',rel='canonical')
    h1=[norm(x.get_text(' ',strip=True)) for x in s.find_all('h1')]
    schemas=[norm(x.string or x.get_text()) for x in s.find_all('script',type='application/ld+json')]
    return {'title':norm(s.title.string if s.title else ''),'description':meta(name='description'),
      'canonical':norm(can.get('href')) if can else '', 'robots':meta(name='robots'), 'h1':h1,
      'schemas':schemas}

def allseo():
    return {str(p.relative_to(ROOT)):extract(p) for p in sorted(ROOT.rglob('*.html'))}
mode=sys.argv[1] if len(sys.argv)>1 else 'check'
if mode=='snapshot':
    SNAP.write_text(json.dumps(allseo(),ensure_ascii=False,indent=2),encoding='utf-8'); print(f'SEO baseline saved: {len(allseo())} pages'); sys.exit()
base=json.loads(SNAP.read_text(encoding='utf-8')); cur=allseo(); errors=[]
for f,old in base.items():
    if f not in cur: errors.append(f'MISSING PAGE: {f}'); continue
    if cur[f]!=old: errors.append(f'SEO CHANGED: {f}')
for f,v in cur.items():
    if not v['title'] or not v['description'] or not v['canonical'] or not v['h1']: errors.append(f'INCOMPLETE SEO: {f}')
    if f not in base: print('NEW PAGE:',f)
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'SEO GUARD PASS: {len(cur)} pages; existing SEO unchanged')
