from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
PAGES={
 'sjekk/forbrukslan/index.html':{
   'title':'Hva vil du løse nå?',
   'lead':'Velg situasjonen som ligner mest. Vi viser de kommersielle alternativene som er relevante for dette sporet – uten å love rente, godkjenning eller besparelse.',
   'choices':[
     ('refinansiere','Jeg vil samle eller refinansiere gjeld','Gå til aktuelle alternativer'),
     ('nytt-lan','Jeg vil undersøke et nytt forbrukslån','Se aktuelle alternativer'),
     ('usikker','Jeg vil bare sammenligne mulighetene','Vis alle alternativer')],
   'partners':{'refinansiere':['Zensum','Sambla','DigiFinans','Tjenestetorget','Axo Finans'],'nytt-lan':['DigiFinans','Tjenestetorget','Sambla','Zensum','Axo Finans'],'usikker':['Zensum','Sambla','DigiFinans','Tjenestetorget','Axo Finans']}
 },
 'sjekk/omstartslan/index.html':{
   'title':'Hva beskriver situasjonen best?',
   'lead':'Velg utgangspunkt. Dette er en sortering av relevante alternativer, ikke en vurdering av hvem som vil godkjenne en søknad.',
   'choices':[
     ('sikkerhet','Jeg kan vurdere refinansiering med sikkerhet i bolig','Se relevante alternativer'),
     ('utfordringer','Jeg har dyr gjeld eller økonomiske utfordringer','Se relevante alternativer'),
     ('samle','Jeg vil undersøke muligheten for å samle gjeld','Se relevante alternativer'),
     ('usikker','Jeg er usikker og vil se alle','Vis alle alternativer')],
   'partners':{'sikkerhet':['Okida','Zen Finans','GjeldsMegleren Norge','Tjenestetorget'],'utfordringer':['Okida','GjeldsMegleren Norge','Zen Finans','Tjenestetorget'],'samle':['GjeldsMegleren Norge','Zen Finans','Okida','Tjenestetorget'],'usikker':['Okida','Zen Finans','GjeldsMegleren Norge','Tjenestetorget']}
 }}

for rel,cfg in PAGES.items():
 p=ROOT/rel; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser'); preview=s.select_one('.partner-preview')
 if not preview: raise SystemExit(f'Missing partner preview: {rel}')
 old=s.select_one('.revenue-matcher')
 if old: old.decompose()
 sec=s.new_tag('section'); sec['class']=['revenue-matcher']; sec['data-revenue-matcher']='v1'
 h=s.new_tag('h2'); h.string=cfg['title']; sec.append(h)
 lead=s.new_tag('p'); lead.string=cfg['lead']; sec.append(lead)
 grid=s.new_tag('div'); grid['class']=['revenue-matcher-grid']
 for key,label,cta in cfg['choices']:
  b=s.new_tag('button'); b['type']='button'; b['class']=['revenue-match-choice']; b['data-match']=key; b['data-revenue-event']='matcher_choice'; b['data-revenue-context']=key
  strong=s.new_tag('strong'); strong.string=label; span=s.new_tag('span'); span.string=cta+' →'; b.extend([strong,span]); grid.append(b)
 sec.append(grid)
 note=s.new_tag('p'); note['class']=['partner-note']; note.string='Valget endrer bare rekkefølgen på alternativene som vises. Sammenlign alltid faktiske vilkår og total kostnad.'; sec.append(note)
 preview.insert_before(sec)
 # annotate cards with match ranks
 cards={c.get('data-partner'):c for c in preview.select('.partner-card[data-partner]')}
 for key,names in cfg['partners'].items():
  for rank,name in enumerate(names,1):
   if name in cards: cards[name][f'data-rank-{key}']=str(rank)
 # progressive enhancement: all partners stay visible; choice only reorders and highlights first card
 js="""(function(){var root=document.querySelector('[data-revenue-matcher="v1"]');if(!root)return;var preview=root.nextElementSibling;if(!preview||!preview.classList.contains('partner-preview'))return;root.addEventListener('click',function(e){var b=e.target.closest('[data-match]');if(!b)return;var key=b.dataset.match,cards=[].slice.call(preview.querySelectorAll('.partner-card[data-partner]'));cards.sort(function(a,z){return Number(a.getAttribute('data-rank-'+key)||999)-Number(z.getAttribute('data-rank-'+key)||999)});cards.forEach(function(c,i){preview.insertBefore(c,preview.querySelector('.partner-note'));c.classList.toggle('revenue-match-primary',i===0);var out=c.querySelector('.partner-cta');var intentUrl=c.getAttribute('data-url-'+key);if(out&&intentUrl)out.href=intentUrl});root.querySelectorAll('[data-match]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});preview.scrollIntoView({behavior:'smooth',block:'start'});});})();"""
 tag=s.new_tag('script'); tag['data-revenue-matcher-script']='v1'; tag.string=js; s.body.append(tag)
 # scoped CSS, deliberately neutral and mobile-first
 style=s.new_tag('style'); style['data-revenue-matcher-style']='v1'; style.string='.revenue-matcher{margin:24px 0;padding:22px;border:1px solid #cddceb;border-radius:18px;background:#f7fbff}.revenue-matcher h2{margin-top:0}.revenue-matcher-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.revenue-match-choice{appearance:none;text-align:left;border:1px solid #d8e2ec;background:#fff;border-radius:14px;padding:16px;cursor:pointer;font:inherit}.revenue-match-choice strong,.revenue-match-choice span{display:block}.revenue-match-choice span{margin-top:7px;font-weight:800}.revenue-match-choice[aria-pressed="true"]{outline:3px solid currentColor;outline-offset:2px}.partner-card.revenue-match-primary{box-shadow:0 0 0 3px rgba(20,80,140,.18)}@media(max-width:700px){.revenue-matcher-grid{grid-template-columns:1fr}}'; s.head.append(style)
 p.write_text(str(s),encoding='utf-8')
 print('Revenue matcher applied:',rel)
