from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parents[1]/'guide-effektiv-nominell-rente.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
if not s.select_one('[data-rate-cost-comparator="v1"]'):
 sec=BeautifulSoup('''<section class="tool-card rate-cost-tool" data-rate-cost-comparator="v1"><p class="eyebrow">SAMMENLIGN I KRONER</p><h2>Hva betyr forskjellen i nominell rente?</h2><p>Legg inn lånebeløp og to nominelle renter. Du får et enkelt estimat på forskjellen i rentekostnad per år, før gebyrer og effekten av nedbetaling.</p><label>Lånebeløp (kr)<input id="rc-amount" inputmode="decimal" value="3000000"></label><div class="rate-cost-grid"><label>Rente A (%)<input id="rc-a" inputmode="decimal" value="5.50"></label><label>Rente B (%)<input id="rc-b" inputmode="decimal" value="5.00"></label></div><button class="calc-action" id="rc-btn" type="button">Sammenlign rentene</button><div aria-live="polite" class="tool-result" id="rc-result">Fyll inn tallene og sammenlign.</div><p class="article-note">Dette er en forenklet illustrasjon av nominell renteforskjell, ikke en beregning av effektiv rente. Gebyrer, nedbetaling og andre vilkår påvirker faktisk kostnad.</p><p><a data-revenue-context="nominal_rate_cost_tool_v1" data-revenue-event="problem_route" href="guide-sammenligne-boliglan.html">Se hvordan boliglånstilbud bør sammenlignes →</a></p><p><a class="cta" data-revenue-context="nominal_rate_cost_tool_v1" data-revenue-event="commercial_route" href="sjekk/boliglan/">Undersøk boliglånsalternativer →</a></p></section>''','html.parser').section
 first=s.select_one('section')
 first.insert_before(sec)
 script=s.new_tag('script');script.string="""(function(){function n(id){return Number((document.getElementById(id).value||'').replace(/\\s/g,'').replace(',','.'))}function fmt(v){return Math.round(v).toLocaleString('nb-NO')+' kr'}document.getElementById('rc-btn').addEventListener('click',function(){var a=n('rc-amount'),r1=n('rc-a'),r2=n('rc-b'),o=document.getElementById('rc-result');if(!(a>0)||!(r1>=0)||!(r2>=0)){o.textContent='Kontroller at alle feltene inneholder gyldige tall.';return}var d=Math.abs(a*(r1-r2)/100);o.innerHTML='<strong>'+fmt(d)+'</strong> estimert forskjell i nominell rentekostnad per år.';});})();"""
 s.body.append(script)
 if not s.select_one('link[href="design-v44.css"]'):
  s.head.append(s.new_tag('link',rel='stylesheet',href='design-v44.css'))
P.write_text(str(s),encoding='utf-8')
print('Nominal rate cost comparator applied')
