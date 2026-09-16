from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
PAGES=['sjekk/forbrukslan/index.html','sjekk/omstartslan/index.html']
for rel in PAGES:
 p=ROOT/rel; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if not s.select_one('[data-revenue-matcher="v1"]'): raise SystemExit('Matcher missing: '+rel)
 old=s.select_one('[data-revenue-sticky="v1"]')
 if old: old.decompose()
 bar=s.new_tag('aside'); bar['data-revenue-sticky']='v1'; bar['class']=['revenue-sticky']; bar['aria-label']='Neste steg'
 txt=s.new_tag('div'); txt['class']=['revenue-sticky-copy']; strong=s.new_tag('strong'); strong.string='Klar til å sammenligne?'; txt.append(strong); small=s.new_tag('span'); small.string='Gå videre til alternativet som vises først.'; txt.append(small); bar.append(txt)
 a=s.new_tag('a'); a['class']=['revenue-sticky-cta']; a['href']='#'; a['data-revenue-event']='sticky_partner_click'; a['data-revenue-stage']='partner_outclick'; a['rel']='sponsored nofollow noopener'; a['target']='_blank'; a.string='Gå videre →'; bar.append(a)
 (s.body or s).append(bar)
 style=s.find('style',attrs={'data-revenue-sticky-style':'v1'})
 if style: style.decompose()
 style=s.new_tag('style'); style['data-revenue-sticky-style']='v1'; style.string='@media(min-width:701px){.revenue-sticky{display:none!important}}@media(max-width:700px){body{padding-bottom:92px}.revenue-sticky{position:fixed;z-index:999;left:10px;right:10px;bottom:10px;display:flex;align-items:center;gap:10px;padding:10px 10px 10px 12px;border-radius:16px;background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.2);border:1px solid rgba(0,0,0,.12)}.revenue-sticky-copy{min-width:0;flex:1;display:flex;flex-direction:column;line-height:1.2}.revenue-sticky-copy strong{font-size:.9rem}.revenue-sticky-copy span{font-size:.72rem;opacity:.75;margin-top:3px}.revenue-sticky-cta{flex:0 0 auto;text-decoration:none;font-weight:850;padding:12px 14px;border-radius:12px;background:#1457d9;color:#fff;min-height:44px;box-sizing:border-box}.revenue-sticky[hidden]{display:none!important}}'; s.head.append(style)
 js=s.find('script',attrs={'data-revenue-sticky-script':'v1'})
 if js: js.decompose()
 js=s.new_tag('script'); js['data-revenue-sticky-script']='v1'; js.string=r'''(function(){var bar=document.querySelector('[data-revenue-sticky="v1"]'),out=bar&&bar.querySelector('a');if(!bar||!out)return;function sync(){var card=document.querySelector('.partner-preview .partner-card');var a=card&&card.querySelector('a[data-revenue-event="partner_click"]');if(!a){bar.hidden=true;return}bar.hidden=false;out.href=a.href;out.dataset.revenuePartner=a.dataset.revenuePartner||'';out.dataset.matcherIntent=a.dataset.matcherIntent||'';out.dataset.revenueContext=a.dataset.revenueContext||'';out.textContent='Gå videre til '+(a.dataset.revenuePartner||'tilbyder')+' →'}sync();var root=document.querySelector('[data-revenue-matcher="v1"]');if(root)root.addEventListener('click',function(){setTimeout(sync,0)});})();'''; (s.body or s).append(js)
 p.write_text(str(s),encoding='utf-8'); print('Mobile sticky CTA:',rel)
