# Runtime Abstraction Guide

Use this guide to keep one codebase portable across Pear desktop, Electron desktop, Pear terminal, and Bare/BareKit mobile targets.

Last reviewed: Wednesday, April 8, 2026.

## Goal
Make the app logic portable by separating the domain model from the worker host and the shell.

## Boundary model

### Shared core
Put in shared core:
- data model
- protocol schema
- state transitions
- validation
- merge rules
- deterministic transforms
- persistence contract interfaces

Do not put in shared core:
- environment detection
- filesystem calls
- UI rendering
- direct networking calls
- app lifecycle hooks
- runtime bootstrap logic

### Worker host
Put in the worker host:
- app startup and shutdown
- storage and transport wiring
- peer lifecycle management
- reconnect behavior
- background/resume reaction
- message routing to the core

### Platform shells
Put in shells/adapters:
- platform bootstrapping
- runtime detection
- UI glue
- CLI parsing
- mobile lifecycle hooks
- update hooks

## Canonical adapter interfaces

```js
export function createAppCore ({ storage, transport, log }) {
  return {
    start () {},
    stop () {},
    handleEvent (event) {},
    getState () {}
  }
}
```

```js
export function createWorkerHost ({ core, storage, transport, clock, log }) {
  return {
    start () {},
    stop () {},
    handleMessage (message) {}
  }
}
```

```js
export function createShellAdapter ({ workerHost, log }) {
  return {
    start () {},
    stop () {},
    send (message) {}
  }
}
```

## Runtime-specific guidance

### Electron desktop v2
- Treat Electron main as the shell coordinator.
- Keep preload as a narrow bridge.
- Keep renderer UI-only.
- Use PearRuntime to launch the worker and manage updates.
- Forward worker stdio and IPC through the bridge rather than importing runtime APIs in the renderer.

### Pear desktop / Pear terminal
- Treat the shell as the place for startup and user interaction.
- Use pear-runtime or Pear runtime metadata for launch and update state.
- Keep the worker host shared across desktop shells.

### Bare mobile / BareKit
- Assume stricter lifecycle constraints.
- Keep discovery handles alive for as long as replication is needed.
- Be explicit about background/resume behavior and native bridge boundaries.
- Avoid browser-only assumptions such as DOM events or window globals.
- Keep the mobile shell thin and let the worker host own networking state.

## Environment detection pattern
Use a thin platform adapter to choose the right implementation.

```js
const runtime = globalThis.Bare ? 'bare' : globalThis.Pear ? 'pear' : 'node'
```

Use the detected runtime only in the outer adapter layer.

## Storage strategy pattern
- Core defines what should be stored.
- Worker host decides when persistence happens.
- Adapter decides where storage lives.
- Use a stable path and keep the schema versioned.
- Persist enough metadata to resume replication after restart.

## Transport strategy pattern
- Core defines topic names, protocol versions, and message shapes.
- Worker host handles peer discovery and connection lifecycle.
- Adapter wires the actual transport implementation.
- If reconnection matters, keep the discovery handle alive and re-subscribe on resume.

## Update strategy pattern
- If the app needs auto-update behavior, keep update orchestration outside the core.
- The core should expose a clean restart-safe state model.
- The worker host should survive update handoff cleanly.
- The platform shell should own the download/apply/restart path.

## Rule of thumb
If a function needs to know whether it is running in Pear, Electron, Bare, terminal, or mobile, it probably belongs in a shell or host adapter rather than in shared core.
