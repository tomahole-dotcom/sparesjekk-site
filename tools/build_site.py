from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json, html, sys
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'site-config.json').read_text(encoding='utf-8'))

# Generated commercial blocks and presentation helpers are touched here.
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

def apply_priority_internal_links():
    # GSC-driven, conservative internal-link reinforcement. No title/meta/H1 changes.
    links=[
        # Highest-impression opportunity: boliglån uten nok egenkapital.
        ('boliglan.html','boliglan-uten-egenkapital.html','Boliglån uten egenkapital: se hvilke muligheter som finnes'),
        ('boliglan-guider.html','boliglan-uten-egenkapital.html','Guide: boliglån uten nok egenkapital'),
        ('egenkapital-bolig.html','boliglan-uten-egenkapital.html','Mangler du nok egenkapital? Se mulighetene og risikoen'),
        ('hvor-mye-kan-jeg-lane-bolig.html','boliglan-uten-egenkapital.html','Boliglån uten nok egenkapital – hva kan være aktuelt?'),
        ('boliglan-uten-egenkapital.html','belaningsgrad-sjekk.html','Sjekk belåningsgraden din med gratisverktøyet'),
        # Strengthen closely related high-impression mortgage pages.
        ('boliglan.html','egenkapital-bolig.html','Egenkapital til bolig – hva teller og hvor mye trenger du?'),
        ('boliglan-guider.html','egenkapital-bolig.html','Guide til egenkapital ved boligkjøp'),
        ('boliglan-uten-egenkapital.html','egenkapital-bolig.html','Se hvordan egenkapitalen beregnes ved boligkjøp'),
        ('boliglan.html','hvor-mye-can-jeg-lane-bolig.html','Se hva som påvirker hvor mye du kan låne til bolig'),
        ('egenkapital-bolig.html','hvor-mye-kan-jeg-lane-bolig.html','Hvor mye kan du låne? Se hvilke faktorer banken vurderer'),
        # GSC opportunity: medlåntaker/medlåntakere. Reinforce from core mortgage-intent pages.
        ('boliglan.html','medlantaker-boliglan.html','Medlåntaker på boliglån – ansvar, muligheter og risiko'),
        ('hvor-mye-can-jeg-lane-bolig.html','medlantaker-boliglan.html','Når kan medlåntaker være relevant for lånerammen?'),
        # Bank switching cluster.
        ('flytte-boliglan.html','bytte-bank-boliglan-komplett.html','Komplett guide til å bytte bank med boliglån'),
        ('guide-bytte-bank-steg.html','bytte-bank-boliglan-komplett.html','Se hele guiden til bankbytte og boliglån'),
        ('boliglan.html','bytte-bank-boliglan-komplett.html','Vurderer du bankbytte? Se komplett guide'),
        # Traffic Engine: route informational bank-switch intent into the decision tool.
        ('guide-bytte-bank-steg.html','bankbytte-break-even.html','Regn ut når et bankbytte faktisk går i pluss'),
        ('bytte-bank-boliglan-komplett.html','bankbytte-break-even.html','Sjekk om rentebesparelsen dekker kostnadene ved bankbytte'),
        ('flytte-boliglan.html','bankbytte-break-even.html','Test bankbyttet med break-even-kalkulatoren'),
        # Effective vs nominal rate cluster.
        ('forbrukslan.html','guide-effektiv-nominell-rente.html','Effektiv eller nominell rente? Se hva du faktisk bør sammenligne'),
        ('guide-refinansiering.html','guide-effektiv-nominell-rente.html','Forstå forskjellen på effektiv og nominell rente'),
        ('refinansiere-forbruksgjeld.html','guide-effektiv-nominell-rente.html','Sammenlign tilbud på effektiv rente – ikke bare nominell rente'),
        # Traffic Engine: turn rate-learning intent into a personal krone calculation.
        ('guide-effektiv-nominell-rente.html','boliglanskalkulator-renteforskjell.html','Se hva en renteforskjell betyr i kroner for boliglånet'),
        ('guide-renteforskjell-kroner.html','boliglanskalkulator-renteforskjell.html','Regn ut renteforskjellen på ditt eget boliglån'),
        ('boliglanskalkulator-renteforskjell.html','min-rente-vs-markedet.html','Sammenlign renten din med markedet'),
        # Refinancing decision path: guide -> calculator -> post-offer check.
        ('guide-refinansiering.html','refinansiering-kalkulator.html','Test refinansiering med dine egne tall'),
        ('refinansiere-forbruksgjeld.html','refinansiering-kalkulator.html','Regn på mulig effekt av refinansiering'),
        ('refinansiering-kalkulator.html','tilbudssjekk-refinansiering.html','Har du fått et tilbud? Kontroller om det faktisk er bedre'),
        # Discovery for the broad problem-first router from an established hub.
        ('guider.html','problemloser.html','Usikker på hvilken guide du trenger? Start med Problemløseren'),
    ]
    changed=0
    for rel,href,label in links:
        path=ROOT/rel
        if not path.exists(): continue
        soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
        if soup.find('a',href=href): continue
        container=soup.select_one('article') or soup.select_one('main')
        if not container: continue
        p=soup.new_tag('p')
        p['class']=['seo-priority-link']
        p['data-seo-priority']='gsc-20260913'
        strong=soup.new_tag('strong'); strong.string='Relatert: '
        a=soup.new_tag('a',href=href); a.string=label+' →'
        p.append(strong); p.append(a)
        disclaimer=container.select_one('.disclaimer,.article-note')
        if disclaimer: disclaimer.insert_before(p)
        else: container.append(p)
        path.write_text(str(soup),encoding='utf-8'); changed+=1
    return changed

