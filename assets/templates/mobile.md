# Bare / BareKit Mobile Scaffold

Use this for apps that need to run on-device with Bare or BareKit on iOS or Android.

## File tree

```text
package.json
src/
  app.js
  runtime.js
  core/
    app.js
  adapters/
    mobile.js
  native-bridge.js
config/
  mobile.config.js
test/
  app.test.js
```

## package.json shape

```json
{
  "name": "my-p2p-mobile-app",
  "private": true,
  "scripts": {
    "dev": "bare src/app.js",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## src/app.js

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

## src/runtime.js
Use this for runtime-specific wiring and lifecycle handling.

```js
export function getRuntimeName () {
  return globalThis.Bare ? 'bare' : 'unknown'
}
```

## config/mobile.config.js
Keep native-specific settings here.

```js
export default {
  name: 'my-p2p-mobile-app',
  version: '0.1.0'
}
```

## Mobile-specific rules
- keep lifecycle and background handling in the adapter layer
- keep native bridge code out of shared core
- preserve discovery handles for as long as replication is needed
- verify resume/suspend behavior explicitly
