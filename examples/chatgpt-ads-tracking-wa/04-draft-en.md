Free Guide · ChatGPT Ads × WhatsApp

# Track WhatsApp clicks from ChatGPT ads in GA4 and OpenAI Ads in 60 minutes

For business owners and marketers who get their leads through WhatsApp. One GTM trigger, two destinations, no code. 100% free tools; ad budget separate.

45–60 min · Intermediate · Tool cost: $0

<!-- wg:box -->
**What you end up with:**

- A GTM trigger that catches every WhatsApp link format
- A `whatsapp_click` event in GA4, marked as a key event
- The OpenAI pixel, installed with OpenAI's official template, sending `page_viewed` and `lead_created`, with Lead Created attached to your campaign
- A ready-to-paste UTM pattern for ChatGPT Ads campaigns

**How you know it worked:** you click your WhatsApp button once, then `whatsapp_click` shows up in GA4 DebugView and `lead_created` shows up in Ads Manager → Conversions → Event Stream within a few minutes.

One honest note up front: this tracks the button click, meaning the intent to get in touch. Whether a chat was actually sent happens inside WhatsApp, and GTM can't see it.
<!-- /wg:box -->

<!-- wg:cols -->
**This is for you if:**

- Your main leads come in through a WhatsApp button on your website
- You run, or plan to run, ChatGPT Ads and want to know which ads lead to chats
- You have admin access to GTM and GA4
<!-- wg:col -->
**Not for you yet if:**

- Your site doesn't use Google Tag Manager. Install it first, then come back.
- You need data on chats sent or deals closed. That takes the WhatsApp Business API or a CRM.
- You need server-side tracking (Conversions API). That's covered in a separate guide.
<!-- /wg:cols -->

## The tools you'll use, all free

| Tool | Used for | Free limit (checked Oct 8, 2026) | Account |
|---|---|---|---|
| Google Tag Manager | The trigger and all tags | Free, up to 3 workspaces per container | Google account, container already on your site |
| Google Analytics 4 | `whatsapp_click` event, key event, DebugView | Free, up to 30 key events per property | Marketer role or higher |
| OpenAI Ads Manager | Pixel, conversion event, Event Stream | Creating the account and data source is free. Ads only run after verification and billing are done | OpenAI Ads account |
| **OpenAI Ads Measurement Pixel** template (by openai) | Installing the pixel without code | Free, OpenAI's official template in the GTM Community Template Gallery | Not needed |
| Tag Assistant (GTM Preview) | Testing before you publish | Free | Google account |

Before you start, make sure you have three things: GTM installed with GA4 running through it, a WhatsApp button that is a regular link, and an OpenAI Ads Manager account.

About OpenAI Ads verification: we created our data source before our tax ID and billing were done (October 2026), so you can work through this whole guide while verification is pending. Business accounts must enter a tax ID (NPWP in Indonesia); personal accounts don't. Both still need identity verification before ads can run. If Ads Manager asks for identity verification first, finish that before Step 1.1.

The guide has three phases: Ads Manager (about 15 minutes), GTM and GA4 (about 20 minutes), then the OpenAI pixel and testing (about 20 minutes).

<!-- wg:gate -->

## Phase 1: set up Ads Manager (about 15 minutes)

By the end of this phase you have your Pixel ID, a Lead created conversion event attached to your campaign, and UTMs on your ad links.

### Step 1.1 — Copy your Pixel ID

The Pixel ID connects your website to your ad account. You'll paste it into GTM in Phase 3.

1. In Ads Manager, click **Conversions** in the left sidebar.
2. Open the **Data Source** tab.
3. Copy the code shown under your data source's name. That's your Pixel ID.
4. No data source yet? Click **+ Create**, choose **Data Source**, and follow the dialog for your website. In the table, a website data source shows the type **Web**.

**You should see:** your Pixel ID copied. It's a string of letters and numbers.

> **Watch out:** Many tutorials say "Tools → Conversions". That path is outdated: Conversions now has its own item in the sidebar.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection-scaled.png | Conversions page in OpenAI Ads Manager with the Create menu: Data Source and Conversion Event]

### Step 1.2 — Create the Lead created conversion event

This tells Ads Manager to count `lead_created` from your website as a conversion.

