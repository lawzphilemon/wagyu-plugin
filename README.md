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
/blueprint → /research → /outline → /draft → /verify → /finaldraft
```

Each stage saves to `wagyu-output/`, so the pipeline can resume after the conversation restarts.

| Command | Stage | Output |
|---|---|---|
| `/blueprint` | One promise, checkable result, free-tool stack, ladder to premium | `01-blueprint.md` |
| `/research` | Official docs, current free-tier limits, reader friction, competitor freebies, the A5 angle | `02-research.md` |
| `/outline` | Phases, single-action steps, assets, checkpoints, max 3 ladder points | `03-outline.md` |
| `/draft` | Full guide in the primary language, humanized | `04-draft.md` |
| `/verify` | Every step marked LIVE / DOC / USER, draft fixed in place | `05-verify.md` |
| `/finaldraft` | A5 quality gate, CTA, second language, guide page HTML | `guide-[slug]-[lang].html` |

Languages: `id`, `en`, or `id+en`. The second language is localized after verification, with UI labels as each interface shows them.

## Guide page

`assets/guide-template.html` is a self-contained page (no external requests, `noindex`) with scoped CSS under `.wg-guide`. Host it on an unlisted URL, or paste it into a WordPress Custom HTML block. Your email tool does the gating by sending the URL in the welcome email.

## Not in this plugin

- Public SEO article that drives traffic to the opt-in: use `nexus`.
- Opt-in page copy and the nurture sequence: use a lead-magnet or email skill.
- Contact numbers, booking links, prices: supplied at runtime, never stored in this repo.
