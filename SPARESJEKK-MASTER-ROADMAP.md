# SPARESJEKK.NO — MASTER ROADMAP

Last updated: 2026-09-24
Source of truth: GitHub branch `seo-content-v34-master` + verified production at Sparesjekk.no.

## CURRENT PRODUCTION STATUS
- Release 69 (`Trigger system repair release 69`, run 36007361520) completed successfully on 2026-09-24.
- Regression hard gate passed across 119 navigation pages.
- FTP deployment completed; deploy reported server files identical to tested release.
- Independent production fetch + browser QA completed 2026-09-24.
- Homepage rate event is live with both CTAs.
- Canonical navigation is live with `Problemløser` and `Om oss`.
- `boliglan.html` visually verified: first decision card is standalone; follow-up sections are outside it; no giant nested text wall.
- `tilbudssjekk-refinansiering.html` visually verified: balanced two-panel desktop layout, readable labels, consistent inputs, no clipping/wrapping defect found.
- `gjeldssjekk.html` production was checked and no concrete regression requiring redesign was identified.
- Stabilization gate for Release 69 is PASSED and LOCKED.

## LOCKED / DONE
- Release 69 stabilization: canonical navigation, 24.09.2026 rate event, boliglan nesting repair and Tilbudssjekk/refinancing layout. Do not alter without a verified defect; regression protection must remain.
- re:member Gold/Black presentation uses real product imagery. Do not replace with CSS-generated cards or redesign without a concrete defect.
- Existing working affiliate integrations must not be removed without a concrete reason.
- Gjeldssjekk has already received UI work; verify before changing and do not redesign by default.

Fixed failure process: root cause → repair source of truth → regression test → deploy → verify production → lock → continue.

## CURRENT PARTNERS / MONETIZATION
Current/previous commercial tracks include boliglan, forbrukslan, refinansiering and kredittkort. Partners used or evaluated include Tjenestetorget, Zensum, Sambla, DigiFinans, Axo Finans and re:member. Preserve working attribution/tracking. Partner presentation should be easy to find and commercially effective without making Sparesjekk look like an aggressive affiliate site.

## PRODUCT DIRECTION
Sparesjekk should help Norwegian consumers discover unnecessary costs, understand financial choices, use simple calculators/problem-solvers, compare relevant alternatives and reach an appropriate provider/partner. Long-term umbrella product: **Ta Sparesjekken**. Avoid becoming a generic AI-content portal.

## DESIGN / CONVERSION BACKLOG
Current active phase after stabilization:
- Reduce visual text walls without deleting useful SEO content.
- Improve whitespace, hierarchy, sectioning, cards/components, relevant visuals, mobile rendering and next-step CTAs.
- Make partner routes easier to discover while preserving trust.
- Keep finished/approved design areas locked unless a verified defect exists.
- Work page/component batches from actual production evidence; avoid broad redesigns and patch stacking.

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

## PRIORITY SEQUENCE
A. Stabilize actual production: COMPLETE + LOCKED 2026-09-24.
B. Design/conversion cleanup: ACTIVE — text walls, visuals, hierarchy, partner discoverability, mobile, CTA.
C. Optimize finance traffic engine: SEO, problem solver, calculators, internal linking, conversion, partner routing.
D. Review saved research together and prioritize business opportunities by revenue potential, probability, cost, technical complexity, passivity, time-to-market and regulatory risk.
E. Lean-validate direct lead model with real banks/insurers.
F. Build MVP only after compliance is clarified, at least one relevant partner shows interest and economics make sense.
G. Add new silos only when monetisation is real.

## NEXT ACTION
Release 69 stabilization is locked. Continue with Phase B design/conversion cleanup using actual production as evidence. First target: identify the highest-impact remaining finance page/component with text-wall, hierarchy, partner-discoverability, mobile or CTA friction; repair source structure rather than stacking overrides; preserve SEO content and all locked areas; regression-test, deploy and verify production before locking the batch.