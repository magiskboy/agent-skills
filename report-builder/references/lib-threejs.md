---
description: Three.js — interactive 3D scenes/models in HTML reports. Use for 3D visualization, model viewers, spatial data.
---

# Three.js — interactive 3D

Use for **interactive 3D**: model viewers, 3D plots, spatial/scientific
visualization. This is the heaviest library here — only use it when 3D
interaction is genuinely the point; otherwise a rendered image or short video is
lighter.

- CDN version pinned here: **0.184.0** (check npm for newer).
- Modern Three.js is loaded via an **import map** (no build step). Always use the
  **same version** for `three` and `three/addons/`.

## Setup with import map + a rotating cube

```html
<style>
  #scene { width: 100%; height: 420px; display: block; }
</style>

<figure>
  <canvas id="scene"></canvas>
  <figcaption>Figure: drag to orbit, scroll to zoom.</figcaption>
</figure>

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.184.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.184.0/examples/jsm/"
  }
}
</script>

<script type="module">
  import * as THREE from 'three';
  import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

  const canvas = document.getElementById('scene');
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf3f4f6);

  const camera = new THREE.PerspectiveCamera(60, 1, 0.1, 100);
  camera.position.set(3, 2, 4);

  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true;

  scene.add(new THREE.AmbientLight(0xffffff, 0.6));
  const dir = new THREE.DirectionalLight(0xffffff, 1);
  dir.position.set(5, 5, 5);
  scene.add(dir);

  const cube = new THREE.Mesh(
    new THREE.BoxGeometry(1.5, 1.5, 1.5),
    new THREE.MeshStandardMaterial({ color: 0x2563eb })
  );
  scene.add(cube);

  function resize() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  addEventListener('resize', resize); resize();

  renderer.setAnimationLoop(() => {
    cube.rotation.y += 0.005;
    controls.update();
    renderer.render(scene, camera);
  });
</script>
```

## Loading a 3D model (glTF)

```js
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
new GLTFLoader().load('model.glb', (gltf) => scene.add(gltf.scene));
```

`.glb`/`.gltf` is the recommended format. For a single self-contained report,
either host the model alongside the HTML or build the geometry in code.

## Gotchas

- **Version match**: `three` and `three/addons/` must be the exact same version,
  or addons break.
- Set a real height on the canvas/container and handle resize, or you'll get a
  zero-size or stretched view.
- Respect `prefers-reduced-motion`: pause auto-rotation for users who opt out.
- WebGL won't run in a sandboxed/no-GPU environment; provide a fallback image and
  a one-line description of what the 3D shows.
- It's an ES module via import map — a normal `<script>` won't work.
- Reference: https://threejs.org/manual/
