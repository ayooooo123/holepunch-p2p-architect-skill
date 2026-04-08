# Canonical App Scaffold

Use this guide when generating a full working app in one pass.

Last reviewed: Wednesday, April 8, 2026.

## Core principle
Split every app into:
- shared domain logic
- runtime/storage/transport adapters
- platform entrypoints
- platform-specific config and packaging

If the app is not split this way, it will usually drift into a platform-specific tangle that is harder to build, test, and port.

## Minimum repo shape

```text
my-p2p-app/
  SKILL.md or README.md
  package.json
  src/
    core/
      app.js
      protocol.js
      state.js
    adapters/
      pear.js
      bare.js
      terminal.js
    transport/
      discovery.js
      replication.js
    storage/
      index.js
  test/
    app.test.js
  scripts/
    dev.js
    package.js
    release.js
  config/
    pear.config.js
    mobile.config.js
```

## Shared core scaffold
The shared core should contain only deterministic logic:
- state transitions
- message schema validation
- peer role decisions
- merge/conflict rules
- persistence contract
- replication rules

It should not contain:
- DOM access
- React Native APIs
- `Pear` globals
- `Bare` globals
- direct filesystem access
- direct network setup
- shell/process assumptions

## Platform scaffold variants

### Pear desktop
Use when the app needs a native desktop shell or peer-to-peer UI.

```text
src/
  main.js
  preload.js
  ui.js
```

Use for:
- app shell startup
- IPC between UI and worker/runtime
- update integration
- desktop-specific permissions and paths

### Pear terminal
Use when the app should be easiest to validate quickly and can run in a terminal.

```text
src/
  index.js
  cli.js
```

Use for:
- fastest runnable prototype
- text-first workflows
- direct peer connection and replication checks

### Bare mobile / BareKit
Use when the app needs on-device JS runtime behavior on iOS or Android.

```text
src/
  app.js
  runtime.js
  native-bridge.js
config/
  mobile.config.js
```

Use for:
- embedded runtime behavior
- lifecycle-aware networking
- background-safe replication
- native bridge setup

## Required file categories for a complete app

1. Entry point
   - `src/main.js`, `src/index.js`, or `src/app.js`
2. Shared core
   - pure logic under `src/core/`
3. Transport/discovery
   - join topics, connect peers, reconnect after lifecycle changes
4. Storage
   - persistent local state and replication source
5. Platform adapter(s)
   - Pear, Bare, terminal, or mobile-specific wrappers
6. Configuration
   - package scripts and platform config
7. Tests
   - at least one runnable test for core behavior
8. Run instructions
   - exact commands to start, test, and package

## Recommended generation order
1. Shared core
2. Transport/discovery adapter
3. Storage adapter
4. Platform entrypoint
5. Package scripts
6. Tests
7. Build/release config
8. Documentation

## Acceptance checklist for a one-shot app
- App launches without manual code edits
- Peer discovery or local startup path works
- Data persists across restart
- Replication or sync path can be exercised
- Platform-specific entrypoint is present
- Tests run successfully
- Packaging or release command exists

## When to use which scaffold
- If the user asks for "desktop app", start from the Pear desktop scaffold.
- If the user asks for "mobile app", start from the Bare/BareKit scaffold.
- If the user asks for "terminal app", start from the Pear terminal scaffold.
- If the user asks for "all platforms", create the shared core first, then add each platform adapter.
