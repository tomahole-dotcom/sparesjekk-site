from pathlib import Path
from bs4 import BeautifulSoup

p=Path('boliglanskalkulator-renteforskjell.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
result=soup.select_one('.tool-result')
if not result:
    raise SystemExit('Missing .tool-result')
old=soup.select_one('.mortgage-result-commercial-cta')
if old:
    old.decompose()
box=soup.new_tag('div')
box['class']='mortgage-result-commercial-cta'
box['hidden']=''
h=soup.new_tag('h3'); h.string='Vil du undersøke hva du faktisk kan få?'
text=soup.new_tag('p'); text.string='Beregningen viser bare størrelsesordenen. Faktiske tilbud viser hvilken rente og hvilke vilkår som er tilgjengelige for deg.'
a=soup.new_tag('a',href='sjekk/boliglan/'); a['class']='cta'; a['data-revenue-event']='commercial_route'; a['data-revenue-context']='mortgage_rate_calculator_result'; a.string='Sjekk aktuelle boliglånstilbud →'
note=soup.new_tag('p'); note['class']='partner-note'; note.string='ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.'
for x in (h,text,a,note): box.append(x)
result.insert_after(box)
script=soup.new_tag('script')
script['data-revenue-result-reveal']='mortgage-v1'
script.string="""(function(){var original=window.calculate;if(typeof original!=='function')return;window.calculate=function(){var out=original.apply(this,arguments);var box=document.querySelector('.mortgage-result-commercial-cta');if(box)box.hidden=false;return out;};})();"""
soup.body.append(script)
p.write_text(str(soup),encoding='utf-8')
print('Mortgage result Revenue CTA applied')
