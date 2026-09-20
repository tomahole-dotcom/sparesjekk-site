from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'refinansiering-lopetid.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-refi-duration-handoff="v1"]')
if old: old.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-refi-duration-handoff']='v1'
h=s.new_tag('h2');h.string='Har du kontrollert løpetiden og vil undersøke faktiske alternativer?';sec.append(h)
q=s.new_tag('p');q.string='Gå videre bare hvis målet er å refinansiere eksisterende dyr usikret gjeld. Sammenlign effektiv rente, gebyrer, løpetid og samlet tilbakebetaling – ikke bare månedsbeløpet.';sec.append(q)
a=s.new_tag('a',href='sjekk/forbrukslan/?intent=refinansiere');a.string='Undersøk refinansieringsalternativer →';a['class']=['cta'];a['data-revenue-event']='commercial_route';a['data-revenue-context']='refi_duration';sec.append(a)
n=s.new_tag('p');n['class']=['partner-note'];n.string='ANNONSE / REKLAME – du sendes videre til kommersielle partnere. Sparesjekk kan motta provisjon dersom du går videre. Ingen besparelse eller godkjenning er garantert.';sec.append(n)
root.append(sec);p.write_text(str(s),encoding='utf-8');print('Refinancing duration handoff applied')
