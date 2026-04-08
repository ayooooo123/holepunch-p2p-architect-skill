# Bare Runtime Deep-Dive Guide

Use this when you need the prebuilt Bare binaries package, runtime lookup, or a spawn helper for desktop, mobile, or packaging flows.

Last reviewed: Wednesday, April 8, 2026.

## What bare-runtime is for
bare-runtime distributes prebuilt Bare binaries for macOS, iOS, Linux, Android, and Windows. It is not the runtime itself; it is the locator/spawn helper around the runtime binary.

Use it when you need:
- a portable way to find the correct Bare binary for a target
- a spawn helper for launching Bare in build/test flows
- tooling around platform-specific runtime bootstrap

## API surface to know

### Resolve a binary path
```js
const prebuild = runtime([referrer][, options])
```

Options:
- `platform`
- `arch`

### Spawn a runtime process
```js
const process = spawn([referrer][, options])
```

Options:
- `platform`
- `arch`
- `args`

## Common usage patterns

### 1) Select the correct runtime for the host target
Use `runtime()` when a build or bootstrap script needs the exact Bare binary path for the current platform.

### 2) Spawn the runtime in packaging or development scripts
Use `spawn()` when a script should launch the Bare binary with a target entrypoint.

### 3) Keep runtime selection outside app logic
The worker host should not care how the binary was found. Runtime resolution belongs in bootstrap, build, or packaging layers.

## bare-runtime in the Bare worker-based architecture

### Recommended placement
- shared core: no direct dependency
- worker host: runs inside Bare once bootstrapped
- shell adapter or build script: uses bare-runtime to locate/spawn the binary

### Worker-host responsibilities
The worker host should:
- assume it is already running in Bare
- avoid runtime discovery logic
- focus on app behavior, transport, and storage

### Bootstrap responsibilities
The bootstrap layer should:
- locate the right runtime binary
- spawn the process or hand off execution
- keep platform-specific selection out of shared core

## Minimal bootstrap shape
```js
import { runtime, spawn } from 'bare-runtime'

export function launchBareApp (entry, args = []) {
  const binary = runtime(import.meta.url, { platform: Bare.platform, arch: Bare.arch })
  return spawn(binary, { args: [entry, ...args] })
}
```

## Practical rules
- Use fixed versions for reproducible prebuilds
- Keep runtime lookup in build/bootstrap code
- Use the spawn helper for scripts and launchers
- Keep worker-host logic independent of the runtime locator

## Good fit app types
- launcher scripts
- cross-platform bootstrap helpers
- packaging pipelines
- runtime-aware tooling
