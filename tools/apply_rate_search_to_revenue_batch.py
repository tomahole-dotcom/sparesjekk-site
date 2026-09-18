from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def add(page,marker,title,body,links):
 p=R/page;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one(f'[data-rate-search-revenue="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-rate-search-revenue']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=body;x.append(q)
 for href,label,event in links:
  q=s.new_tag('p');a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='rate_gsc_v2'
  q.append(a);x.append(q)
 root.append(x);p.write_text(str(s),encoding='utf-8')
add('boliglansrente-komplett-guide.html','rate-v2','Leser du om boliglånsrente fordi du vil betale mindre?','Rentefakta er bare nyttig hvis den leder til en beslutning. Finn først hva en renteforskjell betyr for lånet ditt. Hvis dagens vilkår ikke holder mål, undersøk faktiske alternativer.',[('boliglanskalkulator-renteforskjell.html','Regn renteforskjellen i kroner →','problem_route'),('min-rente-vs-markedet.html','Sjekk renten mot et sammenligningspunkt →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('guide-forhandle-rente.html','negotiate-v2','Skaff et reelt alternativ før renteforhandlingen','Et konkret sammenlignbart alternativ gir et bedre beslutningsgrunnlag enn en generell markedsrente. Du kan bruke det til å vurdere bankens svar og om et bytte er verdt det.',[('sjekk/boliglan/','Undersøk alternativer før du forhandler →','commercial_route'),('bankbytte-break-even.html','Har du et tilbud? Regn om et bytte lønner seg →','problem_route')])
add('slik-far-du-bedre-boliglansrente.html','better-rate-v2','Gjør handlingsplanen komplett','Når tallene er samlet og renteforskjellen er forstått, trenger du et faktisk alternativ å sammenligne med dagens bank. Deretter kan banken få muligheten til å matche før du bestemmer deg.',[('sjekk/boliglan/','Undersøk faktiske boliglånsalternativer →','commercial_route'),('guide-forhandle-rente.html','Bruk alternativet i renteforhandlingen →','problem_route'),('bytte-bank-boliglan-komplett.html','Vurder bytte hvis banken ikke matcher →','problem_route')])
add('guide-effektiv-nominell-rente.html','terms-v2','Forstått rentetallene? Bruk dem til å sammenligne','Når du vet forskjellen på nominell og effektiv rente, er neste steg å sammenligne reelle tilbud på like forutsetninger. Det er der rentekunnskapen kan bli til en faktisk besparelsesbeslutning.',[('guide-sammenligne-boliglan.html','Se hvordan tilbud bør sammenlignes →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
print('Rate search-to-revenue batch applied: 4 pages')
