---
name: export-html
description: Export a finished guide as paste-ready HTML code (style, guide, and script, with no html or head tags) for a WordPress Custom HTML block or a page builder
allowed-tools: Read, Bash
---

# WGY-H — Export as HTML code

**Mission:** Give the user the guide as one block of code they can paste into their own site, where the gated page lives.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** `04-draft.md` (and `04-draft-[lang].md` for a second language), best after /finaldraft. Use the same CTA URL, brand colors, and banner as the page. If `05-stepcheck.md` has `ACCEPTED-OPEN` steps, the banner is required.

## 1. Ask where the screenshots will live

If the guide has screenshot files, ask for the folder URL they'll be uploaded to (for example `https://site.com/wp-content/uploads/2026/09/`). With it, pass `--img-base` so the code points there. Without it, the code keeps `screenshots/...` paths and the user must fix them after uploading.

## 2. Build

For each language:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/build-guide.py" wagyu-output/<slug>/04-draft.md wagyu-output/<slug>/guide-<slug>-<lang>.snippet.html --lang <lang> --cta-url "<CTA URL>" --snippet [--img-base "<URL>"] [--brand "#hex" --brand-ink "#hex"] [--banner "..."]
```

The file contains only `<style>`, the `.wg-guide` block, and the copy-button `<script>`. The CSS is scoped to `.wg-guide`, so it doesn't restyle the rest of the site.

## 3. Deliver

Send the file path. Don't paste the code in chat unless the user asks: it is long, and a paste from chat can pick up formatting.

```text
HTML code ready: wagyu-output/<slug>/guide-<slug>-<lang>.snippet.html
Paste it into:
- WordPress: a Custom HTML block (needs an admin account; other roles get <script> and <style> stripped).
- Elementor or another builder: an HTML widget.
Before publishing:
- Set the page to noindex and leave it out of the sitemap (in Yoast or Rank Math: "Allow search engines to show this page: No").
- Upload the screenshots: [list of files] to [img-base, or "your media library, then replace the screenshots/ paths"].
- If the builder strips <script>, the guide still works; only the Copy buttons stop working.
```
