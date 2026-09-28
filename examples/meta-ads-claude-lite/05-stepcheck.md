# WGY-V — Stepcheck (lite)

Checked on: 2026-09-28 | Evidence carried over from ../meta-ads-claude/05-stepcheck.md (same facts, fewer steps) | Run type: TEST RUN, open steps accepted by the user.

| Lite step | Status | Evidence |
|---|---|---|
| 1 Add connector | USER | screenshots step-1.2 / step-1.3 (Claude Pro) |
| 2 Facebook sign-in, one portfolio | ACCEPTED-OPEN | Connect: CL-B (DOC). Portfolio screen: third-party only (Jon Loomer). Pop-up tip: third-party (charisnicholas.com), generic browser behavior |
| 3 Account check (is_ads_mcp_enabled) | ACCEPTED-OPEN | Tool ads_get_ad_accounts: META-D (DOC). The flag itself: community reports only |
| 4 Read-only lock + test | ACCEPTED-OPEN | Rules path and labels: META-H, META-R (DOC). Lock test: needs a connected, enabled account |
| 5 First performance report | DOC | META-D ads_get_ad_entities |

Quick fixes: 1 (community + Meta blog "gradual rollout", DOC-backed), 2 (third-party, generic), 3 (community report, ~60 days).

To publish: close steps 2 to 4 with the walkthrough in ../meta-ads-claude/05-stepcheck.md (items 1, 3, 5, 8), then rebuild without the banner and with the real CTA URL.
