# Sparesjekk Traffic Engine – competitor gap

Date: 2026-09-13
Status: RESEARCHED – no external publishing or outreach

## Purpose
Identify traffic opportunities that strengthen Sparesjekk without duplicating generic Norwegian finance calculators or weakening existing SEO.

## Market observation
Norwegian finance/calculator competitors increasingly combine calculators with explanatory content. Generic loan calculators are therefore not a sufficient differentiator.

Observed competitors/resources:
- Financer: comparison/review content around loan calculators.
- Regninga: broad calculator library including a mortgage rate checker, refinancing and buy-vs-rent.
- Kalkulatorbanken: large calculator catalogue and free embeddable calculators.
- Lynt: free finance calculators plus explanatory articles/definitions.
- Pengekalkulator: loan/refinancing/debt calculator positioning.
- Finansportalen/Forbrukerrådet: authoritative comparison and bank-switching resources.

## Sparesjekk advantage to build around
Do not compete on calculator count. Build a connected decision path:

1. Official data / market context
   - rentegap-indeks.html
2. Personal diagnosis
   - min-rente-vs-markedet.html
   - belaningsgrad-sjekk.html
3. Krone effect
   - boliglanskalkulator-renteforskjell.html
4. Decision threshold
   - bankbytte-break-even.html
5. Action
   - negotiation / bank-switch guides

This creates a stronger intent chain than a standalone calculator.

## High-priority traffic gaps

### A1 – “Is my mortgage rate good?” cluster
Search/user intent: compare own rate against market, understand whether it is worth negotiating.
Route: Rentegap -> Min rente vs markedet -> krone effect -> negotiation/bank switch.
Priority: VERY HIGH.

### A2 – “Is switching bank worth it?” cluster
Search/user intent: rate saving versus switching/establishment costs.
Route: rate difference -> bankbytte break-even -> practical switching guide.
Priority: VERY HIGH.

### A3 – Loan/equity eligibility cluster
Search/user intent: how much can I borrow, equity shortfall, guarantor/co-borrower.
Existing GSC impressions make this a consolidation opportunity rather than a reason to create many new pages.
Priority: VERY HIGH.

### A4 – Refinancing decision cluster
Search/user intent: whether a refinancing offer is genuinely cheaper after effective rate, fees and monthly cash-flow effects.
Route: refinancing guide -> refinancing calculator -> tilbudssjekk-refinansiering.
Priority: HIGH.

## What NOT to build now
- Another generic mortgage calculator merely calculating monthly payment.
- Thin pages for near-identical rate keywords.
- A duplicate generic “data and insights” page; Rentegap already serves the data-resource role.
- Large numbers of calculators merely to match competitor catalogue size.
- Paid backlink campaigns or low-quality directory links.

## Distribution implication
Every Traffic Engine asset should have one primary problem/intent and one deep-link destination. Social/forum/editorial distribution should send users to the most specific useful tool, not the homepage.

## Next implementation gate
Before adding new pages, inspect the existing internal routing in tools/build_site.py for these missing/desired links:
- guide-bytte-bank-steg.html -> bankbytte-break-even.html
- bytte-bank-boliglan-komplett.html -> bankbytte-break-even.html
- flytte-boliglan.html -> bankbytte-break-even.html
- guide-effektiv-nominell-rente.html -> boliglanskalkulator-renteforskjell.html
- guide-refinansiering.html -> refinansiering-kalkulator.html
- refinansiere-forbruksgjeld.html -> refinansiering-kalkulator.html
- refinansiering-kalkulator.html -> tilbudssjekk-refinansiering.html

Only add links that are missing and contextually natural. Batch any site-visible changes and run SEO guard + full QA before production deployment.

## External-action rule
Do not send email, submit forms, post to forums/social media, or otherwise publish externally without explicit approval. Any future automated email must use a verified Sparesjekk-domain sender in Gmail.