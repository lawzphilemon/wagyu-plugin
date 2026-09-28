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
| `/export-html` | Optional: the guide as paste-ready HTML code (style + guide + script) for a WordPress Custom HTML block or page builder | `guide-<slug>-<lang>.snippet.html` |

Formats: `lite` (one quick win, at most 5 steps, about 1,000 words; the deeper material becomes a nurture email plan) or `full` (complete walkthrough).

Languages: `id`, `en`, or `id+en`. The second language is localized after verification, with UI labels as each interface shows them.

## Guide page

`/finaldraft` builds the page with `scripts/build-guide.py` (needs Python 3 and [pandoc](https://pandoc.org/installing.html)) from the draft's page conventions, described in `commands/draft.md`. Brand themes live in `assets/themes/` (Gwenchana: `gwenchana.css`). The result fills `assets/guide-template.html`, a self-contained page (no external requests, `noindex`) with scoped CSS under `.wg-guide`. Host it on an unlisted URL, or paste it into a WordPress Custom HTML block. Your email tool does the gating by sending the URL in the welcome email.

## Development

```bash
python tests/test_build_guide.py
```

Builds a small sample draft and checks every page component. Skips when pandoc isn't installed.

## Not in this plugin

- Public SEO article that drives traffic to the opt-in: use `nexus`.
- Opt-in page copy and the nurture sequence: use a lead-magnet or email skill.
- Contact numbers, booking links, prices: supplied at runtime, never stored in this repo.
