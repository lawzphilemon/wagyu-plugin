# WGY-R — Research: Tracking klik WhatsApp ke GA4 + OpenAI Ads (ChatGPT Ads)

Captured: 2026-10-08 | Mode: Claude in Chrome (direct page reads) + WebSearch. Reddit is blocked in the browser, so Reddit threads are cited from search snippets only. Read-only browsing: no sign-ins, no forms, no downloads (one public GitHub file, `template.tpl`, was fetched with curl to read its field labels).

Blueprint note: `01-blueprint.md` has no `Status: confirmed` first line. The user handed it over as the blueprint in chat on 2026-10-08, so it was treated as confirmed for this research.

## 0. Blueprint changes this research suggests

1. **Use the official OpenAI GTM template, not Stape.** The GTM Community Template Gallery now lists **"OpenAI Ads Measurement Pixel" by `openai`** (Web, Tag), next to "OpenAI Ads Pixel by Stape". Checked live 2026-10-08 at https://tagmanager.google.com/gallery/#/?filter=openai. Source repo: https://github.com/openai/ads-measurement-pixel-gtm-template (Apache 2.0, © 2026 OpenAI). The blueprint row "Template ... (Stape) ... bukan buatan OpenAI" is out of date. Keep Stape only as a fallback mention.
   → **USER decision 2026-10-08: use the official template.** Steps stay `[VERIFY]` until tested after 2026-10-13. Pre-draft answers (UI labels, warnings, Tracking parameters, Customize columns) are in `05-stepcheck.md` and override the doc-based labels above where they differ.
2. **Wall line confirmed.** Official docs say a conversion-optimized campaign's objective and event setting "cannot be changed after creation". Clicks/impressions campaigns can attach conversion events without changing the objective. Source: https://developers.openai.com/ads/conversion-tracking

## 1. Official procedure

### A. OpenAI Ads Manager: data source (pixel) and conversion event
Sources:
- OpenAI Help Center, "Conversion Measurement", updated "2 months ago" (EN): https://help.openai.com/en/articles/20001409-conversion-measurement
- OpenAI Help Center, "Measure Results", updated "9 days ago" (EN): https://help.openai.com/en/articles/20001214-measure-results
- OpenAI Developers, "Conversion Tracking" (no date): https://developers.openai.com/ads/conversion-tracking
- OpenAI Help Center, "Ads Manager Account Setup", updated "2 days ago": https://help.openai.com/en/articles/20001213-ads-manager-account-setup (an Indonesian version exists at /id-id/; not opened)

What the official docs say:
- Flow: create a **data source** in Ads Manager, send events through the Pixel and/or Conversions API, then a **conversion event setting** picks which event from that source counts. "Sending an event and creating a setting are separate steps."
- Pixel ID: "Create a new Pixel ID in the **conversions tab** of Ads Manager" (Measurement Pixel doc). No Help Center article with the click-by-click UI path was found.
- Use standard event `lead_created` for "submits a lead form or requests contact". Custom events cannot be used for conversion optimization.
- Attribution window in the API example: 30 days. Reporting windows: 7, 14 or 30 days click-through; 0 or 1 day view-through (Measure Results).
- Attach the event to a campaign "before traffic starts". "Historical events from the mismatched setup will not backfill." A conversion "can be firing or accepted and still show 0" if it does not match the event set on the campaign.
- Attributed conversions take **24–48 hours** to show in reporting. Impressions/clicks refresh about every 15 minutes.
- To see individual events in the table: three-dot menu → **Edit columns** → choose events → **Save changes**.
- Billing must be set up before campaigns can deliver. Country/region, currency and time zone **cannot be changed** after account creation.

UI path seen only in third-party guides (EN, dated June 2026 and later):
- "ads.openai.com → **Tools → Conversions** → **+ Create** → **Data Source** → name, Type **Web** → **Create**", pixel code via "three dots → **View Code**" (conversiontracking.io, Jun 16 2026).
- "**+ Create → Conversion Event**, Type: **Lead**, select your pixel" (same source).
- Test: "**Tools → Conversions → Event Stream** → **Start Polling**".
- → /stepcheck: the user's own setup says **Conversions is now its own menu, not under Tools**. The third-party path is likely outdated. Confirm current labels (Pre-draft check A).

