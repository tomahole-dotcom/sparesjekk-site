from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
def load(n):
 p=R/n;return p,BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
def save(p,s):p.write_text(str(s),encoding='utf-8')
def add(n,marker,title,text,links):
 p,s=load(n);old=s.select_one(f'[data-bank-switch-consolidation="{marker}"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 x=s.new_tag('section');x['data-bank-switch-consolidation']=marker
 h=s.new_tag('h2');h.string=title;x.append(h);q=s.new_tag('p');q.string=text;x.append(q)
 for href,label,event in links:
  a=s.new_tag('a',href=href);a.string=label
  if event:a['class']=['cta'];a['data-revenue-event']=event;a['data-revenue-context']='bank_switch_gsc_v1'
  q=s.new_tag('p');q.append(a);x.append(q)
 root.append(x);save(p,s)
add('bytte-bank-boliglan-komplett.html','decision-v1','Bytte bank eller bare flytte boliglånet?','Hvis målet er bedre boliglånsvilkår, trenger du ikke starte med å flytte hele dagligbanken. Sammenlign først boliglånet. Flytt kontoer, kort og betalinger bare når det faktisk er en del av tilbudet du velger.',[('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route'),('flytte-boliglan.html','Har du bestemt deg? Se selve låneflyttingen →','')])
add('flytte-boliglan.html','transfer-v1','Vil du ha et tilbud før du flytter?','Denne siden er for selve flyttingen. Hvis du fortsatt mangler et konkret alternativ å sammenligne med dagens lån, hent sammenligningsgrunnlaget før du starter flytteprosessen.',[('sjekk/boliglan/','Undersøk alternativer før flytting →','commercial_route'),('bankbytte-break-even.html','Har du allerede et tilbud? Regn break-even →','problem_route')])
add('guide-bytte-bank-steg.html','fullmove-v1','Skal du egentlig bare flytte boliglånet?','Denne sjekklisten gjelder hele bankforholdet. Hvis søket ditt egentlig handler om å få bedre vilkår på boliglånet, gå til boliglånssporet først i stedet for å gjøre bankbyttet større enn nødvendig.',[('bytte-bank-boliglan-komplett.html','Vurder boliglånsbyttet først →','problem_route'),('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route')])
add('guide-sammenligne-boliglan.html','compare-v1','Fra sammenligning til faktiske alternativer','Når du vet hvilke tall og vilkår som skal sammenlignes, er neste steg å undersøke alternativer på samme grunnlag. Da kan du vurdere om dagens bank bør få matche før du eventuelt flytter.',[('sjekk/boliglan/','Undersøk boliglånsalternativer →','commercial_route'),('guide-forhandle-rente.html','Vil du bli? Bruk tilbudet i renteforhandling →','problem_route')])
print('Bank-switch consolidation batch applied: 4 pages')
