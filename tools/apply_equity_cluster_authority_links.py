from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
blocks={
'egenkapital-bolig.html':[('boliglan-uten-egenkapital.html','Mangler du egenkapital til bolig? Se alternativene'),('kausjonist-boliglan.html','Slik fungerer kausjonist ved boliglån'),('medlantaker-boliglan.html','Medlåntaker på boliglån – hva betyr det?')],
'guide-forstehjemslan.html':[('boliglan-uten-egenkapital.html','Ikke nok egenkapital til første bolig?'),('kausjonist-boliglan.html','Vurderer du kausjonist?'),('medlantaker-boliglan.html','Vurderer du medlåntaker?')],
'hvor-mye-kan-jeg-lane-bolig.html':[('boliglan-uten-egenkapital.html','Mangler egenkapital til bolig'),('kausjonist-boliglan.html','Boliglån med kausjonist'),('medlantaker-boliglan.html','Boliglån med medlåntaker'),('guide-forstehjemslan.html','Førstehjemslån – hva bør du sammenligne?')]
}
for name,links in blocks.items():
 p=R/name
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for x in s.select('[data-equity-cluster-authority="v1"]'): x.decompose()
 root=s.select_one('article') or s.select_one('main')
 sec=s.new_tag('section');sec['data-equity-cluster-authority']='v1'
 h=s.new_tag('h2');h.string='Hvis egenkapitalen er utfordringen';sec.append(h)
 p1=s.new_tag('p');p1.string='Boligbudsjett, egenkapital, kausjonist og medlåntaker henger sammen. Velg sporet som beskriver situasjonen din best.';sec.append(p1)
 ul=s.new_tag('ul')
 for href,label in links:
  li=s.new_tag('li');a=s.new_tag('a',href=href);a.string=label;li.append(a);ul.append(li)
 sec.append(ul);root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Equity cluster authority links applied')
