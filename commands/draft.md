---
name: draft
description: Write the full guide in the primary language from the confirmed outline, including every asset, then silently apply the matching humanizer
allowed-tools: Read, Write
---

# WGY-D — Guide Draft

**Mission:** Write the complete guide in the primary language. The second language is produced in /finaldraft after verification.

**Dependency:** Confirmed outline. If it is not in the conversation, read `wagyu-output/03-outline.md`. It counts only when its first line is `Status: confirmed`. Read `01-blueprint.md` and `02-research.md` for any data needed.

## Write

Follow the outline exactly. Use this step format:

```markdown
### Langkah 1.1 — [Aksi, kata kerja di depan]

[1-2 sentences: what to do and why it matters.]

1. Buka **[exact UI label]** ...
2. Klik **[exact UI label]** ...

**Hasil yang benar:** [what the reader sees]

> **Hati-hati:** [pitfall, only if the outline has one]

[SCREENSHOT: what to capture]
```

For English, use `Step 1.1`, `You should see`, and `Watch out`.

- Use UI labels exactly as recorded in research, in bold. If only English labels were recorded for an Indonesian guide, keep the English label and explain it in Indonesian, for example **Add property** (Tambah properti).
- Commands, code, URLs to type, and asset content go in fenced code blocks so they can be copied.
- Write every asset in full. No "isi sendiri" placeholders unless the placeholder is the point (for example `[NAMA BRAND]` in a template), and explain each placeholder.
- Troubleshooting uses symptom → cause → fix, in the reader's words.
- Ladder points: write them as a short aside only where the outline tags them. Leave the CTA destination as `[CTA_URL]`; /finaldraft fills it.
- Address the reader directly (kamu/you). Paragraphs of at most 4 sentences. No transition fillers and no hype.
- Never use em dashes in body text. (Step headings use the separator shown above.)

## Humanize

Silently apply `humanizer-id` or `humanizer-en` to match the language. Run its self-check and fix failures. Keep UI labels, code, and asset content untouched by the humanizer.

## Save

Save to `wagyu-output/04-draft.md` (overwrite if it exists) and deliver it in chat.

End: "Review the draft, then run /verify."

## Rules
- No draft without a confirmed outline.
- A step marked `[NEEDS SOURCE]` stays marked. Do not fill it from memory.
