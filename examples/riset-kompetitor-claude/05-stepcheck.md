# WGY-V — Pre-draft checks (research open items)

Checked on: 2026-09-28 | Browser: built-in, not signed in | No draft yet: full step verification runs after /draft.

| # | Item | Status | Evidence | Impact on the outline |
|---|---|---|---|---|
| 1 | Ad Library search flow (Indonesia, no login): Ad category → All ads → APPLY → brand → pick under Advertisers | LIVE | Walked through today: labels "Search ads", "Ad category", "All ads", "APPLY", "Search by keyword or advertiser", "Search this exact phrase", "Advertisers"; advertiser view shows "~670 results", "Keyword", "Filters", "Sort by" | Steps can use these exact labels |
| 2 | Ad card fields | LIVE | "Active", "Library ID", "Started running on [date]", platforms, "N ads use this creative and text", CTA, destination domain | Snapshot columns |
| 3 | Claude in Chrome on Free | DOC | Claude Help, Aug 27, 2026: paid plans only | Optional shortcut only |
| 4 | Claude Free web search / fetch | DOC | Claude Help "Enable and use web search" (updated this week) | Main path for websites |
| 5 | Claude Free fetch of an Ad Library URL | USER | Plain fetch → HTTP 403 (strong signal, not proof) | If it fails: copy-paste is the only path for ads |
| 6 | Claude Free fetch of a brand product page and a Shopee page | USER | Needs a Claude Free account | Decides "paste the link" vs "copy-paste" for websites |
| 7 | Pasting Claude's table into Google Sheets | USER | Needs a Google account | Decides whether we ask Claude for tab-separated output |
| 8 | Web search toggle visible on Free today ("new Claude experience" has none) | USER | Needs a Claude Free account | Exact wording of the step |

## User walkthrough checklist (about 10 minutes, Claude Free account)

```text
[ ] A. New chat. Click + at the bottom left. Is there a "Web search" item? Screenshot the menu (item 8).
[ ] B. Turn web search on (if the item exists), then send:
       "Search the web and read this page: https://somethinc.com . List 5 products with price and main claim, with the URL for each."
       → Did it read the page, or say it can't? Copy the answer (item 6).
[ ] C. Same for a Shopee product page of any local brand (paste its URL).
       → Read it or not? (item 6)
[ ] D. Send: "Read this page and list the active ads: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ID&search_type=page&view_all_page_id=388633974963457"
       → Expected: it can't read it. Copy the answer (item 5).
[ ] E. Ask Claude for any small 3x3 table, copy it, paste into an empty Google Sheet.
       → Separate cells, or everything in one cell? (item 7)
```

## Walkthrough results (USER, Claude Free, 2026-09-28)

- A (item 8): **+** menu shows "Add files or photos", "Take a screenshot", "Add to project", "Add from GitHub", "Skills", "Connectors", "Design system", "Plugins", **"Web search"** (checked), "Memory". Account shows "Free". → screenshots/langkah-2-web-search.png
- B (item 6): somethinc.com homepage is JS-rendered with no listings; Claude searched and read product/collection pages instead. Prices came in **USD from the /en site** ("Prices are the /en site's USD display"); one price "[perlu verifikasi]". → pitfall: ask for the Indonesian site / Rupiah and state the currency. → (screenshot kept private: it shows personal chat history)
- C (item 6): Shopee shop page: "Please enable JavaScript", nothing readable; Claude refused to invent data and offered paste text / screenshot / brand site. → marketplace = copy-paste or screenshot. → (screenshot kept private: it shows personal chat history)
- D (item 5): Ad Library URL: "Meta Ads Library memblokir akses otomatis (robots.txt)" and JS-rendered; Claude suggested manual paste or screenshot. → ads = copy-paste. → (screenshot kept private: it shows personal chat history)
- E (item 7): pasted table splits into separate cells; Claude's intro sentence was pasted into row 1 too. → pitfall: copy only the table. → screenshots/langkah-5-paste-sheets.png

---

# WGY-V — Step verification of 04-draft.md (ID) and 04-draft-en.md

Verified on: 2026-09-28 | Browser: built-in (Ad Library live) + user walkthrough on Claude Free | Run type: TEST RUN (placeholder CTA only; every step is verified)

| Step | Status | Evidence | Fix applied |
|---|---|---|---|
| 1 Pick 3 competitors, empty sheet | DOC | No tool-specific UI beyond creating a Google Sheet | None |
| 2 Web search on + Prompt A | USER | A: + menu shows "Web search" (checked) on Free. B: Claude reads product pages via search; homepage JS-rendered | Pitfall from B: USD prices from the /en site → Prompt A asks for the local site and names the currency |
| 2 pitfall: marketplace pages | USER | C: Shopee "Please enable JavaScript", unreadable | Copy-paste path in the pitfall and quick fix 1 |
| 3 Ad Library flow | LIVE | Walked through today without login: Indonesia → Ad category → All ads → APPLY → Advertisers | Labels taken from the live UI |
| 3 pitfalls: keyword noise, resellers, ad blocker | LIVE / DOC | ~780 keyword results incl. other brands; reseller Pages in the dropdown; Meta notice about ad blockers | None |
| 4 Copy Ad Library text into Claude + Prompt B | USER / LIVE | D: Claude can't read the Ad Library link (robots.txt + JS). Page text copy contains status, dates, copy, CTA, destination (live page-text read) | None |
| 5 Prompt C + paste into Sheets | USER | E: pasted table splits into cells; Claude's intro sentence landed in row 1 | Prompt C says "start with the table"; pitfall tells readers to select from the headers |
| Quick fix 3 (usage limit, 5-hour reset) | DOC | Claude Help "Enable and use web search" | None |

Free-tier limits rechecked: Claude Free (web search/fetch, 5-hour reset) → CL-B, today · Claude in Chrome paid only → CL-A, today · Meta Ad Library, no login → META-AL + live, today.

Screenshots still needed: advertiser page in Meta Ad Library (Step 3). Supplied: langkah-2-web-search.png, langkah-5-paste-sheets.png.

## Final build (2026-09-28)
- CTA from the user: info@gwenchana.digital → `mailto:` with a subject per language ("Riset Kompetitor - Meta Ads" / "Competitor Research - Meta Ads"); the address is also written in the closing text.
- Step 3 screenshot captured with headless Chrome from the public Ad Library advertiser page (Somethinc Beauty, Indonesia) → screenshots/langkah-3-ad-library-advertiser.png.
- Banner removed: every step LIVE / DOC / USER, no screenshots missing. Before publishing: the nurture emails promised in the closing must exist in the email tool.
