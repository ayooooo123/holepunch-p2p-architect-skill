# Pear Runtime API Guide

Use this when the app needs Pear desktop update coordination, a Bare worker host, or the newer v2 Electron shell layout.

Last reviewed: Wednesday, April 8, 2026.

## What Pear Runtime is for
Pear Runtime is the embedded runtime layer that keeps the shell thin and the worker host in charge of app behavior. In the v2 architecture, Electron handles UI, preload, and process lifecycle while pear-runtime owns storage, update state, and worker launch.

Use Pear Runtime when you need:
- a desktop shell for a P2P app
- app metadata, version, upgrade link, or storage path handling
- worker startup and IPC wiring
- update coordination and restart flow

## API surface to know

### Runtime constructor
Common options from the current repo and docs:
- `dir` - application data directory
- `app` - packaged app path, used for update application
- `name` - application name used by the runtime
- `version` - app version for update bookkeeping
- `upgrade` - Pear upgrade link
- `updates` - optional update toggle
- `storage` - optional explicit storage path
- `store` / `swarm` - optional paired Corestore + Hyperswarm injection; pass both together or neither
- `bootstrap` - optional bootstrap nodes

### Worker launch
`PearRuntime.run(entrypoint, args = [], opts = {})` starts a Bare worker and returns the IPC stream.

Inside the worker, the other end of the pipe is `Bare.IPC`.

### Lifecycle helpers
- `await pear.ready()` - wait for the runtime to finish initializing
- `pear.updater.on('updating', ...)` - update is in progress
- `pear.updater.on('updated', ...)` - update has landed and can be applied
- `pear.updater.applyUpdate()` - apply the downloaded update
- `await pear.close()` - shut down the embedded runtime cleanly

## V2 shell pattern
The new desktop pattern from `hello-pear-electron` is:
- Electron main process creates the app window and runtime host
- preload exposes a minimal `bridge`
- renderer is UI only
- `workers/main.js` is the Bare worker entrypoint
- update application and restart stay in the shell layer

### Main process responsibilities
- compute the storage directory
- create `new PearRuntime({ dir, app, version, upgrade, name, updates })`
- start workers with `pear.run(require.resolve('./workers/main.js'), [pear.storage])`
- forward updater events to the renderer
- handle app restart after `applyUpdate()`

### Renderer responsibilities
- display status and update state
- request worker start through preload
- read stdout/stderr/IPC from workers
- never touch Pear or Bare globals directly

### Worker responsibilities
- read storage path from `Bare.argv[2]`
- own peer discovery, storage, and replication
- send messages over `Bare.IPC`
- keep app logic out of the shell

## Example shell bootstrap
```js
const PearRuntime = require('pear-runtime')

const pear = new PearRuntime({
  dir,
  app,
  version,
  upgrade,
  name,
  updates
})

const worker = pear.run(require.resolve('./workers/main.js'), [pear.storage])
```

## Example worker bootstrap
```js
Bare.IPC.on('data', (data) => console.log(data.toString()))
Bare.IPC.write('Hello from worker')
console.log('Application storage:', Bare.argv[2])
```

## Practical rules
- Use Pear for launch, storage, and update coordination
- Keep the shell thin
- Keep the worker host portable across desktop and non-desktop shells
- Pass storage and runtime configuration into the worker instead of reading globals in core code
- Prefer explicit update restart handling in the shell layer

## Good fit app types
- Electron desktop apps
- Pear desktop apps
- update-aware apps
- apps that need storage-managed worker launch
