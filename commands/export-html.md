---
name: export-html
description: Export a finished guide as paste-ready HTML code for a WordPress Custom HTML block or a page builder, either with its own style and script or fully inlined for sites that strip those tags
allowed-tools: Read, Bash
---

# WGY-H — Export as HTML code

**Mission:** Give the user the guide as one block of code they can paste into their own site, where the gated page lives.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** `04-draft.md` (and `04-draft-[lang].md` for a second language), best after /finaldraft. Use the same CTA URL, theme, and banner as the page. If `05-stepcheck.md` has `ACCEPTED-OPEN` steps, the banner is required.

## 1. Ask where the screenshots will live

If the guide has screenshot files, ask for the folder URL they'll be uploaded to (for example `https://site.com/wp-content/uploads/2026/09/`). With it, pass `--img-base` so the code points there. Without it, the code keeps `screenshots/...` paths and the user must fix them after uploading. When the user sends image URLs instead, open each one, match it to its step, and write its file name (plus alt text) into the draft's `[SCREENSHOT: ...]` line; the shared folder becomes `--img-base`.

## 2. Pick the output

| Output | Flag | Use when |
|---|---|---|
| Snippet | `--snippet` | The site keeps `<style>` and `<script>` (WordPress admin with unfiltered HTML, Elementor HTML widget). Has copy buttons. |
| WordPress | `--wordpress` | The site strips `<style>`/`<script>` on save, so CSS or JavaScript shows up as text on the page. Every style is inlined, no script or copy buttons, no H1 (the post title already is one), and screenshots still missing are left out. Needs `python -m pip install premailer`. |

If you don't know yet, build both and say which to try first: `--wordpress` is the safe default for WordPress.

## 3. Build

For each language:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/build-guide.py" wagyu-output/<slug>/04-draft.md wagyu-output/<slug>/guide-<slug>-<lang>.snippet.html --lang <lang> --cta-url "<CTA URL>" --snippet --theme "${CLAUDE_PLUGIN_ROOT}/assets/themes/gwenchana.css" [--img-base "<URL>"] [--banner "..."]
python "${CLAUDE_PLUGIN_ROOT}/scripts/build-guide.py" wagyu-output/<slug>/04-draft.md wagyu-output/<slug>/guide-<slug>-<lang>.wordpress.html --lang <lang> --cta-url "<CTA URL>" --wordpress --theme "${CLAUDE_PLUGIN_ROOT}/assets/themes/gwenchana.css" [--img-base "<URL>"] [--banner "..."]
```

The snippet contains only `<style>`, the `.wg-guide` block, and the copy-button `<script>`; its CSS is scoped to `.wg-guide`. The WordPress file is the `.wg-guide` block alone, with `style=""` on every element. Both use the site's own fonts: the Gwenchana site already loads Montserrat; elsewhere they fall back to the system font.

Open the file in a browser before delivering: check one step, one image, the code blocks, and the CTA.

## 4. Deliver

Send the file path and reveal it in the file manager. Don't paste the code in chat unless the user asks: it is long, and a paste from chat can pick up formatting.

```text
HTML code ready: wagyu-output/<slug>/guide-<slug>-<lang>.[snippet|wordpress].html
Paste it into:
- WordPress: one Custom HTML block (block editor), the Text tab (Classic Editor), or an HTML widget (Elementor). Never a Paragraph block, the Visual tab, or a Text Editor widget.
Before publishing:
- Set the page to noindex and leave it out of the sitemap (in Yoast or Rank Math: "Allow search engines to show this page: No").
- The email form goes where the <!-- wg:gate --> comment is, if the guide has one.
- Upload the screenshots: [list of files] to [img-base, or "your media library, then replace the screenshots/ paths"].
- Check the post's public author name and category: WordPress may show a login email as the author.
- Snippet only: if CSS or JavaScript appears as text on the page, the site strips those tags. Use the .wordpress.html file instead.
```
