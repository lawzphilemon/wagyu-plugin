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
- Premium service it ladders to: a Gwenchana service available now. That is `seo-geo`, `meta-ads`, or `google-ads` (see the `gwenchana-offer` skill), or another service the user confirms is available, by name. Topics are open: the guide doesn't have to be something the user or the team has done before (/research and /stepcheck verify it), but it always ladders to an available service.
- Language: `id`, `en`, or `id+en`. For `id+en`, which one is primary.
- Format: `lite` or `full`. Recommend `lite` for lead magnets: one quick win a reader finishes in one sitting, with the deeper material moved into the nurture emails. `full` is a complete walkthrough.
- Brand context: if a `context_profile.json` or brand profile exists in the project or conversation, read it. Otherwise skip.

If the user has no topic yet, propose three that fit the reader. The `gwenchana-offer` idea list is a starting point, not a limit.

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

If no available service fits the topic, change or narrow the topic until one does. For a service outside `gwenchana-offer`, the wall and the not-for criterion come from the user. Never fill them in from memory.

## Self-critique

Before saving, run the `self-critique` skill for this stage (blueprint): score the rubric, fix every line below 4, and log it in `06-critique.md`.

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
Format: [lite | full]
Free-tool stack:
| Tool | Used for | Account needed | Free-tier limit (unverified) |
Costs outside tools: [ad budget / none]
Future guides: [split-off promises]
Ladder:
  Service line: [seo-geo | meta-ads | google-ads | other: service name the user confirmed]
  Wall: [what they hit next]
  Bridge: [how premium removes it, in service-name terms only]
  Not for premium if: [honest criterion]
```

End: "Confirm the blueprint, then run /research."

## Rules
- One guide, one promise.
- Never invent premium scope, prices, or results. Ask, or leave them out.
- An open topic needs no prior experience. The guide rests on sources that get verified, never on invented experience.
