# Hyperdrive Deep-Dive Guide

Use this when the app needs a replicated file tree, file-like semantics, or blob-backed content stored alongside Hypercore data.

Last reviewed: Wednesday, April 8, 2026.

## What Hyperdrive is for
Hyperdrive is a secure, real-time distributed file system built on Corestore, Hypercore, Hyperbee, and Hyperblobs. In the worker-host architecture, the worker should own the drive and keep shell code limited to rendering and control flow.

Use Hyperdrive when you need:
- file sync or file-sharing apps
- folder-like trees over replicated storage
- versioned content and historical checkout
- blob-backed attachments with metadata

## API surface to know

### Constructor and lifecycle
```js
const drive = new Hyperdrive(store, [key])
await drive.ready()
await drive.close()
```

Key properties:
- `drive.corestore` the Corestore backing the drive
- `drive.db` the Hyperbee backing the file tree
- `drive.core` the Hypercore used by the database
- `drive.discoveryKey` the topic used for discovery
- `drive.contentKey` the Hyperblobs content key
- `drive.version` current version number
- `drive.writable` / `drive.readable`

### File and directory operations
- `await drive.put(path, buffer, [options])`
- `await drive.get(path, [options])`
- `await drive.entry(path, [options])`
- `await drive.del(path)`
- `await drive.symlink(path, linkname)`
- `for await (const file of drive.list(folder, [options])) {}`
- `const rs = drive.createReadStream(path)`
- `const ws = drive.createWriteStream(path, [options])`

### Versioning and space management
- `drive.checkout(version)` returns a read-only snapshot
- `await drive.truncate(version, [options])`
- `await drive.clear(path, [options])`
- `await drive.clearAll([options])`
- `await drive.purge()` removes all data
- `const batch = drive.batch()` then `await batch.flush()` for atomic mutations

### Discovery and replication
- `const done = drive.findingPeers()` to mark discovery activity
- `drive.replicate(isInitiatorOrStream)` to replicate over a transport
- `await drive.download(folder, [options])`
- `await drive.downloadDiff(version, folder, [options])`
- `await drive.downloadRange(dbRanges, blobRanges)`
- `const mirror = drive.mirror(out, [options])`
- `await drive.has(path)` checks local presence
- `await drive.getBlobs()` retrieves the Hyperblobs store
- `await drive.getBlobsLength(checkout)` inspects blob length at a version

## Common usage patterns

### 1) Real file trees over replicated content
Use Hyperdrive when users need file paths, directory listings, read/write streams, and a versioned file tree that can be replicated peer-to-peer.

### 2) Treat the drive as the source of truth for content
Keep path metadata and structure in Hyperdrive. Use Hyperblobs for the binary payloads that back entries.

### 3) Version-aware downloads
Use `downloadDiff` or `downloadRange` to prefetch specific subtrees and versions instead of pulling the entire drive.

### 4) Discovery lifecycle in the worker host
Call `findingPeers()` while a swarm is discovering peers, then clear it when that pass is done. Keep the discovery handle alive in the worker host.

## Hyperdrive in the Bare worker-based architecture

### Recommended placement
- shared core: file schema, metadata rules, sync policy, path validation
- worker host: Hyperdrive instance, Corestore, swarm, download lifecycle
- shell adapter: file picker UI, text UI, CLI commands, lifecycle controls

### Worker-host responsibilities
The worker host should:
- create one Corestore and one Hyperdrive per app area
- join `drive.discoveryKey` in Hyperswarm or a DHT transport
- manage `findingPeers()` and `replicate()`
- route writes through the worker, not directly from the shell
- keep blob lifecycle and cleanup logic in the host layer

### Shell responsibilities
The shell should:
- expose UI for files and folders
- forward edits and file actions
- show sync status
- avoid direct storage wiring

## Minimal worker-host shape
```js
import Corestore from 'corestore'
import Hyperdrive from 'hyperdrive'
import Hyperswarm from 'hyperswarm'

export async function createDriveHost ({ storage, log }) {
  const store = new Corestore(storage)
  const drive = new Hyperdrive(store)
  const swarm = new Hyperswarm()

  await drive.ready()
  const done = drive.findingPeers()
  const discovery = swarm.join(drive.discoveryKey, { client: true, server: true })

  swarm.on('connection', socket => {
    drive.replicate(socket)
  })

  await discovery.flushed()
  done()

  return {
    drive,
    async stop () {
      discovery.destroy()
      await swarm.destroy?.()
      await drive.close()
      await store.close?.()
    }
  }
}
```

## Practical rules
- Use `drive.entry()` when you need metadata instead of file bytes
- Use `drive.getBlobs()` when you need direct access to binary payload storage
- Use `batch()` for grouped mutations
- Use one swarm and one Corestore per app when possible
- Keep filesystem semantics in the worker, not in the UI layer

## Good fit app types
- distributed file sync
- document stores with blob attachments
- media libraries
- offline-first archives
- replicated app assets
