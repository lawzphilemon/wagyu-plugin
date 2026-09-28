Status: confirmed

# WGY-O — Outline (lite): Connect Meta Ads to Claude

Sources: see ../meta-ads-claude/03-outline.md and 02-research.md (same research).

HERO
  Eyebrow: Free Guide · Meta Ads × Claude
  Title: Connect Claude to your Meta Ads account in 15 minutes
  Subtitle: Real performance reports from live data, read-only so Claude can't touch your budget. 100% free tools; ad budget separate.
  Chips: 15 min · Beginner friendly · Tool cost: $0

RESULT (one box)
  - Claude connected to Meta's official Ads connector
  - A read-only lock on Meta's side
  - A first performance report from a prompt you can reuse weekly
  Success check: Claude answers the report prompt with real campaign numbers.

STEPS (one section, no phases)
  1. Add Meta's connector in Claude ([CL-A], screenshots step-1.2/1.3; USER). Pitfall: Free plan = 1 custom connector.
  2. Sign in with Facebook, tick one portfolio ([LOOMER]; OPEN). Tip: allow pop-ups. Pitfall: agencies, client portfolios.
  3. Check Meta has enabled the account (P0; [ADSPEND]; OPEN). Pitfall: false = Meta's rollout, not your setup → Quick fix 1.
  4. Lock read-only in Business Suite ([META-H], [META-R]; DOC) + lock test (OPEN). Pitfall: rules not visible → rollout; second lock arrives by email.
  5. Run the first performance report ([META-D] ads_get_ad_entities; DOC). Pitfall: numbers differ → match the date range and attribution Claude names.
  CHECKPOINT after step 5. Ladder point: soft aside after the checkpoint.

PROMPTS
  A. Account check (Step 3)
  B. First performance report (Step 5, reuse weekly): states dates, time zone, attribution, currency; overview, campaigns ranked, best/worst ads, top problems, 3 options for a human; describe changes, never make them.

QUICK FIXES (top 3)
  1. is_ads_mcp_enabled: false / calls fail → rollout; try other accounts, retry weekly, ignore paid "enablement".
  2. Facebook login doesn't open → pop-up blocker.
  3. Stopped after ~60 days → reconnect.

CLOSING
  Wall, bridge (Starter tier), not-for, mention of the follow-up emails, CTA.

NURTURE PLAN (not on the page, see 04-nurture-plan.md)
  E1 day 0: delivery + the guide link
  E2 day 2: second lock (Claude Tool permissions) + lock test prompt
  E3 day 4: weekly prompt pack (P3 to P11) + run order
  E4 day 6: trust your numbers (Ads Reporting attribution, conversion count) + full troubleshooting
  E5 day 8: the wall → Gwenchana Meta Ads (Starter), not-for, CTA

Ladder points on the page: 2 (after the checkpoint, the close).
