from pathlib import Path
from bs4 import BeautifulSoup

P=Path("sjekk/boliglan/index.html")
s=BeautifulSoup(P.read_text(encoding="utf-8"),"html.parser")
card=s.select_one(".partner-card[data-partner='Tjenestetorget']")
assert card, "mortgage partner card missing"
p=card.find("p")
p.string="Tjenestetorget lar deg gå videre for å innhente og sammenligne aktuelle boliglånstilbud. Du vurderer selv tilbud og vilkår før du eventuelt velger bank."
a=card.select_one("a.partner-cta")
assert a, "mortgage CTA missing"
a.string="Innhent og sammenlign boliglånstilbud →"
a["data-revenue-stage"]="partner_outclick"
a["data-revenue-context"]="mortgage_compare_partner"
note=s.select_one(".partner-note")
if note: note.string="Du sendes videre til Tjenestetorget. Sparesjekk kan motta provisjon dersom du går videre. Det koster ikke ekstra for deg. Sammenlign alltid effektiv rente, gebyrer og øvrige vilkår."

old=s.find("script",attrs={"data-mortgage-intent-attribution":"v1"})
if old: old.decompose()
script=s.new_tag("script")
script["data-mortgage-intent-attribution"]="v1"
script.string=r"""(function(){
var p=new URLSearchParams(location.search), intent=p.get('intent');
if(intent!=='sammenligne')return;
var a=document.querySelector('.partner-card[data-partner="Tjenestetorget"] a.partner-cta');
if(a){a.dataset.matcherIntent='sammenligne';a.dataset.revenueContext='mortgage_compare_partner';}
if(typeof window.gtag==='function')window.gtag('event','matcher_handoff',{revenue_stage:'matcher_handoff',matcher_intent:'sammenligne',revenue_context:'mortgage_compare',source_path:location.pathname});
p.delete('intent');var q=p.toString();history.replaceState({},'',location.pathname+(q?'?'+q:'')+location.hash);
})();"""
s.body.append(script)
tracking=s.find("script",attrs={"data-sparesjekk-revenue-tracking":"v1"})
assert tracking
code=tracking.string or ""
if "matcher_intent" not in code:
    code=code.replace("if(a.dataset.revenueContext)payload.revenue_context=a.dataset.revenueContext;","if(a.dataset.revenueContext)payload.revenue_context=a.dataset.revenueContext;if(a.dataset.matcherIntent)payload.matcher_intent=a.dataset.matcherIntent;")
    tracking.string=code
P.write_text(str(s),encoding="utf-8")
print("Mortgage intent handoff and partner explanation applied")