Event monitoring (official, API side): the recent-events endpoint returns a sample of events "from roughly the last 15 minutes", up to 50. Browser events show channel `pixel_sdk`, server events `server_to_server`. That explains the blueprint's "No recent server-to-server events" warning: a pixel-only setup sends nothing on the `server_to_server` channel. **The exact warning text does not appear in any official doc found** (Unconfirmed, from the user's own setup).

### B. OpenAI Measurement Pixel
Source: OpenAI Developers, "Measurement Pixel": https://developers.openai.com/ads/measurement-pixel
Source: OpenAI Developers, "Supported Events": https://developers.openai.com/ads/supported-events

- Loader: `https://bzrcdn.openai.com/sdk/oaiq.min.js`, init `oaiq("init", { pixelId: "<YOUR-PIXEL-ID>" })`. Place "near the top of your `<head>`".
- Lead event, exact official form:
  `oaiq("measure", "lead_created", { type: "customer_action" });`
  `amount` and `currency` are optional. If `amount` is set, `currency` is required, in **ISO 4217 minor units**. For IDR that would mean ×100 (Rp 50.000 → 5000000). Whether IDR is accepted is Unconfirmed. Recommend: no amount for this guide.
- `page_viewed` uses data type `contents`. "Use page_viewed for page loads." **The official doc does not say page_viewed fires automatically.** Several third-party guides say it does (conversiontracking.io, searchintel snippets) and others say "OpenAI fires nothing until you explicitly call measure". → Pre-draft check D.
- Consent: Pixel consent defaults to `true` unless set to false. The help article says to collect consent "where required by law". Mention briefly, no legal advice.
- CSP: if the site has a Content Security Policy, allow `bzrcdn.openai.com` (script-src, connect-src) and `bzr.openai.com` (connect-src, img-src).
- SDK handles `oppref` itself (captured from the landing URL, stored in `__oppref` cookie for 30 days).
- Troubleshooting from the doc: keep `debug: true` while testing; use integer amounts; "Always use the pixel on the browser."
- Help FAQ: "Can I deploy the Pixel through Google Tag Manager? Yes, as long as your tag manager loads the Pixel snippet on the correct pages and does not block or reorder the initialization and event calls."

### C. Official GTM template "OpenAI Ads Measurement Pixel" (by openai)
Source: https://github.com/openai/ads-measurement-pixel-gtm-template (README + `template.tpl` field labels, read 2026-10-08)

- Install: **Templates → Tag Templates → Search Gallery** (now live in the gallery). Manual import also possible.
- Field labels (EN, from `template.tpl`):
  - Section **Pixel setup**: **Pixel ID** (help: "Paste the Pixel ID from OpenAI Ads. Example: px_123."), checkbox **Send a measurement event when this tag fires** (default on), checkbox **Enable setup diagnostics in the browser console** (debug is on automatically in GTM Preview).
  - Section **Event**: **Event name** dropdown: Page viewed, Contents viewed, Items added, Checkout started, Order created, **Lead created**, Registration completed, Appointment scheduled, Trial started, Subscription created, Custom event. Also **Event ID**, **Per-event opt-out flag**, **Amount**, **Currency**, **Plan ID**, **Contents**.
  - Section **User matching**: Email SHA-256, External ID SHA-256, Country, City, Zip code (all optional).
- README: "Create an OpenAI Ads Measurement Pixel tag for each event... Use the same Pixel ID for every... tag." An optional base tag (checkbox off, Initialization or All Pages trigger) is allowed, but "**Event tags initialize the pixel themselves, so the base tag is not required.**"
- The template has **no consent field** (the Stape one does).
- Implication for the guide: two template tags are enough: `page_viewed` on All Pages + `lead_created` on the WhatsApp click trigger. No Custom HTML. This also removes the double-pixel pitfall's main cause.

