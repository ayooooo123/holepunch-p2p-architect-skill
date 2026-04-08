# Pear Desktop Scaffold

Use this for desktop apps that need a Pear shell, UI layer, and worker-hosted runtime.

## File tree

```text
package.json
src/
  bootstrap/
    desktop.js
  worker/
    host.js
  core/
    app.js
  adapters/
    pear-shell.js
config/
  pear.config.js
test/
  app.test.js
```

## Architecture note
- The shell is thin and only launches the worker host.
- The worker host owns peer discovery, storage orchestration, and replication lifecycle.
- Use the pear-runtime library or equivalent bootstrap instead of modeling the app around `pear run`.

## package.json shape

```json
{
  "name": "my-p2p-desktop-app",
  "private": true,
  "scripts": {
    "dev": "node src/bootstrap/desktop.js",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## src/bootstrap/desktop.js

```js
import { createWorkerHost } from '../worker/host.js'

const host = createWorkerHost({
  storage: {},
  transport: {},
  log: console.log
})

host.start()
```

## config/pear.config.js
Use this file for app metadata and update behavior.

```js
export default {
  name: 'my-p2p-desktop-app',
  version: '0.1.0',
  main: 'src/bootstrap/desktop.js'
}
```

## Desktop-specific rules
- keep shell code outside shared core
- keep IPC in the adapter layer
- route UI events to the worker host
- add hot reload or inspect hooks only if the app needs them