1. Click **+ Create**, then choose **Conversion Event**.
2. In the **Create custom conversion** dialog, set **Data source** to your data source.
3. Under **Base event**, choose **Lead created**.
4. Fill in **Conversion name**, up to 30 characters. There's a suggested name in Asset B.
5. Click **Create**.

**You should see:** Lead Created listed in the **Conversion Events** tab.

> **Watch out:** The dialog title says "custom" even though Lead created is a standard event. Ignore it. Don't pick App installed or App opened, because the website pixel doesn't support them.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection1-scaled.png | Create custom conversion dialog in Ads Manager: Data source, Base event, Conversion name]

### Step 1.3 — Attach Lead Created to your campaign

Creating a conversion event doesn't attach it to any campaign. This is the step people miss most often.

1. Go to **Campaigns**, click ⋯ on your campaign's row, then choose **Edit Campaign**.
2. Scroll to **Conversion event** and choose **Lead Created**.
3. If Page Viewed is attached too, remove it with the ✕ button.
4. Click **Save**.

No campaign yet? Choose Lead Created when you create it.

**You should see:** in the Conversion Events tab, Lead Created shows "Used by 1 campaign".

> **Watch out:** Attach Lead Created before your ads go live. Clicks that happen before the event is attached aren't counted later. We created ours half a day after our ads started, and the clicks from those first hours never made it into the count. Don't attach Page Viewed as a conversion: the Conversions column adds up every attached event, so page views get counted too.

[SCREENSHOT: Conversion event field in Edit Campaign set to Lead Created]

### Step 1.4 — Add UTMs with Tracking parameters

Without UTMs, ChatGPT ad traffic often lands in GA4 as Direct. You only need to set this once, at campaign level.

1. Still in **Edit Campaign**, find **Tracking parameters**.
2. Paste the string from Asset C and replace `<campaign-name>` with your campaign's name.
3. Click **Save**.

**You should see:** the UTM string saved on the campaign.

> **Watch out:** OpenAI's Help Center calls this "Landing page query parameters", but the label in Ads Manager is **Tracking parameters**. Parameters set at the Ad URL, Ad, or Ad group level override the campaign level. The `chatgpt_ads` source only shows up in GA4 after real ad clicks.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection2-scaled.png | Tracking parameters field in Edit Campaign with the supported placeholders]

**Checkpoint**

- [ ] Pixel ID copied
- [ ] Lead Created exists and shows "Used by 1 campaign"
- [ ] Page Viewed is not attached as a conversion
- [ ] Tracking parameters filled in

## Phase 2: send WhatsApp clicks to GA4 (about 20 minutes)

This phase builds one WhatsApp trigger that two tags will share: GA4 now, OpenAI in Phase 3.

### Step 2.1 — Turn on the Click URL variable

The WhatsApp trigger reads the address of the clicked link. Without this variable, the trigger never matches and stays silent.

1. In GTM, open **Variables**.
2. In the **Built-In Variables** section, click **Configure**.
3. Tick **Click URL**.

**You should see:** Click URL listed under Built-In Variables.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection3-scaled.png | Configure Built-In Variables panel in GTM with Click URL and Click Text ticked]

### Step 2.2 — Create the WhatsApp click trigger

WhatsApp links come in several formats: wa.me, api.whatsapp.com, web.whatsapp.com, and whatsapp://. The regex in Asset A catches all of them.

1. Open **Triggers**, then click **New**.
2. Click **Trigger Configuration** and choose **Just Links**.
3. Under **This trigger fires on**, choose the **Some** option (some link clicks).
4. Set the condition: `Click URL`, operator `matches RegEx`, then paste the regex from Asset A.
5. Name it `WA - WhatsApp Click`, then click **Save**.

**You should see:** the `WA - WhatsApp Click` trigger saved.

> **Watch out:** You don't need **Wait for Tags** or **Check Validation** for this guide, so leave them unticked. Buttons from chat widgets that load inside an iframe won't be caught by this trigger; see Troubleshooting.

[SCREENSHOT: Just Links trigger configuration with the regex condition]

### Step 2.3 — Create the GA4 whatsapp_click tag

1. Open **Tags**, then click **New**.
2. Choose **Google Analytics: GA4 Event**.
3. Fill in **Measurement ID** with your GA4 ID.
4. Set **Event Name** to `whatsapp_click`.
5. Under **Triggering**, choose `WA - WhatsApp Click`.
6. Name it `GA4 - whatsapp_click`, then click **Save**.

