from pathlib import Path
P=Path(__file__).resolve().parents[1]/'kredittkort-match.html'
c=P.read_text(encoding='utf-8')
c=c.replace('<link href="design-v43.css" rel="stylesheet"/>','<link href="design-v43.css" rel="stylesheet"/><link href="design-v44.css" rel="stylesheet"/>')
old="""<a class="cta inline" href="sjekk/kredittkort/">Se kredittkortalternativer →</a>"""
new="""<a class="cta inline" data-revenue-event="commercial_route" data-revenue-context="credit_card_match_result_v1" href="sjekk/kredittkort/?intent=match">Se relevante kredittkortalternativer →</a><p class="small">ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.</p>"""
c=c.replace(old,new)
old2="""<a class="cta inline" href="gjeldsmiks-sjekk.html">Sjekk gjeldsmiksen →</a>"""
new2="""<a class="cta inline" data-revenue-event="problem_route" data-revenue-context="credit_card_match_debt_v1" href="nedbetaling-kredittkortgjeld.html">Start med kredittkortgjelden →</a><p class="small"><a href="gjeldsmiks-sjekk.html">Har du flere lån eller kort? Sjekk hele gjeldsmiksen →</a></p>"""
c=c.replace(old2,new2)
P.write_text(c,encoding='utf-8')
print('Credit card match conversion applied')
