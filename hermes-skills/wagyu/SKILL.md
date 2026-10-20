---
name: wagyu
description: A5-quality gated free guides (ID/EN) that ladder to a premium service — blueprint → research → outline → draft → stepcheck → finaldraft
version: 1.0.0
metadata:
  hermes:
    tags: [content, marketing, lead-magnets, guides, gwenchana]
    category: writing
---

# WAGYU Free Guide Pipeline

A pipeline for gated free guides (lead magnets): A5-quality walkthroughs readers finish with free tools, that ladder honestly to a premium service (Gwenchana: SEO/GEO, Meta Ads, Google Ads).

**Rule of the ladder:** free = the full way to do it yourself; premium = speed, scale, or done for you. The guide never holds back steps to sell.

## When to Use

Use `/wagyu` when you want to create a gated free guide (lead magnet). Each guide gets its own folder, `wagyu-output/<slug>/`, so the pipeline can resume after the conversation restarts.

## Pipeline

Run stages in order. Each stage saves a file and ends with "run /[next-stage]".

| Command | Stage | Output file |
|---|---|---|
| `/wagyu blueprint` | One promise, checkable result, free-tool stack, ladder to premium | `01-blueprint.md` |
| `/wagyu research` | Official docs, free-tier limits, reader friction, competitor freebies, A5 angle | `02-research.md` |
| `/wagyu outline` | Phases, single-outcome steps, assets, checkpoints, max 3 ladder points | `03-outline.md` |
| `/wagyu draft` | Full guide in the primary language, humanized | `04-draft.md` |
| `/wagyu stepcheck` | Every step marked LIVE / DOC / SOURCE / USER, draft fixed in place | `05-stepcheck.md` |
| `/wagyu finaldraft` | A5 quality gate, CTA, second language, guide page HTML | `guide-<slug>-<lang>.html` |

Optional:
| `/wagyu queue` | Run the pipeline from a Google Sheet (batch, scheduled) | |
| `/wagyu export-docs` | Export to Google Doc for review | |
| `/wagyu export-html` | WordPress/page builder paste-ready HTML | |

## Procedure

1. Ask the user which stage they want to run, or start from the beginning.
2. Load the corresponding reference file for that stage with `skill_view("wagyu", "references/<stage>.md")`.
3. Follow the stage instructions exactly.
4. Always run the `self-critique` skill before saving each stage output.
5. Save to `wagyu-output/<slug>/` and confirm with the user before proceeding to the next stage.

## Pitfalls

- Never skip stages — each depends on the previous being confirmed.
- Never invent premium scope, prices, or results. Ask, or leave them out.
- An open topic needs no prior experience. The guide rests on verified sources.
- `wagyu-output/` lives in the working directory, not in this skill folder.

## Verification

The pipeline is complete when `guide-<slug>-<lang>.html` exists and the A5 gate passes in `/wagyu finaldraft`.
