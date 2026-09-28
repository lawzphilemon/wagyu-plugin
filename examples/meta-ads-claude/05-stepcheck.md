# WGY-V — Pre-draft checks (research open items)

Verified on: 2026-09-28 | Browser: built-in (not signed in) + curl against the live endpoint
Full step verification runs again after /draft; this file will then be extended.

| # | Item | Status | Evidence | Impact on guide |
|---|---|---|---|---|
| 1 | `ads_get_errors` exists | DOC | Meta tool page "Help and troubleshooting" lists `ads_get_errors` and `ads_get_help_article` | Use in the prompt pack (pre-flight error sweep) |
| 2 | Endpoint requires auth | LIVE | `POST https://mcp.facebook.com/ads` tools/list, no token → `401 {"title":"Authentication Required"}`; invalid bearer → 401 | Nothing works before OAuth; expected |
| 3 | OAuth scopes requested | LIVE | 401 `WWW-Authenticate` and `/.well-known/oauth-protected-resource/ads` list 8 scopes: `ads_management ads_read catalog_management business_management pages_show_list pages_manage_ads instagram_basic ads_mcp_management` | Confirms OAuth is never read-only. Meta's Get started doc lists 7 (misses `pages_manage_ads`), so quote the live list |
| 4 | Claude Tool permissions visible to Free/Pro individuals | OPEN | Official doc frames it under Team/Enterprise owners; third-party tutorials (Tactiq, a Cowork tutorial, HubSpot community) show individuals setting Always allow / Needs approval / Blocked | Decides whether layer 2 of the read-only lock works on Free |
| 5 | Meta rule `all` also blocks reads? | OPEN | Docs: rules "deny a specific agent action"; Help UI groups them as "Take actions in this ad account", which suggests reads are unaffected. Not confirmed | Decides whether we tell readers to use `all` or block actions one by one |
| 6 | Default date range / time zone / attribution of `ads_get_ad_entities` | OPEN | Needs a connected account | Needed for the number-matching success check |
| 7 | `is_ads_mcp_enabled` on Indonesian ad accounts | OPEN | Needs a connected account | Real datapoint for how many readers hit the rollout gate |
| 8 | Current tool count | OPEN | Loomer saw 29 in May 2026; docs list more | Guide says "ask Claude to list its tools", no fixed number |

## Step walkthrough results (USER)

| Step | Status | Evidence | Note for the draft |
|---|---|---|---|
| 1.1 Customize > Connectors | USER | screenshots/step-1.2-add-custom-connector-menu.png | Left nav: Customize > **Connectors**. Connectors panel groups items under **Not connected** |
| 1.2 + > Add custom connector | USER | same screenshot | The **+** is top right of the Connectors panel (next to search). Menu: **Browse connectors**, **Add custom connector** |
| 1.3 Name + URL > Add | USER | screenshots/step-1.3-connector-form.png | Dialog "Add custom connector" has a **BETA** badge. Two unlabeled fields (name, URL). **Advanced settings** (OAuth Client ID/Secret, optional): leave empty. Button **Add**. After adding, Meta Ads appears under Not connected with a Facebook icon and a **CUSTOM** badge |

Plan used for the screenshots: Claude Pro (Free-plan behavior of Tool permissions still unverified)

## Decision 2026-09-28

No ad account with spend was available for this test run. Verify on an empty test ad account (create one in the business portfolio if none exists). Steps 6 and 7 below (numbers) cannot be verified: the guide's number-matching step makes Claude state its own date range, time zone, and attribution, so it does not depend on an unknown default. Mark it DOC with a visible note ("verified on setup, not on a spending account"). Upgrade to USER if a client grants read-only partner access later. Audit answer examples in the guide are labeled illustrations.

## User walkthrough checklist (about 15 minutes, one test ad account)

Use an account you manage. Nothing here spends money. On an empty account, skip steps 6 and 7.

