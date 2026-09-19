from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
sources={
'banken-vil-ikke-senke-renten.html':('Prøv en strukturert renteforhandling først','Hvis banken ikke senker renten, kan du bruke en konkret forhandlingsrunde før du bestemmer deg for å flytte lånet.'),
'bor-jeg-bytte-bank.html':('Forhandle før du eventuelt bytter','Hvis boliglånsrenten er hovedgrunnen til at du vurderer bankbytte, kan en strukturert renteforhandling være et naturlig første steg.'),
'boliglansrente-komplett-guide.html':('Vil du forsøke å få bedre rente?','Når du kjenner renten og sammenligningsgrunnlaget ditt, kan neste steg være å forhandle med banken.')
}
for name,(head,body) in sources.items():
 p=R/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-rate-negotiation-authority="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-rate-negotiation-authority']='v1'
 h=s.new_tag('h2');h.string=head;sec.append(h)
 para=s.new_tag('p');para.string=body+' ';a=s.new_tag('a',href='guide-forhandle-rente.html');a.string='Slik forhandler du boliglånsrenten →';para.append(a);sec.append(para);root.append(sec)
 p.write_text(str(s),encoding='utf-8')
print('Rate negotiation authority links applied')
