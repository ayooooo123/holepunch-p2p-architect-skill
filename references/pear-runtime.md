# Pear Runtime Deep-Dive Guide

Use this when the app is a Pear desktop or terminal app, or when you need the Pear runtime layer and app shell metadata to coordinate a Bare worker host.

Last reviewed: Wednesday, April 8, 2026.

## What Pear Runtime is for
Pear is an installable P2P runtime, development, and deployment platform built on Bare. In the worker-first architecture, Pear is the shell/runtime layer around the worker host, not the place for business logic.

Use Pear Runtime when you need:
- a desktop or terminal shell for a P2P app
- app metadata, DHT bootstrap info, or runtime state
- access to Pear-specific platform APIs
- update, packaging, and launch coordination

## API surface to know

### Pear application metadata
From the official docs, useful fields include:
- `Pear.app.main`
- `Pear.app.storage`
- `Pear.app.dir`
- `Pear.app.dht.nodes`
- `Pear.app.dht.bootstrap`
- `Pear.app.assets`
- `Pear.app.swapDir`
- `Pear.app.pearDir`

### Pear integration/runtime symbols
- `Pear.constructor.RTI` runtime information bootstrap
- `Pear.constructor.RUNTIME` runtime binary used for spawning
- `Pear.constructor.RUNTIME_ARGV` arguments passed to the runtime
- `Pear.constructor.IPC` built-in IPC client symbol
- `Pear.constructor.CUTOVER` for init/buffering handoff behavior

### Lifecycle and exit behavior
- `Pear.exit(code)` exits through Pear teardown flow
- `Bare.exit(code)` is lower-level and bypasses Pear teardown semantics
- `Pear.restart()` is deprecated; use the dedicated restart flow instead

## Common usage patterns

### 1) Keep the shell thin
Use Pear to start the UI or terminal shell and hand off app behavior to a worker host.

### 2) Use Pear runtime metadata, not global state, for startup wiring
Let the shell read app metadata and pass it to the worker host over IPC.

### 3) Use Pear docs and modules for platform-specific features
Use Pear modules such as `pear-ipc`, `pear-terminal`, `pear-electron`, and update helpers when the app needs those integration points.

### 4) Treat `pear run` as a launch mechanism, not an architecture
The new default architecture should still be worker-first even when the app is launched by Pear tooling.

## Pear Runtime in the Bare worker-based architecture

### Recommended placement
- shared core: domain logic and protocol rules
- worker host: app state, replication, storage, and transport
- Pear shell: startup, UI, update handling, and app metadata

### Worker-host responsibilities
The worker host should:
- stay runnable under both Pear and Bare shells
- accept config from the shell over IPC
- own discovery and replication
- keep logic portable across desktop, terminal, and mobile surfaces

### Shell responsibilities
The shell should:
- read `Pear.app` metadata
- launch the worker host
- pass lifecycle events and config
- handle update and packaging concerns

## Minimal Pear shell shape
```js
const ipc = Pear[Pear.constructor.IPC]

ipc.postMessage({ type: 'start', config: Pear.app })
```

## Practical rules
- Use Pear for launch and platform glue
- Keep app logic in the worker host
- Read runtime/bootstrap info from Pear metadata, not from the shell UI tree
- Use Bare for the core runtime work inside the worker
- Avoid mixing UI with replication or storage concerns

## Good fit app types
- desktop P2P apps
- terminal P2P apps
- update-aware apps
- apps that need Pear-specific packaging or shell behavior
