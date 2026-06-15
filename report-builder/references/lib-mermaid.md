---
description: Mermaid.js — diagrams from text (flowcharts, sequence, class, state, ER, Gantt, mindmaps). Use for diagrams and mind maps in HTML (and Markdown).
---

# Mermaid.js — diagrams, flowcharts & mind maps

Use to render **diagrams written as text**: flowcharts, sequence, class, state,
ER, Gantt, and mind maps. In Markdown, fenced ```mermaid``` blocks render
natively on GitHub (see [md-builder.md](md-builder.md)); this file covers the
**HTML** setup and the diagram syntax for both.

- CDN version pinned here: **11** (ESM build; check for newer 11.x).
- Mermaid 11 ships as an **ES module**. Use `<script type="module">`.

## HTML setup

Put each diagram's source inside an element with class `mermaid`, then init:

```html
<pre class="mermaid">
flowchart LR
    A[Client] --> B{API Gateway}
    B -->|cache hit| C[(Redis)]
    B -->|miss| D[Payments service]
    D --> E[(Postgres)]
</pre>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default' });
  // Light reports: use 'default' or 'neutral'. ('dark'/'forest'/'base' also exist.)
  // For a scientific look, set fontFamily to match the report's heading font.
</script>
```

For finer control (e.g. to render after other scripts, or inside reveal.js
slides), initialize once with `startOnLoad: false` and call `await mermaid.run()`
yourself:

```html
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: false, theme: 'neutral' });  // light, low-chroma
  await mermaid.run({ querySelector: '.mermaid' });
</script>
```

## Diagram types (syntax samples)

**Sequence:**

```
sequenceDiagram
    participant U as User
    participant API
    U->>API: POST /checkout
    API-->>U: 200 OK (order id)
```

**Mind map** (great for brainstorming sections of a report):

```
mindmap
  root((p99 regression))
    Causes
      Sync call added
      Cold cache
    Impact
      Checkout SLO breach
    Fix
      Revert PR #812
```

**Gantt** (timelines / plans):

```
gantt
    title Rollout plan
    dateFormat YYYY-MM-DD
    section Phase 1
    Revert & verify   :done,   a1, 2026-06-05, 1d
    Canary 5%         :active, a2, 2026-06-06, 2d
    Full rollout      :        a3, after a2, 1d
```

State, class, and ER diagrams follow the same `<pre class="mermaid">` pattern —
just change the first keyword (`stateDiagram-v2`, `classDiagram`, `erDiagram`).

## Gotchas

- It's an **ES module**: a classic `<script src=...>` to the `.mjs` won't work —
  use `type="module"` and `import`.
- Indentation/leading whitespace inside the diagram matters; keep it clean.
- `securityLevel: 'strict'` (default) sanitizes labels; use `'loose'` only if you
  intentionally embed HTML in labels and trust the content.
- If you generate diagrams after load, call `mermaid.run()` again on the new
  nodes.
- Keep diagrams small and focused — a sprawling flowchart is unreadable (see
  [typography-and-layout.md](typography-and-layout.md)).
- Reference: https://mermaid.js.org/
