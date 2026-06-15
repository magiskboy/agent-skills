---
description: Writing, structure, typography, and layout principles that apply to every report in both Markdown and HTML. Read this for every report.
---

# Typography, layout & content

A report is judged on three things at once: **is it right, is it easy to read,
does it look considered.** These rules apply to both formats. Read them before
writing a single line. Examples are paired *Poor / Better* so the difference is
concrete.

## 1. Content & structure

### Lead with the answer (BLUF — bottom line up front)

The reader should get the conclusion before the evidence. Never make them scroll
to find out what you found.

**Poor (buries the conclusion):**

```markdown
## Methodology
We collected logs from 4 services over 14 days, normalized timestamps...
[600 words later]
## Conclusion
So the p99 latency regression came from the payments service.
```

**Better (answer first, then support):**

```markdown
## Summary
The p99 latency regression comes from the **payments service** — a synchronous
call added on Jun 3 (PR #812). Reverting it restores p99 from 1.9s to 240ms.

## Evidence
... methodology and data follow ...
```

### One idea per section; make headings a table of contents

Headings should read as a skimmable outline of the argument. A reader scanning
only the headings should understand the shape of the report.

- Use a strict hierarchy: one `#` title, `##` for sections, `###` for
  sub-points. Don't skip levels.
- Heading text states a point, not a category. Prefer "Cost is driven by idle
  GPUs" over "Analysis".

### Every claim carries its evidence

Numbers get a source; quotes get an attribution; "X is faster" gets a measurement.
If you don't have a source, say so explicitly rather than implying authority.

**Poor:** "This approach is significantly faster and is the industry standard."

