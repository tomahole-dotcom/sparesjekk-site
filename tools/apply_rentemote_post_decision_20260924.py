from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RATE = "4,50 %"
CHANGE = "0,25 prosentpoeng"


def read(name):
    p = ROOT / name
    return p, BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser")


def write(p, soup):
    p.write_text(str(soup), encoding="utf-8")


def upsert_notice(filename, after_selector="h1"):
    p, s = read(filename)
    for old in s.select('[data-rate-decision="20260924"]'):
        old.decompose()
    anchor = s.select_one(after_selector) or s.select_one("main")
    box = s.new_tag("div")
    box["class"] = ["trust-box"]
    box["data-rate-decision"] = "20260924"
    b = s.new_tag("b")
    b.string = "Norges Bank hever styringsrenten til 4,50 %"
    box.append(b)
    p1 = s.new_tag("p")
    p1.string = "Rentebeslutningen 24. september innebærer en økning på 0,25 prosentpoeng. Det betyr ikke at boliglånsrenten automatisk øker like mye eller samtidig."
    box.append(p1)
    p2 = s.new_tag("p")
    a = s.new_tag("a", href="/rentemote-hva-betyr-det.html")
    a.string = "Se hva rentehevingen kan bety i kroner →"
    p2.append(a)
    box.append(p2)
    if anchor.name == "main":
        anchor.insert(0, box)
    else:
        anchor.insert_after(box)
    write(p, s)


# Main Rentepuls page: convert pre-decision content to confirmed decision content.
p, s = read("rentemote-hva-betyr-det.html")
if s.title:
    s.title.string = "Norges Bank hever renten til 4,50 % – hva betyr det for boliglånet? | Sparesjekk"
desc = s.find("meta", attrs={"name": "description"})
if desc:
    desc["content"] = "Norges Bank hever styringsrenten fra 4,25 til 4,50 prosent. Se hva 0,25 prosentpoeng kan bety i kroner og hva boliglånskunder bør kontrollere nå."
ogt = s.find("meta", attrs={"property": "og:title"})
if ogt:
    ogt["content"] = "Norges Bank hever renten til 4,50 % | Sparesjekk"
ogd = s.find("meta", attrs={"property": "og:description"})
if ogd:
    ogd["content"] = "Styringsrenten heves 0,25 prosentpoeng. Regn kroneeffekten og sjekk om boliglånsrenten din er verdt å utfordre."
h1 = s.select_one("article h1")
if h1:
    h1.string = "Norges Bank hever styringsrenten til 4,50 % – hva betyr det for boliglånet?"
lead = s.select_one("article .lead")
if lead:
    lead.string = "Norges Bank besluttet 24. september å heve styringsrenten fra 4,25 til 4,50 prosent. Her gjør vi økningen om til enkle kroneeksempler og viser hva du bør kontrollere på ditt eget boliglån."

live = s.select_one('[data-renteblitz="v1"]')
if live:
    live.clear()
    h = s.new_tag("h2"); h.string = "Rentehevingen på 60 sekunder"; live.append(h)
    q = s.new_tag("p"); q.string = "Styringsrenten heves med 0,25 prosentpoeng til 4,50 prosent. Bankenes boliglånsrenter bestemmes likevel av bankene selv, så økningen trenger ikke slå gjennom én-til-én eller på samme tidspunkt."; live.append(q)
    strip = s.new_tag("div"); strip["class"] = ["number-strip"]
    for val, label in [("4,50 %", "ny styringsrente"), ("+0,25 pp", "dagens endring"), ("2 500 kr", "per lånte million/år*"), ("25.09", "nye SSB-bankrenter")]:
        d=s.new_tag("div"); a=s.new_tag("strong"); a.string=val; b=s.new_tag("span"); b.string=label; d.extend([a,b]); strip.append(d)
    live.append(strip)
    note=s.new_tag("p"); note["class"]=["small"]; note.string="*Enkelt årsoverslag dersom hele renteøkningen på 0,25 prosentpoeng slår gjennom på lånet. Før skatt, avdrag og virkningsdato."; live.append(note)
    ul=s.new_tag("ul")
    for href,label,event,ctx in [
        ("boliglanskalkulator-renteforskjell.html","Regn rentehevingen på ditt lån →","problem_route","renteblitz_calculator"),
        ("ta-sparesjekken.html?src=rentemote_blitz","Ta Sparesjekken →","savings_check_entry","rentemote_blitz"),
        ("sjekk/boliglan/?intent=sammenligne&origin=rentemote-blitz","Sammenlign boliglån →","commercial_route","rentemote_blitz")]:
        li=s.new_tag("li"); a=s.new_tag("a",href=href); a.string=label; a["data-revenue-event"]=event; a["data-revenue-context"]=ctx; li.append(a); ul.append(li)
    live.append(ul)

