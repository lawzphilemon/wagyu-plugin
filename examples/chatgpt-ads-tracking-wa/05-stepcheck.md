# WGY-S — Stepcheck: chatgpt-ads-tracking-wa

## Step verification (draft 04-draft.md)

Verified on: 2026-10-08 | Browser: Claude in Chrome (public docs, read-only) + WebSearch/WebFetch; account screens via USER screenshots (no sign-in by Claude)

| Step | Status | Evidence | Fix applied |
|---|---|---|---|
| Intro: verification note | USER | Data source created before NPWP and billing; Business/Personal split; identity always required (USER, Settings → Verification screenshot 16) | Reworded to claim only what USER saw; removed the [VERIFY] box ("kalau diminta verifikasi identitas lebih dulu, selesaikan itu") |
| 1.1 Salin Pixel ID | USER | Conversions menu, Data Source tab, ID under name (screenshots 1–2) | — |
| 1.1 sub-step Create → Data Source dialog | OPEN | Only Create dropdown seen (Data Source / Conversion Event); dialog fields not seen | — |
| 1.2 Lead created event | USER | Create custom conversion dialog + Base event list (screenshots 3, 7) | — |
| 1.3 Attach to campaign | USER | Edit Campaign → Conversion event, ✕, + Add event (screenshots 6, 8) | — |
| 1.4 Tracking parameters field | USER | Label, placeholder, supported placeholders (screenshot 5) | — |
| 1.4 UTM reaches GA4 | OPEN | Needs real ad clicks after the parameter is set; USER keeps campaign unchanged until 2026-10-13 | — |
| 2.1 Click URL | USER + DOC | Configure Built-In Variables panel (screenshot 14); https://support.google.com/tagmanager/answer/7182738 | — |
| 2.2 Just Links trigger | DOC | Click trigger https://support.google.com/tagmanager/answer/7679320 (Just Links, Wait for Tags, Check Validation); About triggers https://support.google.com/tagmanager/answer/7679316 ("Some <event>", operator "matches RegEx"), 2026-10-08. USER's existing WA trigger fires (screenshot 11) | — |
| 2.2 exact labels "Some Link Clicks", "matches RegEx (ignore case)" | OPEN | Docs show the pattern, not these exact strings | — |
| 2.2 Wait for Tags (G) | OPEN | Not tested | — |
| 2.3 GA4 Event tag | DOC + USER | https://support.google.com/tagmanager/answer/13034206; USER tag "GA4 Event - WhatsApp Click" fires, event in DebugView (screenshots 11, 13) | — |
| 2.4 Key event (EN labels) | DOC | https://support.google.com/analytics/answer/13128484 rechecked 2026-10-08 (30 key events limit) | — |
| 2.4 Indonesian labels (H) | OPEN | From AI-translated help page | — |
| 3.1 Official template in gallery | LIVE (listing) / OPEN (add flow) | Gallery listing "OpenAI Ads Measurement Pixel" by openai rechecked live 2026-10-08; add flow per README, test after 2026-10-13 | — |
| 3.2 Constant variable | DOC | https://support.google.com/tagmanager/answer/7683362 (Variables → User-Defined Variables → New → Variable Configuration → Constant), USER already uses one | — |
| 3.3 Page viewed tag | DOC / OPEN | Field labels from template.tpl; "base tag not required" per README; not run (D) | — |
| 3.4 Lead created tag | DOC / OPEN | Field labels from template.tpl; not run with official template | — |
| 3.5 Pause old tag | DOC | https://support.google.com/tagmanager/answer/7679308 (open tag → 3-dot icon top right → Pause → Save, then publish) | Step was [NEEDS SOURCE]; rewritten to match the doc, Save added |
| 3.6 Preview test | USER | Tag Assistant Link Click, DebugView whatsapp_click, Event Stream lead_created pixel_sdk (screenshots 11–13, Stape build) | — |
| 3.6 Preview events before publish | OPEN | Container was already published during USER's test | — |
| 3.7 Publish | DOC + USER | https://support.google.com/tagmanager/answer/13034206 (Submit → Publish and Create Version → Publish); USER container published | — |
| Troubleshooting 1–5, 7, 8, 10 | DOC | Research section 1 and 3 sources (GTM, GA4, OpenAI dev docs, WP Rocket) | — |
| Troubleshooting 6 (Customize columns) | USER | screenshot 10 | — |
| Troubleshooting 9 (Diagnostics warnings) | USER | screenshot 15, exact text | — |

