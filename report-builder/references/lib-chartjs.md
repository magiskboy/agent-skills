---
description: Chart.js — charts and plots (line, bar, pie, scatter, etc.). Use for data visualization in HTML reports.
---

# Chart.js — charts & plots

Use for **data visualization**: trends, comparisons, distributions. For a single
number, use text; for a table of numbers that needs interaction, use Grid.js.

- CDN version pinned here: **4.4.7** (check for newer 4.x).
- Charts render into a `<canvas>`. Wrap the canvas in a sized container for
  responsiveness.

## Setup + a line chart

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>

<figure>
  <div style="position:relative; height:360px; width:100%;">
    <canvas id="latencyChart"></canvas>
  </div>
  <figcaption>Figure 1: p99 latency dropped after the Jun 3 revert.</figcaption>
</figure>

<script>
  const ctx = document.getElementById('latencyChart');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jun 1','Jun 2','Jun 3','Jun 4','Jun 5','Jun 6'],
      datasets: [{
        label: 'p99 latency (ms)',
        data: [250, 248, 1900, 1850, 240, 238],
        borderColor: '#2563eb',
        backgroundColor: 'rgba(37,99,235,.15)',
        fill: true,
        tension: 0.3,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,   // honor the container height
      plugins: {
        legend: { position: 'top' },
        title:  { display: true, text: 'p99 latency over time' },
      },
      scales: { y: { beginAtZero: true, title: { display: true, text: 'ms' } } }
    }
  });
</script>
```

## Other chart types

Change `type` and shape `data` accordingly:

```js
// Bar
new Chart(ctx, { type: 'bar', data: {
  labels: ['payments','checkout','search'],
  datasets: [{ label: 'Δ p99 (ms)', data: [-1660, -5, -470],
               backgroundColor: ['#16a34a','#9ca3af','#16a34a'] }]
}, options: { responsive:true, maintainAspectRatio:false }});

// Doughnut / pie
new Chart(ctx, { type: 'doughnut', data: {
  labels: ['Compute','Storage','Network'],
  datasets: [{ data: [62, 23, 15] }]
}});

// Scatter
new Chart(ctx, { type: 'scatter', data: {
  datasets: [{ label: 'load vs latency',
    data: [{x:10,y:120},{x:55,y:240},{x:90,y:1900}] }]
}, options: { scales: { x: { type:'linear' } } }});
```

## Design tips for report charts

- One accent color for the primary series; gray for context/secondary. Use red
  vs green only to mean bad vs good (and add labels — don't rely on color alone).
- Always label axes with units; give the chart a title or a figure caption that
  states the **takeaway** (see [typography-and-layout.md](typography-and-layout.md)).
- Start bar/area y-axes at zero; truncated axes mislead.
- Keep it legible: few series, direct labels over a crowded legend when possible.

## Gotchas

- `maintainAspectRatio:false` + a sized wrapper is the reliable way to control
  height; otherwise canvas can grow unbounded.
- For dark mode, set `Chart.defaults.color` and grid colors from your CSS vars.
- Inside reveal.js, create the chart when its slide is shown (see
  [lib-revealjs.md](lib-revealjs.md)).
- Reference: https://www.chartjs.org/docs/latest/
