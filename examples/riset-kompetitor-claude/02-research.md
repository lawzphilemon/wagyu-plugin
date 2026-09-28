# WGY-R — Research: Riset kompetitor pakai Claude

Captured: 2026-09-28 | Mode: built-in browser (live Google, live Meta Ad Library without login, direct page reads) + curl for a no-JavaScript fetch test. Reddit not opened (blocked in the browser pane).

## 1. Official procedure

### A. Claude in Chrome: paid plans only (blueprint risk confirmed)
Source: Claude Help Center, "Get started with Claude in Chrome", Aug 27, 2026 — https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
- "Claude in Chrome is available for all paid plans (Pro, Max, Team, and Enterprise)." Not on Free.
- Chrome only: "not supported on other Chromium-based web browsers or mobile devices."
- Install: Chrome Web Store → **Add to Chrome** → sign in → pin via the puzzle icon → grant permissions → click the Claude icon to open the side panel.
- The side panel reads the current tab with no extra setup.
→ Impact: the main path must not depend on it. Offer it only as an optional speed-up for Pro users.

### B. Claude Free: web search + web fetch (the free path for websites)
Source: Claude Help Center, "Enable and use web search", updated this week — https://support.claude.com/en/articles/10684626-enable-and-use-web-search
- Turn on: **+** (lower left of the chat) → **Web search** (checkmark). "If you have the new Claude experience, there's no web search toggle. Claude searches the web when it helps."
- With web search on, Claude can "retrieve content directly from web pages when provided with specific URLs" (web fetch).
- Free accounts: usage limits reset every five hours; fetching long pages uses a lot of the limit. Claude's advice: be mindful of direct links, turn search off when not needed.
- Include "Search the web" / "use web search" in the prompt to make sure it's used.

### C. Meta Ad Library (the free path for ads)
Sources: Meta Business Help Centre, "About the Meta Ad Library" — https://www.facebook.com/business/help/2405092116183307 ; live walkthrough of https://www.facebook.com/ads/library/ (Indonesia, not logged in).
- Official: "Anyone can view and search the Ad Library." It contains "all active ads". Searching a term returns ads that include the term **or** ads run by Pages whose name includes it. Downloads require a Facebook login.
- Live UI (EN labels, 2026-09-28):
  1. Landing: **Search ads** → country dropdown (**Indonesia**) and **Ad category**. The search box shows "Choose an ad category" and stays unusable until a category is chosen.
  2. **Ad category** → **All ads** → **APPLY**. The box becomes "Search by keyword or advertiser".
  3. Typing a brand shows a dropdown: first `"brand" Search this exact phrase`, then **Advertisers** with follower counts and Instagram handles.
  4. Picking an advertiser opens the brand's view: name, **Ads** / **About** tabs, "~N results" (active ads), a **Keyword** box to filter within the brand, **Filters**, **Sort by**. URL contains `view_all_page_id=…` (shareable). Default sort in the URL: `sort_data[mode]=total_impressions` (impression numbers themselves are not shown).
  5. Each ad card: **Active**, Library ID, **Started running on [date]**, platforms, "This ad has multiple versions" / "N ads use this creative and text", ad copy, CTA button, destination domain (often SHOPEE.CO.ID for local brands).
- Selecting all text on the results page and copying it captures status, start dates, ad copy, CTA, and destinations (confirmed with the page-text read).

### D. Can Claude's web fetch read the Ad Library?
- Test: plain HTTP fetch (no JavaScript) of an Ad Library search URL → **HTTP 403, no ad content**. Claude's fetcher is different, so this is a strong signal, not proof. → /stepcheck: try it in Claude Free. Plan the guide around **copy-paste** for Ad Library.

### E. Google Sheets
- Free with a Google account. Pasting a table from Claude into Sheets: behavior (splits into cells or lands in one cell) → verify in /stepcheck. Fallback: ask Claude for tab-separated output.

## 2. Free-tier limits (checked 2026-09-28)

| Tool | Needed feature free? | Card? | Limits | Source |
|---|---|---|---|---|
| Claude Free | Chat, web search, web fetch: yes | No | Usage limits reset every 5 hours; fetching long pages uses more | Claude Help (B) |
| Claude in Chrome | **No** (Pro and above) | – | – | Claude Help (A) |
| Meta Ad Library | Yes, no login needed to search | No | Only active ads; spend/reach only for political ads and ads delivered in the EU/UK. Download needs login | Meta Help (C) |
| Google Sheets | Yes | No | Google account | – |

