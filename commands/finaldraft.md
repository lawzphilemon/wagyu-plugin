---
name: finaldraft
description: Pass the verified guide through the A5 quality gate, place the premium ladder CTA, localize to the second language, and build the self-contained guide landing page HTML
allowed-tools: Read, Write, Bash, WebFetch
---

# WGY-Fn — A5 Gate + Guide Page

**Mission:** Ship a free guide good enough that readers trust Gwenchana with the paid version.

**Dependency:** `wagyu-output/04-draft.md` and `05-verify.md`. Every step must be `LIVE`, `DOC`, or `USER`. Any `FAIL` or `OPEN` step → stop and say "Run /verify first", unless the user explicitly accepted it in /verify. Read `01-blueprint.md` and `03-outline.md` as needed.

## 1. Collect the ladder details

Ask in one message for anything missing:
- CTA destination URL and button label. Never invent or reuse one from memory, and never write it into the plugin repo.
- What premium includes, in the user's words, plus any price, threshold, or case study they want shown. Optional: leave out anything not supplied.
- Brand colors as hex, or the website to read them from. Optional: the template default is used otherwise.
- Hosted image URLs for the `[SCREENSHOT: ...]` placeholders. Optional: missing ones render as visible "screenshot needed" boxes.

Apply the claim rules from the `gwenchana-offer` skill.

## 2. A5 quality gate

Re-run the humanizer (`humanizer-id` / `humanizer-en`) silently, then check every item. Fix failures before building. Never ship a failing guide.

- [ ] **Real result:** a reader who follows every step ends with the blueprint's result, and the success check proves it.
- [ ] **100% free path:** no step needs a paid plan, card-required trial, or paid add-on. Ad spend, if any, is stated in the subtitle.
- [ ] **Limits dated:** every free-tier limit shows the date it was checked in /verify.
- [ ] **Executable:** every step has one action, exact bold UI labels, and an expected result.
- [ ] **Verified:** every step is `LIVE`, `DOC`, or `USER` in `05-verify.md`.
- [ ] **Asset:** at least one complete, copy-ready asset.
- [ ] **Troubleshooting:** covers the top friction points from research.
- [ ] **Nothing held back:** no "the full method is in premium" and no step that only works after buying.
- [ ] **Ladder discipline:** at most 3 ladder points including the closing, none before the first checkpoint, none inside a phase.
- [ ] **Honest close:** the closing names the wall, the bridge, and who premium is not for.
- [ ] **Beats the alternatives:** each A5 angle from research is actually in the guide.
- [ ] **Humanizer self-check passed.** No em dashes in body text.

Report the gate as a pass/fix list in chat (short), not the whole guide.

## 3. Second language (`id+en` only)

Localize the finished primary guide into the other language. This is adaptation, not word-for-word translation:
- UI labels as the tool shows them in that interface language, from research or verify notes. If unknown, use the English label.
- Examples, currency, and local references adapted to the audience.
- Run the matching humanizer and the gate again.

## 4. Build the page

Read the template with `cat "${CLAUDE_PLUGIN_ROOT}/assets/guide-template.html"`. For each language, write `wagyu-output/guide-[slug]-[lang].html`:
- Keep the whole `<style>`, the `.wg-guide` wrapper, and the copy-button script. Set `<html lang>`. Keep `noindex, nofollow`. This page is gated.
- Replace every `{{PLACEHOLDER}}`, repeat component blocks as needed, and delete unused ones. No `{{` may remain.
- Every `h2`/`h3` gets an `id`, and the table of contents links to every phase.
- HTML-escape asset and code content inside `<pre><code>`.
- Brand colors go only in `--wg-brand` and `--wg-brand-ink`. Keep the button text readable (contrast ratio 4.5:1 or more).
- `[CTA_URL]` becomes the confirmed destination in every ladder point.

Check it: `grep -c "{{" wagyu-output/guide-*.html` must print 0 for every file.

## 5. Deliver

```text
Guide page ready:
- wagyu-output/guide-[slug]-id.html
- wagyu-output/guide-[slug]-en.html
Screenshots still needed: [list or none]

Publishing: host the page on an unlisted URL (or paste the <style> and .wg-guide block into a WordPress Custom HTML block, noindex). Put that URL in the welcome email of your email tool. The email tool handles the gate.
Next: opt-in page copy and the nurture sequence to premium (ai-geo-by-ivan:lead-magnets and ai-geo-by-ivan:emails, if installed).
```

Do not paste the full HTML in chat unless asked.
