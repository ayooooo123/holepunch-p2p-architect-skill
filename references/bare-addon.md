# bare-addon Deep-Dive Guide

Use this when the app needs to create or consume native Bare addons, or when the worker host depends on native code for performance or platform integration.

Last reviewed: Wednesday, April 8, 2026.

## What bare-addon is for
bare-addon is the template repository for creating Bare native addons. It pairs with bare-make, bare-link, and the Bare addon resolver so native code can be shipped and loaded correctly on each target host.

Use it when you need:
- native performance or platform bindings
- static or dynamic addon loading in Bare
- prebuilt addon distribution
- build system scaffolding for C/C++ bindings

## API surface to know

### Bare addon loading and resolution
From Bare and bare-module:
- `Bare.Addon.cache`
- `Bare.Addon.host`
- `Addon.resolve(specifier, parentURL[, options])`
- `Addon.load(url[, options])`
- `addon.exports`
- `require.addon()` / `import.meta.addon()` for addon-only loading
- `require.addon.resolve()` / `import.meta.addon.resolve()` for resolution

### bare-addon template workflow
- `bare-make generate [--debug]`
- `bare-make build`
- `bare-make install`
- `bare-make install --link`
- prebuild workflows for target hosts

### Dependency workflow
- use `cmake-fetch` for external native dependencies
- link native libraries in `CMakeLists.txt`
- use the repo template as the starting point for addon development

## Common usage patterns

### 1) Use require.addon in package exports
A common addon module shape is to export `require.addon()` from the JavaScript entrypoint.

### 2) Prebuild for each host
Compile bindings for all supported targets before publishing. Addon binaries are host-specific.

### 3) Link during development, copy for release
Use `bare-make install --link` for fast iteration, then ensure the final package contains real prebuilds.

### 4) Keep addon logic narrow
Addons should expose a small native surface and keep higher-level orchestration in JavaScript.

## bare-addon in the Bare worker-based architecture

### Recommended placement
- shared core: no direct native code
- worker host: consumes addon exports when needed
- addon repo: holds the native implementation and build workflow

### Worker-host responsibilities
The worker host should:
- load addon exports explicitly
- handle any addon lifecycle assumptions
- isolate native side effects from shell code
- keep native feature use optional when possible

### Shell responsibilities
The shell should:
- never directly manage native build outputs
- treat addons as host-level capabilities
- avoid mixing UI and native build logic

## Minimal addon consumer shape
```js
module.exports = require.addon()
```

## Practical rules
- Use `require.addon()` for addon entrypoints
- Use `bare-link` when the addon must be linked ahead of time
- Keep version bumps in sync with prebuild outputs
- Do not hide worker lifecycle logic inside native code
- Prefer simple addon APIs that are easy to consume from the worker host

## Good fit app types
- performance-critical parsing
- platform integration layers
- native crypto or media code
- custom bindings for Bare apps
- worker-hosted native modules
