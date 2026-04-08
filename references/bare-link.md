# bare-link Deep-Dive Guide

Use this when the app needs native addon linking ahead of time, especially for packaged Bare apps and mobile targets.

Last reviewed: Wednesday, April 8, 2026.

## What bare-link is for
bare-link is the native addon linker for Bare. It resolves addon builds into linked outputs so packaged apps, especially mobile ones, can load native code that has been linked ahead of time rather than discovered from disk at runtime.

Use it when you need:
- ahead-of-time addon linking
- mobile-safe native addon packaging
- linked addon outputs for `bare-pack`
- per-host linker orchestration

## API surface to know

### Programmatic API
```js
const link = require('bare-link')
for await (const resource of link(base, options)) {}
```

Important options:
- `hosts`
- `out`
- `preset`
- `sign`
- signing fields like `identity`, `keychain`, `subject`, `subjectName`, `thumbprint`

### CLI surface
```sh
bare-link [flags] [entry]
```

Useful flags:
- `--host`
- `--out`
- `--preset`
- `--sign`
- signing-related flags

## Common usage patterns

### 1) Link addons before packaging
Use bare-link when your app must ship with native addons already linked into the target artifact.

### 2) Pair with bare-pack
When bundling an app with native addons, use `bare-pack --linked` so addon specifiers resolve to linked outputs.

### 3) Keep linker logic out of the worker host
The worker host should consume the linked addon, not perform linking itself.

### 4) Target the exact hosts you plan to ship
Specify the host matrix explicitly so linked outputs match the intended runtime environment.

## bare-link in the Bare worker-based architecture

### Recommended placement
- shared core: no direct link dependency
- worker host: loads the linked addon if available
- build/package step: runs bare-link

### Worker-host responsibilities
The worker host should:
- assume linked addons are already present when packaged
- load addon exports in a host-friendly way
- stay agnostic about how linking happened

### Build-script responsibilities
Build scripts should:
- call bare-link before packaging
- target the correct host matrix
- feed linked outputs to bare-pack or bare-build as needed

## Minimal linking shape
```js
const link = require('bare-link')

for await (const resource of link('/path/to/module', { hosts: ['darwin-arm64', 'ios-arm64'] })) {
  console.log(resource)
}
```

## Practical rules
- Use `bare-link` for ahead-of-time addon linkage
- Keep linker workflows in build scripts
- Use `bare-pack --linked` for bundles that rely on linked addons
- Treat linked outputs as release artifacts, not source-of-truth code
- Keep worker code independent of the link step

## Good fit app types
- mobile Bare apps
- packaged desktop apps with native addons
- release pipelines
- cross-platform addon distribution
- worker-host apps with native binaries
