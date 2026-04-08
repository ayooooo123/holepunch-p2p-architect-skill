# Pear Terminal Scaffold

Use this for the quickest runnable P2P app shape and for text-first validation.

## File tree

```text
package.json
src/
  index.js
  cli.js
  core/
    app.js
  adapters/
    terminal.js
test/
  app.test.js
```

## package.json shape

```json
{
  "name": "my-p2p-terminal-app",
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

## src/index.js

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

## src/cli.js
Use for command parsing and lifecycle commands.

```js
export function parseArgs (argv) {
  return { argv }
}
```

## Terminal-specific rules
- keep the runtime surface small
- make startup deterministic
- expose a simple way to inspect state and replication
