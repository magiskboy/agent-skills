---
name: report-builder
description: >-
  Build polished reports in either Markdown or HTML. Use when the user asks to
  create a report, write-up, document, summary, analysis, dashboard, slide deck,
  or any deliverable that presents findings, data, or research. Lets the user
  pick Markdown or HTML; if they do not say, this skill decides for them. For
  HTML, it routes rich content to the right client library: reveal.js (slides),
  Grid.js (interactive tables), Chart.js (charts), Prism.js (code highlight),
  KaTeX (math/science/LaTeX), Mermaid.js (diagrams/flowcharts/mindmaps),
  Three.js (3D), Leaflet (maps). Triggers include "make a report", "build a
  dashboard", "write this up", "create slides", and the Vietnamese equivalents
  ("làm báo cáo", "viết report", "tạo slide", "dựng dashboard"). This SKILL.md
  is an index; each topic lives in references/ and is loaded on demand.
license: MIT
metadata:
  author: Nguyen Khac Thanh - <ask@nkthanh.dev>
  version: "0.1.0"
---

# Report Builder

Build a clean, well-typeset report in one of two formats — **Markdown** or
**HTML** — and route any rich content (slides, tables, charts, math, diagrams,
3D, maps) to the right client library.

This file is an **index**. Read only the reference file you need for the current
step (progressive disclosure). Do not preload every file.

## Global rule — language

> **Always reply to the user in Vietnamese.** This skill is written in English
> for precision, but every user-facing message, question, and the report's own
> prose follow the user's language (default Vietnamese unless the user writes in
> or asks for another language). Keep widely-used technical terms in English
> (e.g. *dashboard*, *slide*, *flowchart*, *importmap*).

## The flow

```
1. Choose format (Markdown vs HTML)   → references/choose-format.md
2. Apply writing & design principles   → references/typography-and-layout.md   (ALWAYS read this)
3. Build:
     Markdown → references/md-builder.md
     HTML     → references/html-builder.md  (+ per-library files as needed)
4. Verify & hand off                    → see "Verify before handing off" below
```

## Step 1 — Choose the format

If the user named a format, use it. If not, **decide** — do not ask unless truly
ambiguous. Read [references/choose-format.md](references/choose-format.md) for
the decision rules. One-line heuristic:

- **Markdown** when the deliverable is text-first, lives in a repo/PR/wiki/chat,
  or must stay diff-able and portable.
- **HTML** when it needs interactivity, custom layout/branding, slides, live
  charts/tables/maps/3D, or will be opened in a browser / shared as one file.

## Step 2 — Writing & design principles (always)

Read [references/typography-and-layout.md](references/typography-and-layout.md)
**for every report, both formats.** It covers document structure, typography,
layout, tone, and the content rules (lead with the answer, one idea per section,
evidence for every claim). A report that is correct but badly structured or
poorly worded is a failed report.

## Step 3 — Build

### Markdown

Read [references/md-builder.md](references/md-builder.md). Covers the standard
section skeleton, tables, callouts, footnotes, and how to embed Mermaid / math /
code so they still render on GitHub and most Markdown viewers.

### HTML

Read [references/html-builder.md](references/html-builder.md) **first** — it has
the base single-file scaffold (semantic HTML + the built-in CSS design system in
`assets/report-template.html`) and the rule of thumb for *when* to reach for a
library. Then open only the library files you actually need:

| Need | Library | Reference |
| --- | --- | --- |
| Slides / presentation | reveal.js | [references/lib-revealjs.md](references/lib-revealjs.md) |
| Interactive tables (sort/search/page) | Grid.js | [references/lib-gridjs.md](references/lib-gridjs.md) |
| Charts & plots | Chart.js | [references/lib-chartjs.md](references/lib-chartjs.md) |
| Source-code highlighting | Prism.js | [references/lib-prism.md](references/lib-prism.md) |
| Math / physics / chemistry / LaTeX | KaTeX | [references/lib-katex.md](references/lib-katex.md) |
| Mind maps, flowcharts, sequence/Gantt | Mermaid.js | [references/lib-mermaid.md](references/lib-mermaid.md) |
| Interactive 3D | Three.js | [references/lib-threejs.md](references/lib-threejs.md) |
| Maps / geospatial data | Leaflet | [references/lib-leaflet.md](references/lib-leaflet.md) |

Principle: **plain HTML/CSS first; add a library only when the content truly
needs it.** Every library you add is weight and a potential point of failure.

## Step 4 — Verify before handing off

- **Markdown:** preview the rendering (GitHub-flavored). Check tables align,
  links resolve, code fences close, and headings form a sane outline.
- **HTML:** open the file in a browser and confirm no console errors, every
  library actually loaded (CDN reachable), charts/tables/diagrams render, and
  the layout is responsive. Prefer a **single self-contained `.html` file** so
  the user can double-click it — pull libraries from a CDN, keep your own CSS/JS
  inline.
- Re-read against [references/typography-and-layout.md](references/typography-and-layout.md):
  is the answer up top, is each claim evidenced, is the prose tight?

## Conventions

- Default output: one file. Markdown → `report.md`; HTML → `report.html`
  (single self-contained file). Confirm the path/name with the user if it
  matters.
- Pin CDN library versions in HTML (don't float on `@latest`) so the report
  doesn't break later; the per-library files list known-good versions.
- Never invent data. If a number/quote has no source, say so in the report.
