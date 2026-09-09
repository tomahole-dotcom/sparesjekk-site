SPARESJEKK AUTOMATED SITE BUILDER — V29

Source of truth is now configuration + existing editorial HTML.
Existing SEO/editorial content is protected and is NOT regenerated.

NORMAL UPDATE FLOW
1. Edit site-config.json only (for example activate an approved partner and add its tracking URL).
2. Run: python tools/build_site.py
3. Run: python tools/qa_site.py
4. Release only when QA passes.

AUTOMATED NOW
- Approved/active partner cards on all four /sjekk/ landing pages
- Advertisement disclosure
- sponsored/nofollow affiliate link attributes
- sitemap.xml generation
- broken internal-link QA
- active-partner validation (must be approved, HTTPS, categorized)
- existing SEO hard gate: title, description, canonical, robots, H1 and JSON-LD cannot silently change

IMPORTANT
Partner status must be active AND approved=true before publishing. No rates, terms or representative examples are invented. Add them only from approved advertiser material.
