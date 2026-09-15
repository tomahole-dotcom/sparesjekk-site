from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'refinansiering-kalkulator.html'
soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
box = soup.select_one('#offerNext')
if not box:
    raise SystemExit('Missing #offerNext')
old = box.select_one('.result-commercial-cta')
if old:
    old.decompose()
wrap = soup.new_tag('div')
wrap['class'] = ['result-commercial-cta']
p = soup.new_tag('p')
p.string = 'Vil du også undersøke hvilke faktiske refinansieringstilbud som er tilgjengelige? Sammenlign tilbudene mot resultatet over – særlig effektiv rente, gebyrer, løpetid og total tilbakebetaling.'
a = soup.new_tag('a', href='sjekk/forbrukslan/')
a['class'] = ['cta', 'inline']
a['data-revenue-event'] = 'commercial_route'
a['data-revenue-context'] = 'refinance_calculator_result'
a.string = 'Sammenlign faktiske tilbud →'
note = soup.new_tag('small')
note['class'] = ['partner-note']
note.string = 'ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.'
wrap.extend([p, a, note])
box.append(wrap)
path.write_text(str(soup), encoding='utf-8')
print('Result-state commercial CTA applied: refinansiering-kalkulator.html')