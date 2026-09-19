from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]

# Privacy-safe result analytics + result-driven commercial route.
p=ROOT/'min-rente-vs-markedet.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for tag in s.find_all('script'):
    code=tag.string or ''
    if "event:'rate_benchmark_complete',rate_gap:Number(gap.toFixed(2)),above_market:gap>0.01" in code:
        code=code.replace("event:'rate_benchmark_complete',rate_gap:Number(gap.toFixed(2)),above_market:gap>0.01",
                          "event:'rate_benchmark_complete',result_class:(gap>0.01?'above_reference':(gap<-.01?'below_reference':'near_reference'))")
        tag.string=code
cta=s.select_one('#commercialCta')
if cta:
    cta['href']='sjekk/boliglan/?intent=sammenligne'
    cta['data-revenue-context']='mortgage_rate_benchmark_above_reference'
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
p.write_text(str(s),encoding='utf-8')

# Citation/data asset -> personal rate check -> commercial journey.
p=ROOT/'rentegap-indeks.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-rentegap-conversion="v1"]')
if old: old.extract()
links=s.select_one('.gap-links')
sec=BeautifulSoup('''<section class="rentegap-conversion" data-rentegap-conversion="v1"><h2>Hva betyr dette for din rente?</h2><p>Rentegapet beskriver markedet, ikke ditt lån. Sammenlign derfor din egen boliglånsrente med den siste offisielle SSB-referansen før du vurderer å forhandle eller bytte.</p><div class="decision-actions"><a data-revenue-event="problem_route" data-revenue-context="rentegap_to_personal_check_v1" href="min-rente-vs-markedet.html"><strong>Sjekk min rente mot markedet</strong><span>Se forskjellen i prosentpoeng og kroner →</span></a><a data-revenue-event="commercial_route" data-revenue-context="rentegap_to_mortgage_compare_v1" href="sjekk/boliglan/?intent=sammenligne"><strong>Jeg vil sammenligne boliglånsalternativer</strong><span>Gå videre til relevante alternativer →</span></a></div><p class="partner-note">ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.</p></section>''','html.parser').section
links.parent.insert_before(sec)
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
p.write_text(str(s),encoding='utf-8')
print('Rentegap conversion and privacy-safe analytics applied')
