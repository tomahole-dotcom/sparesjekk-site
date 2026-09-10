# Sparesjekk – Problem-first Growth Map

## Styrende prinsipp
Bygg rundt problemet brukeren prøver å løse akkurat nå, ikke rundt produktnavnet alene.

Fast flyt:
**Problem/søk → konkret gratis sjekk eller beslutningsstøtte → personlig funn → forklaring → neste riktige handling → kommersiell sammenligning når naturlig.**

## Eksisterende problemspor
1. «Boliglånsrenten min virker for høy» → `boliglansrente-for-hoy.html` → `min-rente-vs-markedet.html` → belåningsgrad/forhandling/bankbytte → `/sjekk/boliglan/`
2. «Jeg har fått et bedre banktilbud» → `bankbytte-break-even.html` → `/sjekk/boliglan/`
3. «Jeg har mange smålån/kredittkort» → `gjeldsmiks-sjekk.html` → `refinansiering-kalkulator.html` → `/sjekk/forbrukslan/`
4. «Refinansiering gir lavere måned, men er det egentlig billigere?» → før/etter-kalkulator + løpetidsguide → `/sjekk/forbrukslan/`
5. «Kredittkortet koster mer enn jeg trodde» → `kredittkort-kostnadssjekk.html` → relevante kostnadsguider → kredittkortsammenligning
6. «Jeg eier bolig, men dyr gjeld presser økonomien» → `refinansiering-med-sikkerhet.html` / omstartslån → riktig kommersielt spor

## Neste problem-first trafikkvinkler
Prioriter etter søkeintensjon + verdi + naturlig konvertering.

### P1 – høy verdi
- **Banken satte opp renten – hva gjør jeg nå?**
  - Hendelses-/nyhetsdrevet inngang rundt renteendringer.
  - Kobles til Rentepuls, Rentegap, egen rente vs markedet og forhandling.
- **Banken satte ikke ned renten etter rentekutt**
  - Offisiell styringsrente vs egen rente; konkret kontrollpunkt.
  - Kan oppdateres automatisk rundt Norges Bank-beslutninger.
- **Har boligen steget nok til at jeg bør be om ny verdivurdering?**
  - Input: gammel boligverdi, estimert ny verdi, restgjeld.
  - Output: gammel/ny belåningsgrad og terskelbevegelser.
- **Når lønner det seg å betale ekstra på boliglånet?**
  - Input: ekstra beløp, rente, restgjeld.
  - Output: enkel renteeffekt og alternativet «behold buffer» uten investeringsråd.
- **Hvor mye dyr gjeld har jeg egentlig?**
  - Gjeldsmiks utvidet med månedlig belastning og andel høy-rente-gjeld.

### P2 – sterk SEO/nytte
- **Hvorfor blir kredittkortet dyrt i utlandet?**
  - Valutapåslag i kroner basert på faktisk reisebudsjett.
- **Er bonuskortet egentlig verdt årsgebyret?**
  - Break-even mellom årsgebyr og faktisk bonus/cashback; produktvilkår må være verifisert.
- **Hvor mye koster det å bare betale minstebeløpet?**
  - Krever forsiktig modellering og tydelige forutsetninger; høy problemløsningsverdi.
- **Har jeg for mange kredittrammer?**
  - Forklar kredittramme/gjeldsbelastning uten å late som kredittscore.
- **Bør jeg samle gjelden eller betale høyeste rente først?**
  - Nøytral beslutningsguide/verktøy; ingen garanti om refinansiering.

### P3 – omstart / vanskeligere situasjoner
- **Jeg får avslag på refinansiering – hva kan være årsaken?**
  - Beslutningstre, ikke kredittvurdering.
- **Jeg har betalingsanmerkning og eier bolig – hvilke spor finnes?**
  - Informasjon om mulige veier, risiko og sikkerhet; ikke lovnader.
- **Lavere månedsbeløp, men høyere totalpris**
  - Egen problem-side som bruker løpetidsfellen fra eksisterende kalkulator.

## Hendelsesdrevet trafikkmotor
Rente- og statistikkoppdateringer skal brukes som trafikkhendelser:
- Norges Bank rentebeslutning → oppdater Rentepuls/Rentegap → problem-side «banken satte opp/ned renten – hva gjør jeg?»
- SSB nye boliglånsrenter → oppdater «Min rente vs markedet» og månedlig dataoppsummering.
- Vesentlig endring → kort kildebasert analyse med internlenker til verktøy.

Ikke lag en ny tynn artikkel for hver måned. Oppdater sterke eviggrønne URL-er og behold historikk/data der det gir verdi.

## Konverteringsregel
Ikke send alle rett til affiliate. Først må brukeren få et konkret funn eller forstå problemet bedre. Kommersiell CTA vises når handlingen naturlig er «undersøk/sammenlign alternativer».

## Måling
For hvert problemspor mål:
- landing
- verktøystart
- fullført verktøy
- resultatkategori
- neste-steg-klikk
- kommersiell CTA-klikk
- partnerklikk/konvertering når tracking er aktiv

## Produksjonsrekkefølge
1. Problemhub + høy boliglånsrente (bygget 11.09.2026)
2. «Banken satte ikke ned renten» koblet til Rentepuls/Rentegap
3. Ny-verdivurdering / belåningsgrad-før-etter
4. Valutapåslag i kroner
5. Bonus break-even
6. Refinansiering-avslag beslutningstre
7. Månedlig data-/hendelsesmotor

## Stoppregel
Ikke masseproduser problem-sider med samme innhold. Ny URL krever eget problem, egen beslutning eller egen beregning og en tydelig kundereise.