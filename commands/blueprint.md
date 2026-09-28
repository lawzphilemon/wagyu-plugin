---
name: blueprint
description: Lock the free guide's single promise, checkable result, free-tool stack, and honest ladder to a Gwenchana premium service before any research or writing
allowed-tools: Read, Write
---

# WGY-B — Guide Blueprint

**Mission:** Decide exactly what this free guide delivers and how it leads to a premium service, before any research.

## Step 1 — Gather

Ask for everything missing in one message:
- The reader's problem or topic.
- Target reader: who they are, business type, current skill level.
- Premium service line it ladders to: `seo-geo`, `meta-ads`, or `google-ads` (see the `gwenchana-offer` skill).
- Language: `id`, `en`, or `id+en`. For `id+en`, which one is primary.
- Brand context: if a `context_profile.json` or brand profile exists in the project or conversation, read it. Otherwise skip.

If the user has no topic yet, propose three from the `gwenchana-offer` idea list that fit the reader.

## Step 2 — One promise

Write the promise as one sentence:

> Setelah mengikuti guide ini, [reader] akan punya [concrete result] dalam [time], hanya dengan tool gratis.

- The result is something the reader **has** or a state they can **check** (a sheet, a working pixel, a submitted sitemap), never "understanding X".
- If the topic produces more than one result, pick the strongest and list the rest under "Future guides".
- Time is realistic for the stated skill level. Beginners need more.

## Step 3 — Free-tool stack

List every tool the steps need. Limits are unverified until /research.
- Separate tool cost from media spend. Ads guides say plainly that ad budget is the reader's own cost.
- A tool that needs a paid plan or a card-required trial is not free. Replace it or drop the step.

## Step 4 — Ladder

From `gwenchana-offer`, pick the wall the reader hits **after** finishing, the premium bridge over it, and who premium is not for.

The guide must deliver the full promise without buying anything. If the promise only works with premium, shrink the promise.

## Step 5 — Save and confirm

Pick a short kebab-case slug for the guide (for example `meta-ads-claude`) and confirm it with the user. Every stage of this guide lives in `wagyu-output/<slug>/`, so several guides never overwrite each other. Save to `wagyu-output/<slug>/01-blueprint.md` (overwrite if it exists), deliver it in chat, and ask for confirmation. On confirmation, apply requested changes and add `Status: confirmed` as the first line.

```text
Slug: [kebab-case]
Promise: [one sentence]
Reader: [who, business type, level]
Result: [what they have at the end]
Success check: [how the reader verifies it worked]
Time to result: [e.g. 60 to 90 minutes]
Language: [id | en | id+en, primary: xx]
Free-tool stack:
| Tool | Used for | Account needed | Free-tier limit (unverified) |
Costs outside tools: [ad budget / none]
Future guides: [split-off promises]
Ladder:
  Service line: [seo-geo | meta-ads | google-ads]
  Wall: [what they hit next]
  Bridge: [how premium removes it, in service-name terms only]
  Not for premium if: [honest criterion]
```

End: "Confirm the blueprint, then run /research."

## Rules
- One guide, one promise.
- Never invent premium scope, prices, or results. Ask, or leave them out.