def apply_design_layer():
    changed=0
    design_names=['design-v36.css','design-v37.css','design-v38.css','design-v39.css','design-v40.css','design-v41.css','design-v42.css','design-v43.css']
    old_design_names={'design-v34.css','design-v35.css'}
    hero_classes={
        'boliglan.html':'premium-mortgage',
        'forbrukslan.html':'premium-consumer',
        'kredittkort.html':'premium-card',
        'omstartslan.html':'premium-restart',
    }
    for path in sorted(ROOT.rglob('*.html')):
        rel=path.relative_to(ROOT).as_posix()
        if rel.startswith('tools/') or rel.startswith('.'):
            continue
        soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
        dirty=False
        for link in list(soup.find_all('link',href=True)):
            href=link.get('href','')
            if any(old in href for old in old_design_names):
                link.decompose(); dirty=True
        depth=len(path.relative_to(ROOT).parents)-1
        for design_name in design_names:
            if not soup.find('link',href=lambda x,n=design_name:isinstance(x,str) and n in x):
                href=('../'*depth)+design_name
                link=soup.new_tag('link',rel='stylesheet',href=href)
                if soup.head: soup.head.append(link); dirty=True
        header=soup.select_one('header.header'); nav=header.select_one('.topnav') if header else None
        if header and nav and not header.select_one('.menu-btn'):
            btn=soup.new_tag('button'); btn['class']=['menu-btn']; btn['aria-label']='Åpne meny'; btn['type']='button'; btn['onclick']="document.querySelector('.topnav').classList.toggle('open')"; btn.string='☰'; nav.insert_before(btn); dirty=True
        if nav:
            existing=nav.find('a',string=lambda x:isinstance(x,str) and x.strip()=='Tilbudssjekken')
            wanted=('../'*depth)+'tilbudssjekk-refinansiering.html'
            if existing:
                if existing.get('href')!=wanted: existing['href']=wanted; dirty=True
            else:
                a=soup.new_tag('a',href=wanted); a.string='Tilbudssjekken'
                guide=nav.find('a',string=lambda x:isinstance(x,str) and x.strip()=='Guider')
                if guide: guide.insert_before(a)
                else: nav.append(a)
                dirty=True
        if rel in hero_classes:
            hero=soup.select_one('.premium-hero')
            if hero:
                classes=list(hero.get('class',[])); marker=hero_classes[rel]
                if marker not in classes: classes.append(marker); hero['class']=classes; dirty=True
        if rel=='guider.html' and soup.body:
            classes=list(soup.body.get('class',[]))
            if 'guide-library-v35' not in classes: classes.append('guide-library-v35'); soup.body['class']=classes; dirty=True
        if dirty: path.write_text(str(soup),encoding='utf-8'); changed+=1
    return changed

def sitemap():
    urls=[]; base=CFG['site']['base_url'].rstrip('/'); excluded=set(CFG.get('automation',{}).get('sitemap_exclude',[]))
    for p in sorted(ROOT.rglob('*.html')):
        rel=p.relative_to(ROOT).as_posix()
        if rel.startswith('tools/') or rel.startswith('.') or rel in excluded: continue
        if rel=='index.html': url=base+'/'
        elif rel.endswith('/index.html'): url=base+'/'+rel[:-10]
        else: url=base+'/'+rel
        urls.append(url)
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{html.escape(u)}</loc></url>\n' for u in urls)+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(xml,encoding='utf-8'); return len(urls)

counts={c['key']:render_landing(c['key']) for c in CFG['categories']}
print('Partner cards:',counts)
print('Priority internal links:',apply_priority_internal_links())
print('Design-normalized pages:',apply_design_layer())
print('Sitemap URLs:',sitemap())