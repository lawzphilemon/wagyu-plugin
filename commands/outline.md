---
name: outline
description: Build the guide outline as phases and single-outcome steps, with ready-to-use assets, checkpoints, screenshot placeholders, and at most three ladder points
allowed-tools: Read, Write
---

# WGY-O — Guide Outline

**Mission:** Turn the blueprint and research into a step tree a beginner can follow without getting stuck.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** Confirmed blueprint and research. Read `wagyu-output/<slug>/01-blueprint.md` and `02-research.md` for anything not in the conversation. Missing → "Run /blueprint and /research first."

## Structure

```text
HERO
  Title: [promise-led, specific result]
  Subtitle: [who it is for + time + "100% tool gratis" (+ "budget iklan terpisah" for ads guides)]
  Chips: [time] · [level] · [tool cost: Rp0]

RESULT PREVIEW
  What the reader has at the end + the success check from the blueprint.

FOR / NOT FOR
  2-3 bullets each. Honest.

TOOLKIT
  | Tool | Used for | Free limit (checked [date]) | Account needed |
  Prerequisites: [anything needed before step 1]

PHASE 1: [name] (~[minutes])
  Goal: [what this phase produces]
  Step 1.1: [one action, verb first]
    — Source: [research doc URL]
    — Expected result: [what the reader sees]
    — Pitfall: [from research friction, or None]
    — Screenshot: [what to capture, or None]
  Step 1.2: ...
  CHECKPOINT: [2-4 checkable items]
  Ladder point: [None | Soft]

PHASE 2 ...

ASSETS
  [At least one ready-to-use asset: template, checklist, prompt, swipe file, naming convention, formula.]
  For each: name, format (copy-paste block or a link to a file the user will host), purpose.

TROUBLESHOOTING
  [Top friction points from research: symptom → cause → fix]

NEXT WALL + PREMIUM (closing)
  The wall from the blueprint, the bridge, who it is not for, CTA.
```

## Lite format

When the blueprint says `Format: lite`, use this structure instead:

```text
HERO            Title, subtitle, chips (as above)
RESULT          2-3 bullets of what the reader has + the success check, in one box
STEPS           One `##` section, at most 5 steps, no phases. Pitfalls only where a reader would really get stuck.
PROMPTS         1 to 3 copy-ready prompts (the quick win)
QUICK FIXES     The top 3 friction points from research, symptom → fix
CLOSING         Wall, bridge, not-for, CTA
NURTURE PLAN    Not on the page. 3 to 4 emails, each carrying one block of the full material
                (extra prompts, deeper checks, second safety layer, troubleshooting) plus one bridge to premium.
```

- Budget: about 1,000 words on the page, not counting prompt text.
- Ladder points: at most 2 (after the last step, and the close).
- Nothing is held back from the free path: moved material goes into the free emails, never behind the paywall.

## Rules for steps
- One outcome per step. The clicks that lead to it go in a numbered list under the step. If a step produces two outcomes, split it.
- Every step has a source from research. A step without one is marked `[NEEDS SOURCE]` for /stepcheck.
- Phases take 15 to 30 minutes each. Split longer ones.
- Ladder points: at most 3 in total, including the closing. Only after a checkpoint (the reader just got a win) or at the close. Never inside a phase and never before the first checkpoint.

## Confirm

Save to `wagyu-output/<slug>/03-outline.md` (overwrite if it exists) and deliver it in chat. On confirmation, apply requested changes and add `Status: confirmed` as the first line.

End: "Confirm the outline, then run /draft."
