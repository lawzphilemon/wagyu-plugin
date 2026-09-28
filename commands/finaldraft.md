---
name: finaldraft
description: Pass the verified guide through the A5 quality gate, place the premium ladder CTA, localize to the second language, and build the self-contained guide landing page HTML
allowed-tools: Read, Write, Bash, WebFetch
---

# WGY-Fn — A5 Gate + Guide Page

**Mission:** Ship a free guide good enough that readers trust Gwenchana with the paid version.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** `wagyu-output/<slug>/04-draft.md` and `05-stepcheck.md`. Every step must be `LIVE`, `DOC`, or `USER`. Any `FAIL` or `OPEN` step → stop and say "Run /stepcheck first". `ACCEPTED-OPEN` steps allow a test build only: pass `--banner` (step 4) and report that the page is not publish-ready. Read `01-blueprint.md` and `03-outline.md` as needed.

## 1. Collect the ladder details

Ask in one message for anything missing:
- CTA destination URL and button label. Never invent or reuse one from memory, and never write it into the plugin repo.
- What premium includes, in the user's words, plus any price, threshold, or case study they want shown. Optional: leave out anything not supplied.
- Brand colors as hex, or the website to read them from. Optional: the template default is used otherwise.
- Screenshots: image files in `wagyu-output/<slug>/screenshots/` or hosted image URLs, one per `[SCREENSHOT: ...]` placeholder. Optional: missing ones render as visible "screenshot needed" boxes. Local files must be uploaded next to the page when publishing.

Apply the claim rules from the `gwenchana-offer` skill.

## 2. A5 quality gate

Re-run the humanizer (`humanizer-id` / `humanizer-en`) silently, then check every item. Fix failures before building. Never ship a failing guide.

- [ ] **Real result:** a reader who follows every step ends with the blueprint's result, and the success check proves it.
- [ ] **100% free path:** no step needs a paid plan, card-required trial, or paid add-on. Ad spend, if any, is stated in the subtitle.
- [ ] **Limits dated:** every free-tier limit shows the date it was checked in /stepcheck.
- [ ] **Executable:** every step has one outcome, numbered sub-actions with exact bold UI labels, and an expected result.
- [ ] **Verified:** every step is `LIVE`, `DOC`, or `USER` in `05-stepcheck.md`. Any `ACCEPTED-OPEN` fails this item: test build only.
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
- UI labels as the tool shows them in that interface language, from research or stepcheck notes. Save it as `wagyu-output/<slug>/04-draft-[lang].md` with the same page conventions. If unknown, use the English label.
- Examples, currency, and local references adapted to the audience.
- Run the matching humanizer and the gate again.

## 4. Build the page

For each language, run the builder (needs Python 3 and pandoc):

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/build-guide.py" wagyu-output/<slug>/04-draft.md wagyu-output/<slug>/guide-<slug>-<lang>.html --lang <lang> --cta-url "<confirmed CTA URL>" [--brand "#hex" --brand-ink "#hex"] [--banner "TEST RUN: not for publishing"]
```

- It fills `assets/guide-template.html` from the draft's page conventions (see /draft), keeps `noindex, nofollow`, adds the table of contents, copy buttons, checkpoints, troubleshooting items, and the CTA block.
- It exits with an error if a template placeholder, `CTA_URL`, `[NEEDS SOURCE]`, or an unconverted `[SCREENSHOT` is left. Fix the draft and rerun; never hand-edit around it.
- Brand colors: keep the button text readable (contrast ratio 4.5:1 or more).
- Open the page in a browser and look at one step, one code block, the troubleshooting, and the CTA before delivering. Check it at phone width too.

No Python or pandoc: copy `assets/guide-template.html` and fill it by hand with the same components. No double-brace placeholder may remain.

## 5. Deliver

```text
Guide page ready:
- wagyu-output/<slug>/guide-[slug]-id.html
- wagyu-output/<slug>/guide-[slug]-en.html
Screenshots still needed: [list or none]

Publishing: host the page on an unlisted URL (or paste the <style> and .wg-guide block into a WordPress Custom HTML block, noindex). Put that URL in the welcome email of your email tool. The email tool handles the gate.
Review copy for the team or a client: /export-docs (Google Docs).
Paste-ready code for WordPress or a page builder: /export-html.
Next: opt-in page copy and the nurture sequence to premium (ai-geo-by-ivan:lead-magnets and ai-geo-by-ivan:emails, if installed).
```

Do not paste the full HTML in chat unless asked.
