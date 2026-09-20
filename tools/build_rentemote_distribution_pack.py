from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
src=R/'data'/'rentemote-traffic-pack.json'
d=json.loads(src.read_text(encoding='utf-8'))
facts=d['facts'];dest=d['destinations']
pp=facts['policy_rate_before'];new=facts['new_mortgage_rate_july'];out=facts['outstanding_mortgage_rate_july']
base=f"""# Sparesjekk – Rentemøte Distribution Pack
Generated from data/rentemote-traffic-pack.json. Verify official figures before publishing after the decision.

## TikTok / Reels / Shorts 1 — kroneeffekten
HOOK: Hva betyr 0,25 prosentpoeng egentlig for boliglånet?
SCRIPT: Har du én million i restgjeld, tilsvarer 0,25 prosentpoeng omtrent 2 500 kroner i året før avdrag og skatt. To millioner: omtrent 5 000. Fire millioner: omtrent 10 000. Rentemøtet 24. september er derfor mer enn bare en prosent i en overskrift. Regn på ditt eget lån hos Sparesjekk.
ON-SCREEN: 0,25 pp → ca. 2 500 kr per million / år
CTA: Regn på ditt lån
URL: {dest['calculator']}

## TikTok / Reels / Shorts 2 — styringsrente ≠ boliglånsrente
HOOK: Banken din trenger ikke følge Norges Bank punkt for punkt.
SCRIPT: Før rentemøtet er styringsrenten {pp:.2f} prosent. Siste offisielle SSB-tall viser {new:.2f} prosent på nye boliglån og {out:.2f} prosent på utestående boliglån. Det er derfor din faktiske rente som teller. Etter rentemøtet: sjekk hva du betaler mot markedet.
CTA: Se Rentepuls
URL: {dest['primary']}

## TikTok / Reels / Shorts 3 — handling
HOOK: Rentemøte torsdag. Men bør DU gjøre noe?
SCRIPT: Ikke bytt bank bare på grunn av en overskrift. Se først hva rentebeslutningen betyr i kroner, hva du faktisk betaler, og om det finnes noe i økonomien din som er verdt å sjekke. Sparesjekken tar rundt to minutter.
CTA: Ta Sparesjekken
URL: {dest['savings_check']}

## Facebook / LinkedIn
Norges Bank har rentemøte 24. september. Styringsrenten før møtet er {pp:.2f} %, mens siste offisielle SSB-tall viser {new:.2f} % på nye boliglån. Vi har samlet beslutningen, kroneeffekten og verktøyene på én side. Ingen spådommer – bare offisielle tall og praktiske beregninger.
URL: {dest['primary']}

## Community answer template
Et nyttig skille er styringsrenten versus renten du faktisk har. Før møtet er styringsrenten {pp:.2f} %, mens siste SSB-tall for nye boliglån er {new:.2f} %. En forskjell på 0,25 prosentpoeng tilsvarer grovt ca. 2 500 kr per million i restgjeld per år før avdrag og skatt. Sparesjekk har en gratis kalkulator her:
URL: {dest['calculator']}
NOTE: Post only where directly relevant. No spam, no disguised promotion.

## Publishing guardrails
- After 24 Sep 10:00, replace pre-decision wording only after official Norges Bank verification.
- After 25 Sep, replace mortgage averages only after official SSB verification.
- Never claim a rate cut/hike before publication.
- Never promise savings, approval, or a better offer.
- Never publish automatically to communities or third-party accounts without explicit authorization.
"""
out=R/'traffic'/'rentemote-distribution-pack-20260924.md'
out.parent.mkdir(exist_ok=True);out.write_text(base.replace('.',',') if False else base,encoding='utf-8')
print(out)
