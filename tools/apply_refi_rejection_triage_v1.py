from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];p=R/'avslag-refinansiering-hva-na.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
old=s.select_one('[data-refi-rejection-triage="v1"]')
if old: old.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-refi-rejection-triage']='v1'
h=s.new_tag('h2');h.string='Avslag – hvilket spor passer situasjonen?';sec.append(h)
q=s.new_tag('p');q.string='Et avslag på vanlig refinansiering betyr ikke at du bør søke bredere uten å forstå årsaken. Velg neste steg ut fra situasjonen, og unngå nye kredittsøknader hvis økonomien allerede er akutt presset.';sec.append(q)
ul=s.new_tag('ul')
items=[
 ('ta-sparesjekken.html?src=refi_rejection','Usikker på hvilket spor som passer →','savings_check_entry','refi_rejection'),
 ('sjekk/forbrukslan/?intent=refinansiere','Vanlig refinansiering er fortsatt relevant å undersøke →','commercial_route','refi_rejection_standard'),
 ('refinansiering-med-sikkerhet.html','Jeg eier bolig og vil forstå refinansiering med sikkerhet →','problem_route','refi_rejection_secured_info'),
 ('betalingsproblemer-hva-gjor-jeg.html','Jeg klarer ikke nødvendige regninger / økonomien er akutt presset →','problem_route','refi_rejection_distress')
]
for href,label,event,ctx in items:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']=ctx;li.append(a);ul.append(li)
sec.append(ul)
note=s.new_tag('p');note.string='Omstartslån eller refinansiering med sikkerhet er bare et relevant spor når sikkerhet i bolig faktisk kan være aktuelt. Det er ikke en garanti for tilbud eller bedre vilkår.';sec.append(note)
root.append(sec);p.write_text(str(s),encoding='utf-8');print('Refinancing rejection triage applied')
