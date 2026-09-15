from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
MARKER = 'v1'
SCRIPT = """document.addEventListener('click',function(e){var a=e.target.closest('[data-revenue-event]');if(!a)return;if(typeof window.gtag!=='function')return;var eventName=a.dataset.revenueEvent;var payload={revenue_stage:eventName,source_path:window.location.pathname,destination:a.getAttribute('href')||'',link_text:(a.textContent||'').trim().slice(0,100)};if(a.dataset.revenuePartner)payload.partner=a.dataset.revenuePartner;window.gtag('event',eventName,payload);});"""

changed = 0
for path in sorted(ROOT.rglob('*.html')):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith('tools/') or rel.startswith('.'):
        continue
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    if not soup.select_one('[data-revenue-event]') or not soup.body:
        continue
    old = soup.find('script', attrs={'data-sparesjekk-revenue-tracking': MARKER})
    if old:
        old.decompose()
    tag = soup.new_tag('script')
    tag['data-sparesjekk-revenue-tracking'] = MARKER
    tag.string = SCRIPT
    soup.body.append(tag)
    path.write_text(str(soup), encoding='utf-8')
    changed += 1

print(f'Revenue tracking injected: {changed} pages')
