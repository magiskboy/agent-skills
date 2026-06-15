---
description: Prism.js — syntax highlighting for source code blocks in HTML reports. Use when showing code that should be readable and highlighted.
---

# Prism.js — code highlighting

Use to make **source code** in an HTML report readable with syntax highlighting,
line numbers, and copy buttons. For a tiny inline snippet, plain
`<code>` is enough.

- CDN version pinned here: **1.29.0**.
- Prism highlights `<pre><code class="language-XXX">` blocks automatically on
  load. Always HTML-escape the code (`<` → `&lt;`, `&` → `&amp;`).

## Setup + highlighted block

```html
<!-- Light themes (default for reports): prism.min.css (light) or prism-coy.
     Dark options: prism-tomorrow, prism-okaidia. Pick one whose contrast meets AA. -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css">

<pre><code class="language-python">def p99(latencies: list[float]) -&gt; float:
    s = sorted(latencies)
    return s[int(0.99 * (len(s) - 1))]
</code></pre>

<!-- Core + the languages you actually use (autoloader can fetch the rest) -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
```

The **autoloader** plugin pulls the right language grammar on demand, so you
don't have to list every `prism-<lang>.js`. If you prefer explicit control, load
specific components instead, e.g.
`components/prism-python.min.js`, `prism-bash.min.js`, `prism-json.min.js`.

## Useful plugins

Add the plugin CSS in `<head>` and JS before `</body>`:

- **Line numbers**: add class `line-numbers` to `<pre>`, include
  `plugins/line-numbers/prism-line-numbers.min.{css,js}`.
- **Copy to clipboard**: include
  `plugins/toolbar/prism-toolbar.min.{css,js}` then
  `plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js`.
- **Highlight specific lines**: add `data-line="3,7-9"` on `<pre>` with the
  `line-highlight` plugin.

```html
<pre class="line-numbers" data-line="3"><code class="language-javascript">const total = items
  .filter(i =&gt; i.active)
  .reduce((a, i) =&gt; a + i.cost, 0); // highlighted line
</code></pre>
```

## Highlighting code added dynamically

If you inject code after page load, re-run Prism:

```js
Prism.highlightAll();            // or Prism.highlightElement(el)
```

## Gotchas

- **Escape the code.** Unescaped `<` will break the markup. When generating the
  report programmatically, run the source through an HTML-escape step.
- Default to a **light** theme (`prism.min.css` / `prism-coy`) to match a light
  report; only use a dark theme if the whole report is dark. Either way, check
  contrast meets AA against the page background.
- Don't over-highlight — keep examples short and focused (see
  [typography-and-layout.md](typography-and-layout.md)).
- Reference: https://prismjs.com/