Stape template (fallback): https://stape.io/helpdesk/documentation/openai-ads-pixel-tag, updated Aug 3, 2026. Labels: tag type "**OpenAI Ads Pixel by Stape**", **OpenAI Pixel ID**, **Event Name Setup Method** (Inherit from DataLayer / Override), Compliance (**Consent Granted**, **Enable GTM consent mode support**). Note: "currently only one Pixel ID is supported on the page."

### D. GTM: WhatsApp click trigger + GA4 event tag + publish
Sources:
- "Click trigger" (EN): https://support.google.com/tagmanager/answer/7679320?hl=en and (ID): https://support.google.com/tagmanager/answer/7679320?hl=id
- "Set up Google Analytics events in Tag Manager" (EN/ID): https://support.google.com/tagmanager/answer/13034206 (`hl=en`, `hl=id`)
- "Built-in variables for web containers": https://support.google.com/tagmanager/answer/7182738?hl=en

| Step | EN label (help) | ID label (help, `hl=id`) |
|---|---|---|
| New trigger | Triggers → New | Pemicu → Baru |
| Trigger type | Trigger Configuration → **Just Links** | Konfigurasi Pemicu → **Hanya Link** |
| Options | **Wait for Tags**, **Check Validation** | **Tunggu Tag**, **Periksa Validasi** |
| Condition | This trigger fires on: **Some Clicks**; "Fire this trigger when an Event occurs and all of these conditions are true" | Pemicu ini diaktifkan pada: **Beberapa Klik** |
| Variable | **Click URL** | **URL klik** |
| GA4 tag | Tags → New → **Google Analytics: GA4 Event**, **Measurement ID**, **Event Name** | Tag → Baru → **Google Analytics: Peristiwa GA4**, **ID Pengukuran**, **Nama Peristiwa** |
| Test | **Preview** → enter URL → **Connect** (Tag Assistant) | (ID page keeps this part in English) |
| Publish | **Submit** → **Publish and Create Version** → **Publish** | (English on ID page) |

