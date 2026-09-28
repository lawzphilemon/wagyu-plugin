Status: confirmed

# WGY-O — Outline: Connect Meta Ads to Claude (read-only)

Sources shorthand (full URLs in 02-research.md):
- [CL-A] Claude Help: custom connectors (Aug 12, 2026) · [CL-B] Claude Help: use connectors (Aug 21, 2026)
- [META-H] Meta Business Help 1456422242197840 · [META-D] Meta dev docs: Get started / tool pages · [META-R] Meta dev docs: Rules best practices
- [LOOMER] Jon Loomer (May 5, 2026) · [ADSPEND] The Ad Spend (Jul 2026) · [PIPE] pipeboard.co/pricing · [LIVE] live endpoint check 2026-09-28

---

HERO
  Eyebrow: Free Guide · Meta Ads × Claude
  Title: Connect Claude to Your Meta Ads Account, Read-Only, in 45 Minutes
  Subtitle: For marketers who live in Claude: live campaign answers and a weekly audit prompt pack, locked so AI can't touch your campaigns or budget. 100% free tools. Your ad budget stays separate.
  Chips: 30 to 45 min · Intermediate · Tool cost: $0

RESULT PREVIEW
  You'll have:
  - Claude connected to Meta's official Ads MCP server
  - A two-layer read-only lock (Meta's rules + Claude's tool permissions)
  - A 12-prompt weekly audit pack mapped to Meta's read tools
  How you'll know it worked:
  - Claude lists your ad account with is_ads_mcp_enabled: true
  - Claude's 7-day numbers match Ads Manager once both use the same date range, time zone, and attribution
  - A request to create a campaign is refused
  Or, within the first 10 minutes: you'll know Meta hasn't enabled your account yet, and what to do instead.

FOR / NOT FOR
  For:
  - You run an active Meta ad account with at least 7 days of data
  - You're tired of exporting to spreadsheets to answer simple questions
  - You want AI in your workflow without risking a single rupiah of budget
  Not for:
  - You want AI to launch or edit campaigns for you (this guide blocks that on purpose)
  - You don't have an ad account with data yet
  - You only use ChatGPT (separate guide)

