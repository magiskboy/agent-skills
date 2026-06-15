---
description: KaTeX — fast, high-quality rendering of math / scientific notation (LaTeX) in HTML reports. Use for equations, physics, chemistry, formulas.
---

# KaTeX — math & scientific notation

Use to render **LaTeX math** (equations, physics, chemistry via `mhchem`,
statistics) crisply and fast. Prefer KaTeX over MathJax for reports — it's
smaller and renders synchronously.

- CDN version pinned here: **0.16.22** (check for newer 0.16.x / 0.17.x).
- The **auto-render** extension scans the page for `$…$` / `$$…$$` delimiters so
  you can write math inline in your HTML, just like in Markdown.

## Setup with auto-render

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/auto-render.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },   // list $$ BEFORE $
        { left: '$',  right: '$',  display: false },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false },
      ],
      throwOnError: false,
    });
  });
</script>
```

Then write math directly in the body:

```html
<p>The p99 estimator is $x_{\lceil 0.99\,n \rceil}$ over sorted samples.</p>

<p>Standard deviation:</p>
$$ \sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2} $$
```

> Order matters: put the `$$` rule **before** the `$` rule, otherwise `$$` is
> mistaken for an empty inline expression.

## Render a single expression (no scanning)

```html
<span id="eq"></span>
<script>
  katex.render("E = mc^2", document.getElementById("eq"), { displayMode: true });
</script>
```

## Chemistry with mhchem

Add the extension to enable `\ce{...}`:

```html
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/mhchem.min.js"></script>
```

```html
<p>Combustion: $\ce{CH4 + 2 O2 -> CO2 + 2 H2O}$</p>
```

## Gotchas

- Requires the **HTML5 doctype** (`<!DOCTYPE html>`) or glyphs may misalign.
- Escape backslashes when you build delimiter strings in JS (`'\\['` not `'\['`).
- Auto-render runs once; if you inject math later, call `renderMathInElement`
  again on the new container.
- KaTeX supports a large but not complete TeX subset; if `throwOnError:false`,
  unsupported input shows in red instead of breaking the page — check the
  console.
- Reference: https://katex.org/ · supported functions:
  https://katex.org/docs/supported.html
