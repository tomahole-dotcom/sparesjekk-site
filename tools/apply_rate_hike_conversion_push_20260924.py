from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
FILES = ["index.html", "boliglan.html", "ta-sparesjekken.html", "min-rente-vs-markedet.html"]

for filename in FILES:
    p = ROOT / filename
    if not p.exists():
        continue
    s = BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser")
    box = s.select_one('[data-rate-decision="20260924"]')
    if not box:
        raise RuntimeError(f"missing rate decision box: {filename}")
    box.clear()
    b = s.new_tag("b")
    b.string = "Renten er hevet – er boliglånet ditt fortsatt konkurransedyktig?"
    box.append(b)
    p1 = s.new_tag("p")
    p1.string = "Norges Bank har hevet styringsrenten fra 4,25 til 4,50 %. Det betyr ikke at banken din automatisk øker boliglånsrenten med 0,25 prosentpoeng, men nå er et naturlig tidspunkt å kontrollere hva du betaler og undersøke alternativer."
    box.append(p1)
    p2 = s.new_tag("p")
    a = s.new_tag("a", href="/sjekk/boliglan/?intent=sammenligne&origin=rate-hike-20260924")
    a["data-revenue-event"] = "commercial_route"
    a["data-revenue-context"] = "rate_hike_20260924"
    a.string = "Sjekk og sammenlign boliglån →"
    p2.append(a)
    box.append(p2)
    p3 = s.new_tag("p")
    p3["class"] = ["small"]
    a2 = s.new_tag("a", href="/rentemote-hva-betyr-det.html")
    a2.string = "Se hva rentehevingen betyr i kroner →"
    p3.append(a2)
    box.append(p3)
    p.write_text(str(s), encoding="utf-8")

p = ROOT / "rentemote-hva-betyr-det.html"
s = BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser")
lead = s.select_one("article .lead")
if lead:
    lead.string = "Norges Bank har hevet styringsrenten fra 4,25 til 4,50 prosent. Nå er et naturlig tidspunkt å kontrollere om boliglånsrenten din fortsatt er konkurransedyktig – og hva selv små renteforskjeller betyr i kroner."
live = s.select_one('[data-renteblitz="v1"]')
if live:
    ul = live.find("ul")
    if ul:
        links = ul.find_all("li", recursive=False)
        commercial = next((li for li in links if li.find("a") and li.find("a").get("data-revenue-event") == "commercial_route"), None)
        if commercial:
            commercial.extract()
            ul.insert(0, commercial)
            a = commercial.find("a")
            a.string = "Sjekk og sammenlign boliglån nå →"
            a["href"] = "sjekk/boliglan/?intent=sammenligne&origin=rentemote-blitz"
p.write_text(str(s), encoding="utf-8")
print("RATE_HIKE_CONVERSION_PUSH_PASS")