TOOLKIT
  | Tool | Used for | Free limit (checked Sep 28, 2026) | Account needed |
  | Claude (web or Desktop) | Chat + connector | Free plan: 1 custom connector | Claude account |
  | Meta Ads MCP server | Official bridge to your ad account | Free open beta; Meta enables accounts gradually | Facebook login with ad account access |
  | Meta Business Suite | Read-only rules on Meta's side | Free; limited availability | Full control of the business portfolio |
  | Meta Ads Manager | Cross-checking numbers | Free | Ad account access |
  Prerequisites:
  - Admin or full advertiser access on the ad account
  - Full control of the business portfolio for Phase 2 (if not, ask the owner, or rely on Claude's lock alone)
  - Free plan only: your one custom connector slot must be free
  - A desktop browser (setup is easiest on claude.ai or Claude Desktop)

---

PHASE 1: Connect and run the pre-flight check (~15 min)
  Goal: Claude connected to Meta, and a clear yes/no on whether your ad account is enabled.

  Step 1.1: Open Customize > Connectors in Claude
    — Source: [CL-A], [CL-B]
    — Expected result: your Connectors list
    — Pitfall: Free plan allows one custom connector. If one is already there, remove it or stop here.
    — Screenshot: Connectors page

  Step 1.2: Click + and choose Add custom connector
    — Source: [CL-B], [LOOMER]
    — Expected result: a form asking for name and URL
    — Pitfall: None
    — Screenshot: Add custom connector menu

  Step 1.3: Enter the name "Meta Ads" and the URL https://mcp.facebook.com/ads, then click Add
    — Source: [META-H], [META-D]
    — Expected result: Meta Ads appears in the list, not connected yet
    — Pitfall: Use only this URL. Third-party servers that route through shared apps carry real account risk.
    — Screenshot: filled-in form

  Step 1.4: Click Connect and sign in with Facebook
    — Source: [LOOMER], [META-D] (OAuth via Facebook Login for Business)
    — Expected result: Meta's permission screen
    — Pitfall: The screen asks for management permissions too (8 scopes, [LIVE]). That's normal: login is never read-only. Phase 2 locks it.
    — Screenshot: permission screen

  Step 1.5: Select only the business portfolio you want Claude to see
    — Source: [LOOMER]
    — Expected result: back in Claude, Meta Ads shows as connected
    — Pitfall: Agencies: the connector inherits every portfolio you select, including client accounts.
    — Screenshot: portfolio selection

  Step 1.6: Start a new chat and turn Meta Ads on under + > Connectors
    — Source: [CL-B]
    — Expected result: the Meta Ads toggle is on
    — Pitfall: The connector is off in chats where you didn't enable it
    — Screenshot: connector toggle

  Step 1.7: Paste the pre-flight prompt (P0)
    — Source: [META-D] ads_get_ad_accounts; [ADSPEND] for the enabled flag
    — Expected result: a table of your ad accounts with ID, currency, time zone, and is_ads_mcp_enabled
    — Pitfall: false = Meta hasn't enabled that account. Not your setup. Go to Troubleshooting T1.
    — Screenshot: pre-flight answer (empty-account screenshot is fine)

  CHECKPOINT:
  - [ ] Meta Ads shows as connected in Customize > Connectors
  - [ ] Claude listed your ad accounts
  - [ ] You know is_ads_mcp_enabled for the account you'll use
  Ladder point: None

PHASE 2: Lock it to read-only (~15 min)
  Goal: two independent locks, so no prompt, mistake, or research run can change your account.

  Step 2.1: Open Meta Business Suite and click Settings
    — Source: [META-H]
    — Expected result: Business Suite settings
    — Pitfall: None
    — Screenshot: Settings

  Step 2.2: Under Integrations, select Ads MCP server
    — Source: [META-H]
    — Expected result: your ad accounts and catalogs listed
    — Pitfall: Not visible = no full control, or not rolled out to you yet (limited availability). Skip to 2.5; Claude's lock still protects you.
    — Screenshot: Ads MCP server page

  Step 2.3: Select the ad account you connected
    — Source: [META-H]
    — Expected result: the list of agent actions with Allowed/Blocked switches
    — Pitfall: None
    — Screenshot: action list

  Step 2.4: Switch every action to Blocked
    — Source: [META-H], [META-R] (create campaigns/ad sets/ads, edit budget, targeting, creative, status)
    — Expected result: Take actions in this ad account shows Blocked
    — Pitfall: [VERIFY] whether a single "block everything" option also blocks reading. The final wording depends on the Gwenchana test.
    — Screenshot: all actions blocked

  Step 2.5: In Claude, open Customize > Connectors, click Meta Ads, and find Tool permissions
    — Source: [CL-B]
    — Expected result: tools grouped as read-only and write/delete
    — Pitfall: [VERIFY] visible on Free plan
    — Screenshot: Tool permissions

  Step 2.6: Set write/delete tools to Blocked
    — Source: [CL-B]; write tool list from [META-D]
    — Expected result: the write/delete group shows Blocked; read-only stays Always allow or Needs approval
    — Pitfall: Claude's Research mode can call connector tools without asking ([CL-A]). Another reason to block writes here.
    — Screenshot: write tools blocked

  Step 2.7: Test the lock with the lock-test prompt (P2)
    — Source: [META-H] (actions need authorisation), [META-R]
    — Expected result: Claude says it can't create the campaign
    — Pitfall: If a campaign appears anyway, it was created paused (no spend, [META-D]). Delete it in Ads Manager and recheck 2.6.
    — Screenshot: refusal message

  CHECKPOINT:
  - [ ] Meta rules set to Blocked (or noted as unavailable to you)
  - [ ] Write/delete tools set to Blocked in Claude
  - [ ] The lock test was refused
  Ladder point: None

PHASE 3: Prove the numbers and run your first audit (~15 min)
  Goal: trust the data, then get your first weekly audit.

  Step 3.1: Paste the number-check prompt (P1)
    — Source: [META-D] ads_get_ad_entities
    — Expected result: spend, results, cost per result, CTR per campaign for the last 7 days, plus the exact date range, time zone, and attribution setting Claude used
    — Pitfall: If Claude doesn't state all three, ask again. You need them for 3.2.
    — Screenshot: illustration (labeled), since no spending account was available
    — Status note: verified on setup, not on a spending account

  Step 3.2: Open Ads Manager and set the same date range and attribution setting
    — Source: [NEEDS SOURCE] Meta help page for the attribution setting column/comparison in Ads Manager
    — Expected result: Ads Manager showing the same 7 days
    — Pitfall: Ads Manager reports in the ad account's time zone; "last 7 days" can shift a day
    — Screenshot: Ads Manager date + attribution settings

  Step 3.3: Compare spend, results, and CTR per campaign
    — Source: none needed (reader comparison)
    — Expected result: numbers match, allowing for rounding
    — Pitfall: Mismatch → Troubleshooting T4
    — Screenshot: None

  Step 3.4: Paste the session starter (P-START), then the weekly snapshot (P3)
    — Source: [META-D] ads_get_ad_entities
    — Expected result: this week vs last week per campaign, with 3 things worth a human look
    — Pitfall: Big accounts can hit rate limits; keep one question per prompt (T7)
    — Screenshot: illustration (labeled)

  CHECKPOINT:
  - [ ] Claude's numbers matched Ads Manager
  - [ ] You ran your first weekly snapshot
  - [ ] You know your weekly run order (asset A1)
  Ladder point: Soft. "Now you can see exactly what's happening. Doing something about it every week (new creative, budget calls, tracking fixes) is the part AI can't own for you."

---

ASSETS
  A1. Weekly audit prompt pack (copy-paste blocks; each notes the read tool it relies on)
    P-START  Session starter: read-only analyst rules (never call write tools, always name the ad account ID, always state date range / time zone / attribution, keep tool calls few)
    P0  Pre-flight: accounts, IDs, currency, time zone, is_ads_mcp_enabled (ads_get_ad_accounts)
    P1  Number check with stated date range / time zone / attribution (ads_get_ad_entities)
    P2  Lock test: create a paused campaign named WAGYU-TEST (expected: refused)
    P3  Weekly snapshot vs previous 7 days (ads_get_ad_entities)
    P4  Delivery-error sweep (ads_get_errors)
    P5  Anomaly sweep (ads_insights_anomaly_signal)
    P6  Creative fatigue: rising frequency + falling CTR over 14 days (ads_insights_performance_trend, ads_get_ad_entities)
    P7  Budget pacing month-to-date (ads_get_ad_entities)
    P8  Change log: what changed this week and who (ads_account_get_activity_logs)
    Monthly:
    P9  Auction and industry benchmarks (ads_insights_auction_ranking_benchmarks, ads_insights_industry_benchmark)
    P10 Signal health: event match quality and event volume (ads_get_dataset_quality, ads_get_dataset_stats)
    P11 Opportunity score, read-only, "list, don't apply" (ads_get_opportunity_score)
    Run order: weekly P4 → P3 → P5 → P6 → P7 → P8; monthly P9 → P10 → P11.

  A2. Read-only lock checklist (copy-paste): the Phase 2 steps as a checklist to repeat for every new ad account or client.

  A3. Weekly audit report template (copy-paste): the format P3 asks Claude to fill: headline, what changed, what moved and why (data only), 3 things for a human to decide.

TROUBLESHOOTING
  T1  Tools listed, but calls fail / is_ads_mcp_enabled: false → Meta's gradual rollout, per ad account; you can't switch it on → try other ad accounts you manage, confirm admin/full advertiser role, reconnect every 1 to 2 weeks, ignore anyone selling "enablement". Free fallback: Pipeboard Free (no card, 30 tool runs/week, 2 accounts); on Claude Free, remove the Meta connector first; block write tools in Claude again. [ADSPEND], [PIPE]
  T2  Can't add a second custom connector → Free plan limit of one [CL-A]
  T3  Ads MCP server missing from Business Suite settings → no full control of the portfolio, or not rolled out yet → ask the portfolio owner; Claude's lock still applies [META-H]
  T4  Numbers don't match Ads Manager → date range, time zone, attribution setting, or currency differ → ask Claude to restate all four and match Ads Manager [DOC]
  T5  Claude answered about the wrong account → name the act_ ID in every prompt; check the portfolio chosen at login [ADSPEND], [LOOMER]
  T6  Worked for weeks, then stopped → Meta access expires (about 60 days reported) → disconnect and reconnect [ADSPEND]
  T7  Rate-limit errors → shorter date ranges, fewer breakdowns, one question per prompt [ADSPEND]
  T8  "Will this get my account banned?" → Meta: using the official server alone won't; stay on Meta's official URL [META-H]
  T9  "redirect_uris are not registered" in Claude Code → a Claude Code CLI issue; use claude.ai or Claude Desktop [ADSPEND]
  T10 A tutorial says custom connectors need a paid Claude plan → outdated; Claude's Help Center (Aug 2026) says Free gets one [CL-A]

NEXT WALL + PREMIUM (closing)
  Wall: Claude now reads your account and spots what's off. Moving the numbers still takes execution every week: fresh creative for testing, budget calls that don't blow up CPA, and tracking (Conversions API, attribution) that makes the data trustworthy in the first place. Handing that to AI with write access and no guardrails is how budgets get burned.
  Bridge: Gwenchana runs Meta Ads end to end (strategy, creative testing, scaling, tracking), starting from the Starter tier, while you keep watching every number with this setup.
  Not for premium if: you're still testing with a small budget and enjoy running it yourself. Use the prompt pack for a few weeks first.
  CTA: [CTA_URL] (collected at /finaldraft)

Ladder points total: 2 (after Phase 3 checkpoint, closing).
Screenshots from an empty test ad account: 1.1 to 2.7. Data screenshots (3.1, 3.4): labeled illustrations.
