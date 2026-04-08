# Hyperblobs Deep-Dive Guide

Use this when the app needs chunked blob storage on top of Hypercore, or when Hyperdrive content should be handled directly as binary payloads.

Last reviewed: Wednesday, April 8, 2026.

## What Hyperblobs is for
Hyperblobs stores large binary values inside a single Hypercore-backed blob store. Each blob is identified by byte and block bounds, which makes it a good fit for attachments, media, and any payload that should live next to replicated metadata but not inside it.

Use Hyperblobs when you need:
- binary attachments
- chunked content storage
- read/write streams for large files
- a blob layer behind Hyperdrive or a worker-owned Hypercore

## API surface to know

### Constructor
```js
const blobs = new Hyperblobs(core, opts)
```

Notable option:
- `blockSize` controls chunking size for large blobs

### Blob operations
- `const id = await blobs.put(blob, opts)` stores a blob and returns its bounds id
- `const content = await blobs.get(id, opts)` returns the full blob as a Buffer
- `await blobs.clear(id, opts)` removes a blob from storage
- `const stream = blobs.createReadStream(id, opts)` reads a blob as a stream
- `const stream = blobs.createWriteStream(opts)` writes a blob as a stream and exposes `stream.id`

## Common usage patterns

### 1) Store bytes separately from metadata
Keep metadata, indexes, and record references in Hypercore/Hyperbee/Hyperdrive, and keep the actual bytes in Hyperblobs.

### 2) Use bounds IDs as stable references
The returned blob id is the canonical reference to the payload. Store that id in your record model instead of duplicating the bytes.

### 3) Stream large payloads
Use the stream APIs for media files, large exports, or resumable uploads instead of buffering everything in memory.

### 4) Prefer Hyperdrive when you want files, Hyperblobs when you want content bytes
If the app should feel like a file tree, use Hyperdrive.
If the app should feel like object storage or attachments, use Hyperblobs directly.

## Hyperblobs in the Bare worker-based architecture

### Recommended placement
- shared core: attachment schema, validation, and blob reference rules
- worker host: Hyperblobs instance, storage decisions, streaming, cleanup
- shell adapter: upload UI, preview UI, download actions

### Worker-host responsibilities
The worker host should:
- create the core or retrieve the Hyperdrive content core
- own the Hyperblobs instance
- attach blob ids to records in the main data model
- manage cleanup and lifecycle
- keep binary payload handling away from the shell

### Shell responsibilities
The shell should:
- select files or display previews
- stream uploads/downloads through the worker
- avoid directly manipulating the blob store

## Minimal worker-host shape
```js
import Hyperblobs from 'hyperblobs'

export async function createBlobHost ({ core, log }) {
  const blobs = new Hyperblobs(core, { blockSize: 64 * 1024 })

  return {
    async putAttachment (buffer) {
      return await blobs.put(buffer)
    },
    async readAttachment (id) {
      return await blobs.get(id)
    },
    async stop () {
      await core.close?.()
    }
  }
}
```

## Practical rules
- Keep metadata and bytes separate
- Use stream APIs for large content
- Persist only blob ids in your record layer
- Clear blobs when the owning record is deleted and no longer needed
- Treat Hyperblobs as host-owned storage, not shell-owned state

## Good fit app types
- file attachments
- media libraries
- image or document uploads
- binary export/import
- Hyperdrive content payloads
