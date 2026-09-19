from pathlib import Path
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]
p=R/'kalkulatorer.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
for x in s.select('[data-late-interest-calculator="v1"]'): x.decompose()
root=s.select_one('article') or s.select_one('main')
sec=s.new_tag('section');sec['data-late-interest-calculator']='v1'
h=s.new_tag('h2');h.string='Forsinkelsesrente-kalkulator';sec.append(h)
p1=s.new_tag('p');p1.string='Beregn et enkelt estimat for forsinkelsesrente ut fra beløp, årlig rentesats og antall dager. Kontroller alltid hvilken sats og periode som faktisk gjelder i saken din.';sec.append(p1)
for ident,label,typ,val in [('late-principal','Beløp (kr)','number','10000'),('late-rate','Årlig forsinkelsesrente (%)','number','12.5'),('late-days','Antall dager','number','30')]:
 lab=s.new_tag('label');lab['for']=ident;lab.string=label;sec.append(lab);inp=s.new_tag('input',id=ident,type=typ,value=val);inp['inputmode']='decimal';inp['min']='0';inp['step']='0.01' if ident!='late-days' else '1';sec.append(inp)
btn=s.new_tag('button',type='button',id='late-calc-btn');btn.string='Beregn forsinkelsesrente';sec.append(btn)
out=s.new_tag('p',id='late-calc-result');out['aria-live']='polite';sec.append(out)
p2=s.new_tag('p');a=s.new_tag('a',href='betalingsproblemer-hva-gjor-jeg.html');a.string='Har du problemer med å betale? Se mulige neste steg →';a['data-event']='problem_route';a['data-context']='late_interest_calc_v1';p2.append(a);sec.append(p2)
script=s.new_tag('script');script.string="""(()=>{const q=id=>document.getElementById(id),b=q('late-calc-btn');if(!b)return;b.addEventListener('click',()=>{const principal=Number(q('late-principal').value),rate=Number(q('late-rate').value),days=Number(q('late-days').value);if(principal<0||rate<0||days<0||![principal,rate,days].every(Number.isFinite)){q('late-calc-result').textContent='Fyll inn gyldige tall.';return;}const interest=principal*(rate/100)*(days/365);q('late-calc-result').textContent='Estimert forsinkelsesrente: '+interest.toLocaleString('nb-NO',{style:'currency',currency:'NOK',maximumFractionDigits:2});});})();""";sec.append(script)
root.append(sec);p.write_text(str(s),encoding='utf-8')
print('Late-interest calculator applied')
