from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'sjekk/kredittkort/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
card=s.select_one('.partner-card[data-partner="Zensum"]')
if not card: raise SystemExit('Missing Zensum credit-card partner card')
desc=card.find('p')
if desc: desc.string='Gå videre til Zensum for å se og sammenligne aktuelle kredittkortalternativer. Kontroller renter, gebyrer, fordeler og øvrige vilkår før du velger.'
cta=card.select_one('a.partner-cta')
if not cta: raise SystemExit('Missing credit-card partner CTA')
cta.string='Se kredittkortalternativer hos Zensum →'
cta['data-revenue-stage']='partner_outclick'
cta['data-revenue-context']='credit_card_match'
note=s.select_one('.partner-preview .partner-note')
if note: note.string='Du sendes videre til Zensum. Sparesjekk kan motta provisjon dersom du går videre. Det koster ikke ekstra å bruke lenken. Sammenlign alltid faktiske vilkår og total kostnad før du velger.'
p.write_text(str(s),encoding='utf-8')
print('Credit-card partner clarity applied')
