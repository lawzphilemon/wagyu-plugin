Free Guide · Competitor Research × Claude

# Research 3 competitors and their Meta ads in 45 minutes with free Claude

Prices, claims, and the ads they're running right now, in one Google Sheet plus 3 ideas you can test straight away. 100% free tools, no paid extension.

30–45 min · Beginner · Tool cost: $0

<!-- wg:box -->
**You'll finish with:**

- A Competitor Snapshot in Google Sheets for 3 competitors
- Their live Meta ads: angles, start dates, and where the ads send people
- 3 gaps and 3 test ideas for your brand

**It worked if:** every row has a source link and a check date, and every test idea names the competitor ad it came from.

On Claude Pro? Claude in Chrome can read your tabs directly and speeds up steps 2 and 4. This guide doesn't need it; that extension is for paid plans only.
<!-- /wg:box -->

## Research in 5 steps

### Step 1 — Pick 3 competitors

Choose the brands that sell most like you: same category, price range, and buyers. The biggest name in your category isn't always the most relevant one.

1. Write down 3 competitors, their websites, and their Instagram or Facebook account names.
2. Open Google Sheets and create an empty sheet called **Competitor Snapshot**.

**You should see:** a list of 3 competitors and an empty sheet ready to fill.

### Step 2 — Pull their website data

1. In Claude, start a new chat, click **+** at the bottom left, and make sure **Web search** is checked.
2. Copy **Prompt A** below, fill in the first competitor's name and website, and send it.
3. Repeat for the second and third competitor, one message each.

**You should see:** a product table with price, main claim, and a source link on every row.

> **Watch out:** Check the currency. In our test, Claude took dollar prices from a site's international version. If a competitor only sells on a marketplace like Shopee, Claude can't read the page. Open the shop, select all (Ctrl+A), copy, and paste the text into Claude.

[SCREENSHOT: screenshots/langkah-2-web-search.png]

### Step 3 — Find the competitor in Meta Ad Library

Ad Library shows every ad currently running on Facebook and Instagram. Anyone can open it without logging in.

1. Open `facebook.com/ads/library` and choose your country.
2. Click **Ad category**, choose **All ads**, then **APPLY**. The search box only works after this.
3. Type the competitor's name and pick the brand under **Advertisers**, not the "Search this exact phrase" line.

**You should see:** the brand's page with the number of active ads above the list, for example "~670 results".

> **Watch out:** One brand can have several Pages, and many resellers use the brand name. Pick the one with the most followers and the official Instagram handle. Blank page or errors? Turn off your ad blocker for facebook.com.

[SCREENSHOT: screenshots/langkah-3-ad-library-advertiser.png]

### Step 4 — Copy the ad text and let Claude analyze it

Claude can't open Ad Library links because Meta blocks automated access. You can still copy the text.

1. Scroll slowly until about 20 to 30 ads have loaded.
2. Press Ctrl+A, then Ctrl+C to copy all the text on the page.
3. In Claude, turn **Web search** off, copy **Prompt B**, paste the Ad Library text under it, and send.

**You should see:** the number of active ads, the 3 most-used angles, the longest-running ad, and where the ads send people.

> **Watch out:** Ad Library doesn't show budgets or results. An ad that has run for a long time is a hint that it might be working, not proof.

### Step 5 — Build the Competitor Snapshot and 3 test ideas

1. Once all three competitors are done, send **Prompt C** in the same chat.
2. Select only the table, copy it, and paste it into cell A1 of your sheet.
3. Copy the gaps and test ideas below the table.

**You should see:** one row per competitor, each column in its own cell, with source links and a check date.

> **Watch out:** If Claude's opening sentence gets copied too, it lands in the first row. Start your selection at the table's column headers.

[SCREENSHOT: screenshots/langkah-5-paste-sheets.png]

**Checkpoint**

- [ ] 3 competitors with website data and source links
- [ ] Live ads analyzed for all three
- [ ] Competitor Snapshot in Google Sheets with a check date
- [ ] 3 test ideas, each naming the ad it's based on

> You now know what your competitors are running. Those test ideas only pay off once they're turned into ads and tested every week. [Email the Gwenchana team](CTA_URL)

## Your prompts

**Prompt A: Website data** (Step 2, one competitor per message)

```text
Search the web and read [COMPETITOR NAME]'s product pages on [COMPETITOR WEBSITE]. Take up to 5 main products.
For each product give: product name, price in local currency, main claim, and the URL of the source page.
Rules:
- Use the site version for my country. If the price is in another currency, name the currency and don't convert it.
- Don't guess. If a price or claim isn't on the page, write "not found".
Show it as a table.
```

**Prompt B: Ad analysis** (Step 4, one competitor per message)

```text
Below is text from Meta Ad Library for the advertiser [COMPETITOR NAME], active ads in my country. Analyze only this text. Don't guess.
1. Number of active ads (the "results" number above the list).
2. The 3 most frequent angles or messages. For each, give one example line from an ad and its Library ID.
3. The longest-running ad: Library ID and its "Started running on" date.
4. Where the ads send people (website, marketplace, WhatsApp, and so on) and the most used CTA.
Remember: Ad Library shows no budget or results. Describe long-running ads as a hint, not proof.

[PASTE AD LIBRARY TEXT HERE]
```

**Prompt C: Competitor Snapshot and test ideas** (Step 5)

```text
Combine all results in this chat into one Competitor Snapshot table, one row per competitor, with these columns:
Competitor | Main products and prices | Main claim | Active ads | Top ad angles | Longest-running ad (date) | Where ads send people | Source links | Check date
Check date: [TODAY'S DATE].
After the table, write 3 gaps the competitors leave open and 3 ad test ideas for my brand, [YOUR BRAND], which sells [YOUR PRODUCT]. Each idea must name the competitor and the Library ID of the ad it's based on.
Start your answer with the table, no opening sentence.
```

## Quick fixes

<!-- wg:details -->

**1. Claude says it can't read the page**
Marketplace shops, Ad Library, and sites built with JavaScript often can't be read by Claude. Open the page yourself, select all, copy, and paste the text into Claude. If the text is messy, upload a screenshot with **+** > **Add files or photos**.

**2. Ad Library results mix in other brands or resellers**
You searched a keyword instead of picking an advertiser. Type the brand again and pick it under **Advertisers**. Check the follower count and the official handle.

**3. You hit the Free plan's usage limit**
Long pages and many competitors in one chat use up the limit fast. Send one competitor per message, turn **Web search** off while pasting text, and wait for the reset. On the Free plan, limits reset every five hours.

<!-- wg:cta -->
## What's next: from research to tested ads

Your snapshot shows which angles competitors use and which gaps you could fill. What a sheet can't do: turn those ideas into creative, test them every week on a controlled budget, and read the results with tracking you can trust.

Gwenchana turns research like this into Meta Ads campaigns that get tested every week, starting from the Starter tier.

Not advertising on Meta yet, or still validating your product? Run this research first and repeat it monthly. Over the next week we'll email you prompts for reading competitor pricing and promos, 7 deeper research prompts, and a creative brief template built from competitor ads.

Want to talk first? Email info@gwenchana.digital with your brand and the ads you're running.

[Email Gwenchana about Meta Ads](CTA_URL)

---

Checked on September 28, 2026. Meta and Claude change their screens often. If something looks different, start with the quick fixes.
