# Pear Desktop Scaffold

Use this for desktop apps that need an Electron shell, pear-runtime update handling, and a worker-hosted runtime.

## File tree

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
src/
  core/
    app.js
    protocol.js
    state.js
  adapters/
    storage.js
    transport.js
```

## Architecture note
- The Electron main process is the shell coordinator.
- The preload script exposes a narrow bridge.
- The renderer is UI only.
- The worker host owns peer discovery, storage orchestration, and replication lifecycle.
- Use the pear-runtime library for the runtime host and updater flow.

## package.json shape

```json
{
  "name": "my-p2p-desktop-app",
  "private": true,
  "type": "commonjs",
  "main": "electron/main.js",
  "scripts": {
    "dev": "electron-forge start -- --no-updates",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "electron-forge package",
    "release": "node scripts/release.js"
  }
}
```

## Electron shell rules
- keep shell code outside shared core
- keep IPC in the preload bridge
- route UI events to the worker host
- handle `updating` / `updated` in the main process and restart after `applyUpdate()`
- pass the packaged app path and storage dir into pear-runtime
