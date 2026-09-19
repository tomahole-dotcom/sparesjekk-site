from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]

def save(name,s):
    if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
    (ROOT/name).write_text(str(s),encoding='utf-8')

# High-intent comparison guide: early decision bridge
p=ROOT/'sammenligne-kredittkort.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-card-compare-conversion="v1"]')
if old: old.extract()
lead=s.select_one('.lead')
sec=BeautifulSoup('''<section class="card-commercial-bridge" data-card-compare-conversion="v1"><h2>Klar til å sammenligne ut fra din bruk?</h2><p>Velg først om du faktisk skal finne et kort, eller om problemet er saldo som allerede koster renter.</p><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="card_compare_v1" href="kredittkort-match.html"><strong>Jeg skal velge eller bytte kort</strong><span>Finn hva du bør prioritere og gå videre til relevante alternativer →</span></a><a data-revenue-event="problem_route" data-revenue-context="card_compare_debt_v1" href="nedbetaling-kredittkortgjeld.html"><strong>Jeg har saldo som blir stående</strong><span>Start med kostnaden på kortgjelden →</span></a></div></section>''','html.parser').section
lead.insert_after(sec); save('sammenligne-kredittkort.html',s)

# Fee guide: add result-oriented next step without replacing informational tool
p=ROOT/'kredittkort-gebyrer.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-card-fee-conversion="v1"]')
if old: old.extract()
score=s.select_one('.fee-score')
sec=BeautifulSoup('''<section class="card-commercial-bridge compact" data-card-fee-conversion="v1"><h2>Hva vil du gjøre med kostnadene?</h2><div class="decision-actions"><a data-revenue-event="commercial_route" data-revenue-context="card_fee_choose_v1" href="kredittkort-match.html"><strong>Sammenligne kort for min bruk</strong><span>Start med bruksmønsteret ditt →</span></a><a data-revenue-event="problem_route" data-revenue-context="card_fee_debt_v1" href="kredittkort-effektiv-rente.html"><strong>Jeg betaler renter på saldo</strong><span>Se på rente og nedbetaling først →</span></a></div></section>''','html.parser').section
score.insert_after(sec); save('kredittkort-gebyrer.html',s)
print('Credit card commercial cluster applied')
