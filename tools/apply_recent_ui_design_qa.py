from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
# Give all recent generated sections a shared visual component class without altering copy/SEO.
markers=[
'data-card-debt-conversion','data-ltv-rate-decision-v2','data-ltv-authority-v2',
'data-payment-relief-authority-v2','data-payment-relief-support-v2','data-payment-relief-problem-v2',
'data-mortgage-compare-owner-v2','data-mortgage-compare-support-v2','data-toploan-housing-intent']
for p in R.glob('*.html'):
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');changed=False
 for m in markers:
  for sec in s.select(f'[{m}="v1"]'):
   classes=sec.get('class',[])
   if 'decision-card' not in classes: sec['class']=classes+['decision-card'];changed=True
 if changed:
  if not s.select_one('link[href="design-v44.css"]'):
   head=s.select_one('head'); link=s.new_tag('link',rel='stylesheet',href='design-v44.css'); head.append(link)
  p.write_text(str(s),encoding='utf-8')
# Upgrade calculator markup to native Sparesjekk tool-card styling.
p=R/'kalkulatorer.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');sec=s.select_one('[data-late-interest-calculator="v1"]')
if sec:
 if not s.select_one('link[href="design-v44.css"]'):
  head=s.select_one('head'); link=s.new_tag('link',rel='stylesheet',href='design-v44.css'); head.append(link)
 sec['class']=list(dict.fromkeys(sec.get('class',[])+['tool-card','late-interest-tool']))
 btn=sec.select_one('#late-calc-btn')
 if btn: btn['class']=list(dict.fromkeys(btn.get('class',[])+['calc-action']))
 out=sec.select_one('#late-calc-result')
 if out: out['class']=list(dict.fromkeys(out.get('class',[])+['tool-result']))
p.write_text(str(s),encoding='utf-8')
print('Recent UI design classes applied')
