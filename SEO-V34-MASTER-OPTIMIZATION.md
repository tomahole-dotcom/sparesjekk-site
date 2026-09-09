# Sparesjekk V34 – Master SEO & Content Optimization

Status: WORKING BRANCH ONLY. Do not deploy until full QA.

## Objective
Optimize the existing site as one coherent search ecosystem before scaling partner monetization. Preserve useful existing SEO signals while improving content depth, search-intent separation, internal linking, UX and partner readiness.

## Non-negotiable controls
- Preserve existing URLs unless a deliberate migration is approved.
- Preserve canonical, robots, title, meta description, H1 and JSON-LD by default; any change must be intentional and reviewed.
- Do not mass-delete thin pages solely because they are thin.
- Do not create near-duplicate pages for keyword variants.
- No keyword stuffing or templated filler.
- Every page must have a clear primary search intent.
- Informational guides and commercial /sjekk/ pages must support each other, not target the same primary intent.
- Affiliate/sponsored links must be clearly labelled and use appropriate sponsored link attributes when activated.
- No invented rates, terms, rankings or partner claims.
- Financial/rule-sensitive claims must be verified against suitable authoritative sources before publication.
- Full QA once after the consolidated batch; one production deploy after QA passes.

## Current four-cluster architecture

### Kredittkort
Pillar: kredittkort.html
Commercial: sjekk/kredittkort/index.html
How-to comparison: sammenligne-kredittkort.html
Supporting intents include: effective interest, interest-free period, fees, annual fee, FX markup, cash withdrawal, minimum payment, repayment, cashback/bonus, use case and credit-card debt/refinancing.

### Forbrukslån / refinansiering
Pillar: forbrukslan.html
Commercial: sjekk/forbrukslan/index.html
Supporting intents include: effective vs nominal interest, fees, term, total cost, refinancing, debt register, repayment and comparison methodology.

### Omstartslån / secured refinancing
Pillar: omstartslan.html
Commercial: sjekk/omstartslan/index.html
Supporting intents include: refinancing secured on home, collateral, total debt, cost, term, risks, eligibility concepts and alternatives.

### Boliglån
Pillar: boliglan.html
Commercial: sjekk/boliglan/index.html
Supporting intents include: mortgage rate, effective/nominal rate, LTV, home value, switching bank, negotiating rate, equity, amortization, repayment, fixed/floating rate and first-home topics.

## Page-role rules
1. Pillar pages: broad orientation + cluster navigation + key concepts; do not become giant duplicates of every guide.
2. Guides: solve one concrete informational/decision task deeply.
3. Commercial /sjekk/: comparison/conversion intent and later approved partner modules.
4. Guide index pages: discovery/navigation, not competing long-form articles.
5. Homepage: concise navigation/trust/calculator/three useful guides; move depth to dedicated pages.

## Thin-content upgrade standard
A high-priority guide should normally contain, where relevant:
- direct answer/summary near the top
- clear decision framework
- comparison table or structured criteria
- concrete example without invented live market rates
- common mistakes / pitfalls
- actionable checklist
- relevant definitions in context
- links to narrower supporting guides instead of duplicating them
- link back to pillar
- contextual path to relevant /sjekk/ page when commercially appropriate
- visible update/editorial note where appropriate

Word count is not a target. Added content must solve additional user questions.

## Internal linking model
Pillar -> important guides + commercial comparison.
Guide -> pillar + 2–4 genuinely related guides + commercial comparison when intent naturally progresses.
Commercial -> pillar/explainers for users needing more information.
Avoid sitewide keyword-rich link blocks designed only for ranking.
Use descriptive, natural anchor text.

## Cannibalization review
Before changing SEO fields, review overlaps such as:
- multiple bank-switch/mortgage guides
- broad complete guides vs pillar pages
- general effective-rate guide vs category-specific effective-rate guides
- credit-card minimum-payment/factura/repayment pages
- refinancing topics spanning unsecured and secured refinancing

Resolve primarily by sharpening page intent and internal links. Merge/redirect only after explicit URL-level review.

## Partner-ready model
Partner data remains centrally controlled. No hard-coded winner claims.
Commercial modules should support:
- clear ANNONSE/REKLAME disclosure
- provider name and verified proposition
- payout/analytics metadata internally where useful, not presented as consumer ranking evidence
- tracking URL
- rel=sponsored for paid/affiliate links
- category relevance
- ranking methodology separated from payout alone

## UX/content batch already in scope
- Homepage simplification without discarding useful SEO substance.
- Omstartslån visual normalization.
- Guide-category navigation consistency.
- Om oss redesign from V33 work, reconciled safely rather than force-overwriting branch history.
- Thin-guide upgrades beginning with high-value money pages.

## First priority: sammenligne-kredittkort.html
Primary intent: teach the user HOW to compare credit cards.
Do not turn this into the commercial provider ranking page.
Upgrade with:
- quick comparison framework
- criteria table: full-balance payer vs revolving-balance user vs travel vs bonus use
- effective interest explanation with link to dedicated guide
- fee/FX/cash-withdrawal comparison with links to dedicated guides
- interest-free-period logic with link to dedicated guide
- bonus/cashback value test with link to dedicated guide
- concrete hypothetical comparison method
- checklist before choosing
- natural route to sjekk/kredittkort/ once partner comparison is useful
- reduce repetitive short H2 paragraphs currently saying similar things

## Measurement/readiness
Before production:
- full link QA
- SEO guard passes
- GA4 present
- sitemap/indexability checks
- no unintended canonical/title/meta/H1/robots/schema changes
- no broken mobile navigation/layout
- no unapproved active partner modules
- inspect important changed pages manually

After production and indexing, use Search Console query/page data to decide which pages get the next optimization cycle. Do not manufacture new pages just to cover keyword variants.

## Current Google-aligned notes (reviewed Sep 2026)
- People-first/non-commodity content and established SEO best practices remain important for Search and generative Search features.
- Avoid scaled low-value content and keyword stuffing.
- Similar/duplicate pages can create canonicalization ambiguity; do not solve overlap by blindly creating more variants.
- Breadcrumb structured data remains useful for communicating hierarchy.
- FAQ rich-result presentation was deprecated in 2026, so FAQs may be used for user value but not as a reason to mass-add FAQ markup.

## Release rule
No production deployment from this branch until the consolidated SEO/content/layout batch is complete and QA has passed. Keep GitHub Actions runs to a minimum.