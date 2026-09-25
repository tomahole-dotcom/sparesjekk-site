# Sparesjekk recovery status — 2026-09-25

## Root cause
`main` and `seo-content-v34-master` diverged after merge base `723bdcf9d8a0f838f9aa6a2682dca576af4da361`.

The active development branch contains the large body of current product, SEO, conversion, design and release work. `main` contains a small separate line of commits, including the latest approved About-page redesign.

## Recovery rule
Do not bulk-reset either branch and do not redeploy from `main` as a substitute for the active development branch.

Reconcile approved newer fixes onto the active development history file-by-file, then use regression QA before production deployment.

## Known approved fixes to preserve
- Current navigation must include Problemløser and Om oss.
- Current rate-event component must not disappear on release.
- Boliglån nesting regression must remain fixed.
- Tilbudssjekk/refinansiering modern UI must remain fixed.
- Belåningsgrad result UI v2 must remain fixed.
- About page redesign from `main` commit `5d10b76a47eb7f1fdd8479d223af81376b1c78ea` must be preserved.
- re:member must use approved real product imagery, not CSS/card-silhouette placeholders.

## Pending UI fixes already reported
- bankbytte break-even result component
- gjeldssjekk debt-entry rows
- gjeldssjekk custom/test-rate component
- re:member Gold/Black regression

## Do not redo
Do not replace approved real re:member product imagery with generated/CSS placeholders. Do not repair branch divergence by choosing `main` wholesale and discarding the active development history.
