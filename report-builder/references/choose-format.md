---
description: Decide between Markdown and HTML for a report, and confirm with the user only when genuinely ambiguous.
---

# Choosing the format: Markdown vs HTML

If the user explicitly asked for one, use it — skip the rest of this file.
Otherwise **decide yourself** using the rules below. Only ask the user when the
signals genuinely conflict (see "When to ask").

## Decide by destination and content

Score the request against both tables. Pick the format with more / stronger hits.

### Pick **Markdown** when…

| Signal | Why |
| --- | --- |
| Output lives in a repo, PR description, issue, wiki, or README | Renders natively; stays diff-able and reviewable |
| It will be pasted into chat, Slack, Notion, email | Plain text travels everywhere |
| Content is text-first: prose, lists, a few tables, some code | No interactivity needed |
| It must be edited later by humans or other tools | Lowest-friction format |
| Long-term archival / version control matters | Future-proof, dependency-free |

### Pick **HTML** when…

| Signal | Why |
| --- | --- |
| The user wants **slides / a presentation** | reveal.js |
| Tables must be **sortable / searchable / paginated** | Grid.js |
| Data needs **charts, plots, live visuals** | Chart.js |
| Content has **diagrams, flowcharts, mind maps** that should look polished | Mermaid.js |
| Heavy **math / scientific notation** that must render crisply | KaTeX |
| **Maps / geospatial** or **3D** content | Leaflet / Three.js |
| Custom **branding, layout, colors, print-to-PDF styling** is wanted | Full CSS control |
| Deliverable is a **standalone artifact** to open in a browser or share as one file | Self-contained `.html` |
| It's a **dashboard** or anything the reader will *interact* with | Needs JS |

## Default when truly unspecified

If nothing in the request leans either way (e.g. "write me a report on X"):

- Short, text-heavy, or clearly headed for a repo/chat → **Markdown**.
- Data-/visual-heavy, exploratory, or meant to impress / be presented → **HTML**.
- When still a coin-flip, default to **Markdown** (lighter, portable, easy to
  convert to HTML later) and mention you can produce an HTML version if they
  want interactivity.

## When to ask

Ask a single, quick question only if:

- The content strongly needs interactivity (charts/tables/slides) **but** the
  destination strongly favors plain text (e.g. "put this in the PR description").
- The user implied a constraint you can't reconcile (e.g. "one file I can email"
  vs. "I want live filtering").

Otherwise commit to a format, state it in one line ("Mình sẽ làm dạng HTML một
file vì báo cáo cần biểu đồ tương tác"), and proceed.

## Mixing

You can have both: a Markdown report that embeds Mermaid/math (GitHub renders
these) for the repo, plus an HTML version for interactivity. Don't build both
unless the user wants it — pick one, offer the other.