# Replace the old pre-decision trust box content without touching later historical explanations.
trust = s.select_one("article .trust-box")
if trust:
    trust.clear()
    b=s.new_tag("b"); b.string="Rentebeslutning 24. september 2026"; trust.append(b)
    x=s.new_tag("p"); x.string="Norges Bank hever styringsrenten fra 4,25 til 4,50 prosent, en økning på 0,25 prosentpoeng."; trust.append(x)
    y=s.new_tag("p"); y.string="Siste publiserte SSB-tall før dagens beslutning viser 5,29 % på nye boliglån og 5,31 % på utestående boliglån i juli. Nye SSB-bankrenter er planlagt 25. september."; trust.append(y)
    z=s.new_tag("p"); sm=s.new_tag("small"); sm.string="Styringsrenten er ikke boliglånsrenten. Bankene avgjør selv sine utlånsrenter."; z.append(sm); trust.append(z)

# Turn the old 'next meeting' section into the immediate post-decision explanation.
for sec in s.select("article section"):
    h2=sec.find("h2")
    if h2 and h2.get_text(" ", strip=True).startswith("Neste rentemøte: 24. september"):
        sec.clear()
        h=s.new_tag("h2"); h.string="Norges Bank hevet renten – hva skjer nå?"; sec.append(h)
        for txt in [
            "Beslutningen er en heving på 0,25 prosentpoeng fra 4,25 til 4,50 prosent.",
            "For boliglånskunder er neste spørsmål hva den enkelte banken gjør. En endring i styringsrenten bestemmer ikke automatisk størrelsen eller tidspunktet på en eventuell endring i boliglånsrenten.",
            "Bruk derfor dagens beslutning som et tidspunkt for å kontrollere egen nominell og effektiv rente, regne kroneverdien av renteforskjeller og eventuelt sammenligne eller forhandle med banken."
        ]:
            q=s.new_tag("p"); q.string=txt; sec.append(q)
        break

# Update the first current-status strip after 'Rentepuls akkurat nå'.
for sec in s.select("article section"):
    h2=sec.find("h2")
    if h2 and h2.get_text(" ", strip=True)=="Rentepuls akkurat nå":
        strip=sec.select_one(".number-strip")
        if strip:
            vals=strip.find_all("strong")
            labels=strip.find_all("span")
            if vals: vals[0].string="4,50 %"
            if len(vals)>3: vals[3].string="05.11 kl. 10"
            if len(labels)>3: labels[3].string="neste rentebeslutning"
        break

# Update decision checklist wording.
for li in s.select("article li"):
    t=li.get_text(" ", strip=True)
    if "om den holdes på 4,25 prosent eller endres" in t:
        li.clear(); st=s.new_tag("strong"); st.string="Selve beslutningen:"; li.append(st); li.append(" styringsrenten ble hevet fra 4,25 til 4,50 prosent.")

article_note=s.select_one(".article-note")
if article_note:
    article_note.string="Datakontroll: 24. september 2026. Rentebeslutningen er oppdatert etter offentliggjøringen kl. 10. Detaljert PPR 3/26-guidance oppdateres separat når full primærkilde er tilgjengelig."
write(p, s)

# Surface the event on the highest-value relevant entry pages without redesigning them.
for filename in ["index.html", "boliglan.html", "ta-sparesjekken.html", "min-rente-vs-markedet.html"]:
    if (ROOT / filename).exists():
        upsert_notice(filename)

print("POST_DECISION_RATE_UPDATE_PASS")
