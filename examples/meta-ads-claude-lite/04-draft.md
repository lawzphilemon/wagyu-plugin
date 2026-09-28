Free Guide · Meta Ads × Claude

# Connect Claude to your Meta Ads account in 15 minutes

Real performance reports from live data, read-only so Claude can't touch your budget. 100% free tools. Your ad budget stays separate.

15 min · Beginner friendly · Tool cost: $0

<!-- wg:box -->
**You'll finish with:**

- Claude connected to Meta's official Ads connector
- A read-only lock on Meta's side, so Claude can look but not change
- Your first performance report, from a prompt you can reuse every week

**It worked if:** Claude answers the report prompt with your real campaign numbers.
<!-- /wg:box -->

## Connect in 5 steps

### Step 1 — Add Meta's connector in Claude

1. In Claude, open **Customize** in the left menu, then **Connectors**.
2. Click **+** at the top right of the Connectors panel and choose **Add custom connector**.
3. Type `Meta Ads` in the first field and paste this address into the second:

```text
https://mcp.facebook.com/ads
```

4. Leave **Advanced settings** empty and click **Add**.

**You should see:** Meta Ads under **Not connected**, with a **CUSTOM** badge.

> **Watch out:** Claude's free plan allows one custom connector. If you already have one, remove it first.

[SCREENSHOT: screenshots/step-1.3-connector-form.png]

### Step 2 — Sign in with Facebook and pick one portfolio

1. Click **Meta Ads**, then **Connect**.
2. Sign in with the Facebook account that manages your ad account. Nothing opens? Allow pop-ups for claude.ai and click **Connect** again.
3. When Meta asks which business portfolios to share, tick only the one you'll use.

**You should see:** Meta Ads marked as connected.

> **Watch out:** [VERIFY] Claude can reach every portfolio you tick, client accounts included. Agencies: tick one.

[SCREENSHOT: portfolio selection screen]

### Step 3 — Check that Meta has switched your account on

Meta is enabling this account by account. This check takes ten seconds and saves you from debugging a setup that's already fine.

1. Start a new chat, click **+** at the bottom left, open **Connectors**, and switch **Meta Ads** on.
2. Paste the **account check** prompt from below and send it.

**You should see:** your ad accounts listed with `is_ads_mcp_enabled: true`.

> **Watch out:** [VERIFY] If it says `false`, your setup is fine. Meta just hasn't enabled that account yet. See quick fix 1.

[SCREENSHOT: account check answer]

### Step 4 — Lock it to read-only

Signing in also gives Claude permission to edit campaigns. One setting on Meta's side takes that away. You need full control of the business portfolio.

1. In Meta Business Suite, open **Settings**, then **Ads MCP server** under **Integrations**.
2. Select your ad account and switch every action to **Blocked**.
3. Test it: in a new chat, ask Claude to "create a paused campaign named WAGYU-TEST in act_[AD_ACCOUNT_ID]".

**You should see:** **Take actions in this ad account** marked as blocked, and Claude reporting that the request was denied.

> **Watch out:** [VERIFY] No **Ads MCP server** in your settings? Meta is still rolling it out. Until then, don't ask Claude to change anything. The second lock, inside Claude, is in the email we send you in two days. If the test campaign does appear, it's paused and hasn't spent anything; delete it in Ads Manager.

[SCREENSHOT: Ads MCP server rules, all blocked]

### Step 5 — Run your first performance report

1. Copy the **first performance report** prompt below.
2. Replace `[AD_ACCOUNT_ID]` with the number from Step 3 (without `act_`) and send it.

**You should see:** an overview table, your campaigns ranked, and three options for you to decide on. At the top, Claude names the dates, time zone, and attribution setting it used.

> **Watch out:** Numbers differ from Ads Manager? Set Ads Manager to the same dates and attribution setting Claude names, then compare again.

[SCREENSHOT: report example, labeled as an illustration]

**Checkpoint**

- [ ] Meta Ads connected in Claude
- [ ] `is_ads_mcp_enabled: true` for your account
- [ ] Every action blocked in Business Suite
- [ ] Your first report in hand

> You can see what's happening in the account now. Results come from acting on it every week, and that part AI can't own for you. [See how Gwenchana runs it](CTA_URL)

## Your prompts

**Account check** (Step 3)

```text
Using the Meta Ads connector, list every ad account I can access with its name, account ID, currency, time zone, and is_ads_mcp_enabled (with the reason if it is false). Read only. Don't change anything.
```

**First performance report** (Step 5, reuse it every week)

```text
Read-only analysis. Don't change anything in the account.
Ad account: act_[AD_ACCOUNT_ID]. Period: the last 30 complete days.
At the top, state the exact dates, time zone, attribution setting, and currency you used.

1. Overview: one table with spend, impressions, reach, CPM, CTR, CPC, results, cost per result, and ROAS if available.
2. Campaigns: rank by cost per result, best to worst, with spend and results. Mark the top performers and the biggest budget drains.
3. Ads: the 3 best and 3 worst by cost per result, with one line on why.
4. Problems: the 3 issues costing the most money, with the numbers behind them.
5. For me to decide: 3 options for the next 7 days. Describe each change; don't make it.
Keep it short. Tables over paragraphs.
```

## Quick fixes

<!-- wg:details -->

**1. Claude connects, but Meta calls fail or show `is_ads_mcp_enabled: false`**
Meta hasn't enabled that ad account yet, and you can't switch it on yourself. Try another ad account you manage, and run the account check again every week or two. Skip anyone who offers to "enable" it for a fee.

**2. The Facebook login never opens**
Your browser blocked the pop-up. Allow pop-ups for claude.ai, then click **Connect** again.

**3. It worked for weeks, then stopped**
Meta's access expires after about 60 days. Disconnect Meta Ads in **Customize** > **Connectors** and connect it again.

<!-- wg:cta -->
## What's next: the part AI can't do for you

Claude can now read your account and tell you what's off. Results still come from what you do each week: fresh creative to test, budget calls that don't blow up your CPA, and tracking you can trust.

Gwenchana runs Meta Ads end to end, starting from the Starter tier, while you keep watching every number with this setup.

Testing with a small budget and enjoying doing it yourself? Keep going on your own first. Over the next week we'll email you the second safety lock, a 12-prompt weekly audit pack, and how to make Claude's numbers match Ads Manager.

[Talk to Gwenchana about Meta Ads](CTA_URL)

---

Checked on September 28, 2026. Meta and Claude change these screens often. If something looks different, start with the quick fixes.
