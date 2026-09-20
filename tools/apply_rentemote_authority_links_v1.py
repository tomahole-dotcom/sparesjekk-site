from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
TARGETS=[
 ('boliglansrente-komplett-guide.html','Følg neste rentemøte og hva det kan bety for boliglånet →'),
 ('rentehistorikk-boliglan.html','Se neste rentemøte i Rentepuls →'),
 ('guide-rentekutt.html','Følg rentemøtet og bankrentene →'),
 ('banken-vil-ikke-senke-renten.html','Se Rentepuls før neste rentemøte →')
]
for rel,label in TARGETS:
 p=R/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 old=s.select_one('[data-rentemote-authority-link="v1"]')
 if old:old.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('aside');sec['data-rentemote-authority-link']='v1'
 h=s.new_tag('h2');h.string='Rentemøte 24. september 2026';sec.append(h)
 q=s.new_tag('p');q.string='Norges Bank offentliggjør neste rentebeslutning og Pengepolitisk rapport 24. september. Rentepuls samler beslutningen med de offisielle bankrentene og viser hva endringer kan bety for boliglån.';sec.append(q)
 a=s.new_tag('a',href='rentemote-hva-betyr-det.html');a.string=label;sec.append(a)
 root.append(sec);p.write_text(str(s),encoding='utf-8');print('Rentemote authority link:',rel)
