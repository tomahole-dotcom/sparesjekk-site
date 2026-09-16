from pathlib import Path

TARGET='banken-vil-ikke-senke-renten.html'
links={
 'bor-jeg-bytte-bank.html':('<a href="bankbytte-break-even.html">Regn break-even ved bankbytte →</a>','<a href="bankbytte-break-even.html">Regn break-even ved bankbytte →</a><br><a href="banken-vil-ikke-senke-renten.html">Banken vil ikke senke renten – se neste steg →</a>'),
 'min-rente-vs-markedet.html':('</main>','<section class="card"><h2>Har du allerede prøvd å forhandle?</h2><p>Hvis banken ikke vil senke renten, kan du bruke veiviseren for å finne et naturlig neste steg.</p><p><a href="banken-vil-ikke-senke-renten.html">Banken vil ikke senke renten – hva nå? →</a></p></section></main>'),
 'bankbytte-break-even.html':('</main>','<section class="card"><h2>Har banken sagt nei?</h2><p>Se hva som er fornuftig å kontrollere før du bestemmer deg for om lånet skal flyttes.</p><p><a href="banken-vil-ikke-senke-renten.html">Finn neste steg etter et nei fra banken →</a></p></section></main>')
}
for name,(needle,repl) in links.items():
 p=Path(name)
 if not p.exists():
  continue
 h=p.read_text(encoding='utf-8')
 if TARGET in h:
  continue
 if needle not in h:
  print('Skip link insertion, marker missing:',name)
  continue
 p.write_text(h.replace(needle,repl,1),encoding='utf-8')
 print('Linked:',name)
