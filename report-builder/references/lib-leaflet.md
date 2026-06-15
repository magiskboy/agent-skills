---
description: Leaflet — interactive maps and geospatial data (markers, popups, GeoJSON, choropleth) in HTML reports.
---

# Leaflet — maps & geospatial data

Use for **interactive maps**: locations, routes, GeoJSON overlays, choropleths.
For a single static location, a screenshot may be lighter — use Leaflet when
pan/zoom or data layers matter.

- CDN version pinned here: **1.9.4** (current stable).
- Needs both the CSS and JS, a sized container, and a tile source.

## Setup + map with a marker

```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<figure>
  <div id="map" style="height:420px; width:100%; border-radius:8px;"></div>
  <figcaption>Figure: incident locations, last 30 days.</figcaption>
</figure>

<script>
  const map = L.map('map').setView([21.0278, 105.8342], 12); // Hà Nội

  // OpenStreetMap tiles — attribution is REQUIRED by the tile terms.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  L.marker([21.0278, 105.8342])
    .addTo(map)
    .bindPopup('<b>HQ</b><br>3 incidents')
    .openPopup();
</script>
```

## GeoJSON overlay & simple choropleth

```js
fetch('regions.geojson')
  .then(r => r.json())
  .then(geo => {
    L.geoJSON(geo, {
      style: f => ({
        color: '#374151', weight: 1,
        fillColor: colorFor(f.properties.value),
        fillOpacity: 0.6,
      }),
      onEachFeature: (f, layer) =>
        layer.bindPopup(`${f.properties.name}: ${f.properties.value}`),
    }).addTo(map);
  });

function colorFor(v) {
  return v > 100 ? '#7f1d1d' : v > 50 ? '#dc2626' : v > 10 ? '#f59e0b' : '#16a34a';
}
```

Add a legend with a custom control (`L.control({position:'bottomright'})`) so the
color scale is readable — never rely on color alone (see
[typography-and-layout.md](typography-and-layout.md)).

## Fit the view to your data

```js
const group = L.featureGroup([m1, m2, m3]).addTo(map);
map.fitBounds(group.getBounds().pad(0.2));
```

## Gotchas

- **Sized container**: the `#map` div needs an explicit height or the map is
  invisible. If the map is created while hidden (tabs, reveal.js slides), call
  `map.invalidateSize()` once it becomes visible.
- **Attribution is mandatory** for OSM tiles; keep it. For heavy use or custom
  styling, use a tile provider with an API key (MapTiler, Mapbox, Stadia).
- Coordinates are `[lat, lng]` (latitude first) — a common mistake.
- Tiles need network access; for offline reports, note the dependency or use a
  static map image instead.
- Reference: https://leafletjs.com/
