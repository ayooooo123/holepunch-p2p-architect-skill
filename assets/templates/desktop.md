# Pear Desktop Scaffold

Use this for desktop apps that need a Pear shell, UI layer, and update-aware runtime wiring.

## File tree

```text
package.json
src/
  main.js
  preload.js
  ui.js
  core/
    app.js
  adapters/
    pear.js
config/
  pear.config.js
test/
  app.test.js
```

## package.json shape

```json
{
  "name": "my-p2p-desktop-app",
  "private": true,
  "scripts": {
    "dev": "pear run .",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## src/main.js

```js
import { createAppCore } from './core/app.js'

const app = createAppCore({
  storage: {},
  transport: {},
  clock: () => Date.now(),
  log: console.log
})

app.start()
```

## src/preload.js
Keep the bridge small and explicit.

```js
export const api = {
  version: 1
}
```

## config/pear.config.js
Use this file for app metadata and update behavior.

```js
export default {
  name: 'my-p2p-desktop-app',
  version: '0.1.0',
  main: 'src/main.js'
}
```

## Desktop-specific rules
- keep shell code outside shared core
- keep IPC in the adapter layer
- add hot reload or inspect hooks only if the app needs them
