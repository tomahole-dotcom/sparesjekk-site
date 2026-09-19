from pathlib import Path
from bs4 import BeautifulSoup

PAGE=Path("fastrente-vs-flytende-kalkulator.html")
if PAGE.exists():
    raise SystemExit("page already exists")

html=r'''<!doctype html>
<html lang="nb"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fastrente vs flytende rente: break-even-kalkulator | Sparesjekk</title>
<meta name="description" content="Sammenlign et konkret fastrentetilbud med flytende boliglånsrente. Se break-even-renten og hva renteforskjellen betyr i kroner.">
<link rel="canonical" href="https://sparesjekk.no/fastrente-vs-flytende-kalkulator.html">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="stylesheet" href="style.css?v=27"><link rel="stylesheet" href="design-v36.css"><link rel="stylesheet" href="design-v44.css">
<style>
.fixed-shell{max-width:960px;margin:auto;padding:48px 20px 80px}.fixed-hero{max-width:780px}.fixed-hero h1{font-size:clamp(2rem,5vw,3.35rem);line-height:1.06}.fixed-tool,.fixed-note,.fixed-data{border:1px solid var(--line);border-radius:20px;background:#fff;padding:22px;margin:24px 0}.fixed-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.fixed-grid label{font-weight:750}.fixed-grid input{width:100%;margin-top:7px}.fixed-result{margin-top:20px;padding:20px;border-radius:16px;background:var(--soft)}.fixed-actions{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px}.fixed-actions a{display:block;border:1px solid var(--line);border-radius:14px;padding:16px;text-decoration:none;font-weight:800}.fixed-data strong{font-size:1.4rem}.fixed-shell p,.fixed-shell li{line-height:1.7}@media(max-width:650px){.fixed-grid,.fixed-actions{grid-template-columns:1fr}}
</style>
</head><body>
<header class="header"><a class="logo" href="index.html">Spare<span>sjekk</span></a><button aria-label="Åpne meny" class="menu-btn" onclick="document.querySelector('.topnav').classList.toggle('open')">☰</button><nav class="topnav"><a href="boliglan.html">Boliglån</a><a href="forbrukslan.html">Forbrukslån</a><a href="omstartslan.html">Omstartslån</a><a href="kredittkort.html">Kredittkort</a><a href="guider.html">Guider</a></nav></header>
<main class="fixed-shell">
<section class="fixed-hero"><p class="eyebrow">BOLIGLÅN · BESLUTNINGSVERKTØY</p><h1>Fastrente eller flytende? Finn break-even</h1><p class="lead">Sammenlign et konkret fastrentetilbud med dagens flytende rente. Verktøyet viser hvilken <strong>gjennomsnittlig flytende rente</strong> over bindingstiden som gir samme enkle rentekostnad som fastrenten.</p></section>
<section class="fixed-data"><strong>Offisiell temperaturmåling: juli 2026</strong><p>SSB målte nye boliglån med flytende rente til <strong>5,29 %</strong> og nye boliglån med fast rente til <strong>5,42 %</strong>. Dette er markedsstatistikk, ikke priser du nødvendigvis kan få.</p><p><a href="https://www.ssb.no/bank-og-finansmarked/finansinstitusjoner-og-andre-finansielle-foretak/statistikk/renter-i-banker-og-kredittforetak" target="_blank" rel="noopener">Kilde: SSB – Renter i banker og kredittforetak →</a></p></section>
<section class="fixed-tool" data-fixed-break-even="v1"><h2>Regn på ditt tilbud</h2><div class="fixed-grid">
<label>Fastrentetilbud (%)<input id="fx-fixed" inputmode="decimal" placeholder="f.eks. 5,10"></label>
<label>Flytende rente i dag (%)<input id="fx-float" inputmode="decimal" placeholder="f.eks. 5,29"></label>
<label>Lånesaldo (kr)<input id="fx-loan" inputmode="numeric" placeholder="f.eks. 3000000"></label>
<label>Bindingstid (år)<input id="fx-years" inputmode="numeric" placeholder="f.eks. 3"></label>
</div><button id="fx-calc" type="button">Vis break-even</button><div id="fx-result" class="fixed-result" hidden></div>
<p class="article-note">Forenklet sammenligning av renter på uendret saldo. Den modellerer ikke nedbetaling, gebyrer, skatt, terminpremie eller fremtidige renteendringer og er ikke en prognose.</p></section>
<section><h2>Hva betyr break-even?</h2><p>Hvis fastrenten er 5,10 %, er break-even for den enkle rentekostnaden også 5,10 %: flytende rente må i gjennomsnitt ligge på samme nivå gjennom perioden for å gi samme renteutgift på samme saldo. Dagens forskjell forteller derfor ikke hva som faktisk blir billigst.</p><p>Norges Bank peker på at forventede kostnader påvirkes av blant annet terminpremie og bankenes utlånsmargin, og at utfallet avhenger av hvordan rentene faktisk utvikler seg.</p></section>
<section class="fixed-note"><h2>Fastrente kjøper også forutsigbarhet</h2><p>Valget handler ikke bare om lavest forventet rente. Fastrente kan gjøre betalingene mer forutsigbare, mens flytende rente normalt gir større fleksibilitet. Å gå ut av en fastrenteavtale før tiden kan utløse over- eller underkurs/rentetapserstatning avhengig av renteutviklingen og avtalen.</p><p><a href="https://www.norges-bank.no/bankplassen/arkiv/2025/flytende-rente-eller-fastrente/" target="_blank" rel="noopener">Bakgrunn: Norges Bank om fast og flytende rente →</a></p></section>
<section><h2>Hva bør du gjøre med resultatet?</h2><div class="fixed-actions"><a data-revenue-event="commercial_route" data-revenue-context="fixed_vs_float_compare_v1" href="sjekk/boliglan/?intent=sammenligne">Sammenlign boliglånsalternativer →</a><a data-revenue-event="problem_route" data-revenue-context="fixed_vs_float_negotiate_v1" href="guide-forhandle-rente.html">Forhandle dagens rente →</a></div><p class="partner-note">ANNONSE / REKLAME – går du videre til en kommersiell partner kan Sparesjekk motta provisjon.</p></section>
<section><h2>Relaterte verktøy</h2><p><a href="min-rente-vs-markedet.html">Sjekk renten din mot markedet</a> · <a href="boliglanskalkulator-renteforskjell.html">Regn renteforskjell i kroner</a> · <a href="rentegap-indeks.html">Se Rentegap-indeksen</a></p></section>
<p class="article-note">Generell informasjon, ikke personlig økonomisk rådgivning. Datakontroll: 20. september 2026.</p>
</main><footer><div class="footer-logo">Spare<span>sjekk</span></div><p>En uavhengig informasjonsside om privatøkonomi.</p></footer>
<script>
(function(){function n(id){return Number((document.getElementById(id).value||'').replace(/\s/g,'').replace(',','.'))}var b=document.getElementById('fx-calc'),o=document.getElementById('fx-result');b.addEventListener('click',function(){var f=n('fx-fixed'),v=n('fx-float'),l=n('fx-loan'),y=n('fx-years');if(!(f>0)||!(v>0)||!(l>0)||!(y>0)){o.hidden=false;o.innerHTML='<strong>Fyll inn alle fire feltene.</strong>';return}var d=v-f,annual=Math.abs(l*d/100),cls=d>0.05?'fixed_below_today':d<-.05?'fixed_above_today':'near_today';o.hidden=false;o.innerHTML='<h3>Break-even: '+f.toLocaleString('nb-NO',{minimumFractionDigits:2,maximumFractionDigits:2})+' % gjennomsnittlig flytende rente</h3><p>Dagens oppgitte flytende rente er <strong>'+v.toLocaleString('nb-NO',{minimumFractionDigits:2,maximumFractionDigits:2})+' %</strong>. Forskjellen mot fastrentetilbudet er <strong>'+Math.abs(d).toLocaleString('nb-NO',{minimumFractionDigits:2,maximumFractionDigits:2})+' prosentpoeng</strong>, omtrent <strong>'+annual.toLocaleString('nb-NO',{maximumFractionDigits:0})+' kr</strong> i rente første år på uendret saldo.</p><p>Dette sier <strong>ikke</strong> hvilken renteform som blir billigst over '+y.toLocaleString('nb-NO')+' år. Det avhenger av den faktiske utviklingen i flytende rente og avtalevilkårene.</p>';if(typeof gtag==='function')gtag('event','fixed_rate_break_even_result',{result_class:cls,source_path:location.pathname});});})();
</script>
<script data-sparesjekk-revenue-tracking="v1">document.addEventListener('click',function(e){var a=e.target.closest('[data-revenue-event]');if(!a||typeof gtag!=='function')return;gtag('event',a.dataset.revenueEvent,{revenue_stage:a.dataset.revenueEvent,source_path:location.pathname,destination:a.getAttribute('href')||'',link_text:(a.textContent||'').trim().slice(0,100),revenue_context:a.dataset.revenueContext||''});});</script>
</body></html>'''
PAGE.write_text(html,encoding="utf-8")

# add focused discovery links; do not rewrite ranking copy
for name in ["boliglan.html","boliglan-guider.html","guider.html"]:
    p=Path(name)
    if not p.exists(): continue
    s=BeautifulSoup(p.read_text(encoding="utf-8"),"html.parser")
    if s.select_one('[data-fixed-rate-tool-link="v1"]'): continue
    target=s.find("main") or s.body
    box=s.new_tag("section")
    box["class"]="fixed-rate-tool-link"
    box["data-fixed-rate-tool-link"]="v1"
    box.append(BeautifulSoup('<h2>Fast eller flytende rente?</h2><p>Har du fått et fastrentetilbud? <a href="fastrente-vs-flytende-kalkulator.html">Finn break-even mot flytende rente →</a></p>',"html.parser"))
    target.append(box)
    p.write_text(str(s),encoding="utf-8")

# sitemap
sp=Path("sitemap.xml")
if sp.exists():
    t=sp.read_text(encoding="utf-8")
    url="https://sparesjekk.no/fastrente-vs-flytende-kalkulator.html"
    if url not in t:
        t=t.replace("</urlset>",f"<url><loc>{url}</loc></url></urlset>")
        sp.write_text(t,encoding="utf-8")
print("Fixed-vs-floating break-even asset applied")
