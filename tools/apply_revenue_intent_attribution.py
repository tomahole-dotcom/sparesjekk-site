from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
PAGES=['sjekk/forbrukslan/index.html','sjekk/omstartslan/index.html']
for rel in PAGES:
 p=ROOT/rel; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 matcher=s.select_one('[data-revenue-matcher="v1"]'); assert matcher,rel
 old=s.find('script',attrs={'data-revenue-intent-attribution':'v1'})
 if old: old.decompose()
 js=s.new_tag('script'); js['data-revenue-intent-attribution']='v1'
 js.string=r'''(function(){
var root=document.querySelector('[data-revenue-matcher="v1"]');if(!root)return;
var currentIntent='';
function clean(v){return /^[a-z0-9-]{1,40}$/.test(v||'')?v:''}
function setIntent(v,source){v=clean(v);if(!v)return;currentIntent=v;document.querySelectorAll('.partner-card a[data-revenue-event="partner_click"]').forEach(function(a){a.dataset.matcherIntent=v;a.dataset.revenueContext='matcher_'+v});if(window.gtag)gtag('event','matcher_intent_set',{revenue_stage:'commercial_match',matcher_intent:v,intent_source:source||'unknown',source_path:location.pathname});}
root.addEventListener('click',function(e){var b=e.target.closest('button[data-match]');if(b)setIntent(b.dataset.match,'manual_choice')});
var q=clean(new URLSearchParams(location.search).get('intent'));if(q)setIntent(q,'handoff');
document.addEventListener('click',function(e){var a=e.target.closest('a[data-revenue-event="partner_click"]');if(!a||!currentIntent)return;a.dataset.matcherIntent=currentIntent;a.dataset.revenueContext='matcher_'+currentIntent;},true);
})();'''
 (s.body or s).append(js)
 # Extend central event payload so partner_click includes the selected commercial intent.
 tr=s.find('script',attrs={'data-sparesjekk-revenue-tracking':'v1'})
 if tr:
  code=tr.string or ''
  needle="if(a.dataset.revenueContext)payload.revenue_context=a.dataset.revenueContext;"
  add=needle+"if(a.dataset.matcherIntent)payload.matcher_intent=a.dataset.matcherIntent;"
  if 'payload.matcher_intent' not in code: tr.string=code.replace(needle,add)
 p.write_text(str(s),encoding='utf-8'); print('Revenue intent attribution:',rel)
