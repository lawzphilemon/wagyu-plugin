# WGY-R — Research: Connect Meta Ads to Claude (read-only)

Captured: 2026-09-28 | Mode: built-in browser (live Google + direct page reads). Reddit could not be opened in the browser pane, so Reddit threads are cited from Google snippets only.

## 1. Official procedure

### A. Claude: add the custom connector
Source: Claude Help Center, "Get started with custom connectors using remote MCP", updated Aug 12, 2026 (EN) — https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
Source: Claude Help Center, "Use connectors to extend Claude's capabilities", updated Aug 21, 2026 (EN) — https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities

- Custom connectors (remote MCP) work on Claude web, Cowork, and Claude Desktop on **Free**, Pro, Max, Team, Enterprise. **Free users are limited to one custom connector.**
- Steps (doc lists them for Pro/Max; the Aug 21 article lists the same path for all users):
  1. **Customize** > **Connectors**
  2. Click **+** next to Connectors, then **Add custom connector**
  3. Enter the connector's name and URL
  4. (Optional) **Advanced settings**: OAuth Client ID/Secret — not needed for Meta
  5. Click **Add**, then **Connect** and follow authentication
- Enable per chat: **+** (lower left of the chat) > **Connectors** > toggle it on.
- Tool permissions: **Customize** > **Connectors** > select the connector > **Tool permissions**, grouped as read-only vs write/delete tools; each set to **Always allow**, **Needs approval**, or **Blocked**. The doc frames this under "Owners on Team and Enterprise plans". → /verify: confirm whether Free/Pro individuals see Tool permissions.
- Remote connectors are called from Anthropic's cloud, not the user's machine. No local install needed.
- Security guidance from the doc: review requested permissions, only click "Allow always" for trusted tools, disable write tools when using Research mode (Research can call connector tools without further approval).

### B. Meta: the official Ads MCP server
Source: Meta Business Help Centre, "Manage ads from an AI agent with Meta ads AI connectors" — https://www.facebook.com/business/help/1456422242197840 (no date shown)
Source: Meta for Developers, "Ads MCP Server" overview, updated Jul 14, 2026 — https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview
Source: Meta for Developers, "Get started" — https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-get-started
Source: Meta for Developers blog, Jul 16, 2026, updated Sep 22, 2026 — https://developers.facebook.com/blog/post/2026/07/16/meta-ads-mcp-server/

- Server URL (all supported agents): `https://mcp.facebook.com/ads`. Live check today: GET returns HTTP 405 "MCP endpoints accept POST for JSON-RPC", i.e. the endpoint is up.
- Officially supported agents: ChatGPT, Claude, Claude Code, Perplexity. Meta's Claude link points to the Claude custom connector article above.
- **No Meta developer app is needed** for Claude web/Desktop: "Owning a Meta app is not a prerequisite." Auth is OAuth via Facebook Login for Business. (Own-app setup is only for developers/agencies.)
- OAuth permissions requested include `ads_mcp_management`, `ads_read`, `ads_management`, `catalog_management`, `business_management`, `pages_show_list`, `instagram_basic` (token list from Get started). → OAuth alone is NOT read-only. Read-only must be enforced by rules (C) and Claude tool permissions (A).
- Write tools create campaigns/ad sets/ads **paused**; "Any actions taken on your behalf require your authorisation through the AI agent."
- Meta states: connecting via the official server does not on its own put an account at risk of a ban.
- Help page banner: "You may not have access to all tools/features yet." Blog: "we'll be gradually rolling out access to tools… ask your agent what tools you have access to."

**Read tools (safe for this guide)** — from the tool pages (reporting, ad creation & management, signals, activity logs):
- Reporting: `ads_get_ad_entities` (spend, impressions, CTR, CPC, CPM, conversions; filters, breakdowns, date ranges), `ads_get_opportunity_score`, `ads_insights_advertiser_context`, `ads_insights_anomaly_signal`, `ads_insights_auction_ranking_benchmarks`, `ads_insights_industry_benchmark`, `ads_insights_performance_trend`
- Discovery: `ads_get_ad_accounts`, `ads_get_ad_account_pages`, `ads_get_pages_for_business`, `ads_get_user_pages`, `ads_get_field_context`
- Creative reads: `ads_get_creatives`, `ads_get_creative_ads`, `ads_get_ad_images`, `ads_get_ad_videos`, `ads_get_ad_preview`, `ads_library_search`
- Audiences (read): `ads_get_ad_account_custom_audiences`, `ads_get_custom_audience`, `ads_get_custom_audience_adsets`
- Signals: `ads_get_datasets`, `ads_get_dataset_details`, `ads_get_dataset_stats` (≤28 days), `ads_get_dataset_quality` (EMQ), `ads_pixel_event_read`, `ads_pixel_parameter_read`, `ads_get_customconversions`
- Activity: `ads_account_get_activity_logs`
- Also reported by Jon Loomer (May 2026): `ads_get_errors` (delivery-blocking errors). Not seen on the doc pages read today. → /verify.