```text
[ ] 1. Claude (note your plan: Free / Pro): Customize > Connectors > + > Add custom connector
       Name: Meta Ads | URL: https://mcp.facebook.com/ads > Add > Connect
       → Screenshot the Facebook Login permission screen and the portfolio selection step.
[ ] 2. Customize > Connectors > click Meta Ads
       → Is "Tool permissions" there? Screenshot it. Can you set write/delete tools to Blocked?
[ ] 3. New chat > + > Connectors > Meta Ads on. Prompt:
       "List my Meta ad accounts. For each, show the account ID, currency, time zone, and is_ads_mcp_enabled."
       → Copy the answer.
[ ] 4. Prompt: "List every tool you have from the Meta Ads connector, grouped into read and write."
       → Copy the count.
[ ] 5. Business Suite > Settings > Integrations > Ads MCP server
       → Visible? Screenshot. On one ad account set everything to Blocked (the most restrictive option).
[ ] 6. Back in Claude: "Show spend, impressions, CTR, and cost per result per campaign for act_<ID>, last 7 days.
       State the exact date range, time zone, and attribution setting you used."
       → Does it still answer (reads allowed)? Copy the answer.
[ ] 7. Ads Manager, same account, same 7 days, same attribution setting → do the numbers match? Note any difference.
[ ] 8. With write tools still Blocked in Claude (step 2), prompt: "Create a paused campaign named WAGYU-TEST."
       → Expected: refused. Paste what happened. If a campaign was created anyway, it is paused (no spend): delete it in Ads Manager.
```

---

# WGY-V — Step verification of 04-draft.md

Verified on: 2026-09-28 | Browser: built-in (not signed in) | Run type: **DUMMY (plugin test run)**. The user explicitly accepted OPEN steps for this run; the guide is not publish-ready until they are resolved.

| Step | Status | Evidence | Fix applied |
|---|---|---|---|
| 1.1 Customize > Connectors | USER | screenshot step-1.2 (Claude Pro) | Labels taken from screenshot |
| 1.2 + > Add custom connector | USER | screenshot step-1.2 | "+ at top right, next to search" added |
| 1.3 Name + URL > Add | USER | screenshot step-1.3 | Unlabeled fields and Advanced settings explained |
| 1.4 Connect + Facebook sign-in | DOC | CL-B ("Click Add, then follow the same connection process"; "Connect"); META-D (OAuth via Facebook Login for Business); scopes LIVE | None |
| 1.5 Tick one portfolio | OPEN (dummy-accepted) | Third-party only (Jon Loomer). Needs user screenshot | None |
| 1.6 + > Connectors > toggle | DOC | CL-B, Aug 21, 2026 | None |
| 1.7 P0 pre-flight | OPEN (dummy-accepted) | ads_get_ad_accounts DOC; `is_ads_mcp_enabled` field is community-reported, not in Meta docs | None |
| 2.1 to 2.3 Business Suite > Settings > Integrations > Ads MCP server | DOC | META-H (help 1456422242197840) | None |
| 2.4 Block every action | DOC | META-H labels (Allowed/Blocked, Take actions in this ad account, Limited); META-R action list | Keeps "block one by one" until `all` is tested |
| 2.5 Tool permissions | OPEN (dummy-accepted) | CL-B documents it for Team/Enterprise owners | **FAIL fixed:** draft wrongly said "Confirmed on Claude Pro"; reworded |
| 2.6 Block write/delete | OPEN (dummy-accepted) | Depends on 2.5 | None |
| 2.7 Lock test (P2) | OPEN (dummy-accepted) | Needs a connected, enabled account | None |
| 3.1 P1 number check | DOC | META-D ads_get_ad_entities; visible note "tested on setup only" kept | None |
| 3.2 Ads Reporting attribution | DOC | https://www.facebook.com/business/help/654970342692714 (en-GB: "Customise", "Options", "Select attribution settings", "All conversions" / "First conversion", "Apply"; requires admin/advertiser/analyst access) | **NEEDS SOURCE resolved.** Rewritten for Meta Ads Reporting; US spelling "Customize" is assumed, UK spelling noted in text |
| 3.3 Compare numbers | DOC | Reader comparison | Conversion count added to T4 |
| 3.4 P3 weekly snapshot | DOC | META-D ads_get_ad_entities | None |

Free-tier limits rechecked: Claude Free → 1 custom connector → CL-A/CL-B (read today) · Pipeboard Free → 30 tool executions/week, 2 ad accounts, no card → pipeboard.co/pricing (read today) · Meta Ads MCP → free open beta, gradual rollout → META-D blog (updated Sep 22, 2026).

Screenshots still needed: Meta permission screen (1.4), portfolio selection (1.5), chat connector toggle (1.6), pre-flight answer (1.7), Business Suite settings (2.1), Ads MCP server page (2.2), action list (2.3), all actions blocked (2.4), Tool permissions (2.5), write tools blocked (2.6), refusal message (2.7), Ads Reporting attribution settings (3.2). Illustrations to label: 3.1, 3.4.

Open steps to close before publishing: 1.5, 1.7, 2.5, 2.6, 2.7 (walkthrough checklist above, items 1 to 5 and 8).
