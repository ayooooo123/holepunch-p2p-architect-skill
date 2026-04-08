# Hypercore Deep-Dive Guide

Use this when the app needs an append-only log, sparse replication, or a durable replicated source of truth inside the worker-host architecture.

Last reviewed: Wednesday, April 8, 2026.

## What Hypercore is for
Hypercore is the base log primitive for ordered, verifiable data streams. In worker-first apps, the worker host should own Hypercore instances and expose higher-level app behavior to shells through adapters.

Use Hypercore when you need:
- an append-only event log
- sparse replication of only the blocks a peer needs
- durable local persistence with network sync
- a base layer for Hyperbee or higher-level indexed views

## API surface to know

### Constructor
```js
const core = new Hypercore(storage, [key], [options])
```

Key concepts:
- `storage`: directory or storage implementation for local data and metadata
- `key`: the public key for an existing core, if opening one
- `options`: value encoding, encryption, writable/readable behavior, and peer behavior

Common options worth knowing:
- `valueEncoding`: usually `json`, `utf-8`, or `binary`
- `keyPair`: explicit keypair when the worker host needs deterministic identity
- `encryption`: block encryption key when the data should stay private
- `onwait`: hook for waiting downloads
- `writable`: disable writes for follower peers
- `allowFork`: keep in mind if your app can tolerate log forks

### Lifecycle and inspection
- `await core.ready()` to open the core before relying on synchronous properties
- `core.on('ready')` when the core has opened
- `core.on('close')` when it is fully closed
- `core.key`, `core.discoveryKey`, `core.length`, `core.signedLength`, `core.contiguousLength`, `core.readable`, `core.writable`

### Read/write operations
- `await core.append(...)` to add blocks
- `await core.get(index)` to read a block
- `await core.head()` / related read helpers when you need the most recent data
- `await core.truncate(length)` when the log needs pruning or rollback behavior

### Replication and discovery hooks
- `const stream = core.replicate(isInitiatorOrStream, opts)` to replicate over a transport
- `const done = core.findingPeers()` to tell Hypercore that discovery is in progress
- `core.setActive(true/false)` to control whether the core should linger for background downloading
- `core.on('append')`, `core.on('peer-add')`, `core.on('peer-remove')` for sync-aware UI or logging

### Extensions and higher-level composition
- `core.registerExtension(name, handlers)` exists but is legacy-style; prefer Protomux for new protocols
- Many apps should layer Hyperbee or Autobase on top of Hypercore rather than building ad hoc indexes manually

## Common usage patterns

### 1) Event log for the app core
Use one Hypercore as the durable append-only log of user actions, peer events, or replicated records.

Pattern:
- append normalized events in the worker host
- derive state in shared core logic
- persist local cursor / metadata alongside the core
- replay on startup to rebuild app state

### 2) Public discovery key, private write key
Expose `discoveryKey` for peer discovery without leaking the signing key. Keep the writer key only in the worker host or secure storage layer.

### 3) Sparse replication + active state
Mark the core active only while the app needs live syncing. In mobile or suspended contexts, deactivate cleanly and re-activate on resume.

### 4) Hypercore as the source for Hyperbee
For apps that need fast lookups, keep Hypercore as the immutable log and build a Hyperbee index in the worker host or a derived view.

## Hypercore in the Bare worker-based architecture

### Recommended placement
- shared core: schema, reducers, validation, merge rules
- worker host: Hypercore creation, storage, replication, lifecycle, and peer management
- shell adapter: display state, route user actions, and forward lifecycle events

### Worker-host responsibilities
The worker host should:
- open the core
- attach to transport
- call `findingPeers()` during discovery windows
- manage `setActive()` across foreground/background changes
- persist enough metadata to resume replication after restart

### Shell responsibilities
The shell should:
- boot the worker host
- translate UI/CLI/mobile events into messages
- stay free of data-model and replication logic

## Minimal worker-host shape
```js
import Hypercore from 'hypercore'

export async function createFeedHost ({ storage, transport, log }) {
  const core = new Hypercore(storage)
  await core.ready()

  const stopFinding = core.findingPeers()
  const discovery = transport.join(core.discoveryKey)

  discovery.on('connection', async (socket, details) => {
    const stream = core.replicate(details.client, { live: true })
    socket.pipe(stream).pipe(socket)
  })

  return {
    async appendEvent (event) {
      await core.append(event)
    },
    async stop () {
      stopFinding()
      discovery.destroy?.()
      await core.close()
    }
  }
}
```

## Practical rules
- Prefer `corestore` when an app uses many Hypercores
- Prefer `valueEncoding: 'json'` only when the data model is stable and small
- Use `await core.ready()` before reading synchronous properties in startup code
- Keep replication lifecycle in the worker host, not in UI code
- Use Protomux for custom messaging, not `registerExtension`, for new systems

## Good fit app types
- feeds
- activity logs
- append-only event timelines
- replicated metadata indexes
- durable event sourcing inside a worker host
