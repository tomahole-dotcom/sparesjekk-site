from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
support={
'bytte-bank-boliglan-komplett.html':('Skal du faktisk flytte boliglånet?','Når du har bestemt deg for å undersøke en annen bank, går du videre til guiden om selve låneflyttingen.'),
'guide-bytte-bank-steg.html':('Flytting av selve boliglånet','Denne guiden gjelder bankbyttet rundt konto, kort og betalinger. For selve boliglånet bruker du den egne låneflytteguiden.'),
'guide-sammenligne-boliglan.html':('Fra sammenligning til låneflytting','Har sammenligningen vist at en annen bank kan være aktuell, fortsetter du med guiden om å flytte boliglånet.')
}
for name,(head,body) in support.items():
 p=R/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-mortgage-move-owner="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-mortgage-move-owner']='v1'
 h=s.new_tag('h2');h.string=head;sec.append(h)
 para=s.new_tag('p');para.string=body+' ';a=s.new_tag('a',href='flytte-boliglan.html');a.string='Flytte boliglån til annen bank →';para.append(a);sec.append(para);root.append(sec)
 p.write_text(str(s),encoding='utf-8')
# reinforce hub without changing title/H1/canonical
p=R/'boliglan-guider.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-mortgage-move-owner="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main');sec=s.new_tag('section');sec['data-mortgage-move-owner']='v1'
h=s.new_tag('h2');h.string='Vil du flytte boliglånet?';sec.append(h)
para=s.new_tag('p');para.string='For spørsmål om selve flyttingen mellom banker: ';a=s.new_tag('a',href='flytte-boliglan.html');a.string='se guiden om å flytte boliglån';para.append(a);sec.append(para);root.append(sec)
p.write_text(str(s),encoding='utf-8')
print('Mortgage move query ownership reinforced')