Free-tier limits rechecked (2026-10-08):
- Google Tag Manager → free, **3 workspaces** in the standard version (360: unlimited) → https://marketingplatform.google.com/about/tag-manager/compare/ → added to the toolkit table.
- GA4 → 30 key events per standard property → https://support.google.com/analytics/answer/13128484
- OpenAI Ads Manager → account creation free; "Billing must be set up before your campaigns can deliver" → https://help.openai.com/en/articles/20001213-ads-manager-account-setup (updated "2 days ago")
- Official OpenAI template → listed in the GTM Community Template Gallery → https://tagmanager.google.com/gallery/#/?filter=openai
- Tag Assistant → free (no pricing page; part of GTM).

Screenshots still needed (all placeholders; blur Pixel ID and account data):
- 1.1 Conversions page with 4 tabs · 1.2 Create custom conversion dialog · 1.3 Edit Campaign Conversion event · 1.4 Tracking parameters · 2.1 Configure Built-In Variables · 2.2 Just Links trigger with regex · 2.3 GA4 Event tag · 2.4 GA4 Create event / key event · 3.1 gallery search · 3.3 Page viewed tag · 3.4 Lead created tag · 3.6 Tag Assistant, DebugView, Event Stream
- USER already has usable captures for 1.1, 1.2, 1.3, 1.4, 2.1, 3.6 (chat screenshots 1–15) once cropped/blurred: Pixel ID, ad account ID, API key name, promotion box, ad group names, spend figures.

User walkthrough (safe now; in an existing workspace, close without saving; nothing published):
```text
[ ] 1.1  Conversions → + Create → Data Source → screenshot the dialog fields → Cancel
[ ] 2.2  Triggers → New → Trigger Configuration → Just Links → screenshot: label of the "Some …" option and the operator list (look for "matches RegEx (ignore case)") → tick Wait for Tags → screenshot what GTM asks → close without saving
[ ] 2.4  GA4 Admin → Data display → Events → + Create event → is "Mark as key event" in the form? screenshot → Cancel
[ ] 2.4  (optional, H) Switch Google account language to Indonesian once → screenshot the same two screens
After 2026-10-13 (template switch):
[ ] 3.1  Search Gallery "OpenAI" → Add to workspace → screenshot permissions
[ ] 3.3  Tag Page viewed only + old Stape tags paused → Preview → Event Stream: page_viewed appears? (and no separate base tag needed)
[ ] 3.4  Tag Lead created → WA click in Preview → lead_created in Event Stream
[ ] 3.6  Do the Preview test BEFORE publishing → does lead_created reach Event Stream?
[ ] 1.4  Next campaign / after the switch: set Tracking parameters → after real ad clicks, GA4 Traffic acquisition shows source chatgpt_ads?
```

### Resolution before /finaldraft (2026-10-08)
USER declined ACCEPTED-OPEN (campaign live, no test-banner build). Every OPEN item was resolved by rewriting the step to verified content only:

