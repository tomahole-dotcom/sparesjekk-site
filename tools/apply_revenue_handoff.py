from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]

# Carry high-intent context into the matcher without collecting or transmitting financial inputs.
ROUTES={
 'refinansiering-kalkulator.html':('refinansiere','refinance_calculator_result'),
 'gjeldsmiks-sjekk.html':('refinansiere','debt_mix_result'),
 'refinansiere-forbruksgjeld.html':('refinansiere','refinance_guide'),
 'samle-smalan-kredittkortgjeld.html':('refinansiere','debt_consolidation_guide'),
 'omstartslan.html':('sikkerhet','restart_loan_guide'),
 'refinansiering-med-sikkerhet.html':('sikkerhet','secured_refinance_guide'),
}

for rel,(intent,ctx) in ROUTES.items():
 p=ROOT/rel
 if not p.exists(): continue
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for a in s.select('a[data-revenue-event="commercial_route"]'):
  href=a.get('href','')
  if href.startswith('sjekk/forbrukslan/') or href.startswith('sjekk/omstartslan/'):
   base=href.split('?')[0]
   a['href']=f'{base}?intent={intent}'
   a['data-revenue-context']=a.get('data-revenue-context') or ctx
 p.write_text(str(s),encoding='utf-8')
 print('Revenue handoff applied:',rel,intent)

# Matcher reads only an allow-listed intent from the URL, preselects/reorders and then removes it from the visible URL.
for rel,allowed in {
 'sjekk/forbrukslan/index.html':{'refinansiere','nytt-lan','usikker'},
 'sjekk/omstartslan/index.html':{'sikkerhet','utfordringer','samle','usikker'},
}.items():
 p=ROOT/rel
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.find('script',attrs={'data-revenue-handoff-script':'v1'})
 if old: old.decompose()
 js="""(function(){var root=document.querySelector('[data-revenue-matcher="v1"]');if(!root)return;var params=new URLSearchParams(location.search),key=params.get('intent');var allowed=JSON.parse(root.getAttribute('data-allowed-intents')||'[]');if(!key||allowed.indexOf(key)<0)return;var b=root.querySelector('[data-match="'+key+'"]');if(!b)return;var preview=root.nextElementSibling;if(!preview||!preview.classList.contains('partner-preview'))return;var cards=[].slice.call(preview.querySelectorAll('.partner-card[data-partner]'));cards.sort(function(a,z){return Number(a.getAttribute('data-rank-'+key)||999)-Number(z.getAttribute('data-rank-'+key)||999)});cards.forEach(function(c,i){preview.insertBefore(c,preview.querySelector('.partner-note'));c.classList.toggle('revenue-match-primary',i===0)});root.querySelectorAll('[data-match]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});var h=root.querySelector('.revenue-handoff-note');if(!h){h=document.createElement('p');h.className='revenue-handoff-note partner-note';root.appendChild(h)}h.textContent='Vi har tatt med valget fra forrige steg og sortert alternativene etter situasjonen du nettopp undersøkte. Du kan velge et annet spor når som helst.';params.delete('intent');var q=params.toString();history.replaceState({},'',location.pathname+(q?'?'+q:'')+location.hash);if(typeof window.gtag==='function')window.gtag('event','matcher_handoff',{revenue_stage:'matcher_handoff',source_path:location.pathname,revenue_context:key});})();"""
 root=s.select_one('[data-revenue-matcher="v1"]')
 if not root: raise SystemExit(f'Missing matcher: {rel}')
 import json
 root['data-allowed-intents']=json.dumps(sorted(allowed),ensure_ascii=False)
 tag=s.new_tag('script'); tag['data-revenue-handoff-script']='v1'; tag.string=js
 # Run after matcher script so card ranks are available.
 matcher=s.find('script',attrs={'data-revenue-matcher-script':'v1'})
 matcher.insert_after(tag)
 p.write_text(str(s),encoding='utf-8')
 print('Revenue handoff receiver applied:',rel)