- The ID help pages carry the note "may contain content translated using AI technology", so the ID labels may not match the real ID interface. → Pre-draft check H.
- Built-in variables doc lists Click URL etc. but **does not say whether they are on or off by default**. Third-party guides say "Click Variables are disabled by default... Variables → Configure" (boei.help, adnanagic.com snippet). → Pre-draft check F.
- GA4 event name rules (https://support.google.com/analytics/answer/13316687): case sensitive, start with a letter, letters/numbers/underscores only, no spaces, max 40 characters. `whatsapp_click` is valid.

### E. GA4: key event and DebugView
Sources:
- "Mark events as key events" (EN/ID): https://support.google.com/analytics/answer/13128484 (`hl=en`, `hl=id`)
- "Monitor events in DebugView": https://support.google.com/analytics/answer/7201382?hl=en

- Requires **Marketer** role or above (Editor for an existing event, per the note).
- New event (before data arrives): **Admin → Data display → Events → + Create event** → name → toggle **Mark as key event** → **Default key event value**, **Counting method** → **Create**. ID: **Admin → Tampilan data → Peristiwa → + Buat peristiwa** → **Tandai sebagai peristiwa utama** → **Nilai peristiwa utama default**, **Metode penghitungan** → **Buat**.
- Existing event: **Recent events** tab (ID: **Peristiwa terbaru**) → star icon.
- Limit: **30 key events** for standard properties.
- Key events affect reports from creation, up to 24 hours for standard reports; Realtime updates in minutes.
- DebugView: **Admin → Data display → DebugView**. Debug mode is switched on by Tag Assistant / GTM Preview. "Events are not visible in debug mode if... consent mode [is implemented] and users have not given consent for Analytics cookies."

### F. UTM pattern for ChatGPT Ads
Source: "Measure Results" FAQ (official).
- Ads Manager supports **Landing page query parameters** at Campaign, Ad group, Ad level via the three-dot menu → **Edit campaign / Edit ad group / Edit ad**.
- Supported macros: **{campaign_id}**, **{ad_group_id}**, **{ad_id}**, **{ad_account_id}**. Precedence: Ad URL → Ad → Ad Group → Campaign; an existing Ad URL parameter is not overwritten.
- Official FAQ also explains why Ads clicks differ from GA4 sessions (page load, redirects, consent, blocking, UTM handling, time zone).
- Third-party pattern seen: `utm_source=openai-ads&utm_medium=cpc&utm_campaign=...&utm_content=...` (conversiontracking.io). No official OpenAI UTM convention exists. The guide's own pattern can use the macros above.

### G. WhatsApp link formats
Source: WhatsApp Help Center, "How to use click to chat" — https://whatsapp.com/faq/en/general/26000030 (cited from search snippet; the page rendered without text in the browser).
- `https://wa.me/<number>`, full international format, no zeroes, brackets or dashes. Pre-filled text: `https://wa.me/<number>?text=<urlencoded>`.
- Other formats seen on real sites (third-party): `api.whatsapp.com/send`, `web.whatsapp.com`, `whatsapp://`. Trigger must cover all of them. Indonesian numbers: `62...`, not `08...`.

### H. WP Rocket "Delay JavaScript execution"
Sources: https://docs.wp-rocket.me/article/1349-delay-javascript-execution and https://docs.wp-rocket.me/article/1492-google-analytics-google-ads-tracking-issues
- Delays all scripts in the page HTML "until there is a user interaction", on the **File Optimization** tab.
- Official fix for tracking issues: under **One-click exclusions → Analytics & Ads**, tick **Google Analytics** and **Google Tag Manager** (targets `/gtm.js`, `/gtag/js`, etc.). Alternatives: "Excluded JavaScript Files" box, or `nowprocket` attribute.

## 2. Free-tier limits (checked 2026-10-08)

| Tool | Needed feature free today? | Account / card | Limits | Source |
|---|---|---|---|---|
| Google Tag Manager | Yes (Community templates, Preview, Publish) | Google account; no card | Not re-verified on a Google pricing page today | Unconfirmed (no official pricing page opened) |
| GA4 | Yes (events, key events, DebugView) | Google account; Marketer role or above | 30 key events per standard property | support.google.com/analytics/answer/13128484 |
| OpenAI Ads Manager | Account creation free; ads need billing to deliver | OpenAI login, business details, verification (Persona), card for billing | Can a data source/pixel be created before verification and billing? **Unconfirmed** | help.openai.com/en/articles/20001213 |
| OpenAI Ads Measurement Pixel template (openai) | Yes, gallery template, Apache 2.0 | None | None stated | GitHub repo + gallery |
| Stape OpenAI Ads Pixel template | Yes, gallery template | None for the web tag | One Pixel ID per page | stape.io helpdesk |
| Tag Assistant / GTM Preview | Yes | Google account | None stated | GTM help |
| OpenAI Ads Pixel Helper (Chrome, optional) | Yes, third-party, "not affiliated with OpenAI", ~779 users | None | Optional only | Chrome Web Store snippet |

Availability: Indonesia is in the self-serve Ads Manager country list since late September 2026 (bestmediainfo.com, gptadsai.com snippets; no official OpenAI country page opened → Unconfirmed on an official page). The account's legal entity must be registered in an available country (snippet).

## 3. Reader friction (top 10)

1. **Trigger never fires because Click URL is not enabled.** "GTM's built-in Click Variables are disabled by default... your trigger condition will never match." Fix: Variables → Configure → enable Click URL. Source: adnanagic.com / boei.help (search snippet + page). Official status unknown (check F).
2. **WhatsApp widget inside an iframe or built by JS.** "Standard GTM Link Click triggers will not detect clicks inside an iframe" (Elfsight, Join.chat etc.). Fix: widget pushes to dataLayer, or switch to **All Elements** for JS-built buttons. Sources: boei.help, respond.io ID help (snippet).
3. **Only `wa.me` covered.** Buttons use `api.whatsapp.com/send`, `web.whatsapp.com` or `whatsapp://`. Fix: Click URL **matches RegEx** `wa\.me|api\.whatsapp\.com|web\.whatsapp\.com|^whatsapp:`. Source: adnanagic.com snippet, boei.help.
4. **Tag fires in Preview but nothing in DebugView.** Wix forum: "all tags fired correctly in GTM Preview... nothing appeared in GA4 DebugView"; Shopify community: "No hits were sent by this tag". Causes: wrong Measurement ID, consent not granted, debug mode off. Sources: https://forum.wixstudio.com/t/ga4-via-gtm-on-wix-tags-fire-but-no-data-in-debugview/72133, https://community.shopify.dev/t/ga4-custom-events-not-sending-through-gtm-in-shopify-app/25858, official DebugView consent note.
5. **Pixel installed, Event Stream empty.** Causes: no `measure` call; wrong loader URL copied from blogs (`ads.openai.com/pixel.js` returns 403); CSP blocking `bzrcdn.openai.com` / `bzr.openai.com`. "Miss this and the failure is invisible." Source: https://www.searchintel.tech/blog/chatgpt-ads-conversion-tracking/ + official CSP section.
6. **Ads Manager shows 0 conversions although events arrive.** Event not matching the campaign's conversion event, or attached after traffic started (no backfill), or still inside the 24–48 h delay. Source: official Measure Results FAQ.
7. **WP Rocket delays GTM until the visitor interacts**, so quick clicks or test sessions miss events. Fix: One-click exclusions for Google Tag Manager. Source: official WP Rocket docs. (Also the user's own setup.)
8. **"Wait for Tags" side effects on link clicks.** Snippet: with Wait for Tags, gtm.js "will start mimicking the click (location.href = ...)" and calls preventDefault; disabling it fixed issues for some. For WhatsApp links opening a new tab/app this matters. Source: search snippet (wearefine.com / community). The user's own pitfall: ticking it asks for a page condition. → check G.
9. **Double pixel (template + Custom HTML)**, so events are sent twice. The official template initializes once per page ("idempotency", per ppc.land on the community template; the official README says event tags initialize the pixel themselves). Stape: "only one Pixel ID is supported on the page". Source: user's own setup + docs above.
10. **ChatGPT Ads traffic shows as Direct in GA4.** r/PPC summary: "Analytics filed demo requests as direct traffic." Fix: UTM on every ad using Landing page query parameters. Source: https://www.sprites.ai/blog/what-marketers-say-about-chatgpt-ads-reddit (summary of Reddit threads; snippet only).

Also from the user's own setup (to verify, no public source): **Page Viewed attached to the campaign as a conversion** (inflates Conversions); "user data" warning in Ads Manager (likely related to advanced matching; no official text found).

## 4. Competitor freebies

| # | Source | Lang / format | Promise | Depth / assets | Missing or outdated |
|---|---|---|---|---|---|
| 1 | conversiontracking.io, "ChatGPT Ads Conversion Tracking: How to Set It Up" (Jun 16, 2026) | EN blog | Pixel + GTM conversions | Custom HTML snippets, form submit, thank-you page, ecommerce, UTM tip, Event Stream test | No WhatsApp. Custom HTML instead of the official template. "Tools → Conversions" path likely outdated. Adds `currency: "USD"` to lead with no amount. No GA4 key event. |
| 2 | Stape helpdesk, "OpenAI Ads Pixel tag" (Aug 3, 2026) | EN docs | Install pixel via Stape template | Field-by-field config, Preview test | No WhatsApp, no GA4, example trigger is "subscription created". Leads to paid server-side Stape. |
| 3 | boei.help, "Track WhatsApp Button Clicks in GTM & GA4" (updated Aug 22, 2026) | EN blog | WA click → GA4 | Click vars, Just Links trigger, GA4 tag, DebugView, iframe caveats, honest "click ≠ conversation" | Says "Mark as conversion" (GA4 now uses key events). Regex misses `api.whatsapp.com`. No OpenAI. Upsells paid widget ($19/mo). |
| 4 | olakses.com, "Google Tag Manager Setup Panduan Conversion Tracking untuk Pemula" | ID blog | GTM for Google Ads conversions | Concepts, 5 steps, common issues | Mentions "Klik nomor WhatsApp" as a priority event but gives no WA steps. No GA4 key event, no OpenAI. Ends with agency consultation CTA. |
| 5 | searchintel.tech, "ChatGPT Ads Conversion Tracking Setup (2026)" | EN blog | Why conversions show 0 | Correct loader URL, CSP, 3 checks | No GTM steps, no WhatsApp, no GA4. |

No Indonesian-language guide on ChatGPT Ads conversion tracking was found (searches: "panduan tracking whatsapp ChatGPT Ads pixel OpenAI GTM", "ChatGPT Ads pixel konversi cara pasang Indonesia"). Shopify apps exist for the pixel, but not for WhatsApp clicks.

## 5. The A5 angle

1. **One WhatsApp trigger, two destinations.** The only guide found that sends a WhatsApp click to both GA4 (`whatsapp_click` key event) and OpenAI (`lead_created`) from a single GTM trigger. Competitors cover one side only.
2. **Official OpenAI template, zero code.** Uses "OpenAI Ads Measurement Pixel" by openai from the gallery. Competitors use Custom HTML or Stape. This also avoids the wrong-loader-URL and double-pixel problems.
3. **Current UI, in Indonesian.** Verified Ads Manager path (Conversions as its own menu), GA4 "peristiwa utama" (not the old "conversion"), and ID/EN GTM label pairs. Competitors are English or outdated.
4. **Ready-to-paste assets.** WA regex covering wa.me, api.whatsapp.com, web.whatsapp.com and `whatsapp:`; naming sheet (tag/trigger names); UTM pattern built on the official `{campaign_id}`, `{ad_group_id}`, `{ad_id}` macros; a 2-minute test checklist (Preview → DebugView → Event Stream).
5. **Troubleshooting from a real setup.** WP Rocket delay, Wait for Tags, double pixel, Page Viewed attached as a conversion, the server-to-server warning explained, plus the honest limits: click ≠ chat sent, and conversion bidding must be chosen when the campaign is created.

## 6. Open items and the early walkthrough

Facts not confirmed from official docs or a live public page:

| # | Open item | Changes how a step is written? |
|---|---|---|
| A | Current Ads Manager path and labels: where Conversions sits in the menu, Create → Data source → Type Web, where the Pixel ID shows | **Yes** |
| B | Can a data source/pixel be created before business verification (NPWP) and billing are done? | **Yes** (prerequisites + promise) |
| C | Conversion Event form: label for lead type ("Lead"?), data source picker, and can it be attached to an existing clicks campaign in the UI? | **Yes** |
| D | Does `page_viewed` appear in Event Stream with only init (no measure call)? Decides whether a separate Page viewed tag is needed | **Yes** |
| E | Gallery search "OpenAI" in a container shows "OpenAI Ads Measurement Pixel" by openai; permissions shown on add | **Yes** |
| F | In a fresh workspace, is Click URL already enabled, or must it be turned on in Variables → Configure? | **Yes** |
| G | Wait for Tags: does ticking it force a page condition, and does the WA click still record when the link opens a new tab / the app? | **Yes** |
| H | Real ID interface labels in GTM and GA4 (help pages are AI-translated) | Labels only |
| I | Does Ads Manager offer an Indonesian interface? | Labels only |
| J | Where "Landing page query parameters" sits in the UI and whether macros fill in | **Yes** (UTM asset) |
| K | Exact text of the "server-to-server" and "user data" warnings | Labels only |

Early walkthrough, run on the Gwenchana ChatGPT Ads account + a test GTM workspace:

```text
[ ] A. Ads Manager: open the Conversions area from the left menu → screenshot the menu and the Create options (Data source / Conversion event), plus where Pixel ID and "View Code" appear
[ ] B. Report: was the data source created while TIN/NPWP verification was still pending and before billing was complete? (yes / no / don't remember)
[ ] C. Create → Conversion event → screenshot the form (type list, data source picker). Then Edit campaign on the test campaign → is there a field to attach conversion events? screenshot
[ ] D. GTM Preview with ONLY an OpenAI tag that has "Send a measurement event" unchecked → Event Stream: does page_viewed appear? (yes / no)
[ ] E. GTM → Templates → Tag Templates → Search gallery → type "OpenAI" → screenshot the list and the permissions dialog for "OpenAI Ads Measurement Pixel"
[ ] F. New workspace → Variables → Configure: are Click URL / Click Text already ticked? screenshot
[ ] G. Trigger "Just Links" → tick Wait for Tags → screenshot what GTM asks for. Test one WA click with it on and off: does whatsapp_click reach DebugView both times?
[ ] H. Switch Google account language to Indonesian once → screenshot GTM trigger editor and GA4 Admin → Tampilan data (Peristiwa / Peristiwa utama / DebugView)
[ ] I. Ads Manager Settings: is Indonesian offered as interface language? (yes / no)
[ ] J. Edit ad group → screenshot "Landing page query parameters" and the macro picker
[ ] K. Screenshot the exact text of the server-to-server and user data warnings
```

Answers go into `05-stepcheck.md` under "Pre-draft checks" as `USER`. Skipped items will be marked `[VERIFY]` in /outline.

## Sources
- https://help.openai.com/en/articles/20001409-conversion-measurement
- https://help.openai.com/en/articles/20001214-measure-results
- https://help.openai.com/en/articles/20001213-ads-manager-account-setup
- https://help.openai.com/en/articles/20001224-quickstart-launch-your-first-campaign
- https://developers.openai.com/ads/conversion-tracking
- https://developers.openai.com/ads/measurement-pixel
- https://developers.openai.com/ads/supported-events
- https://github.com/openai/ads-measurement-pixel-gtm-template
- https://tagmanager.google.com/gallery/#/?filter=openai
- https://stape.io/helpdesk/documentation/openai-ads-pixel-tag
- https://support.google.com/tagmanager/answer/7679320 (hl=en, hl=id)
- https://support.google.com/tagmanager/answer/13034206 (hl=en, hl=id)
- https://support.google.com/tagmanager/answer/7182738?hl=en
- https://support.google.com/analytics/answer/13128484 (hl=en, hl=id)
- https://support.google.com/analytics/answer/7201382?hl=en
- https://support.google.com/analytics/answer/13316687 (snippet)
- https://whatsapp.com/faq/en/general/26000030 (snippet)
- https://docs.wp-rocket.me/article/1349-delay-javascript-execution
- https://docs.wp-rocket.me/article/1492-google-analytics-google-ads-tracking-issues
- https://conversiontracking.io/blog/openai-chatgpt-ads-conversion-tracking/
- https://www.searchintel.tech/blog/chatgpt-ads-conversion-tracking/
- https://ppc.land/gtm-template-fills-the-gap-left-by-openais-ads-pixel-launch/
- https://boei.help/blog/track-whatsapp-clicks-google-tag-manager/
- https://olakses.com/google-tag-manager-setup-panduan-conversion-tracking-untuk-pemula/
- https://adnanagic.com/blog/track-whatsapp-clicks-google-tag-manager/ (snippet)
- https://respond.io/id/help/capture-leads/how-to-attribute-whatsapp-conversations-to-non-meta-ads (snippet)
- https://forum.wixstudio.com/t/ga4-via-gtm-on-wix-tags-fire-but-no-data-in-debugview/72133 (snippet)
- https://community.shopify.dev/t/ga4-custom-events-not-sending-through-gtm-in-shopify-app/25858 (snippet)
- https://www.sprites.ai/blog/what-marketers-say-about-chatgpt-ads-reddit (snippet, Reddit summary)
- https://chromewebstore.google.com/detail/flikhpmmgnmahgnjkcdgonpacaleemah (snippet)
- https://bestmediainfo.com/mediainfo/advertising/chatgpt-ads-expands-across-indonesia-singapore-thailand-and-four-more-markets-12571053 (snippet)
