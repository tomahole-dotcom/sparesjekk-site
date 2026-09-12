# Sparesjekk commercial diagnosis engine

Dato: 12. september 2026

## Styrende retning
Sparesjekk skal ikke vinne ved å kopiere store markedsoversikter. Vi skal ligge ett steg før markedsplassen: brukeren beskriver sin faktiske økonomi, får en konkret diagnose/estimat, og sendes deretter til relevant sammenligning når det gir mening.

## 1. Gjeldsdiagnose – høyeste kommersielle prioritet
Eksisterende `gjeldsmiks-sjekk.html` er kjernen, men skal utvides fra oversikt til handlingsmotor.

Input per gjeldspost:
- type: kredittkort / forbrukslån / smålån / annen kreditt
- restsaldo
- effektiv rente (foretrukket) eller nominell rente hvis effektiv ikke er kjent
- månedlig betaling
- gjenstående løpetid når kjent
- løpende gebyr når kjent

Resultat:
- samlet gjeld
- estimert dagens rentekostnad/kostnadsnivå
- vektet rente
- samlet månedsbelastning
- scenarioer ved lavere rente, tydelig merket som estimater – ikke tilbud
- estimert forskjell per måned og over valgt sammenligningsperiode
- advarsel mot løpetidsfellen: lavere termin er ikke nødvendigvis lavere totalpris
- prioritert neste handling

Kommersiell overgang:
`Sjekk hvilke faktiske tilbud du kan få fra flere banker`.
Partner/markedsplass (f.eks. Lendo) aktiveres bare når avtale, destinasjon og tracking er verifisert. Vi lover aldri at brukeren får lavere rente. Faktiske tilbud avgjør besparelsen.

Viktig differensiering:
Lendo har allerede gjeldsoversikt og refinansieringskalkulator. Sparesjekk skal derfor ikke være en svak kopi. Vår fordel skal være at brukeren kan legge inn hver gjeldspost og forstå HVOR problemet ligger før søknad: hvilke poster driver kostnaden, hva et realistisk rentescenario ville bety, og om en lavere termin bare skyldes lengre løpetid.

## 2. Kredittkortdiagnose – separat motor
Ikke bygg enda en komplett liste over hundrevis av kort. Store sammenligningstjenester dekker dette allerede.

Spør først hvordan kortet brukes:
- betales hele fakturaen hver måned? ja/nei
- omtrent månedlig kortbruk
- dagligvarer
- drivstoff
- reise
- utenlandsk valuta
- netthandel
- bonus/cashback ønskes
- reise-/andre forsikringer viktige
- eksisterende kortsaldo og rente hvis saldo bæres

To resultatspor:
A. Betaler alltid hele fakturaen: ranger KORTTYPE/egenskaper etter estimert nettoverdi = relevante fordeler minus kjente gebyrer/kostnader. Senere kan verifiserte partnerkort kobles til.
B. Bærer saldo: bonus/cashback nedprioriteres. Vis estimert finansieringskostnad og pek først mot nedbetaling/refinansieringsvurdering når relevant.

Dette løser et konkurransehull: brukeren starter med eget bruksmønster, ikke en 100+ kort lang produktliste.

## 3. Boliglånsdiagnose – trafikk + lead
Input: saldo, rente, boligverdi, evt. gebyr, gjenværende løpetid.
Resultat: belåningsgrad, rente vs markedsreferanse, estimert kroneeffekt av lavere rente, break-even ved bankbytte og konkret forhandlingsgrunnlag. CTA: undersøk faktisk tilbud/forhandle/bytte når relevant.

## 4. Felles flyt
Trafikkside/artikkel -> diagnose -> personlig estimat -> forklaring -> handling -> verifisert kommersiell sammenligning.

Artikler er innganger, ikke sluttproduktet.

## 5. Konkurrentfunn som styrer produktet
- Store aktører har allerede brede produktlister og filtrering for kredittkort.
- Markedsplasser har allerede generelle låne-/refinansieringskalkulatorer og søknad til flere banker.
- Cashback/rabatt-oversikter finnes allerede.

Derfor skal Sparesjekk eie `før sammenligningen`: problemidentifikasjon, scenario, kroner og prioritert handling.

## 6. Monetiseringsprioritet
1. Refinansiering / usikret gjeld
2. Kredittkort – behovsmatching + kryssignal til gjeldsdiagnose når saldo bæres
3. Boliglån

## 7. Compliance / tillit
- Estimat skal aldri presenteres som faktisk besparelse eller lånetilbud.
- Effektiv rente foretrekkes ved sammenligning av faktiske lånekostnader.
- Ingen oppdiktede partnerpriser, renter eller godkjenningssannsynlighet.
- Kommersielle CTA-er merkes ANNONSE / REKLAME.
- Partnerlenker aktiveres først etter verifisert avtale og tracking.
- Tall brukeren legger inn bør som standard behandles lokalt i nettleseren.

## 8. Neste byggegate
Før ny produksjonsdeploy:
1. spesifiser Gjeldsdiagnose V2-beregning og UI
2. spesifiser Kredittkortdiagnose V1
3. kartlegg eksisterende sider som skal mate disse motorene
4. samle teknisk SEO-opprydding (`?v=` og URL-signaler)
5. implementer i én større batch
6. full QA
7. én deploy
