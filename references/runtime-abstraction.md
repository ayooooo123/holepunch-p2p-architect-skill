# Runtime Abstraction Guide

Use this guide to keep one codebase portable across Pear desktop, Pear terminal, and Bare/BareKit mobile targets.

Last reviewed: Wednesday, April 8, 2026.

## Goal
Make the app logic portable by separating the domain model from runtime-specific code.

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
- update logic

### Platform adapters
Put in adapters:
- platform bootstrapping
- runtime detection
- transport wiring
- storage wiring
- UI glue
- lifecycle events
- update hooks

## Canonical adapter interfaces

```js
export function createAppCore ({ storage, transport, clock, log }) {
  return {
    start () {},
    stop () {},
    handleEvent (event) {},
    getState () {}
  }
}
```

```js
export function createStorageAdapter ({ basePath }) {
  return {
    readState () {},
    writeState () {},
    readSnapshot () {},
    writeSnapshot () {}
  }
}
```

```js
export function createTransportAdapter ({ topic, log }) {
  return {
    connect () {},
    disconnect () {},
    broadcast () {},
    onMessage () {}
  }
}
```

## Runtime-specific guidance

### Pear desktop
- Treat the desktop shell as the place for UI orchestration and app updates.
- Keep IPC on the adapter side, not inside the core.
- Route hot reload and inspect/debug behavior through Pear-specific modules.

### Pear terminal
- Keep startup fast and stateful behavior explicit.
- Prefer deterministic startup paths and small CLI entrypoints.
- Use the terminal scaffold when the goal is to validate behavior quickly before adding UI.

### Bare mobile / BareKit
- Assume stricter lifecycle constraints.
- Keep discovery handles alive for as long as replication is needed.
- Be explicit about background/resume behavior and native bridge boundaries.
- Avoid browser-only assumptions such as DOM events or window globals.

## Environment detection pattern
Use a thin platform adapter to choose the right implementation.

```js
const runtime = globalThis.Bare ? 'bare' : globalThis.Pear ? 'pear' : 'node'
```

Use the detected runtime only in the outer adapter layer.

## Storage strategy pattern
- Core defines what should be stored.
- Adapter decides where storage lives.
- Use a stable path and keep the schema versioned.
- Persist enough metadata to resume replication after restart.

## Transport strategy pattern
- Core defines topic names, protocol versions, and message shapes.
- Adapter handles peer discovery and connection lifecycle.
- If reconnection matters, keep the discovery handle alive and re-subscribe on resume.

## Update strategy pattern
- If the app needs auto-update behavior, keep update orchestration outside the core.
- The core should expose a clean restart-safe state model.
- The platform adapter should own the download/apply/restart path.

## Rule of thumb
If a function needs to know whether it is running in Pear, Bare, terminal, or mobile, it probably belongs in an adapter rather than in shared core.
