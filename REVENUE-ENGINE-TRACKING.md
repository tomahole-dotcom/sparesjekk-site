# Revenue Engine tracking

GA4 funnel events generated from existing Revenue Engine attributes:

- `commercial_route`: click from an informational/tool page into a Sparesjekk commercial comparison page.
- `partner_click`: outbound click from a Sparesjekk comparison page to an approved affiliate partner.

Parameters:
- `revenue_stage`
- `source_path`
- `destination`
- `link_text`
- `partner` (partner clicks only)

This intentionally measures only high-intent funnel actions. It does not claim or infer a completed loan application; downstream application/conversion remains the affiliate network/partner's source of truth.