Tool cost for the guide: Rp0. Ad spend: none.

## 3. Reader friction (top problems)

1. **"Claude in Chrome" isn't there on Free.** Readers of Charis's guide on the Free plan hit this at step 3 to 6 with no explanation. Cause: paid plans only (A). Fix: free path via web search + copy-paste.
2. **Keyword search returns ads from other advertisers.** "somethinc" returned ~780 results including Beauty Haul and NESCAFÉ. Cause: term matching (C). Fix: pick the brand under **Advertisers**, not the phrase.
3. **Many Pages for one brand, plus resellers.** Dropdown showed Somethinc Beauty (1.4M IG), Somethinc Makeup, Somethinc Aesthetic Clinic, and resellers ("Stokist RESMI Somethinc", "Somethinc Malang"). Fix: pick by follower count and the official handle; research sub-brand Pages separately if relevant.
4. **Search box doesn't work.** Cause: no ad category chosen yet (observed). Fix: **Ad category** → **All ads** → **APPLY** first.
5. **Ad Library loads blank or misbehaves.** Meta's own notice: advertising tools "might not work as expected when an ad blocker is enabled." Fix: turn off the ad blocker for facebook.com.
6. **Claude can't read the link.** Web fetch blocked (403-style) on Ad Library and likely on some shop and marketplace pages. Fix: select all, copy, paste the page text into Claude.
7. **Claude invents prices or claims.** When a page isn't readable, a model may fill gaps. Fix: every cell needs a source URL, and the prompt says to write "tidak ditemukan" instead of guessing.
8. **Usage limit reached on Free.** Long pages and many competitors in one chat. Fix: one competitor per message, paste only the relevant part, turn web search off when pasting.
9. **"How much are they spending?"** Not shown for commercial ads in Indonesia (C). Fix: use proxies and label them as proxies: number of active ads, how long an ad has run, and how many ads reuse the same creative.
10. **Data goes stale.** Prices and promos change weekly. Fix: date column in the sheet; rerun monthly.

## 4. Competitor content

| Source | Format | Good | Missing / outdated |
|---|---|---|---|
| charisnicholas.com/claude-riset-kompetitor (checked today) | Free page, ID, 11 steps + 10 prompts, skincare example | Clear install steps, prompt library, illustrated result table | Depends on Claude in Chrome (paid) without saying so; websites only, no ads; no sources or dates in the table; no advice on resellers or unreadable pages |
| Jagoan Hosting (Aug 2023), Sasana Digital (Jun 2023) | Blog, ID | How to open Ad Library | Old UI (no Ad category step), no AI, no structured output |
| Privyr (Nov 2024), Kaya (Jul 2024), Adsumo (Feb 2025) | Blog, ID/EN | Steps to see competitor ads | No AI analysis, no sheet, no "what to test next" |

No free guide found that combines website + Ad Library + AI analysis into a sourced sheet on a free plan.

## 5. The A5 angle

1. **Actually free:** built on Claude Free (web search + copy-paste). Claude in Chrome is only an optional shortcut for Pro users, stated honestly.
2. **Ads, not only websites:** Meta Ad Library shows what competitors are paying to push right now, with start dates. Long-running ads and creatives reused across many ads are strong signals.
3. **Picks the right advertiser:** avoids the keyword-noise and reseller traps with a verified search flow.
4. **Sourced, dated sheet:** every row has a source link and check date; the prompt forbids guessing.
5. **Ends in tests, not a table:** 3 gaps → 3 test ideas, each tied to the competitor ad it came from. That's the bridge to running those tests (Meta Ads).

## Blueprint impact (for /outline)
- Tool stack: Claude in Chrome moves from core to optional (Pro). The steps use Claude Free web search for websites and copy-paste for Ad Library.
- Time: 30 to 45 minutes still realistic for 3 competitors.

## Open items for /stepcheck
- Does Claude Free web fetch read an Ad Library URL? (Expected: no.)
- Does it read a typical local brand product page, and a Shopee product page?
- Pasting Claude's table into Google Sheets: separate cells?
- Web search toggle vs "new Claude experience" (no toggle): what does a Free account see today?
