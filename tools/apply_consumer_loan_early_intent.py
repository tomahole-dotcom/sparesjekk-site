from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'forbrukslan-komplett-guide.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
if not s.select_one('[data-consumer-early-intent="v1"]'):
 sec=BeautifulSoup('''<section class="tool-card consumer-early-intent" data-consumer-early-intent="v1"><p class="eyebrow">FINN RIKTIG SPOR</p><h2>Hva prøver du å løse?</h2><p>Velg situasjonen som passer best. Du kan fortsatt lese hele guiden under.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="consumer_early_new_v1" href="sjekk/forbrukslan/?intent=nytt-lan"><strong>Jeg vurderer et nytt lån</strong><span>Gå til sammenligning av aktuelle alternativer →</span></a><a data-revenue-event="problem_route" data-revenue-context="consumer_early_refi_v1" href="refinansiere-forbruksgjeld.html"><strong>Jeg vil samle eller redusere dyr gjeld</strong><span>Gå til refinansieringssporet →</span></a><a data-revenue-event="content_route" data-revenue-context="consumer_early_research_v1" href="#forbrukslan-guide-start"><strong>Jeg undersøker bare hvordan forbrukslån fungerer</strong><span>Fortsett til guiden →</span></a></div></section>''','html.parser').section
 lead=s.select_one('.lead');lead.insert_after(sec)
 first=s.find('section',attrs={'data-consumer-authority':'definition-v1'})
 if first: first['id']='forbrukslan-guide-start'
 if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Consumer loan early intent applied')
