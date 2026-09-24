# SPARESJEKK.NO — MASTER ROADMAP

Last updated: 2026-09-25
Source of truth: GitHub branch `seo-content-v34-master` + verified production where verification is actually available.

## CURRENT PRODUCTION STATUS
- Release 69 stabilization completed and locked: canonical navigation, 24.09.2026 rate event, Boliglån nesting repair and Tilbudssjekk/refinancing layout repair.
- Releases 70–76 continued Phase B conversion cleanup.
- Release 76 (`credit-card partner clarity`, run 36066148456) completed successfully through system repair, regression hard gate, tested release creation, FTP-secret validation and production FTP deploy.
- Canonical navigation is protected by `tools/system_repair.py`; QA requires `Problemløser` and `Om oss`.
- Homepage/current-rate component is regression protected.
- Boliglån nesting repair and follow-up structure are regression protected.
- Tilbudssjekk/refinansiering structural layout and no-offer route to Gjeldssjekken are regression protected.
- Gjeldssjekk → Tilbudssjekk route is regression protected.
- Forbrukslån and Omstartslån expose direct partner routes from the hero and partner names before sorting/matching.
- Kredittkort now clearly separates concrete re:member Gold/Black products from Sambla/Zensum comparison services; hero routes directly to the partner area.

## LOCKED / DONE
- Release 69 stabilization items. Do not reopen without a verified defect.
- re:member Gold/Black presentation uses real product imagery. Do not replace with CSS/generated cards or redesign without a concrete defect.
- Existing working affiliate integrations must not be removed without a concrete reason.
- Gjeldssjekk has already received UI work; verify before changing and do not redesign by default.
- Conversion bridges on Kredittkort and Forbrukslån.
- Direct partner anchors/routes on Forbrukslån and Omstartslån.
- Credit-card partner clarity: direct re:member products separated from comparison/intermediary services.

Fixed failure process: root cause → repair source of truth → regression test → deploy → verify production when a real verification method is available → lock → continue.

## CURRENT QA LIMITATION
- Paid TinyFish browser automation is intentionally not being used unless explicitly requested by the user.
- Do not claim browser/visual production verification when it has not actually been performed.
- GitHub Actions success confirms tested release/deploy mechanics, not by itself visual correctness.
- Use available free production retrieval, user screenshots, source inspection and regression gates; visual defects found in screenshots become concrete repair inputs.

## CURRENT PARTNERS / MONETIZATION
Current/previous commercial tracks include boliglån, forbrukslån, refinansiering and kredittkort. Partners used/evaluated include Tjenestetorget, Zensum, Sambla, DigiFinans, Axo Finans and re:member. Preserve working attribution/tracking.

Known project links:
- Sambla kredittkort: `https://go.adt246.net/t/t?a=2020411608&as=2102543040&t=2&tk=1`
- Sambla refinansiering: `https://go.adt246.net/t/t?a=2021427585&as=2102543040&t=2&tk=1`

Partner presentation principles:
- partner names should be discoverable before a user is asked to choose a commercial route;
- explain what happens when the user clicks;
- distinguish direct products from comparison/intermediary services;
- keep advertising/commission disclosure clear;
- do not turn pages into aggressive affiliate walls.

## PRODUCT DIRECTION
Sparesjekk should help Norwegian consumers discover unnecessary costs, understand financial choices, use simple calculators/problem-solvers, compare relevant alternatives and reach an appropriate provider/partner. Long-term umbrella product: **Ta Sparesjekken**. Avoid becoming a generic AI-content portal.

## DESIGN / CONVERSION — ACTIVE PHASE B
Goal: reduce visible text chaos while preserving useful SEO content.

Principles:
- shorter visible text surfaces and stronger sectioning;
- more whitespace and a clear visual hierarchy;
- one obvious primary next action per decision point;
- users should understand where a CTA leads before clicking;
- partner names should not be hidden deep in the journey;
- preserve SEO copy but improve its presentation rather than deleting valuable content;
- mobile should collapse naturally to a clear single-column journey;
- flow target: `see → understand → choose → click`;
- repair component/source structure instead of accumulating CSS patches.

Completed Phase B batches through Release 76:
- Kredittkort main-page conversion bridge.
- Forbrukslån conversion bridge.
- Gjeldssjekk → Tilbudssjekk route.
- Correct Tilbudssjekk no-offer route back to Gjeldssjekken.
- Earlier partner visibility on Forbrukslån and Omstartslån.
- Direct hero-to-partner anchors on Forbrukslån/Omstartslån.
- Credit-card partner labeling/navigation without changing locked re:member imagery.
- Mobile protection for squeezed Gjeldssjekk debt rows and clearer Tilbudssjekk action hierarchy in V45.