**You should see:** the `GA4 - whatsapp_click` tag saved.

> **Watch out:** GA4 event names are case sensitive, can't contain spaces, and max out at 40 characters. Type exactly `whatsapp_click`.

[SCREENSHOT: GA4 Event tag configuration with Event Name whatsapp_click]

### Step 2.4 — Mark whatsapp_click as a key event

A key event makes WhatsApp clicks read as an important outcome in GA4 reports. You can mark it before the first event arrives.

1. In GA4, open **Admin**, then under **Data display** click **Events**.
2. Click **+ Create event**.
3. Enter the name `whatsapp_click`, then switch on **Mark as key event**.
4. Click **Create**.

If `whatsapp_click` already appears in your events list, just click the star next to it.

**You should see:** `whatsapp_click` listed as a key event.

> **Watch out:** GA4 also logs a built-in `click` event for the same click. We saw both in DebugView. Mark `whatsapp_click` as the key event, not `click`. Standard reports can take up to 24 hours to show a new key event.

[SCREENSHOT: GA4 Create event form with Mark as key event switched on]

**Checkpoint**

- [ ] Click URL is on
- [ ] Trigger `WA - WhatsApp Click` saved
- [ ] Tag `GA4 - whatsapp_click` saved
- [ ] `whatsapp_click` marked as a key event

## Phase 3: install the OpenAI pixel, test, and publish (about 20 minutes)

This phase uses OpenAI's official template from the GTM Gallery, so you don't paste any code. The WhatsApp trigger from Phase 2 gets reused for the Lead created tag.

### Step 3.1 — Add OpenAI's official template

1. In GTM, open **Templates**.
2. In the **Tag Templates** section, click **Search Gallery**.
3. Type "OpenAI", then choose **OpenAI Ads Measurement Pixel** by **openai**.
4. Click **Add to workspace** and approve the permissions it asks for.

**You should see:** OpenAI Ads Measurement Pixel listed under Tag Templates.

> **Watch out:** The gallery has several OpenAI templates, including ones by Stape and Webaround. Pick the one by openai. The Stape template works too (we used it until October 2026), but its fields differ from this guide.

[SCREENSHOT: "OpenAI" search results in the Community Template Gallery]

### Step 3.2 — Save your Pixel ID as a constant variable

With this variable, you paste the Pixel ID once and reuse it in every OpenAI tag.

1. Open **Variables**.
2. Under **User-Defined Variables**, click **New**, then choose **Constant**.
3. Paste the Pixel ID from Step 1.1.
4. Name it `Const - OpenAI Pixel ID`, then click **Save**.

**You should see:** `Const - OpenAI Pixel ID` listed under User-Defined Variables.

### Step 3.3 — Create the Page viewed tag

1. Open **Tags**, click **New**, then choose the **OpenAI Ads Measurement Pixel** template.
2. Under **Pixel ID**, choose the `Const - OpenAI Pixel ID` variable with the variable icon next to the field.
3. Leave **Send a measurement event when this tag fires** ticked.
4. Under **Event name**, choose **Page viewed**.
5. Choose the **All Pages** trigger.
6. Name it `OpenAI - Page viewed`, then click **Save**.

**You should see:** the `OpenAI - Page viewed` tag saved.

> **Watch out:** You don't need a separate "base" tag. According to OpenAI's template documentation, every event tag loads the pixel itself.

[SCREENSHOT: OpenAI Page viewed tag configuration, Pixel ID blurred]

### Step 3.4 — Create the Lead created tag

1. Create a new tag with the **OpenAI Ads Measurement Pixel** template.
2. Under **Pixel ID**, choose the `Const - OpenAI Pixel ID` variable with the variable icon next to the field.
3. Under **Event name**, choose **Lead created**.
4. Choose the `WA - WhatsApp Click` trigger.
5. Name it `OpenAI - Lead created`, then click **Save**.

**You should see:** the `OpenAI - Lead created` tag saved.

> **Watch out:** Leave **Amount** and **Currency** empty. A WhatsApp click has no money value yet, and if you do fill it in, the amount must be in the currency's smallest unit.

[SCREENSHOT: OpenAI Lead created tag configuration with the WA - WhatsApp Click trigger]

