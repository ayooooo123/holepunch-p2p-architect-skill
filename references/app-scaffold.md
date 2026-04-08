# Canonical App Scaffold

Use this guide when generating a full working app in one pass.

Last reviewed: Wednesday, April 8, 2026.

## Core principle
Split every app into:
- shared domain logic
- Bare worker host
- platform bootstrap / shell adapters
- platform-specific config and packaging

If the app is not split this way, it will usually drift into a platform-specific tangle that is harder to build, test, and port.

## Default generation shape
The default one-shot output should start with a worker-first scaffold, then add platform shells around it.

```text
my-p2p-app/
  package.json
  src/
    core/
      app.js
      protocol.js
      state.js
    worker/
      host.js
      lifecycle.js
    bootstrap/
      desktop.js
      terminal.js
      mobile.js
    adapters/
      storage.js
      transport.js
      shell.js
  electron/
    main.js
    preload.js
  renderer/
    index.html
    app.js
  workers/
    main.js
  config/
    pear.config.js
    mobile.config.js
  test/
    app.test.js
  scripts/
    build.js
    package.js
    release.js
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
- shell lifecycle hooks

## Worker host scaffold
The worker host owns the runtime behavior that used to live in the shell.

Responsibilities:
- start and stop the app core
- wire storage and transport adapters
- keep discovery handles alive
- handle reconnect and resume logic
- isolate shared app state from shell code

## Electron v2 desktop scaffold
Use this shape when the user wants a desktop app that follows the current pear-runtime standard.

```text
package.json
electron/
  main.js
  preload.js
renderer/
  index.html
  app.js
workers/
  main.js
src/
  core/
    app.js
    protocol.js
    state.js
  adapters/
    storage.js
    transport.js
```

Use for:
- app shell startup
- preload bridge exposure
- worker launch through pear-runtime
- update integration
- desktop-specific permissions, paths, and single-instance handling

## Pear terminal scaffold
Use when the app should be easiest to validate quickly and can run in a terminal.

```text
src/
  bootstrap/
    terminal.js
  adapters/
    terminal-shell.js
```

Use for:
- fastest runnable prototype
- text-first workflows
- direct peer connection and replication checks

## Bare mobile / BareKit scaffold
Use when the app needs on-device JS runtime behavior on iOS or Android.

```text
src/
  bootstrap/
    mobile.js
  adapters/
    mobile-shell.js
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
   - `electron/main.js`, `src/bootstrap/desktop.js`, `src/bootstrap/terminal.js`, or `src/bootstrap/mobile.js`
2. Shared core
   - pure logic under `src/core/`
3. Worker host
   - runtime orchestration and lifecycle in `workers/` or `src/worker/`
4. Transport/discovery
   - join topics, connect peers, reconnect after lifecycle changes
5. Storage
   - persistent local state and replication source
6. Platform adapter(s)
   - Pear, Electron, Bare, terminal, or mobile-specific wrappers
7. Configuration
   - package scripts and platform config
8. Tests
   - at least one runnable test for core behavior
9. Run instructions
   - exact commands to start, test, and package

## Recommended generation order
1. Shared core
2. Worker host
3. Transport/discovery adapter
4. Storage adapter
5. Platform bootstrap
6. Package scripts
7. Tests
8. Build/release config
9. Documentation

## Acceptance checklist for a one-shot app
- App launches without manual code edits
- Worker host starts successfully
- Peer discovery or local startup path works
- Data persists across restart
- Replication or sync path can be exercised
- Platform-specific entrypoint is present
- Tests run successfully
- Packaging or release command exists

## When to use which scaffold
- If the user asks for "desktop app", use the Electron v2 scaffold when the app needs Pear Runtime updates or Electron shell integration.
- If the user asks for "mobile app", start from the Bare/BareKit scaffold.
- If the user asks for "terminal app", start from the Pear terminal scaffold.
- If the user asks for "all platforms", create the shared core and worker host first, then add each platform bootstrap and shell adapter.
- If the user does not specify a platform, default to the Bare worker scaffold.
