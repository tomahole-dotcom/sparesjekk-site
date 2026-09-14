# Sparesjekk – GSC commercial development gap

Dato: 2026-09-14
Kilde: Google Search Console, siste 28 settled days gjennom 2026-09-11.

## Hovedfunn

### 1. Bankbytte/flytte boliglån – reell query-overlap
De samme kjøpsnære søkene vises på flere sider samtidig:
- `bytte-bank-boliglan-komplett.html`
- `flytte-boliglan.html`
- `guide-bytte-bank-steg.html`

Eksempler: `bytte bank`, `bytte bank boliglån`, `flytte boliglån`, `flytte boliglån til annen bank`, `hvordan bytte bank`.

Dette er ikke grunnlag for å slette eller canonicalisere sider automatisk. Sidene har separate selv-canonicals og ulike tiltenkte roller. Første tiltak skal derfor være å tydeliggjøre informasjonsarkitekturen og gjøre hovedguiden til eksplisitt hub, mens `flytte-boliglan.html` rendyrkes mot selve låneflyttingen og `guide-bytte-bank-steg.html` mot operativ sjekkliste/prosess.

### 2. Kredittkort bonus/cashback – liten volumprøve, men sterk posisjon
`cashback-bonus-kredittkort.html` vises allerede rundt posisjon 5–9 for flere svært kommersielle søk som `bonus kredittkort`, `kredittkort bonus` og `kredittkort med bonus`.

Dette er et høyverdiområde for neste commercial batch, men volumet er foreløpig lite. Ikke lag duplikatsider. Styrk eksisterende side + kredittkortmatch + intern linking når bankbytte-batchen er avklart.

### 3. Refinansiering – høy kommersiell prioritet, men svake generiske posisjoner
`guide-refinansiering.html` og `refinansiere-forbruksgjeld.html` har impressions på relevante queries, men hoveddelen ligger fortsatt langt nede. `forbruksgjeld` har et signal rundt posisjon 18 på `refinansiere-forbruksgjeld.html` og bør følges tett. `Tilbudssjekken` og `gjeldsmiks-sjekk` skal brukes som produktdifferensiering fremfor å bygge flere generiske guider.

### 4. Bolig uten egenkapital – stor demand, lav kommersiell prioritet
`boliglan-uten-egenkapital.html` har mange query-varianter og betydelig impression-volum, men typisk posisjon 60–85. Bruk som topical-authority/traffic asset, ikke som første kommersielle utviklingsspor.

## Neste utviklingsrekkefølge
1. Bankbytte/flytte boliglån: rydde rolle/hierarki uten å endre canonical/title/meta tilfeldig.
2. Kredittkort bonus/cashback: styrke eksisterende side og veien til kredittkort-match.
3. Refinansiering: styrke verktøyreisen og interne signaler rundt samle gjeld/refinansiering.
4. Authority cluster: egenkapital/kausjonist/bolig uten egenkapital når kommersielle spor er gjort.

## SEO-regel
Ingen title/meta/H1/canonical/robots/schema-endringer uten separat kontroll mot SEO guard/baseline. Ingen nye sider hvis eksisterende side allerede dekker intentet.
