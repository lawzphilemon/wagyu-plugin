# WAGYU Free Guide Pipeline

Claude Code plugin for gated free guides (lead magnets): A5-quality walkthroughs that readers can finish with free tools, and that ladder honestly to a premium service (Gwenchana: SEO/GEO, Meta Ads, Google Ads).

Rule of the ladder: **free = the full way to do it yourself; premium = speed, scale, or done for you.** The guide never holds back steps to sell.

## Install

```text
/plugin marketplace add lawzphilemon/wagyu-plugin
/plugin install wagyu@wagyu-plugin
```

## Pipeline

```text
/blueprint → /research → /outline → /draft → /stepcheck → /finaldraft
```

`/stepcheck` is named so it doesn't collide with Claude Code's built-in `/verify`.

Each guide gets its own folder, `wagyu-output/<slug>/` (slug set in `/blueprint`), so the pipeline can resume after the conversation restarts and guides never overwrite each other. Screenshots go in `wagyu-output/<slug>/screenshots/`.

| Command | Stage | Output |
|---|---|---|
| `/blueprint` | One promise, checkable result, free-tool stack, ladder to premium | `01-blueprint.md` |
| `/research` | Official docs, current free-tier limits, reader friction, competitor freebies, the A5 angle | `02-research.md` |
| `/outline` | Phases, single-outcome steps, assets, checkpoints, max 3 ladder points | `03-outline.md` |
| `/draft` | Full guide in the primary language, humanized | `04-draft.md` |
| `/stepcheck` | Every step marked LIVE / DOC / USER (or ACCEPTED-OPEN for test runs), draft fixed in place | `05-stepcheck.md` |
| `/finaldraft` | A5 quality gate, CTA, second language, guide page HTML | `guide-<slug>-<lang>.html` |
| `/export-docs` | Optional: the guide as a Google Doc for review or handoff (text and structure; screenshots inserted by hand) | Google Doc via the Drive connector |
| `/export-html` | Optional: the guide as paste-ready HTML code for a WordPress Custom HTML block or page builder: a snippet (style + guide + script), or a fully inlined version for sites that strip `<style>` and `<script>` | `guide-<slug>-<lang>.snippet.html`, `guide-<slug>-<lang>.wordpress.html` |

Formats: `lite` (one quick win, at most 5 steps, about 1,000 words; the deeper material becomes a nurture email plan) or `full` (complete walkthrough).

Languages: `id`, `en`, or `id+en`. The second language is localized after verification, with UI labels as each interface shows them.

## Guide page

`/finaldraft` builds the page with `scripts/build-guide.py` (needs Python 3 and [pandoc](https://pandoc.org/installing.html)) from the draft's page conventions, described in `commands/draft.md`. Brand themes live in `assets/themes/` (Gwenchana: `gwenchana.css`). The result fills `assets/guide-template.html`, a self-contained page (no external requests, `noindex`) with scoped CSS under `.wg-guide`. Host it on an unlisted URL, or paste it into a WordPress Custom HTML block. Your email tool does the gating by sending the URL in the welcome email, or the site's own form unlocks the guide at the `<!-- wg:gate -->` marker.

Some WordPress setups strip `<style>` and `<script>` on save, and the leftover CSS shows up as text above the guide. `--wordpress` avoids that: every style is inlined, with no script, no copy buttons, and no H1 (the post title already is one). It needs `python -m pip install premailer`.

## Examples

`examples/` holds the first test runs, every stage kept so you can see what each command produces. The two Meta Ads runs are marked TEST RUN (some steps unverified, placeholder CTA). The competitor research run is complete.

| Folder | Format | What's inside |
|---|---|---|
| `examples/meta-ads-claude/` | full, EN | Blueprint, research, outline, draft, stepcheck, the guide page, the paste-ready snippet, and the Google Docs HTML |
| `examples/meta-ads-claude-lite/` | lite, EN + ID | The same stages in lite form, the nurture plan, the five nurture emails (EN + ID), and the pages and snippets in both languages |
| `examples/riset-kompetitor-claude/` | lite, ID + EN | Every step verified (live, docs, or a walkthrough on the Claude Free plan), real CTA, no banner. Includes the early-walkthrough results in the stepcheck, the nurture plan, and pages and snippets in both languages |
| `examples/chatgpt-ads-tracking-wa/` | full, ID + EN, behind an email gate | WhatsApp click tracking to GA4 and OpenAI Ads (ChatGPT Ads). Every step LIVE, DOC, or USER; the steps that could not be verified were rewritten to verified content instead of shipping with a banner. Screenshots come from a WordPress media library (`--img-base`). Includes pages, snippets, and the inlined `.wordpress.html` files that went live |

GitHub shows `.html` files as code. Download one and open it in a browser to see the page.

## Development

```bash
python tests/test_build_guide.py
```

Builds a small sample draft and checks every page component, the Docs export, the snippet, and the WordPress export. Skips when pandoc isn't installed, and skips the WordPress check without premailer.

## Not in this plugin

- Public SEO article that drives traffic to the opt-in: use `nexus`.
- Opt-in page copy and the nurture sequence: use a lead-magnet or email skill.
- Contact numbers, booking links, prices: supplied at runtime, never stored in this repo.
