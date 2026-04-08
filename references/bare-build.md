# bare-build Deep-Dive Guide

Use this when the app needs packaging, standalone binaries, native runtime targets, or platform-specific build output for Bare apps.

Last reviewed: Wednesday, April 8, 2026.

## What bare-build is for
bare-build packages JavaScript applications as native application bundles or standalone executables for desktop and mobile. It is the build step that turns a worker-first app into a distributable artifact.

Use it when you need:
- app packaging
- standalone executables
- per-platform builds
- runtime selection for desktop/mobile targets

## API surface to know

### Programmatic API
```js
const build = require('bare-build')
for await (const resource of build(entry, preflight, options)) {}
```

Helpful options:
- `name`, `version`, `author`, `description`
- `icon`, `identifier`, `manifest`, `resources`
- `base`, `hosts`, `out`, `runtime`
- `standalone`, `package`, `sign`

### CLI surface
```sh
bare-build [flags] <entry>
```

Useful flags:
- `--host`
- `--icon`
- `--identifier`
- `--runtime`
- `--standalone`
- `--package`
- `--sign`

## Common usage patterns

### 1) Build per-target artifacts
Use `hosts` or `--host` values to produce the artifacts needed for desktop, mobile, or cross-platform release pipelines.

### 2) Choose the correct runtime
Portable runtimes are good for CLI-like workflows. Native GUI apps should use a platform-specific runtime when needed.

### 3) Keep packaging outside the worker host
The worker host should not know how the app is packaged. Packaging is a build concern.

### 4) Pair with bare-link for native addons
When addons are linked ahead of time, build output should match the linked addon strategy.

## bare-build in the Bare worker-based architecture

### Recommended placement
- shared core: no direct dependency
- worker host: the code that runs inside the runtime
- build scripts: invoke bare-build for packaging

### Worker-host responsibilities
The worker host should:
- remain package-agnostic
- not hardcode build flags or target matrices
- stay valid whether launched from source or packaged output

### Build-script responsibilities
Build scripts should:
- select target hosts
- choose runtime integration
- produce output packages and standalone binaries
- sign artifacts when needed

## Minimal build-script shape
```js
import build from 'bare-build'

for await (const resource of build('src/bootstrap/desktop.js', null, {
  hosts: ['darwin-arm64', 'darwin-x64'],
  package: true,
  standalone: false
})) {
  console.log(resource)
}
```

## Practical rules
- Keep runtime selection in the build layer
- Use the right host targets for each platform
- Package after the worker host is already correct
- Use `--linked` workflows when mobile/native addons require it
- Keep build concerns out of shared core and worker logic

## Good fit app types
- desktop app packaging
- mobile app packaging
- release automation
- standalone binaries
- platform-specific distribution
