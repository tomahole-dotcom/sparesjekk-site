from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'guide-sammenligne-boliglan.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-mortgage-compare-early="v1"]')
if old: old.extract()
hero=s.select_one('.compare-hero')
sec=BeautifulSoup('''<section class="mortgage-compare-early" data-mortgage-compare-early="v1"><h2>Har du tallene klare?</h2><p>Velg neste steg ut fra hvor langt du har kommet. Du trenger ikke lese hele guiden før du går videre.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="mortgage_compare_early_v1" href="sjekk/boliglan/?intent=sammenligne"><strong>Jeg vil sammenligne boliglånsalternativer</strong><span>Gå videre med rente, kostnader og vilkår i fokus →</span></a><a data-revenue-event="problem_route" data-revenue-context="mortgage_compare_rate_v1" href="boliglanskalkulator-renteforskjell.html"><strong>Jeg har to renter jeg vil regne på</strong><span>Se forskjellen i kroner først →</span></a><a data-revenue-event="content_route" data-revenue-context="mortgage_compare_learn_v1" href="#mortgage-compare-guide"><strong>Jeg vil lære å sammenligne riktig</strong><span>Fortsett med scorecard og guide →</span></a></div></section>''','html.parser').section
hero.insert_after(sec)
first=s.select_one('section')
# first section may be inserted section now; target next content section
sections=s.find_all('section')
for x in sections:
    if x is not sec:
        x['id']='mortgage-compare-guide'; break
if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Mortgage comparison early conversion applied')
