from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json, html, sys
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'site-config.json').read_text(encoding='utf-8'))

# Only generated commercial blocks are touched. Editorial/SEO fields are deliberately untouched.
def active_partners(cat):
    out=[]
    for p in CFG.get('partners',[]):
        if p.get('status')!='active': continue
        if cat not in p.get('categories',[]): continue
        if not p.get('url'): continue
        out.append(p)
    return sorted(out,key=lambda x:(x.get('priority',999),x.get('name','')))

def card(p):
    name=html.escape(p['name']); url=html.escape(p['url'],quote=True)
    desc=html.escape(p.get('description','Se vilkår hos tilbyder.'))
    badges=''.join(f'<span>{html.escape(str(x))}</span>' for x in p.get('badges',[])[:3])
    rep=p.get('representative_example','').strip()
    rep_html=(f'<div class="partner-example"><b>Rente- og kostnadseksempel:</b> {html.escape(rep)}</div>' if rep else '')
    return f'<div class="partner-card" data-partner="{name}"><div><h3>{name}</h3><p>{desc}</p><div class="partner-badges">{badges}</div>{rep_html}</div><a class="partner-cta" href="{url}" rel="sponsored nofollow noopener" target="_blank">Se hos tilbyder →</a></div>'

def render_landing(cat):
    path=ROOT/'sjekk'/cat/'index.html'
    if not path.exists(): raise SystemExit(f'Missing landing: {path}')
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    box=soup.select_one('.partner-preview')
    if not box: raise SystemExit(f'Missing .partner-preview: {path}')
    ps=active_partners(cat)
    disclosure='<div class="partner-disclosure">ANNONSE / REKLAME – vi kan motta provisjon dersom du går videre via en kommersiell lenke</div>'
    if ps:
        body=disclosure+''.join(card(p) for p in ps)+'<p class="partner-note">Sammenlign alltid vilkår og total kostnad før du velger.</p>'
    else:
        body=disclosure+'<div class="partner-card"><div><h3>Ingen aktive partnere ennå</h3><p>Godkjente tilbydere publiseres her når avtale, sporingslenke og nødvendig markedsføringsinformasjon er kontrollert.</p></div></div><p class="partner-note">Ingen ikke-godkjente tilbydere, renter eller vilkår publiseres.</p>'
    frag=BeautifulSoup(body,'html.parser')
    box.clear()
    for node in list(frag.contents): box.append(node)
    path.write_text(str(soup),encoding='utf-8')
    return len(ps)

def sitemap():
    # Keep public HTML URLs except URLs explicitly consolidated into another canonical page.
    urls=[]
    base=CFG['site']['base_url'].rstrip('/')
    excluded=set(CFG.get('automation',{}).get('sitemap_exclude',[]))
    for p in sorted(ROOT.rglob('*.html')):
        rel=p.relative_to(ROOT).as_posix()
        if rel.startswith('tools/') or rel.startswith('.') or rel in excluded: continue
        if rel=='index.html': url=base+'/'
        elif rel.endswith('/index.html'): url=base+'/'+rel[:-10]
        else: url=base+'/'+rel
        urls.append(url)
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{html.escape(u)}</loc></url>\n' for u in urls)+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(xml,encoding='utf-8')
    return len(urls)

counts={c['key']:render_landing(c['key']) for c in CFG['categories']}
print('Partner cards:',counts)
print('Sitemap URLs:',sitemap())
