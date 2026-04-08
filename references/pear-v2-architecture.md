# Pear v2 Architecture Guide

Use this guide when building a modern desktop app with Electron + pear-runtime.

Last reviewed: Wednesday, April 8, 2026.

## The v2 shape
The new standard is:
- Electron main process for window and lifecycle management
- preload as the only bridge into the renderer
- renderer for UI only
- Bare worker host for app behavior
- pear-runtime for storage, worker launch, and update coordination

## Canonical file layout
```text
package.json
electron/
  main.js
  preload.js
renderer/
  index.html
  app.js
workers/
  main.js
```

## What goes where

### electron/main.js
Owns:
- app startup
- storage directory selection
- `new PearRuntime(...)`
- worker process launch
- updater events
- restart / deep-link / single-instance handling

### electron/preload.js
Owns:
- a minimal `bridge`
- update notifications
- worker stdout/stderr/IPC forwarding
- worker write helpers

### renderer/app.js
Owns:
- UI rendering
- event display
- update button / user interaction
- no direct runtime or filesystem work

### workers/main.js
Owns:
- business logic
- peer discovery
- storage and replication
- protocol handling
- `Bare.IPC`

## Recommended runtime flow
1. Read package metadata.
2. Resolve the packaged app path when packaged.
3. Create a PearRuntime instance with `dir`, `app`, `version`, `upgrade`, and `name`.
4. Launch the Bare worker with `pear.run(require.resolve('./workers/main.js'), [pear.storage])`.
5. Wire updater events to the renderer.
6. Apply the update and restart from the shell.

## Design rules
- Keep business logic out of Electron main, preload, and renderer.
- Keep the worker host independent from Electron so it can be reused elsewhere.
- Pass storage and runtime configuration into the worker rather than reading shell globals.
- Keep preload small and explicit.
- Treat `pear-runtime` as the runtime host, not the app architecture itself.

## Why this matters
This pattern makes the shell swappable, keeps the worker portable, and preserves the one-shot goal: the repo can be generated with the same core logic across desktop shells while the shell handles only the v2 launch/update path.
