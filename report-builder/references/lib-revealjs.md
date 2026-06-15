---
description: reveal.js — turn an HTML report into a slide deck / presentation. Use when the user wants slides.
---

# reveal.js — slides / presentations

Use when the deliverable is a **presentation**. A reveal.js report is a whole
deck and owns the page — don't embed it inside a normal scrolling report; instead
put other widgets (charts, tables) *inside* slides.

- CDN version pinned here: **5.2.1** (check for a newer 5.x before shipping).
- Each `<section>` is a slide. Nesting `<section>`s creates vertical slides.

## Minimal deck

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Deck title</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/theme/white.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section>
        <h1>Quarterly report</h1>
        <p>Platform team — as of 2026-06-15</p>
      </section>

      <section>
        <h2>Summary</h2>
        <ul>
          <li class="fragment">p99 regression traced to payments service</li>
          <li class="fragment">Revert restores p99 1.9s → 240ms</li>
        </ul>
      </section>

      <!-- Vertical stack: press Down to go deeper -->
      <section>
        <section><h2>Evidence</h2><p>Press ↓</p></section>
        <section><h3>Methodology</h3><p>14 days, 4 services…</p></section>
      </section>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.2.1/dist/reveal.js"></script>
  <script>
    Reveal.initialize({
      hash: true,        // deep-link to slides
      slideNumber: true,
      transition: 'slide'
    });
  </script>
</body>
</html>
```

## Speaker notes, themes, fragments

- **Notes** (press `S` for speaker view): add `<aside class="notes">…</aside>`
  inside a slide.
- **Themes**: swap the theme CSS. For a **light** deck use `white` (clean) or
  `serif` (academic/scientific). Dark options: `black`, `league`, `night`,
  `dracula`. To align a deck with the report design language, use `white` and
  override reveal's CSS variables, e.g.
  `:root{ --r-background-color:#fff; --r-main-color:#14181f; --r-link-color:#1b4d8a;
  --r-main-font:Georgia,serif; --r-heading-font:system-ui,sans-serif; }`.
- **Fragments**: `class="fragment"` reveals an element on the next click; add
  `fade-in`, `fade-up`, `highlight-red`, etc. for effects.

## Putting other libraries inside slides

You can use Chart.js, Grid.js, KaTeX, or Mermaid inside slides — initialize
them after `Reveal.initialize`. For content that must render only when its slide
is shown (charts can mis-size on hidden slides), hook the slide-change event:

```html
<section data-chart>
  <h2>Latency over time</h2>
  <canvas id="latencyChart" width="800" height="400"></canvas>
</section>
<script>
  Reveal.on('slidechanged', (e) => {
    if (e.currentSlide.hasAttribute('data-chart')) {
      // create the Chart.js chart here, once
    }
  });
</script>
```

## Export to PDF

Append `?print-pdf` to the URL and use the browser's Print → Save as PDF (set
margins to none, enable background graphics). Optionally include the print CSS:
`reveal.js@5.2.1/css/print/pdf.css`.

## Gotchas

- Plugins (Markdown, Highlight, Math, Notes) are separate scripts under
  `dist/plugin/...`; register them in the `plugins:` array of `initialize`.
- Keep one idea per slide; reveal makes it tempting to overpack. Apply
  [typography-and-layout.md](typography-and-layout.md) per slide.
- Reference: https://revealjs.com/
