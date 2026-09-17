from pathlib import Path
from bs4 import BeautifulSoup

ROUTES = {
    'minimumsbetaling-kredittkort.html': {
        'title': 'Blir kredittkortsaldoen stående måned etter måned?',
        'text': 'Hvis minimumsbetaling ikke får saldoen tydelig ned, kan det være nyttig å skille mellom nedbetaling, gjeldsoversikt og eventuell refinansiering før du velger neste steg.',
        'href': 'hva-bor-jeg-gjore-med-dyr-gjeld.html',
        'label': 'Finn riktig neste steg for dyr gjeld →',
        'context': 'credit_minimum_to_debt_capture'
    },
    'nedbetaling-kredittkortgjeld.html': {
        'title': 'Trenger du mer enn en nedbetalingsplan?',
        'text': 'Har du flere gjeldsposter eller vurderer du refinansiering, bruk veiviseren til å finne ut om du bør starte med oversikt, nedbetaling eller sammenligning av alternativer.',
        'href': 'hva-bor-jeg-gjore-med-dyr-gjeld.html',
        'label': 'Sjekk hva som er riktig neste steg →',
        'context': 'credit_paydown_to_debt_capture'
    },
    'refinansiere-forbruksgjeld.html': {
        'title': 'Usikker på hvilken refinansieringsvei som passer?',
        'text': 'Svar på tre spørsmål og skill mellom vanlig refinansiering, behov for gjeldsoversikt og situasjoner der sikkerhet i bolig kan være relevant.',
        'href': 'hva-bor-jeg-gjore-med-dyr-gjeld.html',
        'label': 'Bruk gjeldsveiviseren →',
        'context': 'refi_guide_to_debt_capture'
    }
}

changed = 0
for rel, cfg in ROUTES.items():
    path = Path(rel)
    if not path.exists():
        continue
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    old = soup.select_one('[data-conversion-route="credit-debt-v1"]')
    if old:
        old.decompose()
    container = soup.select_one('article') or soup.select_one('main')
    if not container:
        continue
    sec = soup.new_tag('section')
    sec['class'] = ['revenue-next-step']
    sec['data-conversion-route'] = 'credit-debt-v1'
    h = soup.new_tag('h2'); h.string = cfg['title']
    p = soup.new_tag('p'); p.string = cfg['text']
    a = soup.new_tag('a', href=cfg['href']); a['class'] = ['cta']; a['data-revenue-event'] = 'problem_route'; a['data-revenue-context'] = cfg['context']; a.string = cfg['label']
    sec.extend([h,p,a])
    related = container.select_one('.related-box')
    note = container.select_one('.article-note')
    if related:
        related.insert_before(sec)
    elif note:
        note.insert_before(sec)
    else:
        container.append(sec)
    path.write_text(str(soup), encoding='utf-8')
    changed += 1

# GSC shows this page already receives impressions for debt-register, debt-overview
# and unsecured-debt searches. Turn that informational traffic into useful next
# steps without forcing a commercial route.
path = Path('gjeldsregisteret-forbrukslan.html')
if path.exists():
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    old = soup.select_one('[data-debt-overview-next="v1"]')
    if old:
        old.decompose()
    container = soup.select_one('article') or soup.select_one('main')
    faq = container.select_one('.faq') if container else None
    if container:
        sec = soup.new_tag('section')
        sec['class'] = ['revenue-next-step']
        sec['data-debt-overview-next'] = 'v1'
        h = soup.new_tag('h2'); h.string = 'Har du fått oversikt over gjelden? Velg neste steg'
        p = soup.new_tag('p'); p.string = 'En gjeldsoversikt er mest nyttig når den fører til en konkret handling. Velg det som ligner mest på situasjonen din.'
        links = soup.new_tag('div'); links['class'] = ['related-links']
        options = [
            ('gjeldsmiks-sjekk.html', 'Jeg vil forstå hvilke deler av gjelden som koster mest →'),
            ('hva-bor-jeg-gjore-med-dyr-gjeld.html', 'Jeg har dyr gjeld og vil finne riktig neste steg →'),
            ('betalingsproblemer-hva-gjor-jeg.html', 'Jeg sliter med å betale regninger eller gjeld →'),
        ]
        for href, label in options:
            a = soup.new_tag('a', href=href); a.string = label; links.append(a)
        note = soup.new_tag('p'); note['class'] = ['article-note']; note.string = 'Har du bare behov for å kontrollere registrerte opplysninger, trenger du ikke gå videre til en lånesammenligning.'
        sec.extend([h,p,links,note])
        if faq:
            faq.insert_before(sec)
        else:
            container.append(sec)
        path.write_text(str(soup), encoding='utf-8')
        changed += 1

print(f'Credit/debt conversion routing applied to {changed} pages')