### Step 3.5 — Pause any old OpenAI tags

If you installed the OpenAI pixel before through Custom HTML or another template, that tag has to be switched off.

1. In **Tags**, click the name of the old tag that loads the OpenAI pixel.
2. Click the three-dot icon in the top right, then choose **Pause**.
3. Click **Save**. The change takes effect once you publish in Step 3.7.

**You should see:** only `OpenAI - Page viewed` and `OpenAI - Lead created` active.

> **Watch out:** A double pixel sends every event twice, and your Ads Manager numbers stop being trustworthy.

### Step 3.6 — Test in Preview

Preview confirms the trigger and both tags work before the change goes live. Open GA4 in a separate tab first.

1. In GTM, click **Preview**, enter your website URL, then click **Connect**.
2. In the website window that opens, click your WhatsApp button once.
3. In Tag Assistant, select the **Link Click** event. `GA4 - whatsapp_click` and `OpenAI - Lead created` should both show "Fired 1 time".
4. In GA4, open **Admin**, then **DebugView**. Look for `whatsapp_click`.

**You should see:** both tags "Fired 1 time" in Tag Assistant, and `whatsapp_click` in DebugView.

> **Watch out:** GA4 also shows a `click` event for the same click. That's normal.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection4-scaled.png | GA4 DebugView showing the whatsapp_click and click events]

### Step 3.7 — Publish and test again on your live site

Once published, the OpenAI pixel runs on your real website. The final check happens in Event Stream.

1. In GTM, click **Submit**.
2. Choose **Publish and Create Version**, name the version, then click **Publish**.
3. In Ads Manager, open **Conversions**, then the **Event Stream** tab. Make sure polling is on (the button reads **Pause polling**).
4. Open your website in a normal tab without Preview, then click your WhatsApp button.
5. In Event Stream, look for `lead_created` with API Channel `pixel_sdk`.

**You should see:** `lead_created` in Event Stream. In our account, it arrived within the same minute as the test click.

> **Watch out:** Event Stream only shows events from roughly the last 15 minutes. If you waited too long, click the WhatsApp button again. The Conversions column in campaign reports takes 24–48 hours to fill in, so use Event Stream for testing.

[SCREENSHOT: screenshots/Ads-Manager-Slide-selection5-scaled.png | Ads Manager Event Stream showing lead_created with API Channel pixel_sdk]

**Checkpoint**

- [ ] `whatsapp_click` shows up in GA4 DebugView
- [ ] `lead_created` shows up in Event Stream
- [ ] Only two OpenAI tags are active
- [ ] The container is published

> Your tracking is live. The next job is reading the data every week and deciding which ads to keep. If you'd rather hand that part off, [see Gwenchana's Digital Advertising services](CTA_URL).

## Ready-to-paste assets

### Asset A — WhatsApp trigger regex

Used in Step 2.2, with the condition `Click URL` `matches RegEx`. The regex is lowercase, matching how WhatsApp links are normally written.

```text
wa\.me|api\.whatsapp\.com|web\.whatsapp\.com|^whatsapp:
```

### Asset B — Naming convention

Consistent names make life easier for anyone who opens your container later.

```text
Trigger           WA - WhatsApp Click
GA4 tag           GA4 - whatsapp_click
OpenAI tag 1      OpenAI - Page viewed
OpenAI tag 2      OpenAI - Lead created
Variable          Const - OpenAI Pixel ID
Conversion name   Lead WhatsApp
```

### Asset C — UTMs for Tracking parameters

Used in Step 1.4. Replace `<campaign-name>` with your campaign's name in lowercase with no spaces, for example `home-renovation-oct26`. Ads Manager fills in the parts in curly braces automatically when someone clicks your ad.

```text
utm_source=chatgpt_ads&utm_medium=cpc&utm_campaign=<campaign-name>&utm_content={ad_id}&utm_term={ad_group_id}
```

We use `chatgpt_ads` rather than `chatgpt` so ad traffic stays separate from organic ChatGPT traffic in GA4. Other placeholders Ads Manager supports: `{campaign_id}`, `{ad_account_id}`, and `{oppref}`.

### Asset D — 2-minute test checklist

Run it every time you change your WhatsApp button or your GTM container.