## TRAFFIC ENGINE / SAVED RESEARCH
- Focus on problem- and intent-led search demand, not generic article volume.
- Examples: `Jeg har X – hva bør jeg gjøre?`, `Er rente X høy?`, `Hvor mye koster X?`, `Kan jeg refinansiere når …?`, `Bør jeg bytte …?`.
- Scale long-tail/problem capture only with high-quality useful pages/tools.
- Newsjacking: major economic events should feed a robust current-event component plus relevant tools/guides/CTAs, not ad-hoc HTML that disappears in later releases.
- Embeddable calculators/widgets are a future distribution/link-asset opportunity (renteforskjell, lånekostnad, gjeldskostnad, belåningsgrad etc.).
- Potential anonymised/aggregated benchmark data may support unique content/PR/B2B products, but only after legal/privacy review.

## MONETIZATION BACKLOG
### Direct qualified-lead routing
High-upside hypothesis: qualify consumer need and, with compliant permission, route a lead to a relevant bank, local/regional savings bank, insurer or other provider. Potential economics: CPL, qualified CPL, meeting, acquired customer, hybrid or revenue share.

Value must come from traffic + qualification + matching + consent + transfer + attribution, not merely publishing adviser contact information.

Possible lean flow: Sparesjekk form → simple qualification → explicit permission → secure storage → partner routing → email/API if needed → lead ID/status. Do not build a heavy CRM/partner portal before demand and economics are validated.

### Personal routing
Potential differentiator: connect a user to a genuinely relevant adviser/provider rather than a generic institution. Sparesjekk should not perform underwriting, decide credit, process the loan, or present itself as individual regulated financial advice. Intended role: need discovery → matching/routing → permission → introduction → partner handles the regulated/commercial process.

### Future B2B layer
Only after validation: partner dashboard, lead status/conversion, geography/category, exclusivity, qualification level, meeting booking and commercial reporting.

## LEGAL / COMPLIANCE GATES
Hard gate before direct-lead implementation. Research Norwegian/EEA requirements for:
- GDPR lawful basis and valid informed/freely given/specific consent where used
- named/identifiable recipients and purpose transparency
- data minimisation, retention, deletion and consent logging
- controller/processor roles and agreements
- secure transfer
- profiling implications
- marketing rules
- credit intermediation / financial-regulatory boundaries
- insurance distribution boundaries
- distinction between lead generation, intermediation and regulated advice

Do not assume consent alone solves compliance.

## CURRENT BUSINESS CONSTRAINT
Project owner currently lacks an organisation number for several projects. Distinguish what can be tested now from what requires a company/organisation number for commercial launch, invoicing, B2B/data agreements, payment rails or regulation. Do not discard a strong model solely because incorporation is not yet in place.

## FUTURE SILOS
Consider only after finance core/traffic engine is mature and real monetisation exists:
- insurance
- electricity
- broadband
- mobile
- flight compensation/claims
- other material household-cost categories

Normal entry gate: real user need + meaningful traffic potential + real monetisation partner/model + sensible economics.

## PARTNER DISCOVERY
After stabilization, validate interest before heavy build. Map local/regional banks, insurers, electricity providers and other relevant providers without attractive public affiliate programs. Capture acquisition appetite, personal-adviser model, lead buying interest, categories, geography, CPL/CPA, exclusivity, qualification requirements, technical intake and compliance requirements.

## EXPERIMENTS
1. Lean partner-interest validation for direct qualified leads.
2. Current-event/newsjacking component made data/content driven and regression protected.
3. Embeddable calculators as backlink/referral assets.
4. Later, legally reviewed aggregated benchmark/data content.

## DO NOT REDO
- Do not restart project strategy or repeat completed research.
- Do not repair navigation page-by-page; canonical/system repair owns it.
- Do not repeatedly layer CSS patches over broken component structure.
- Do not redesign re:member cards.
- Do not redesign Gjeldssjekk without first verifying a concrete production defect.
- Do not reopen Release 69 stabilization items without a verified production defect.
- Do not mass-produce thin AI SEO pages.
- Do not build heavy lead-routing infrastructure before compliance + partner validation.
- Do not use paid TinyFish automation unless explicitly requested by the user.

## PRIORITY SEQUENCE
A. Stabilize actual production: COMPLETE + LOCKED.
B. Design/conversion cleanup: ACTIVE — text walls, visuals, hierarchy, partner discoverability, mobile, CTA.
C. Optimize finance traffic engine: SEO, problem solver, calculators, internal linking, conversion, partner routing.
D. Review saved research together and prioritize business opportunities by revenue potential, probability, cost, technical complexity, passivity, time-to-market and regulatory risk.
E. Lean-validate direct lead model with real banks/insurers.
F. Build MVP only after compliance is clarified, at least one relevant partner shows interest and economics make sense.
G. Add new silos only when monetisation is real.

## NEXT ACTION
Continue Phase B from successful Release 76. Inspect source structure of the highest-value remaining finance pages/components for excessive visible text density, duplicated choices or unclear CTA/partner hierarchy. Make the smallest structural improvement that materially clarifies the journey, protect it with regression QA, deploy, and only claim production/visual verification that was actually performed.