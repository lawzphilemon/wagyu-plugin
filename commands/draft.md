---
name: draft
description: Write the full guide in the primary language from the confirmed outline, including every asset, then silently apply the matching humanizer
allowed-tools: Read, Write
---

# WGY-D — Guide Draft

**Mission:** Write the complete guide in the primary language. The second language is produced in /finaldraft after verification.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** Confirmed outline. If it is not in the conversation, read `wagyu-output/<slug>/03-outline.md`. It counts only when its first line is `Status: confirmed`. Read `01-blueprint.md` and `02-research.md` for any data needed.

## Write

Follow the outline exactly. Use this step format:

```markdown
### Langkah 1.1 — [Aksi, kata kerja di depan]

[1-2 sentences: what to do and why it matters.]

1. Buka **[exact UI label]** ...
2. Klik **[exact UI label]** ...

**Hasil yang benar:** [what the reader sees]

> **Hati-hati:** [pitfall, only if the outline has one]

[SCREENSHOT: screenshots/step-1.1-short-name.png]
```

For English, use `Step 1.1`, `You should see`, and `Watch out`.

- Use UI labels exactly as recorded in research, in bold. If only English labels were recorded for an Indonesian guide, keep the English label and explain it in Indonesian, for example **Add property** (Tambah properti).
- Commands, code, URLs to type, and asset content go in fenced code blocks so they can be copied.
- Write every asset in full. No "isi sendiri" placeholders unless the placeholder is the point (for example `[NAMA BRAND]` in a template), and explain each placeholder.
- Troubleshooting uses symptom → cause → fix, in the reader's words.
- Ladder points: write them as a short aside only where the outline tags them, with the link written as `[link text](CTA_URL)`. /finaldraft fills in the URL.
- Address the reader directly (kamu/you). Paragraphs of at most 4 sentences. No transition fillers and no hype.
- Never use em dashes in body text. (Step headings use the separator shown above.)

## Page conventions

/finaldraft builds the page from this file with `scripts/build-guide.py`, so keep this shape:

- **Hero** (top of the file, blank line between each): eyebrow line, `# Title`, subtitle paragraph, chips paragraph separated by ` · ` (for example `30 to 45 min · Intermediate · Tool cost: $0`).
- **Intro boxes:** wrap the result preview in `<!-- wg:box -->` … `<!-- /wg:box -->`. For / not-for columns: `<!-- wg:cols -->` first column `<!-- wg:col -->` second column `<!-- /wg:cols -->`. Each marker on its own line.
- **Sections:** `## ` for toolkit, phases, assets, troubleshooting, closing. `### ` for steps.
- **Expected result and pitfall** labels exactly as in the step format above: `**You should see:**` / `**Hasil yang benar:**`, and a `> **Watch out:**` / `> **Hati-hati:**` quote. Any other `>` quote becomes a ladder aside.
- **Screenshots:** `[SCREENSHOT: screenshots/<file>.png]` for an image you have (files in `wagyu-output/<slug>/screenshots/`), `[SCREENSHOT: what to capture]` for one still needed.
- **Unverified steps:** `[VERIFY]` inside the pitfall. It renders as a visible "Not yet verified" note.
- **Checkpoints:** a bold-only line (`**Checkpoint**`) followed by `- [ ]` items.
- **Troubleshooting:** put `<!-- wg:details -->` right after the heading. Each item starts with a bold title on its own line, followed by its cause and fix.
- **Closing:** put `<!-- wg:cta -->` on the line before the closing `## ` heading. End it with the not-for paragraph, then the CTA link alone on its own line: `[Button text](CTA_URL)`.
- **Footer:** a `---` line, then the "checked on [date]" note.

## Humanize

Silently apply `humanizer-id` or `humanizer-en` to match the language. Run its self-check and fix failures. Keep UI labels, code, and asset content untouched by the humanizer.

## Save

Save to `wagyu-output/<slug>/04-draft.md` (overwrite if it exists) and deliver it in chat.

End: "Review the draft, then run /stepcheck."

## Rules
- No draft without a confirmed outline.
- A step marked `[NEEDS SOURCE]` stays marked. Do not fill it from memory.
