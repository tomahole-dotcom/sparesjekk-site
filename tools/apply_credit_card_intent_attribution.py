from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'sjekk/kredittkort/index.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
# Remove previous version for idempotence.
old=s.find('script',attrs={'data-card-intent-attribution':'v1'})
if old: old.decompose()
partner=s.select_one('a[data-revenue-event="partner_click"]')
if not partner: raise SystemExit('Missing credit card partner click')
js=s.new_tag('script'); js['data-card-intent-attribution']='v1'
js.string=r'''(function(){
var q=new URLSearchParams(location.search).get('intent');
if(q!=='match')return;
document.querySelectorAll('a[data-revenue-event="partner_click"]').forEach(function(a){
 a.dataset.matcherIntent='match';
 a.dataset.revenueContext='credit_card_match';
});
if(typeof window.gtag==='function')window.gtag('event','matcher_handoff',{revenue_stage:'matcher_handoff',source_path:location.pathname,revenue_context:'credit_card_match'});
var p=new URLSearchParams(location.search);p.delete('intent');var rest=p.toString();history.replaceState({},'',location.pathname+(rest?'?'+rest:'')+location.hash);
})();'''
(s.body or s).append(js)
tr=s.find('script',attrs={'data-sparesjekk-revenue-tracking':'v1'})
if tr:
 code=tr.string or ''
 needle="if(a.dataset.revenueContext)payload.revenue_context=a.dataset.revenueContext;"
 add=needle+"if(a.dataset.matcherIntent)payload.matcher_intent=a.dataset.matcherIntent;"
 if 'payload.matcher_intent' not in code: tr.string=code.replace(needle,add)
# ensure locked design profile is loaded
if not s.select_one('link[href="../../design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='../../design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Credit card intent attribution applied')
