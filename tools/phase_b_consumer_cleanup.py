from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'forbrukslan.html'
soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
article = soup.select_one('article#forbrukslan-hub-guide')
if not article:
    raise SystemExit('Forbrukslan guide article missing')

# Keep the useful guide/SEO copy, but remove competing end-of-guide action blocks.
for old in article.select('[data-consumer-end-flow="v1"]'):
    old.decompose()
for old in article.select('[data-commercial-ranking-links="v1"]'):
    old.decompose()

end_html = '''<section class="revenue-next-step consumer-end-step" data-consumer-end-flow="v1">
<p class="eyebrow">NESTE STEG</p>
<h2>Hva vil du gjøre nå?</h2>
<p>Har du forstått effektiv rente, gebyrer, løpetid og total kostnad, velg sporet som passer situasjonen din. Du trenger ikke gå gjennom flere mellomsteg.</p>
<div class="conversion-bridge-actions">
<a class="cta" data-revenue-event="commercial_route" data-revenue-context="consumer_end_new_v1" href="sjekk/forbrukslan/?intent=nytt-lan&amp;origin=forbrukslan-end">Se alternativer for nytt lån →</a>
<a class="secondary-cta" data-revenue-event="problem_route" data-revenue-context="consumer_end_debt_v1" href="gjeldssjekk.html?src=forbrukslan-end">Jeg har gjeld fra før →</a>
</div>
<p class="conversion-bridge-note">Har du allerede konkrete tilbud? <a href="sammenligne-forbrukslan.html">Sammenlign tilbudene på samme beløp og løpetid.</a></p>
</section>'''
flow = BeautifulSoup(end_html, 'html.parser').section
note = article.select_one('.article-note')
if note:
    note.insert_before(flow)
else:
    article.append(flow)

path.write_text(str(soup), encoding='utf-8')
print('PHASE B PASS: Forbrukslan end flow consolidated; SEO guide retained')
