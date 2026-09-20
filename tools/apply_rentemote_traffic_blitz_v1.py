from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1]
p=R/'rentemote-hva-betyr-det.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-renteblitz="v1"]'): x.decompose()
article=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-renteblitz']='v1';sec['id']='rentemote-live'
h=s.new_tag('h2');h.string='Rentemøtet på 60 sekunder';sec.append(h)
q=s.new_tag('p');q.string='24. september kl. 10 publiserer Norges Bank rentebeslutningen og Pengepolitisk rapport 3/26. Denne boksen er laget som den raske inngangen: beslutning → hva den betyr i kroner → om boliglånet ditt er verdt å kontrollere.';sec.append(q)
strip=s.new_tag('div');strip['class']=['number-strip']
for val,label in [('4,25 %','styringsrente før møtet'),('5,29 %','nye boliglån, juli'),('5,31 %','utestående boliglån, juli'),('25.09','nye SSB-bankrenter')]:
 d=s.new_tag('div');a=s.new_tag('strong');a.string=val;b=s.new_tag('span');b.string=label;d.extend([a,b]);strip.append(d)
sec.append(strip)
ul=s.new_tag('ul')
for href,label,event,ctx in [
 ('boliglanskalkulator-renteforskjell.html','Regn renteendringen i kroner →','problem_route','renteblitz_calculator'),
 ('ta-sparesjekken.html?src=rentemote_blitz','Ta Sparesjekken →','savings_check_entry','rentemote_blitz'),
 ('sjekk/boliglan/?intent=sammenligne','Innhent og sammenlign boliglånstilbud →','commercial_route','rentemote_blitz')]:
 li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;a['data-revenue-event']=event;a['data-revenue-context']=ctx;li.append(a);ul.append(li)
sec.append(ul)
note=s.new_tag('p');note['class']=['small'];note.string='Sparesjekk oppdaterer med offisielle tall. Et rentemøte bestemmer ikke automatisk hvilken rente banken tilbyr deg.';sec.append(note)
lead=article.find('p',class_='lead')
if lead: lead.insert_after(sec)
else: article.insert(0,sec)
# Social/share metadata for link previews.
og=s.find('meta',attrs={'property':'og:title'})
if og: og['content']='Rentemøte 24. september: hva betyr det for boliglånet? | Sparesjekk'
ogd=s.find('meta',attrs={'property':'og:description'})
if ogd: ogd['content']='Rentebeslutningen forklart på 60 sekunder. Regn utslaget i kroner og sjekk om boliglånet ditt er verdt å sammenligne.'
p.write_text(str(s),encoding='utf-8')
# Machine-readable content pack: one source for Shorts/Reels/posts/manual distribution.
pack={
 'version':'2026-09-20-v1','event':'Norges Bank rentebeslutning 24. september 2026 kl. 10:00',
 'status':'pre_decision','facts':{'policy_rate_before':4.25,'new_mortgage_rate_july':5.29,'outstanding_mortgage_rate_july':5.31,'ssb_next_update':'2026-09-25'},
 'hooks':[
  'Rentemøte 24. september: dette bør boliglånskunder faktisk følge med på',
  '0,25 prosentpoeng er 2 500 kr per million i lån per år – før avdrag og skatt',
  'Styringsrenten er ikke boliglånsrenten: sjekk forskjellen før du reagerer på overskriftene'
 ],
 'destinations':{
  'primary':'https://sparesjekk.no/rentemote-hva-betyr-det.html?utm_source=social&utm_medium=organic&utm_campaign=rentemote_20260924',
  'calculator':'https://sparesjekk.no/boliglanskalkulator-renteforskjell.html?utm_source=social&utm_medium=organic&utm_campaign=rentemote_20260924',
  'savings_check':'https://sparesjekk.no/ta-sparesjekken.html?src=rentemote_social&utm_source=social&utm_medium=organic&utm_campaign=rentemote_20260924'
 },
 'guardrails':['Do not predict the rate decision.','Use official Norges Bank/SSB figures only.','Do not promise savings or approval.']
}
(R/'data'/'rentemote-traffic-pack.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rentemote Traffic Blitz v1 applied')
