# Hypercore Storage Deep-Dive Guide

Use this when the app needs the low-level storage engine behind Hypercore, or when you are working on atomic batch behavior, custom persistence, or direct storage introspection.

Last reviewed: Wednesday, April 8, 2026.

## What hypercore-storage is for
hypercore-storage is the RocksDB-backed storage engine that Hypercore 11 binds to for I/O. It exposes read batches, write batches, atomization, and core lifecycle helpers.

Use it when you need:
- direct control over Hypercore storage
- atomic batching across storage operations
- custom storage inspection or migration tools
- the storage backend for a worker-hosted Hypercore app

## API surface to know

### Storage instance
```js
const store = new Storage(dbOrPath)
```

Useful methods:
- `await store.createCore({ key, discoveryKey, manifest, keyPair, encryptionKey, ... })`
- `await store.resumeCore(discoveryKey)`
- `await store.hasCore(discoveryKey)`
- `store.createAtom()` creates an atomic batch
- `store.createCoreStream()` lists all cores
- `await store.close()` closes the storage instance

### Read batch API
```js
const rx = core.read()
```

Important behavior:
- read batch calls do not resolve until `rx.tryFlush()` is called
- methods include `getAuth`, `getHead`, `getSessions`, `getDependency`, `getHints`, `getBlock`, `getTreeNode`, `getBitfieldPage`, `getUserData`

### Write batch API
```js
const tx = core.write()
```

Important behavior:
- write batch methods buffer mutations until `await tx.flush()`
- methods include `setAuth`, `setHead`, `setSessions`, `setDependency`, `setHints`, `putBlock`, `deleteBlock`, `deleteBlockRange`, `putTreeNode`, `deleteTreeNode`, `deleteTreeNodeRange`, `putBitfieldPage`, `deleteBitfieldPage`, `deleteBitfieldPageRange`, `putUserData`, `deleteUserData`

### Atomization and sessions
- `const atom = store.createAtom()` for cross-core atomic changes
- `core.atomize(atom)` attaches a core to an atom
- `core.createSession(name, head)` creates a named branch/session
- `core.dependencies` lists the dependency tree
- `core.createBlockStream()`, `core.createTreeNodeStream()`, `core.createBitfieldStream()`, `core.createUserDataStream()` expose raw storage views

## Common usage patterns

### 1) Batch then flush
Treat write operations as buffered until flush time. This keeps persistence explicit and helps the worker host coordinate writes safely.

### 2) Atomize cross-core changes
If you need multiple Hypercores to commit together, create an atom and atomize the related cores before flushing.

### 3) Named sessions for branching
Use named sessions for branch-like workflows or migration checkpoints.

### 4) Storage as a private worker concern
Do not surface hypercore-storage directly to the shell. Put it under the worker host or a storage adapter.

## hypercore-storage in the Bare worker-based architecture

### Recommended placement
- shared core: storage schema, migration rules, validation
- worker host: storage engine, atom flush policy, session management
- shell adapter: never directly touches the storage engine

### Worker-host responsibilities
The worker host should:
- own the storage path
- create Hypercore instances through the storage engine or through Hypercore default storage helpers
- flush write batches explicitly
- manage atomization for grouped changes
- keep read/write coordination out of the UI thread

### Shell responsibilities
The shell should:
- request changes from the worker
- show sync or migration status
- avoid direct storage mutation

## Minimal worker-host shape
```js
import Storage from 'hypercore-storage'
import Hypercore from 'hypercore'

export async function createStorageHost ({ path, log }) {
  const store = new Storage(path)
  const core = new Hypercore(store)
  await core.ready()

  return {
    store,
    core,
    async stop () {
      await core.close?.()
      await store.close()
    }
  }
}
```

## Practical rules
- Call `rx.tryFlush()` for read batches
- Call `await tx.flush()` for write batches
- Use atoms when multiple core changes must commit together
- Keep storage logic inside the host or a dedicated adapter
- Prefer Hypercore helpers unless you truly need low-level storage access

## Good fit app types
- migration tools
- diagnostics and repair utilities
- custom data engines
- storage adapters
- advanced Hypercore host implementations
