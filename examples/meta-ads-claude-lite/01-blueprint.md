Status: confirmed

Slug: meta-ads-claude-lite
Promise: In 15 minutes, a digital marketer has Claude connected read-only to their Meta ad account and a first performance report from live data, using only free tools. Or they know within 10 minutes that Meta hasn't enabled their account yet, and what to do.
Reader: Digital marketers (in-house, freelance, or small agency) who already run an active Meta ad account and are heavy Claude/ChatGPT users. Intermediate: comfortable in Ads Manager, not necessarily with terminals or APIs.
Result: Claude connected to Meta's official Ads MCP server (https://mcp.facebook.com/ads), locked read-only on Meta's side (Ads MCP server rules), plus a reusable first performance report prompt. Claude's tool permissions (second lock) and the weekly prompt pack move to the nurture emails.
Success check: (1) Claude lists the ad account with is_ads_mcp_enabled: true. (2) Claude answers "spend, CPA, and CTR per campaign for the last 7 days" and states the date range, time zone, and attribution setting it used; the reader sets Ads Manager to the same and the numbers match. (3) A request to create a campaign is refused.
Time to result: about 15 minutes
Language: id+en, primary: en (UI labels were verified in English)
Format: lite (derived from the full guide in meta-ads-claude/; the deeper material moves to the nurture emails)

Free-tool stack:
| Tool | Used for | Account needed | Free-tier limit (checked 2026-09-28) |
|---|---|---|---|
| Claude (web or Desktop, Free plan) | Chat + custom connector host | Claude account | Free plan: 1 custom connector |
| Meta Ads MCP (official, mcp.facebook.com/ads) | Bridge from Claude to the ad account | Facebook login with ad account access | Free open beta; per-account rollout gate (is_ads_mcp_enabled) |
| Meta Business Suite: Ads MCP server rules | Block write actions on Meta's side | Full control of the business portfolio | Free; limited availability |
| Meta Ads Manager | Cross-check numbers | Ad account access | Free |
| Fallback: Pipeboard Free | Only if the account is not enabled yet | Pipeboard account (no card) | 30 tool executions/week, 2 ad accounts; uses the Free plan's single custom connector slot |

Costs outside tools: No new ad spend; the guide is read-only. The ad account needs existing campaign data for the audit prompts (running ads is the reader's own budget).

Scope decisions: Read-only only. Claude only (ChatGPT and Claude Code excluded). No Meta developer app.

Verification plan: Setup, permissions, rules, rollout flag, and write-block test verified on an empty test ad account (USER). Number matching marked DOC with a visible note, because no ad account with spend is available.

Future guides:
- Connect Meta Ads to ChatGPT
- AI write actions (pause, budget changes) with a human approval guardrail
- Scheduled weekly Meta Ads report
- Meta Ads + GA4 combined analysis in Claude

Ladder:
  Service line: meta-ads (Gwenchana Digital Advertising Services, entry tier: Starter)
  Wall: Claude can now read data and diagnose, but results still come from execution: fresh creative for testing, scaling budget without CPA blowing up, and tracking (Conversions API, attribution) that makes the data the AI reads trustworthy. Giving AI write access without guardrails also puts budget at risk.
  Bridge: Gwenchana runs Meta Ads strategy, creative testing, scaling, and tracking, starting from the Starter tier, while the reader keeps monitoring with this Claude setup.
  Not for premium if: You are still testing with a small budget and enjoy running it yourself. Use this setup and the prompt pack first.