**Write tools (block for this guide):** `ads_create_campaign`, `ads_create_ad_set`, `ads_create_ad`, `ads_update_entity`, `ads_activate_entity` (starts spending), `ads_create_creative`, `ads_boost_ig_post`, `ads_create_custom_audience`, `ads_update_custom_audience`, `ads_update_custom_audience_users`, `ads_delete_custom_audience`, `ads_pixel_event_create/update/delete`, `ads_pixel_parameter_create/update/delete`, plus catalog write tools.

### C. Meta: Ads MCP server rules (the read-only lock on Meta's side)
Source: Help Centre article (B) and "Rules best practices" — https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-rules-best-practices

- UI path: Meta Business Suite > **Settings** > under **Integrations**, **Ads MCP server** > select the ad account > allow or block actions. Requires **full control of the business portfolio**. "If you can't see this, you do not have access to this feature yet."
- Rule actions: `create_campaign`, `create_ad_set`, `create_ad`, `edit_budget` (percentage / absolute / ceiling), `edit_targeting`, `edit_creative`, `edit_status`, `all` ("every agent action on the account").
- Rules are in **limited availability**.
- Rules do not list custom audience, pixel, or IG boost writes separately. Only `all` would cover them. → /verify: does `all` block read/reporting tools too? If yes, block the individual write actions instead.
- Agency note: partners with access can set rules that apply only to their own employees.

## 2. Free-tier limits (checked 2026-09-28)

