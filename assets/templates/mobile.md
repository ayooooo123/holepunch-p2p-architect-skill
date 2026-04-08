# Bare / BareKit Mobile Scaffold

Use this for apps that need to run on-device with Bare or BareKit on iOS or Android.

## File tree

```text
package.json
src/
  bootstrap/
    mobile.js
  worker/
    host.js
  core/
    app.js
  adapters/
    mobile-shell.js
    native-bridge.js
config/
  mobile.config.js
test/
  app.test.js
```

## Architecture note
- The mobile shell handles lifecycle and native wiring.
- The worker host owns peer discovery, storage, and replication.
- Keep BareKit and native bridge code outside shared core.
- Keep discovery handles alive across suspend/resume cycles.
- If the app also has a desktop shell, keep the worker host compatible with the Electron v2 pattern.

## package.json shape

```json
{
  "name": "my-p2p-mobile-app",
  "private": true,
  "scripts": {
    "dev": "node src/bootstrap/mobile.js",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## src/bootstrap/mobile.js

```js
import { createWorkerHost } from '../worker/host.js'

const host = createWorkerHost({
  storage: {},
  transport: {},
  log: console.log
})

host.start()
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
