from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'kontantuttak-kredittkort.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
if not s.select_one('[data-cash-withdrawal-tool="v1"]'):
 sec=BeautifulSoup('''<section class="tool-card cash-withdrawal-tool" data-cash-withdrawal-tool="v1"><p class="eyebrow">KOSTNADSSJEKK</p><h2>Hva kan kontantuttaket koste?</h2><p>Legg inn uttaksbeløp og gebyrene fra kortets prisliste. Kalkulatoren viser gebyrkostnaden før eventuell rente og valutaeffekt.</p><label>Uttaksbeløp (kr)<input id="cw-amount" inputmode="decimal" value="2000"></label><div class="cash-tool-grid"><label>Fast uttaksgebyr (kr)<input id="cw-fixed" inputmode="decimal" value="40"></label><label>Uttaksgebyr (%)<input id="cw-pct" inputmode="decimal" value="1"></label></div><label>Minibankens eget gebyr (kr)<input id="cw-atm" inputmode="decimal" value="0"></label><button class="calc-action" id="cw-btn" type="button">Beregn gebyrkostnad</button><div aria-live="polite" class="tool-result" id="cw-result">Fyll inn gebyrene som gjelder for kortet og minibanken.</div><p class="article-note">Dette er et gebyrestimat. Renter, valutapåslag og vekslingskurs er ikke med og kan øke kostnaden.</p><p><a data-revenue-context="cash_withdrawal_cost_v1" data-revenue-event="problem_route" href="kredittkort-gebyrer.html">Sjekk flere kredittkortgebyrer →</a></p><p><a class="cta" data-revenue-context="cash_withdrawal_cost_v1" data-revenue-event="commercial_route" href="kredittkort-match.html">Sammenlign kredittkort ut fra bruk →</a></p></section>''','html.parser').section
 target=s.select_one('.cash-warning')
 target.insert_after(sec)
 js=s.new_tag('script');js.string="""(function(){function n(id){return Number((document.getElementById(id).value||'').replace(/\\s/g,'').replace(',','.'))||0}document.getElementById('cw-btn').addEventListener('click',function(){var a=n('cw-amount'),f=n('cw-fixed'),p=n('cw-pct'),m=n('cw-atm'),o=document.getElementById('cw-result');if(!(a>0)||f<0||p<0||m<0){o.textContent='Kontroller at feltene inneholder gyldige tall.';return}var fee=f+a*p/100+m,total=a+fee;o.innerHTML='<strong>'+Math.round(fee).toLocaleString('nb-NO')+' kr</strong> i oppgitte gebyrer. Uttaket blir da minst '+Math.round(total).toLocaleString('nb-NO')+' kr før eventuell rente og valutaeffekt.';});})();"""
 s.body.append(js)
 if not s.select_one('link[href="design-v44.css"]'): s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Cash withdrawal cost tool applied')