| Tool | Needed feature free? | Card? | Limits | Source |
|---|---|---|---|---|
| Claude Free | Yes: custom connectors | No | **1 custom connector** on Free. Message/usage limits apply (not quantified for connector use: Unconfirmed) | Claude Help Center (A) |
| Meta Ads MCP server | Yes: free open beta (third-party reports), no official pricing page | No | Per-account rollout gate (see friction #1). Rate limits: Unconfirmed officially; community reports ~200 calls/hour | Meta docs (B); The Ad Spend (community) |
| Meta Business Suite rules | Free | No | Limited availability; needs full control of the portfolio | Meta (C) |
| Fallback: Pipeboard Free | Yes | **No card** | **30 AI tool executions/week, 2 ad accounts**, no permission-scoped tokens. Uses the Free plan's only custom connector slot | https://pipeboard.co/pricing |

Tool cost for the main path: $0. Ad spend: none added (read-only).

## 3. Reader friction (top problems)

1. **`is_ads_mcp_enabled: false`** — "OAuth was smooth, all 29 tools loaded… anyone actually been enabled?" Cause: Meta's per-ad-account rollout gate; not user-fixable. Reported order: US and higher-spend accounts first. Fix: confirm it's the flag, try other ad accounts you manage (flag differs per account), check you have admin/full advertiser role, reconnect and retry every 1 to 2 weeks, or use a vetted fallback. Sources: The Ad Spend (Jun 26, 2026, updated Jul 2026) https://theadspend.com/blog/meta-ads-mcp-not-enabled ; Claude Community FB group (snippet); r/FacebookAds "is_ads_mcp_enabled: false" (snippet); AdAdvisor (Sep 4, 2026, snippet).
2. **Fear of account bans** — r/FacebookAds "Is the Official Meta MCP REALLY Safe…" (1 week ago, snippet: "I had read stories of people getting banned…"). Jon Loomer notes earlier unexplained shutdowns from unapproved AI integrations. Fix: use only Meta's official server; Meta's help page says using it alone won't trigger a ban. Avoid third-party servers that route through shared apps.
3. **Connector inherits all your access, including client accounts** — Jon Loomer. Fix: at the Facebook Login step, select only the business portfolio(s) you intend; name the ad account ID in prompts.
4. **Worked, then stopped after ~2 months** — token expiry (~60 days reported, Unconfirmed officially). Fix: disconnect and reconnect in Customize > Connectors. Source: The Ad Spend.
5. **Wrong account answered** — Fix: put the ad account ID in the prompt; check the profile used at OAuth. Source: The Ad Spend.
6. **Rate-limit errors on big accounts** — Fix: smaller date ranges, fewer breakdowns per question. Source: The Ad Spend (community figure).
7. **Claude Code CLI: "redirect_uris are not registered for this client" / 401 on health check** — Claude Code issue (anthropics/claude-code, May 2026, snippet). Fix for this guide: use claude.ai or Claude Desktop, which work. Keeps Claude Code (paid) out of scope anyway.
8. **Numbers don't match Ads Manager** — no specific thread found; expected causes are date range, time zone, and attribution setting differences. → /verify with a real account; troubleshoot entry written from the check.
9. **Conflicting claims that custom connectors need a paid Claude plan** — Pipeboard README and The Ad Spend say so; Claude's own Help Center (Aug 2026) says Free gets one. Use the official source and note it, since readers will see the conflicting advice.

## 4. Competitor content

| Source | Format / promise | What's good | What's missing or outdated |
|---|---|---|---|
| Jon Loomer, "Meta Ads AI Connectors and Claude: Setup, Uses, and Risks" (May 5, 2026) https://www.jonloomer.com/meta-ads-ai-connectors-claude/ | Free blog post | Clear Claude steps, 6 use cases, honest risks | No read-only lock (rules or Claude tool permissions), no rollout-gate troubleshooting, no ready prompts, no number-matching check |
| Guillermo Flor, "Claude for Meta Ads: The Complete Guide" (productmarketfit.tech) | Paywalled newsletter (7-day trial) | "Prompts that move budget", skills | Behind a paywall; positioned as "Meta Ads just stopped being an agency job", pushing write automation |
| The Ad Spend, "Meta Ads MCP Not Enabled?" (Jul 2026) | Free troubleshooting post | Best rollout-gate explanation | Vendor pitch; says connectors need a paid Claude plan (contradicts Claude docs) |
| Pipeboard README / Windsor.ai / Whatagraph / Ryze tutorials | Vendor tutorials | Fast setup | Each steers to its own paid tool; Pipeboard says Claude Pro/Max required (outdated) |
| adlibrary.com "50 Claude Prompts for Marketers" | Free prompt list | Many copy prompts | Generic copywriting, not account-audit prompts run on live data; no read-only safety |

No gated freebie found that combines setup + read-only lock + verified audit prompts.

## 5. The A5 angle

1. **The only guide that makes it actually read-only, twice:** Meta's Ads MCP server rules (block write actions per ad account) plus Claude's tool permissions (write/delete tools set to Blocked). Competitors connect with full write access.
2. **10-minute pre-flight before anything else:** check `is_ads_mcp_enabled` for each ad account first, so readers know immediately whether they're in Meta's rollout, with the honest fallback (wait and retry schedule, or Pipeboard Free with its 30 calls/week) and clear warnings about shady "we'll enable it for you" offers.
3. **A number-matching test:** the success check compares Claude's answer to Ads Manager for the same date range, time zone, and attribution setting. Nobody else proves the data is right.
4. **A weekly audit prompt pack built on real tool names:** each prompt maps to a read tool (`ads_get_ad_entities`, `ads_insights_anomaly_signal`, `ads_get_dataset_quality`, `ads_account_get_activity_logs`…), written to be light on calls so it stays inside rate limits.
5. **Agency-safe setup:** pick only the right portfolio at login, always name the ad account ID, and know how the connector reaches client accounts.

## Blueprint impact (for /outline)

- Stack simplifies: **no Meta developer app, token, Node.js, or Python.** Main path = Claude (web or Desktop, Free) + official Meta connector + Business Suite rules. Remove the local fallback from the blueprint.
- Time to result drops to roughly **30 to 45 minutes** if the account is enabled.
- **Promise risk:** readers whose ad accounts aren't in Meta's rollout can't reach the result that day. Suggested promise wording: "…or know within 10 minutes whether Meta has enabled your ad account, with a free fallback." Needs your confirmation before /outline.
- Fallback trade-off: Pipeboard Free uses the Free plan's single custom connector slot, so readers must remove the Meta connector first, and 30 calls/week covers only a light weekly audit.

## Open items for /verify
- Tool permissions visible to Free/Pro individual users? Exact labels.
- Does the `all` rule block read tools?
- `ads_get_errors` exists today? Current tool count.
- Current OAuth screen labels and the portfolio selection step.
- Number-matching: which date range/attribution the tool uses by default.
