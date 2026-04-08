# Pear Terminal Scaffold

Use this for the quickest runnable P2P app shape and for text-first validation.

## File tree

```text
package.json
src/
  bootstrap/
    terminal.js
  worker/
    host.js
  core/
    app.js
  adapters/
    terminal-shell.js
test/
  app.test.js
```

## Architecture note
- The terminal shell is only a launcher and inspector.
- The worker host owns state, transport, and replication.
- Prefer the pear-runtime library or equivalent bootstrap layer instead of `pear run` as the mental model.

## package.json shape

```json
{
  "name": "my-p2p-terminal-app",
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

## src/bootstrap/terminal.js

```js
import { createWorkerHost } from '../worker/host.js'

const host = createWorkerHost({
  storage: {},
  transport: {},
  log: console.log
})

host.start()
```

## Terminal-specific rules
- keep the runtime surface small
- make startup deterministic
- expose a simple way to inspect state and replication
- keep all peer logic inside the worker host
