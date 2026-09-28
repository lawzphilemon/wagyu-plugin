---
name: export-docs
description: Export a finished guide to Google Docs for team review or client handoff, with text, structure, and links, and markers where the screenshots go
allowed-tools: Read, Bash
---

# WGY-X — Export to Google Docs

**Mission:** Put the guide in a Google Doc so the team or a client can review and comment on it. The landing page from /finaldraft stays the delivery format.

**Guide folder:** `wagyu-output/<slug>/`, using the slug from the conversation. If it's unclear, list the folders in `wagyu-output/`: use the only one, or ask which guide.

**Dependency:** `04-draft.md` (and `04-draft-[lang].md` for a second language), best after /finaldraft. Use the same CTA URL as the page. If it isn't known, ask for it. If `05-stepcheck.md` has `ACCEPTED-OPEN` steps, pass the same `--banner` as the page.

## 1. Build the Docs version

For each language:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/build-guide.py" wagyu-output/<slug>/04-draft.md wagyu-output/<slug>/guide-<slug>-<lang>.docs.html --lang <lang> --cta-url "<CTA URL>" --docs [--banner "..."]
```

This writes plain HTML: headings, lists, tables, code blocks, and links, with no page styling, buttons, or script. Checkpoints become ☐ items. Each screenshot becomes an `[Insert image: ...]` or `[Screenshot needed: ...]` marker.

## 2. Upload

Use the Google Drive connector's create-file tool:
- Title: the guide's H1, plus ` (EN)` or ` (ID)`.
- Content: the full `.docs.html` file as text, content type `text/html`. Leave conversion to Google Docs on.
- Folder: only if the user names one. Find it with the connector's search first.

No Google Drive connector: say so, and offer the local fallback. The user uploads the `.docx` to Drive and opens it with Google Docs:

```bash
pandoc wagyu-output/<slug>/guide-<slug>-<lang>.docs.html -o wagyu-output/<slug>/guide-<slug>-<lang>.docx
```

## 3. Deliver

```text
Google Doc ready: [link]
Images to insert by hand: [each "Insert image" marker → local file path]
Screenshots still needed: [list or none]
```

Screenshots are not uploaded. The connector would have to carry them inside the tool call as base64, which is far too large. The user drags the files into the Doc at the markers.

## Rules
- Don't change sharing. The Doc stays private to the user until they share it.
- Upload only the guide. Never upload research notes, stepcheck reports, or contact details.
