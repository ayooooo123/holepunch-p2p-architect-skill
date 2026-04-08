# Bare Worker Scaffold

Use this as the default shape for one-shot P2P app generation.

## Core principle
The worker host owns application behavior. The shell only boots the worker, routes platform-specific events, and renders UI or CLI output.

## File tree

```text
package.json
src/
  core/
    app.js
    protocol.js
    state.js
  worker/
    index.js
    lifecycle.js
    host.js
  bootstrap/
    desktop.js
    terminal.js
    mobile.js
  adapters/
    storage.js
    transport.js
    shell.js
config/
  pear.config.js
  mobile.config.js
test/
  app.test.js
scripts/
  build.js
  package.js
  release.js
```

## package.json shape

```json
{
  "name": "my-p2p-worker-app",
  "private": true,
  "scripts": {
    "dev": "node src/bootstrap/terminal.js",
    "test": "node --test",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## src/worker/host.js
Keep the worker host thin and adapter-driven.

```js
import { createAppCore } from '../core/app.js'

export function createWorkerHost ({ storage, transport, log }) {
  const core = createAppCore({ storage, transport, log })

  return {
    start () {
      core.start()
    },
    stop () {
      core.stop?.()
    },
    handleMessage (message) {
      core.handleEvent(message)
    }
  }
}
```

## src/bootstrap/terminal.js
Use the bootstrap layer to launch the worker host.

```js
import { createWorkerHost } from '../worker/host.js'

const host = createWorkerHost({
  storage: {},
  transport: {},
  log: console.log
})

host.start()
```

## Runtime guidance
- Prefer the pear-runtime library or equivalent runtime bootstrap for Pear shells.
- Keep the same worker host across desktop, terminal, and mobile.
- Put only the shell-specific setup in `bootstrap/*.js`.
- If an app needs platform behavior, wrap it in an adapter instead of branching in core.

## What to avoid
- `pear run` as the primary architecture model
- platform globals in core
- UI state stored in the worker host
- direct filesystem access in the shared core
- transport setup buried inside UI code