**Better:** "This approach cut build time from 92s to 31s on our CI runner
(median of 5 runs, [job #4471]). It's used by the Vite and esbuild docs as the
recommended setup."

### Cut filler

Delete throat-clearing ("In today's fast-paced world…", "It is important to note
that…"). Prefer short declarative sentences. One thought per sentence.

### Standard section skeleton

Adapt, don't follow blindly. A general analytical report:

1. **Title + one-line subtitle** (what + for whom + as-of date)
2. **Summary / TL;DR** — the answer in 3-5 sentences or bullets
3. **Context** — why this report exists, scope, what's out of scope
4. **Findings** — one section per finding, most important first
5. **Evidence / data** — tables, charts, detail backing the findings
6. **Recommendations / next steps** — concrete, owned, actionable
7. **Appendix** — methodology, raw data, references, glossary

## 2. Typography

Good typography is invisible; bad typography is exhausting.

- **Measure (line length):** aim for **60–80 characters** per line for body text.
  In HTML, cap content width (e.g. `max-width: 70ch`). Full-width text is hard to
  read.
- **Line height:** body ~1.5–1.65; headings tighter (~1.2).
- **Hierarchy through scale, not decoration.** Use a consistent type scale
  (e.g. 1.250 "major third": 16 → 20 → 25 → 31 → 39 px). Don't bold random words
  for emphasis; reserve **bold** for genuinely key terms and *italic* for the
  first use of a term or light emphasis.
- **Font pairing:** at most two families — one for headings, one for body — plus
  a monospace for code. A safe, dependency-free system stack:
  - Body/UI: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`
  - Mono: `ui-monospace, "SF Mono", "Cascadia Code", Consolas, monospace`
- **Numbers in tables:** right-align, use tabular figures, consistent decimal
  places, and thousands separators. `1,240.0` not `1240`.
- **Don't shout:** avoid ALL CAPS for sentences, avoid more than one exclamation,
  avoid underlining (reads as a link).
- **One space after a period.** Use real punctuation: en dash for ranges
  (3–5), em dash for breaks (—), curly quotes if the platform supports them.

## 3. Layout & whitespace

- **Whitespace is structure.** Generous spacing between sections; group related
  things close, separate unrelated things. Don't fear empty space.
- **Alignment:** pick a grid and stick to it. Left-align body text by default.
  For a print/scientific look you may justify body text **only** together with
  `hyphens: auto` (justification without hyphenation creates "rivers" of white
  space). Never justify short lines, headings, or table cells.
- **Visual rhythm:** consistent spacing scale (e.g. 4/8/16/24/32px). Headings get
  more space above than below (they belong to the content beneath them).
- **Default to a light background.** Reports are read in daylight, printed, and
  exported to PDF — a light theme (near-white background, near-black text) is the
  safe, professional, print-friendly default. Use **one accent color**, plus
  neutral grays for text/borders/background. Prefer a calm, low-chroma accent
  (e.g. a scholarly navy/teal) over a loud one for a serious/scientific report.
  Only build a dark theme when the user asks, and if you do, offer it *in
  addition* to light (`prefers-color-scheme`), never replacing it. Use color to
  **mean** something (red = regression/bad, green = improvement/good), never for
  decoration. Ensure text contrast meets WCAG AA (≥ 4.5:1 for body).
- **Tables:** light or no vertical borders, subtle row separation (zebra or hair
  lines), padded cells, a clearly distinct header row. Don't box every cell.
- **Figures:** every chart/table/diagram gets a number and a caption that states
  the takeaway, not just the subject. "Figure 3: GPU cost is 70% idle" beats
  "Figure 3: GPU cost".
- **Don't overcrowd:** a page packed edge-to-edge reads as noise. If a section is
  dense, split it.

## 4. Tone & wording

- Match the audience: an exec summary is plainer than an engineering appendix.
- Be specific and concrete; prefer nouns and verbs over adjectives.
- Be honest about uncertainty: "likely", "we couldn't measure X", "n=12, small
  sample". Don't overclaim.
- Consistent terminology — one name per concept throughout the document.
- Active voice, present tense for findings ("the cache misses", not "it was
  observed that the cache was missing").

## 5. Consistency (tính đồng nhất)

A report reads as "considered" only when the same thing always looks and is named
the same way. Inconsistency makes the reader distrust the content. Lock these
*once* at the start and apply everywhere:

- **Terminology:** one name per concept for the whole document (don't switch
  between "latency", "delay", "response time" for the same metric).
- **Numbers:** one decimal precision per metric, one thousands separator, units
  always present and always in the same place (`240 ms`, not `240ms` here and
  `0.24s` there). Right-align all numeric columns.
- **Dates & locale:** one date format (`YYYY-MM-DD`) and one number locale
  throughout.
- **Color semantics:** fix the meaning of each color once (e.g. accent = neutral
  emphasis, green = good, red = bad) and never reuse those colors decoratively.
- **Headings:** parallel grammatical structure (all noun phrases, or all
  claims — don't mix). Same capitalization style at each level.
- **Figures/tables:** every one is numbered and captioned in the same style;
  refer to them by number in the text ("see Figure 3"), never "the chart above".
- **Visual style:** one spacing scale, one type scale, one chart palette and
  one chart style (same axis treatment, same legend position) across all figures.
- **Voice & tense:** consistent (active voice, present tense for findings).

If you generate figures with different libraries (Chart.js, Mermaid, etc.), give
them a **shared palette and font** so they look like one document, not a collage.

## 6. Scientific / academic style

When the report should read as a scientific/technical paper, layer these on top
of the rules above:

- **Structure:** Title + authors/affiliation + date → **Abstract** (unnumbered)
  → numbered sections (Introduction, Methods, Results, Discussion, Conclusion)
  → References. Methods must be reproducible.
- **Numbering:** auto-number sections (1, 1.1) and figures/tables/equations;
  cross-reference by number. The HTML template uses CSS counters for this.
- **Typography:** a serif body (Georgia/Times-like) with a sans-serif heading
  font reads as academic; keep a comfortable measure (~65–75ch). Justify body
  text only with `hyphens: auto`.
- **Tone:** precise, impersonal, hedged appropriately ("results suggest",
  "within measurement error"). Define notation and units on first use.
- **Equations:** display important equations centered on their own line, with
  consistent symbol usage; render with KaTeX (see [lib-katex.md](lib-katex.md)).
- **Evidence & citations:** every claim is backed by data or a citation; keep a
  numbered References list and cite inline by number/author.
- **Figures:** captions are descriptive and self-contained (a reader should
  understand the figure from the caption alone); state units on every axis.

## 7. Accessibility (especially HTML)

- Real semantic structure: `<h1>`–`<h3>`, `<table>` with `<th>`, lists for lists.
- Every image/chart has alt text or an adjacent text description of the takeaway.
- Don't encode meaning in color alone (add labels/patterns).
- Keyboard- and screen-reader-friendly; sufficient contrast; respect
  `prefers-reduced-motion` for any animation.

## Quick checklist (run before handing off)

- [ ] The conclusion is in the first screen of content.
- [ ] Headings alone tell the story.
- [ ] Every number/quote has a source (or is flagged as unsourced).
- [ ] Body line length is comfortable (~70ch); generous whitespace.
- [ ] Light, print-friendly background; one accent color used meaningfully; AA contrast.
- [ ] Tables: right-aligned numbers, captions state the takeaway.
- [ ] Consistency: one term per concept, uniform number/unit/date formatting,
      figures numbered + captioned in one style, one shared palette across figures.
- [ ] No filler sentences; consistent terminology; honest about uncertainty.
