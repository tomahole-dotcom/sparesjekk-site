# Sparesjekk recovery status — 2026-09-25

## Source of truth
Active development source: `seo-content-v34-master`.

`main` and the active branch diverged after merge base `723bdcf9d8a0f838f9aa6a2682dca576af4da361`. Do not deploy `main` wholesale over the active branch.

## Preserve
- Problemløser + Om oss in canonical navigation
- current rate-event component and release guard
- repaired boliglån nesting
- modern Tilbudssjekk/refinansiering UI
- Belåningsgrad result UI v2
- approved About-page redesign from main commit `5d10b76a47eb7f1fdd8479d223af81376b1c78ea`
- approved real re:member product imagery; never CSS/card-silhouette placeholders

## Pending reported UI regressions
1. bankbytte break-even result component
2. gjeldssjekk debt-entry rows
3. gjeldssjekk custom/test-rate component
4. re:member Gold/Black product-image regression

## Recovery process
Reconcile approved fixes file-by-file onto this active history, add regression checks, deploy, then verify production. Do not solve divergence by replacing the active history with `main`.
