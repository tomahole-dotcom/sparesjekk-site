from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'rammelan-bolig.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-creditline-early-intent="v1"]')
if old: old.extract()
sec=BeautifulSoup('''<section class="tool-card creditline-early-intent" data-creditline-early-intent="v1"><p class="eyebrow">RAMMELÅN ELLER VANLIG BOLIGLÅN?</p><h2>Hva er grunnen til at du vurderer rammelån?</h2><p>Velg det som passer best. Rammelån er ikke nødvendigvis riktig bare fordi du ønsker mer fleksibilitet.</p><div class="decision-actions"><a data-revenue-event="problem_route" data-revenue-context="creditline_early_equity_v1" href="belaningsgrad-sjekk.html"><strong>Jeg vil bruke ledig verdi i boligen</strong><span>Sjekk først om belåningsgraden gjør rammelån relevant →</span></a><a data-revenue-event="commercial_route" data-revenue-context="creditline_early_compare_v1" href="sjekk/boliglan/"><strong>Jeg vil sammenligne finansieringsalternativer</strong><span>Gå til boliglånsalternativer →</span></a><a data-revenue-event="content_route" data-revenue-context="creditline_early_learn_v1" href="#rammelan-guide-start"><strong>Jeg vil bare forstå hvordan rammelån fungerer</strong><span>Fortsett til guiden →</span></a></div></section>''','html.parser').section
lead=s.select_one('.lead');lead.insert_after(sec)
first=sec.find_next_sibling('section')
if first: first['id']='rammelan-guide-start'
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Creditline early intent applied')
