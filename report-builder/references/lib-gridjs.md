---
description: Grid.js — interactive data tables (sort, search, pagination, custom cell rendering). Use when a table needs interaction.
---

# Grid.js — interactive tables

Use when a table must be **sortable, searchable, or paginated**. For a small
static table, use plain `<table>` instead (see [html-builder.md](html-builder.md)).

- CDN version pinned here: **6.2.0** (check for newer 6.x).
- Global object is `gridjs` (UMD build): use `gridjs.Grid` and `gridjs.html`.
- Comes with a light default theme (`theme/mermaid.min.css`).

## Setup + minimal table

```html
<link href="https://cdn.jsdelivr.net/npm/gridjs@6.2.0/dist/theme/mermaid.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/gridjs@6.2.0/dist/gridjs.umd.js"></script>

<div id="report-table"></div>

<script>
  const rows = [
    { service: "payments", before: 1900, after: 240,  owner: "Mai" },
    { service: "checkout", before: 310,  after: 305,  owner: "Quân" },
    { service: "search",   before: 880,  after: 410,  owner: "Linh" },
  ];

  new gridjs.Grid({
    // Grid.js maps object data via column `id`; or pass plain arrays.
    columns: [
      { id: "service", name: "Service" },
      { id: "before",  name: "p99 before (ms)" },
      { id: "after",   name: "p99 after (ms)" },
      { id: "after", name: "Δ", sort: false,
        formatter: (_cell, row) => {
          const before = row.cells[1].data, after = row.cells[2].data;
          const pct = Math.round((after - before) / before * 100);
          const color = pct < 0 ? "#1f7a4d" : "#b4232a";
          return gridjs.html(`<span style="color:${color}">${pct}%</span>`);
        }
      },
      { id: "owner", name: "Owner" },
    ],
    data: rows,
    sort: true,
    search: true,
    pagination: { limit: 10 },
    fixedHeader: true,
    className: { table: "report-grid" },
  }).render(document.getElementById("report-table"));
</script>
```

> Object data: each column's `id` must match the object key. Two columns can
> reuse the same `id` (as with `after` above for a computed Δ). Alternatively
> pass `data` as an array of arrays in column order and drop the `id`s.

## Common features

- **Sorting**: `sort: true` (whole grid) or `sort: true/false` per column.
- **Search**: `search: true` adds a global search box. Server-side search is
  possible via the `server` option.
- **Pagination**: `pagination: { limit: 10 }` (also `summary`, `server`).
- **Custom cells**: `formatter: (cell, row, column) => gridjs.html('<b>…</b>')`.
  Always wrap HTML strings in `gridjs.html(...)` or they're shown as text.
- **Column widths**: prefer **percentages that sum to 100%** (e.g. `width: "27%"`)
  over fixed `px`. Percentages keep columns balanced and make the table fill its
  container; mixing `px` widths that sum to less than the container leaves an ugly
  trailing gap and over-wide text columns. Give wide text columns a larger share
  and numeric columns a smaller, equal share.
- **Right-aligning numbers**: Grid.js has no per-column align option; target
  cells with CSS, e.g. give the grid a class and style nth-child columns:
  `.report-grid td:nth-child(2), .report-grid td:nth-child(3){ text-align:right;
  font-variant-numeric:tabular-nums; }`.
- **Loading from JSON/AJAX**: use the `server` config
  (`server: { url, then: data => data.map(...) }`).
- **Localization**: the `language` option overrides search/pagination labels.

## Design tips for report tables

- Right-align numeric columns and keep decimals consistent (see
  [typography-and-layout.md](typography-and-layout.md)).
- The default `mermaid` theme is light and clean; restyle via CSS variables /
  the `className` config to match the report's accent and fonts.

## CSS conflicts (important inside reveal.js / themed pages)

Grid.js renders a **real `<table>`** with `<th class="gridjs-th">`/`<td class="gridjs-td">`.
A host theme that styles bare elements — e.g. reveal.js `white.css` has
`.reveal table td { padding:…; border-bottom:1px solid }` — has **higher specificity**
(`.reveal table td` = one class + two elements) than Grid.js's own class rules
(`.gridjs-td` = one class). So the host wins and the table looks cramped, with wrong
borders/padding and (if you also wrote `.reveal table{font-size:.5em}`) tiny text.

Fix: scope your generic table rules away from the grid and add **higher-specificity**
overrides for the grid:

```css
/* don't let the generic rule touch Grid.js */
.reveal table:not(.gridjs-table) { font-size:.5em; }

/* own the grid (specificity beats `.reveal table td`) */
.reveal table.gridjs-table { width:100%; margin:0; font-size:15px; border-collapse:collapse; }
.reveal .gridjs-table th.gridjs-th { background:var(--surface); border:none;
  border-bottom:2px solid #c7ccd3; padding:12px 16px; text-transform:none; }
.reveal .gridjs-table td.gridjs-td { border:none;
  border-bottom:1px solid var(--border); padding:11px 16px; }
.reveal #my-table td.gridjs-td:nth-child(3) { text-align:right; font-variant-numeric:tabular-nums; }
```

Outside reveal, the same idea applies to any framework/theme that styles bare `th`/`td`.

## Gotchas

- Object data needs matching column `id`s; if cells come up empty, that's why —
  or switch to array-of-arrays data.
- Inside reveal.js slides the grid renders fine (it doesn't depend on measuring a
  scaled container the way some grids do); build it when the slide is shown to be
  safe (see [lib-revealjs.md](lib-revealjs.md)).
- Use `gridjs.html()` for any HTML in a formatter; a raw string is escaped.
- Reference: https://gridjs.io/