```text
[ ] GTM Preview → Connect → click the WhatsApp button
[ ] Tag Assistant: Link Click event, GA4 and OpenAI tags "Fired 1 time"
[ ] GA4 DebugView: whatsapp_click appears
[ ] Submit → Publish
[ ] Ads Manager Event Stream: polling on
[ ] Click the WhatsApp button on the live site → lead_created appears (pixel_sdk)
```

## Troubleshooting: the problems that come up most

<!-- wg:details -->

**The trigger doesn't fire when the WhatsApp button is clicked**

The most common cause: the Click URL variable is off, so GTM can't read the link's address. Turn it on in Step 2.1, then test again in Preview.

**Buttons from chat widgets (Elfsight, Join.chat, and similar) aren't caught**

Many widgets load their button inside an iframe, and GTM link triggers can't see clicks inside an iframe. Your options: ask the widget to send an event to the dataLayer, or replace the widget with a regular link button. If the button is built with JavaScript and no iframe, try an **All Elements** trigger with the same condition.

**Some WhatsApp clicks aren't recorded**

One of your buttons probably uses a link format outside the regex. Click that button in Preview, then check the Click URL value in the **Variables** tab of Tag Assistant. Make sure Asset A covers that format.

**The tag shows "Fired" in Preview, but DebugView is empty**

Check the Measurement ID in your GA4 tag and make sure it matches the property you have open. If your site uses a cookie banner, events don't appear in DebugView until Analytics cookies are accepted. Accept the banner, then test again.

**The pixel is installed, but Event Stream is empty**

First, make sure the `OpenAI - Lead created` tag actually shows "Fired" in Tag Assistant. If it fired and Event Stream is still empty, your site may use a Content Security Policy that blocks OpenAI's domains. Ask your developer to allow `bzrcdn.openai.com` and `bzr.openai.com`. Snippets copied from blogs sometimes use the wrong loader URL. The official template avoids that problem.

**Events reach Event Stream, but the Conversions column stays at 0**

There are three possibilities: Lead Created isn't attached to the campaign (Step 1.3), it was attached after the clicks happened so they weren't counted, or the data is still inside the 24–48 hour delay. To see numbers per event, click the columns icon next to the filter icon, choose **Customize columns**, tick **Lead Created** under **Events**, then click **Save changes**.

**Events go missing on a WordPress site running WP Rocket**

WP Rocket's **Delay JavaScript execution** holds GTM back until the visitor interacts with the page. Quick clicks or short tests may not get recorded. Open WP Rocket, go to the **File Optimization** tab, and under **One-click exclusions** in **Analytics & Ads**, tick **Google Tag Manager** and **Google Analytics**.

**One click is counted twice**

Almost always a double pixel: the new template running alongside an old Custom HTML tag. Repeat Step 3.5.

**Two warnings appear in Conversions → Diagnostics**

Both showed up in our account, and both are expected for a WhatsApp click pixel setup. "No recent server-to-server events" appears because this setup only uses the browser pixel, without the Conversions API. "Some events are missing user data" (Email coverage and External ID coverage at 0%) appears because a WhatsApp click carries no email or customer ID. Tracking still works. Clearing them takes the Conversions API, which is covered in the next guide.

**GA4 and Ads Manager show different numbers**

That's normal. They use different attribution, time zones, and cookie rules, and ad blockers affect GA4. OpenAI itself notes that a difference doesn't necessarily mean an error. Compare the same date range and time zone before drawing conclusions.

<!-- wg:cta -->
## Once tracking is live: reading the data every week

WhatsApp click data only pays off when someone reads it and acts on it every week. You need to know which ad groups and context hints bring in clicks, when to pause an ad, and when to switch to conversion bidding. That last decision has to be made when you create the campaign, because a campaign's objective can't be changed afterward. Then there's the part GTM can't do at all: connecting a WhatsApp click to a chat that actually became a client.

Gwenchana's Digital Advertising service handles that part: campaign strategy and setup, ad creation, targeting, performance monitoring and optimization, and monthly analytics reports.

Not a fit yet if you only want to try ChatGPT Ads once with a small budget, or don't have a regular monthly ad budget. Run this guide and read the data yourself first.

[See Digital Advertising services](CTA_URL)

---

The steps, menu labels, and free limits in this guide were checked on October 8, 2026 in Gwenchana's own Ads Manager, GTM, and GA4 accounts. Written by Lawrence, Gwenchana.
