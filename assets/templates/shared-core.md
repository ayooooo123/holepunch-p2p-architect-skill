# Shared Core Scaffold

Use this when the app has reusable domain logic that must stay portable across Pear and Bare runtimes.

## Role in the worker-first architecture
The shared core is the pure logic layer that the worker host uses. It does not boot the runtime, create the shell, or manage platform lifecycle events.

## File tree

```text
src/
  core/
    app.js
    protocol.js
    state.js
    reducers.js
  worker/
    host.js
    lifecycle.js
  adapters/
    runtime.js
    storage.js
    transport.js

test/
  app.test.js
```

## package.json shape

```json
{
  "name": "my-p2p-app",
  "private": true,
  "scripts": {
    "test": "node --test",
    "dev": "node src/bootstrap/terminal.js",
    "build": "node scripts/build.js",
    "package": "node scripts/package.js",
    "release": "node scripts/release.js"
  }
}
```

## core/app.js

```js
export function createAppCore ({ storage, transport, log }) {
  const state = storage.readState?.() ?? { items: [] }

  return {
    start () {
      log?.('starting app core')
    },
    handleEvent (event) {
      state.items.push(event)
      storage.writeState?.(state)
      transport.broadcast?.(event)
    },
    stop () {
      storage.writeState?.(state)
    },
    getState () {
      return state
    }
  }
}
```

## protocol.js
Keep protocol shape stable and versioned.

```js
export const PROTOCOL_VERSION = 1
export const TOPIC = 'my-p2p-app:v1'
```

## state.js
Keep state updates deterministic and testable.

```js
export function reduceState (state, event) {
  return {
    ...state,
    items: [...state.items, event]
  }
}
```

## What to avoid
- direct use of `Pear`
- direct use of `Bare`
- direct UI code
- direct process/env checks in the core
- bootstrapping or lifecycle code in the shared core