| Item | Was | Now | How |
|---|---|---|---|
| 1.1 Create Data Source dialog | OPEN | USER | Dialog fields removed; step only says + Create → Data Source → follow the dialog; "Web" type taken from the Data Source table (USER) |
| 1.4 UTM reaching GA4 | OPEN | USER | Claim removed; step ends at "string saved" (USER screenshot 5); pitfall says `chatgpt_ads` appears in GA4 only after real ad clicks |
| 2.2 "Some Link Clicks", "matches RegEx (ignore case)" | OPEN | DOC | Rewritten to doc wording: **This trigger fires on** → **Some**, operator `matches RegEx` (https://support.google.com/tagmanager/answer/7679316, /7679320) |
| 2.2 Wait for Tags | OPEN | DOC | No behavior claim; only "not needed, leave unticked" (doc lists it as optional) |
| 2.4 + 2.3 Indonesian labels | OPEN | DOC | All AI-translated Indonesian labels removed; English labels only (DOC), with a note that ID interfaces change labels but not menu order |
| 3.1–3.4 official template | OPEN | DOC | OpenAI's own README + template.tpl labels (official doc) + gallery listing LIVE 2026-10-08. USER test after 2026-10-13 will upgrade to USER |
| 3.6 Preview events before publish | OPEN | DOC + USER | Event Stream check moved to 3.7 (after publish, USER-verified); 3.6 now checks Tag Assistant + DebugView only (DOC + USER) |

All steps are now LIVE, DOC, or USER. No [VERIFY] or [NEEDS SOURCE] left in 04-draft.md.

Status summary (before resolution): 6 OPEN groups (1.1 dialog, 1.4 UTM in GA4, 2.2 labels + Wait for Tags, 2.4 ID labels, 3.1–3.4 official template, 3.6 Preview-before-publish). No FAIL. Blocked from a publish-ready /finaldraft until these are USER or the user accepts them as ACCEPTED-OPEN.

## Pre-draft checks

### A. Ads Manager Conversions path (USER, screenshot 2026-10-08) — partial
- Left menu: **Overview**, **Campaigns**, **Conversions**, **Tools** (expandable), **Billing** (expandable), **Settings** (expandable). **Conversions is its own top-level item, not under Tools.** Third-party "Tools → Conversions" path is outdated.
- Conversions page header: title **Conversions**, help icon (?), key icon, **+ Create** button with dropdown (top right).
- Summary cards: **Total events**, **Conversion objective adoption** ("0 of 1 active campaigns optimizing for conversions"), **Active warnings** with **View warnings →** button.
- Tabs: **Data Source**, **Conversion Events**, **Event Stream**, **Diagnostics**.
- Data Source table columns: **Name**, **Type**, **Status**, **EQS**, **Events**, plus a **⋯** menu per row. The data source name shows a short ID under it (likely the Pixel ID; blur it in screenshots).
- **+ Create** dropdown has exactly two options: **Data Source** and **Conversion Event** (USER screenshot 2).
- Pixel ID: USER confirms the ID shown under the data source name in the Data Source table is the Pixel ID. Guide step: copy it from there.
- Not checked: the **⋯** row menu (View Code). Not needed if the guide uses the GTM template, which only asks for the Pixel ID.
- Not checked: the Create → Data Source dialog fields (name, Type Web). Gwenchana already has one data source; only the "Web" Type column is confirmed. Mark the dialog fields `[VERIFY]` or capture when a reader-side test account is available.
### B. Pixel before verification and billing (USER, 2026-10-08)
- The data source was created **before NPWP/TIN verification and before billing was set up**. Confirms the promise holds: the reader can build and test the whole setup (pixel + events) without verification or a payment method. Only campaign delivery needs them.
- Caveat for the guide: one account, one point in time. Word it as "bisa dibuat sebelum verifikasi dan billing (dicek Oktober 2026)".

- Verification detail (USER): verification splits into two paths. **Business** account → TIN (NPWP) is required. **Personal** account → no TIN needed. **Both paths still ask for identity verification** (matches the help doc: account verification "through Persona").
- Guide wording: do not say "wajib NPWP". Say: business needs NPWP, personal does not, both must complete identity verification before ads can run. Fix the blueprint's free-tool row ("Perlu dicek apakah pixel bisa dibuat sebelum verifikasi bisnis (NPWP)") accordingly.

- Identity verification status when the data source was created: USER does not remember. → Unknown. Guide must not claim the pixel works before identity verification. Safe wording: "data source bisa dibuat sebelum NPWP dan billing selesai; verifikasi identitas mungkin diminta lebih dulu" `[VERIFY]`.

### C. Conversion Event form (USER, screenshot 3, 2026-10-08) — partial
- **+ Create → Conversion Event** opens a dialog titled **Create custom conversion** (note: "custom" in the title even for standard events).
- Fields, in order:
  - **Data source** — "Where your conversions are tracked from." Dropdown placeholder **Select a data source**.
  - **Base event** — "The action that you'll track as a conversion." Dropdown placeholder **Select an event**.
  - **Conversion name** — "This name will appear in reporting and campaign setup." Placeholder "Enter a conversion name, like Purchase", **max 30 characters**.
  - **Attribution windows** (display only): **Click-through attribution window 30 Days**, **View-through attribution window 1 Day**.
  - Buttons **Cancel**, **Create**.
- Conversion Events tab table (background): columns **Events**, …, **Used by**, **Identifier cover.**, **Events**. Rows: **Lead Created** (Used by "-", 0%, 0 events) and **Page Viewed** (Used by **1 campaign**, 24%, 175 events).
  - Confirms the pitfall: **Page Viewed is attached to the campaign as a conversion**, Lead Created is attached to none.
  - Lead Created shows 0 events: the lead tag may not be live yet, or no test click was made. Check before using this account for the guide's success-check screenshots.
- Campaign edit (USER, screenshots 4–6): **Campaigns** → row **⋯** → modal **Edit Campaign**. Fields in order: **Campaign Name**, **Objective** (shows "Clicks", greyed out → objective cannot be changed after creation, matches docs), **Locations for this campaign**, **Locations to exclude from this campaign**, **Eligible platforms**, **Tracking parameters** (+ "Learn more"), **Included custom audiences**, **Exclude custom audiences**, **Budget** (Campaign budget, account currency), **Start Date**, **End Date** ("Set an End Date"), **Conversion event** (dropdown, ✕ to remove, **+ Add event**). Buttons **Cancel**, **Save**.
  - **A Clicks campaign can swap or add conversion events after creation**: replace Page Viewed with Lead Created via the dropdown, or **+ Add event**. Guide step confirmed.
  - Reminder from docs: events do not backfill; attach Lead Created once the lead tag is live.
- Observation (not for the guide, no results claims): the campaign table shows Conversions 0 while Page Viewed is attached and has events. Possible causes: 24–48 h attribution delay, or events not matched to ad clicks. Do not use as a claim.
- **Base event** dropdown (USER, screenshot 7), visible items in order: App installed, App opened, Appointment scheduled, Checkout started, Contents viewed, Items added, **Lead created**, Order created, **Page viewed**, Registration completed, Subscription created (list scrolls further; rest not seen, docs suggest Trial started / Custom). Note: App installed/opened appear in the list although the Pixel does not support them (Conversions API only, per docs).
- Multiple conversion events per campaign (USER, screenshot 8): **+ Add event** adds a second row; USER attached **Page Viewed + Lead Created** to the Clicks campaign. Conversion Events tab now shows Lead Created "Used by 1 campaign".
  - Root cause of the earlier gap (USER): Lead Created was simply never attached. Keep as a guide pitfall: "event dibuat ≠ event terpasang di campaign".
  - Guide advice: official docs say the **Conversions column combines all attached events into one total**, so with Page Viewed attached the Conversions number mixes page views and leads. Recommend attaching **Lead Created only**; if Page Viewed stays, read per-event columns via **Edit columns**.
- USER removed Page Viewed; campaign now uses **Lead Created only**.
- "Edit columns" location (USER, screenshot 9): the table **⋯** menu (Campaigns / Ad groups / Ads) shows only **Segment**, **Export**, **Upload in bulk**, **View Insights**. **No "Edit columns"** there, contrary to the Help Center ("three-dot menu → Edit columns"). Candidate: the columns icon between the filter icon and ⋯. → pending USER check. Guide must not cite the Help Center path until confirmed.
- **Confirmed (USER, screenshot 10):** the **columns icon** next to the filter icon opens **Customize columns**. Left: **Search for a column**, collapsible sections **Events** (checkboxes: App Installed, App Opened, Appointment Scheduled, Checkout Started, Contents Viewed, Items Added, **Lead Created**, Order Created, Page Viewed, Registration Completed, Subscription Created, Trial Started), **Setup**, **Delivery** (list scrolls; further sections not seen). Right: **Shown** list (drag to reorder, ✕ to remove). Button **Save changes**.
  - Guide step: columns icon → Customize columns → Events → tick **Lead Created** → Save changes. Gives a per-event Lead Created column next to Conversions.
  - Not seen: the Help Center's "Attribution windows" / "Conversions (by conv. time)" / "View-through conversions" options (likely further down). Not needed for this guide.
- C complete.

### J. UTM / tracking parameters (USER, screenshot 5) — answered at campaign level
- Real UI label is **Tracking parameters** (with "Learn more"), not "Landing page query parameters" as the Help Center FAQ says. → Use the UI label in the guide.
- Placeholder example: `campaign_id={campaign_id}&ad_id={ad_id}`.
- Helper text: "Optional. Added to your link when someone clicks your ad. Supported placeholders: **{campaign_id}, {ad_group_id}, {ad_id}, {ad_account_id}, {oppref}**." (`{oppref}` is not in the Help Center list.)
- Available in the Edit Campaign modal. Ad group / ad level not checked (Help Center says all three levels exist; precedence Ad URL → Ad → Ad Group → Campaign).
- Guide asset: set UTM once at campaign level, e.g. `utm_source=chatgpt&utm_medium=cpc&utm_campaign={campaign_id}&utm_content={ad_id}`, plus `utm_term={ad_group_id}` if wanted. Exact pattern to be fixed in /outline.

### Current Gwenchana GTM setup (USER, screenshot 11, Tag Assistant Preview, 2026-10-08)
- Tag Assistant header: **Connected** + site, "**2 Google tags found**" (GTM container + GA4 tag). Left event list: Consent Initialisation, Initialisation, Container loaded, DOM Ready, Window Loaded, **Link Click**. Panel: **Summary**, "Output of GTM-…", tabs **Tags / Variables / Data Layer / Consent / Console**, section **Tags fired**.
- After one WhatsApp click (Link Click event), fired once each: **Google Analytics Tag** (Google Tag), **OpenAI** (OpenAI Ads Pixel by Stape, base), **GA4 Event - WhatsApp Click** (Google Analytics: GA4 Event), **OpenAI - Lead Whatsapp** (OpenAI Ads Pixel by Stape). Also unrelated Custom HTML tags (Clarity, Ahrefs, Meta Pixel).
- Meaning: the existing Just Links trigger works and fires both destination tags in Preview. Current build uses the **Stape** template, not the official one.
- **Success check PASSED (USER, screenshots 12–13, same Preview session, one WA click):**
  - **Event Stream** (Conversions → Event Stream): toolbar **Search visible rows**, data source filter chip, **Pause polling** button (polling is on; the button toggles). Columns: **Event Type**, **Custom Event Name**, **Data Source**, **Received** (UTC), **API Channel**, **Event Data JSON**. Rows, all `pixel_sdk`: **Pixel Initialization**, **page_viewed** (`{"contents":[],"type"…`), **lead_created** (`{"type":"customer_act…`). Footer "3 recent events received". Arrived within the same minute.
  - **GA4 DebugView** (Admin → Property settings → Data display → DebugView): **whatsapp_click** appeared, plus `click`, `session_start`, `page_view`, and user property `non_personalized_ads = 1`.
  - ~~GTM Preview events reach OpenAI while unpublished~~ **Corrected (USER):** the container was already published, so this test does not prove that unpublished Preview events reach OpenAI. → `[VERIFY]`. Guide wording for now: "tes di Preview, lalu publish, lalu tes sekali lagi di situs live".
  - USER confirms the DebugView screenshot shows both `whatsapp_click` and `click`.
- Lead Created timing (USER): the Lead Created conversion event was **created about half a day after the ads started running**. Clicks before that were not counted (docs: no backfill). Guide pitfall: **create and attach Lead Created before the campaign goes live.**
- Template decision (USER): Gwenchana stays on the **Stape** template until the test campaign ends on **2026-10-13**, then switches to the official OpenAI template, to avoid disturbing campaign learning. → E and D (official template) are tested after 2026-10-13, before the guide is published. Outline/draft mark the official-template steps `[VERIFY]`.
- New pitfall for the guide: GA4 also logs its own **`click`** event (Enhanced Measurement outbound clicks) on the same WA click. Mark **whatsapp_click** as key event, not `click`, and expect both in DebugView. (Inference from the screenshot + GA4 outbound-click behavior; Enhanced Measurement setting not checked.)
- `page_viewed` here came from the **Stape** base tag, so D (does the official template's init-only tag send page_viewed?) is still open.
- GA4 UI language in this account is English; Indonesian labels still unverified (H).
- Guide labels confirmed: Tag Assistant event name for a Just Links trigger is **Link Click**; the tag card shows "[template name] - Fired 1 time".

- **Decision (USER, 2026-10-08): the guide uses the official "OpenAI Ads Measurement Pixel" template.** Official-template steps stay `[VERIFY]` until USER tests after 2026-10-13. Stape is mentioned only as an alternative.

### F. Built-in click variables (USER, screenshot 14) — partial
- Path: **Variables** → Built-In Variables → **Configure** → panel **Configure Built-In Variables**, sections Clicks / Forms / History…
- In the Gwenchana workspace, **Click URL** and **Click Text** are ticked; Click Element, Click Classes, Click ID, Click Target are not. This is an existing container, so it does not show the default for a fresh container.
- Guide step (safe either way): "Buka Variables → Configure, pastikan **Click URL** tercentang."
- Extra pattern seen: user-defined **Constant** variable `Const-OpenAI Pixel ID`. Good asset: store the Pixel ID once, reuse in every OpenAI tag.

### K. Warnings (USER, screenshot 15) — answered
- Path: **Conversions → Diagnostics** (also via **View warnings**). Summary: **Needs attention** (0 high · 2 medium), **Sources affected**, **Events at risk** ("in the last 7 days"). Filters **All sources**, **All severities**. Columns **Description**, **Source**, **Severity**.
- Warning 1: **No recent server-to-server events** — "We have not received server-to-server conversion events for this ad account in the last 24 complete UTC hours." Source "-", Severity **Medium**.
- Warning 2: **Some events are missing user data** — **Email coverage 0.0%**, **External ID coverage 0.0%**, Source = the data source, Severity **Medium**, **Learn more →**.
- Guide explanation: both are expected for a pixel-only WhatsApp-click setup (no Conversions API → no server events; no form → no email or customer ID to hash). They do not stop tracking. "Events at risk" counts every event affected by these warnings, not lost events (wording to keep careful; no official definition seen). Fixing them = Conversions API / user data, out of scope → future guide.

### I. Ads Manager interface language (USER, screenshot 16) — answered
- **Settings** submenu: **General**, **Users**, **Connected Apps**. Settings → General has **Account details**, **Regional settings**, **Verification**, **API Keys**. **No interface language option.** → Guide uses English Ads Manager labels.
- Confirms docs: Regional settings "Location, currency, and time zone can't be changed. Create a new ad account to use different settings."
- Confirms B: **Verification → Advertiser type** dropdown (here "Business"), "Changing this requires verification for the newly selected type."
- **Manage conversion keys** link sits under API Keys (Conversions API, out of scope).

### Still open (mark `[VERIFY]` in /outline)
- **E, D**: official template in gallery + permissions; whether an init-only tag sends `page_viewed`. Test after 2026-10-13.
- **G**: Wait for Tags behavior on WA links.
- **H**: Indonesian GTM/GA4 interface labels.
- Unpublished Preview events reaching OpenAI.
- Create → Data Source dialog fields.
- Identity verification before data source creation.

### A (cont.)
- Bonus for K: warnings are reached via **Active warnings → View warnings**; the data source row shows a warning icon in **Status**.
