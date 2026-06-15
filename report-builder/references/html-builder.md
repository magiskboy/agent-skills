---
description: How to build an HTML report — the single-file scaffold with a built-in CSS design system, and when to reach for each client library.
---

# Building an HTML report

Use HTML when the report needs interactivity, custom layout/branding, slides, or
live charts/tables/maps/3D. Default to a **single self-contained `.html` file**
the user can double-click: pull libraries from a CDN, keep your own CSS/JS
inline. No build step, no server.

> Read [typography-and-layout.md](typography-and-layout.md) first — HTML gives
> you full control over type, spacing, and color, so there's no excuse for poor
> typography. The scaffold below already encodes the key rules.

## Core principle: plain HTML/CSS first

Add a library **only when the content truly needs it.** A static table is a
`<table>`, not Grid.js. A single number is a `<strong>`, not a chart. Every
CDN dependency is page weight, a render-blocking request, and a thing that can
break. Reach for a library only when its interactivity or rendering is the point.

| Content | Use plain HTML/CSS when… | Reach for a library when… |
| --- | --- | --- |
| Tables | Static, < ~30 rows, read-only | Sort / search / paginate → [Grid.js](lib-gridjs.md) |
| Numbers/trends | A few KPIs, a sparkline image | Interactive charts → [Chart.js](lib-chartjs.md) |
| Diagrams | A simple SVG/image | Flowcharts/sequence/mindmap from text → [Mermaid](lib-mermaid.md) |
| Code | Short snippet in `<pre><code>` | Multi-language, line numbers → [Prism](lib-prism.md) |
| Math | One symbol via HTML entities | Real equations → [KaTeX](lib-katex.md) |
| Presentation | A long scrolling page | Actual slides → [reveal.js](lib-revealjs.md) |
| Geo | A screenshot of a map | Pan/zoom/markers → [Leaflet](lib-leaflet.md) |
| 3D | An image/video | Interactive 3D → [Three.js](lib-threejs.md) |

## The base scaffold

A complete, copy-ready scaffold with the design system lives in
[../assets/report-template.html](../assets/report-template.html) — **start from
it.** It is a single file with a **light, scientific/academic** look: semantic
structure, a CSS-variable design system (type scale, spacing scale, one calm
navy accent), serif body + sans-serif headings, **auto-numbered sections and
figures** via CSS counters, an abstract block, readable measure (`max-width`),
styled tables, numbered figure captions, print-to-PDF styles, and
`prefers-reduced-motion` handling.

> **Default to light.** Use a near-white background with near-black text — it's
> the professional, print-friendly default and pairs with the light library
> themes below. Only add a dark theme when the user asks (and then *in addition*
> to light, via `prefers-color-scheme`), never instead of it.

Minimal shape of that file (the asset is the full version — read it, don't
retype it):

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report title</title>
  <style>
    :root{
      --bg:#ffffff; --fg:#14181f; --muted:#5b6573; --accent:#1b4d8a;
      --border:#dfe3e8; --maxw:70ch;
      --font-body: Georgia,"Iowan Old Style","Times New Roman",serif;
      --font-head: system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
      --mono: ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;
      --s1:.25rem; --s2:.5rem; --s3:1rem; --s4:1.5rem; --s5:2.5rem;
    }
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-body);
         line-height:1.65;font-size:18px}
    main{max-width:var(--maxw);margin-inline:auto;padding:var(--s5) var(--s3)}
    h1,h2,h3{font-family:var(--font-head);line-height:1.2;margin:var(--s5) 0 var(--s3)}
    h1{font-size:2.1rem} h2{font-size:1.5rem;border-bottom:1px solid var(--border)} h3{font-size:1.2rem}
    p,li{max-width:var(--maxw)} p{text-align:justify;hyphens:auto}
    a{color:var(--accent)}
    table{border-collapse:collapse;width:100%;margin:var(--s4) 0}
    th,td{padding:var(--s2) var(--s3);border-bottom:1px solid var(--border);
          text-align:left}
    td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
    figure{margin:var(--s4) 0}
    figcaption{color:var(--muted);font-size:.9rem;margin-top:var(--s2)}
    code{font-family:var(--mono)}
    @media print{ a{color:inherit} main{max-width:none} }
    @media (prefers-reduced-motion:reduce){ *{animation:none!important;
          transition:none!important} }
  </style>
</head>
<body>
  <main>
    <h1>Report title</h1>
    <p class="subtitle">What this answers — as of YYYY-MM-DD</p>

    <section id="summary"><h2>Summary</h2><p>Answer first…</p></section>
    <section id="findings"><h2>Findings</h2></section>
    <!-- library widgets go in their own <section> blocks -->
  </main>
  <!-- CDN libraries + init scripts at end of body, only those you need -->
</body>
</html>
```

## Adding a library — the pattern

1. Add the CDN `<link>`/`<script>` (or `importmap` for Three.js) — **pin the
   version** listed in the library's reference file.
2. Add a container element with an `id` in the right `<section>`.
3. Initialize it in a `<script>` at the end of `<body>` (or `type="module"` for
   ESM libraries: Mermaid, Three.js).
4. Verify it renders with no console errors before moving on.

Open the matching reference file for copy-ready, verified snippets:
[reveal.js](lib-revealjs.md) · [Grid.js](lib-gridjs.md) ·
[Chart.js](lib-chartjs.md) · [Prism.js](lib-prism.md) · [KaTeX](lib-katex.md) ·
[Mermaid.js](lib-mermaid.md) · [Three.js](lib-threejs.md) · [Leaflet](lib-leaflet.md).

## Combining libraries

- They coexist fine in one file; just include each one's assets once.
- **reveal.js is different**: it owns the whole page (slide deck), so a reveal
  report is *either* a normal scrolling document *or* a deck — don't nest a deck
  inside a normal report. Put other libraries *inside* slides instead (see
  [lib-revealjs.md](lib-revealjs.md)).
- Mind the load order: CSS in `<head>`, JS before `</body>`. ESM modules
  (Mermaid, Three.js) run after classic scripts regardless of position.
- Keep total payload reasonable. If you're pulling in 5 libraries, reconsider
  whether the report needs all of them.

## Responsiveness & print

- The scaffold is mobile-first with a capped measure; test at narrow widths.
- Make charts/tables/maps fluid: set their containers to `width:100%` and a
  sensible `height`. Chart.js needs `responsive:true` + a sized wrapper.
- For "export to PDF", the print CSS in the scaffold handles it — tell the user
  to print to PDF from the browser.

## Before handing off

- Open the file in a real browser. Check: no console errors, every CDN loaded,
  every widget rendered, layout works narrow→wide, dark mode looks right.
- If a CDN could be blocked in the user's environment, mention it (or offer to
  vendor the libraries locally).
- Run the checklist in [typography-and-layout.md](typography-and-layout.md).
- Default filename `report.html`.
