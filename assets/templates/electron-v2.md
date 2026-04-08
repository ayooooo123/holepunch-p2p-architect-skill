# Electron + Pear Runtime v2 Scaffold

Use this as the canonical desktop template when the app follows the current `hello-pear-electron` and `pear-runtime` pattern.

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
```

## Core principle
Electron owns the shell. pear-runtime owns the embedded runtime host and update flow. The worker owns the app behavior.

## package.json shape

```json
{
  "name": "hello-p2p-desktop",
  "productName": "HelloP2P",
  "version": "1.0.0",
  "upgrade": "pear://<upgrade-link>",
  "type": "commonjs",
  "main": "electron/main.js",
  "private": true,
  "scripts": {
    "lint": "prettier --check . && lunte",
    "format": "prettier --write . && lunte --fix",
    "start": "electron-forge start -- --no-updates",
    "package": "electron-forge package",
    "make:darwin": "electron-forge make --platform=darwin",
    "make:win32": "electron-forge make --platform=win32",
    "make:linux": "electron-forge package && ./scripts/build-app-image.sh"
  },
  "dependencies": {
    "paparam": "^1.10.0",
    "pear-runtime": "^1.1.1",
    "which-runtime": "^1.3.2"
  }
}
```

## electron/main.js
Use the main process to create the runtime host, manage storage, and launch the worker.

```js
const { app, BrowserWindow, ipcMain } = require('electron')
const PearRuntime = require('pear-runtime')

const pear = new PearRuntime({
  dir,
  app: getAppPath(),
  version,
  upgrade,
  name: productName,
  updates
})

const worker = pear.run(require.resolve('../workers/main.js'), [pear.storage])
```

## electron/preload.js
Expose only a minimal bridge:
- `pkg()`
- `applyUpdate()`
- `appRestart()`
- `startWorker()`
- worker stdout/stderr/IPC listeners
- worker IPC write helper
- update event listeners

## renderer/app.js
Use the renderer for UI and event display only.

## workers/main.js
Use the worker for app logic and `Bare.IPC`.

```js
Bare.IPC.on('data', (data) => console.log(data.toString()))
Bare.IPC.write('Hello from worker')
console.log('Application storage:', Bare.argv[2])
```

## Rules
- keep business logic out of the shell
- keep preload narrow
- keep updates in the main process
- keep storage, discovery, and replication in the worker
- keep the worker portable across desktop shells
