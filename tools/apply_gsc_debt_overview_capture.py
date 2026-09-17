from pathlib import Path

path = Path('gjeldsregisteret-forbrukslan.html')
html = path.read_text(encoding='utf-8')
marker = '<section class="faq"><h2>Vanlige spørsmål</h2>'
if marker not in html:
    raise SystemExit('FAQ marker not found')
if 'data-debt-overview-next' in html:
    print('Debt overview capture already present')
    raise SystemExit(0)
block = '''<section data-debt-overview-next="true"><h2>Har du fått oversikt over gjelden? Velg neste steg</h2><p>En gjeldsoversikt er mest nyttig når den fører til en konkret handling. Velg det som ligner mest på situasjonen din:</p><div class="related-links"><a href="gjeldsmiks-sjekk.html">Jeg vil forstå hvilke deler av gjelden som koster mest →</a><a href="hva-bor-jeg-gjore-med-dyr-gjeld.html">Jeg har dyr gjeld og vil finne riktig neste steg →</a><a href="betalingsproblemer-hva-gjor-jeg.html">Jeg sliter med å betale regninger eller gjeld →</a></div><p class="article-note">Har du bare behov for å kontrollere registrerte opplysninger, trenger du ikke gå videre til en lånesammenligning.</p></section>'''
html = html.replace(marker, block + marker, 1)
path.write_text(html, encoding='utf-8')
print('GSC debt overview capture applied: 1 page')
