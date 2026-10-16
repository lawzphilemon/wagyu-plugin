---
name: self-critique
description: Stage-end self-critique for every wagyu stage (blueprint, research, outline, draft, stepcheck, finaldraft). Three critics score the stage output against its rubric, everything below 4 gets fixed before saving, and the result is logged in 06-critique.md. Use at the end of each stage, before saving or asking for confirmation.
---

# Self-critique

Run this at the end of a stage, on the output you are about to save. It is a gate, not a report: fix what fails, then save.

## 1. Read it as three critics

| Critic | Asks |
|---|---|
| **The reader** (the blueprint's reader, at their level, with no extra context) | Where do I get stuck, confused, or bored? What do I have to guess? Would I finish? |
| **The brand owner** (Gwenchana) | Is every claim supported? Any price, invented result, client name, or guarantee? Does the ladder feel honest, not salesy? |
| **A senior editor** | Is it the shortest version that still works? Does every part earn its place? Is it better than the best free alternative? |

## 2. Score the stage rubric

Score each line 1 to 5 (5 = nothing to improve). Any line below 4 is a finding.

**blueprint**
- The promise is one result the reader can check, not "understanding"
- The time fits the reader's level
- Every tool is free for this use; ad spend is named as the reader's cost
- The wall comes after the promise is fully delivered; the not-for line is honest

**research**
- Every fact a step depends on has an official source or a live check, with a date
- Friction comes from real user problems; snippet-only sources are labeled
- The A5 angles are concrete and checkable against the competitor freebies
- Open items say which ones change how a step is written

**outline**
- Each step has one outcome a beginner can see
- The opening lines work as a teaser on their own (gated previews show only those)
- At least one asset is complete and copy-ready
- Lite limits and ladder discipline hold

**draft**
- A cold reader can follow every step without outside help; jargon is explained once
- UI labels are exact and bold; every step has an expected result
- Nothing is claimed beyond the sources and the allowed claims
- It reads like a person wrote it (humanizer self-check passed), within the word budget
- Text-first guides: a reader finds every control from the text alone (position and label), with no screenshot

**stepcheck**
- No step rests on a single blog or an undated source
- Every label in the draft was seen in a doc, a live page, or the user's screenshot
- Screenshots were checked for account data, prices, and personal details
- Every fix was applied to the draft, not only logged

**finaldraft**
- The A5 gate passes
- The second language reads as written in that language, not translated
- CTA, examples, and currency fit the published language and audience
- Promises made in the closing (emails, follow-ups) actually exist or are flagged

## 3. Fix, then re-score once

- Fix every finding in the stage output itself.
- A fix that needs a new fact goes back to research or becomes an open item. Never invent a fact, label, source, or result to raise a score.
- Re-score only the lines you changed. A line still below 4 after one fix pass is logged as remaining, with the reason.

## 4. Log

Append to `wagyu-output/<slug>/06-critique.md` (create it if missing):

```markdown
## [stage] · [date]
| Rubric line | Score before | Fix | Score after |
|---|---|---|---|
Remaining: [line → why it can't be fixed now, or "none"]
```

Then tell the user in one line: `Self-critique: [n] findings fixed, [n] remaining ([short list])`.

The review brief (/export-docs) lists every remaining finding, so the reviewer sees what Claude could not fix.
