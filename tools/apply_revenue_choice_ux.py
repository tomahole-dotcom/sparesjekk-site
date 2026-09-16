from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
PAGES=['sjekk/forbrukslan/index.html','sjekk/omstartslan/index.html']
for rel in PAGES:
 p=ROOT/rel; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser'); preview=s.select_one('.partner-preview'); matcher=s.select_one('[data-revenue-matcher="v1"]')
 if not preview or not matcher: raise SystemExit('Missing revenue UI: '+rel)
 # Make commercial alternatives understandable at a glance without inventing rates/approval claims.
 for card in preview.select('.partner-card[data-partner]'):
  name=card.get('data-partner','')
  cta=card.select_one('a.partner-cta')
  if not cta: continue
  cta['data-revenue-stage']='partner_outclick'
  cta.string='Gå videre til '+name+' →'
  if not card.select_one('.revenue-card-kicker'):
   kicker=s.new_tag('p'); kicker['class']=['revenue-card-kicker']; kicker.string='Kommersielt alternativ'
   h=card.find(['h2','h3'])
   if h: h.insert_before(kicker)
  if not card.select_one('.revenue-card-action-note'):
   note=s.new_tag('p'); note['class']=['revenue-card-action-note']; note.string='Åpner tilbyderens side. Sjekk vilkår, kostnader og om løsningen passer situasjonen din før du går videre.'
   cta.insert_after(note)
 # Add a compact decision header immediately above partner cards.
 old=s.select_one('.revenue-choice-header')
 if old: old.decompose()
 head=s.new_tag('div'); head['class']=['revenue-choice-header']; head['aria-live']='polite'
 h=s.new_tag('h2'); h.string='Aktuelle alternativer'; head.append(h)
 t=s.new_tag('p'); t.string='Alternativene under er kommersielle partnere. Bruk situasjonsvalget over for å sortere dem, og sammenlign faktiske vilkår hos tilbyder før du søker.'; head.append(t)
 preview.insert_before(head)
 # Improve selected-state copy after manual matching, without claiming recommendation/best.
 js=s.find('script',attrs={'data-revenue-matcher-script':'v1'})
 if js and 'revenue-choice-status' not in (js.string or ''):
  addon="""\n(function(){var root=document.querySelector('[data-revenue-matcher="v1"]'),head=document.querySelector('.revenue-choice-header');if(!root||!head)return;root.addEventListener('click',function(e){var b=e.target.closest('[data-match]');if(!b)return;var label=(b.querySelector('strong')||b).textContent.trim();var p=head.querySelector('.revenue-choice-status');if(!p){p=document.createElement('p');p.className='revenue-choice-status';head.appendChild(p)}p.textContent='Sortert etter valget: '+label+'. Du kan fortsatt se og sammenligne alle alternativene.';});})();"""
  js.string=(js.string or '')+addon
 style=s.find('style',attrs={'data-revenue-choice-style':'v1'})
 if not style:
  style=s.new_tag('style'); style['data-revenue-choice-style']='v1'; style.string='.revenue-choice-header{margin:28px 0 12px}.revenue-choice-header h2{margin-bottom:6px}.revenue-choice-status{font-weight:800}.revenue-card-kicker{margin:0 0 5px;font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em}.revenue-card-action-note{font-size:.86rem;line-height:1.45;margin:10px 0 0;opacity:.82}.partner-card .partner-cta{display:block;text-align:center;width:100%;box-sizing:border-box;font-weight:850;padding:14px 16px}@media(max-width:700px){.partner-card .partner-cta{min-height:48px}.revenue-choice-header{margin-top:22px}}'; s.head.append(style)
 p.write_text(str(s),encoding='utf-8'); print('Decision-ready partner UX:',rel)
