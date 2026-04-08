# IPC/Runtime Repos & Grep Patterns

This file is the repo index for finding the most relevant Holepunch/Pear/Bare code when solving a problem.

Last reviewed: Wednesday, April 8, 2026.

## Repo sync
Use the skill cache:
- `scripts/sync_holepunch_repos.py --org holepunchto --org tetherto --org pearopen`

Local cache:
- `~/.codex/skills-cache/holepunch-p2p-architect/repos/<org>/<repo>`

## How to use this index
- Start with the repo that matches the user’s problem domain.
- Prefer pearopen examples first for realistic patterns and best practices.
- Use holepunchto repos when you need lower-level API details, implementation edge cases, or current module behavior.
- Check Pear docs stability labels before treating a repo as production guidance.

## Problem-first repo index

### Discovery, networking, and relays
- `holepunchto/hyperswarm`
- `holepunchto/hyperdht`
- `holepunchto/blind-peer`
- `holepunchto/blind-peering`
- `holepunchto/blind-peer-muxer`
- `holepunchto/blind-relay-service`

Use these when the problem is peer discovery, NAT traversal, relay routing, direct peer connection setup, or blind/mirror connectivity.

### Data and replication
- `holepunchto/hypercore`
- `holepunchto/hyperbee`
- `holepunchto/corestore`
- `holepunchto/autobase`
- `holepunchto/hyperdrive`
- `holepunchto/localdrive`
- `holepunchto/mirrordrive`
- `holepunchto/hyperdb`

Use these when the problem is append-only history, indexed reads, multi-writer collaboration, or file-tree replication.

### Pear runtime, updates, and app shell
- `holepunchto/pear`
- `holepunchto/pear-run`
- `holepunchto/pear-updates`
- `holepunchto/pear-runtime-updater`
- `holepunchto/pear-electron`
- `holepunchto/pear-terminal`
- `holepunchto/pear-inspect`
- `holepunchto/pear-hotmods`

Use these when the problem is app startup, auto-update behavior, shell/runtime behavior, hot reload, or debugging Pear apps.

### Bare runtime and native/mobile work
- `holepunchto/bare`
- `holepunchto/bare-kit`
- `holepunchto/react-native-bare-kit`
- `holepunchto/bare-ipc`
- `holepunchto/bare-atomics`
- `holepunchto/bare-worker`
- `holepunchto/bare-thread`
- `holepunchto/bare-fs`
- `holepunchto/bare-fetch`
- `holepunchto/bare-http1`
- `holepunchto/bare-zlib`
- `holepunchto/bare-readline`
- `holepunchto/bare-repl`
- `holepunchto/bare-build`
- `holepunchto/bare-bundle`
- `holepunchto/bare-pack`
- `holepunchto/bare-unpack`

Use these when the problem is on-device JS runtime behavior, native bindings, mobile app bridging, IPC, workers/threads, or packaging delivery.

### Transport and messaging
- `holepunchto/hyperbeam`
- `holepunchto/protomux`
- `holepunchto/secretstream`
- `holepunchto/pear-ipc`

Use these when the problem is encrypted pipes, multiplexing, message framing, or app-to-app communication.

## Key repos to inspect first
- pearopen/*: up-to-date cross-platform examples for desktop, mobile, and CLI
- tetherto/*: Pear/Bare examples and adjacent tooling
- holepunchto/pear
- holepunchto/bare-kit
- holepunchto/hyperswarm
- holepunchto/hypercore
- holepunchto/hyperdrive
- holepunchto/autobase

## Priority guidance
- Start with pearopen examples for realistic patterns and best practices.
- Move to the relevant holepunchto repo only when you need low-level API details or the example repo does not show the behavior you need.
- If the work involves mobile or native runtime behavior, inspect Bare repos before assuming browser or Node patterns apply.

## Grep patterns
Run in the local cache:
- `rg "ipc|rpc|request|response|message" holepunchto/pear-ipc holepunchto/bare-ipc`
- `rg "SharedArrayBuffer|Atomics" holepunchto/bare-atomics`
- `rg "worker|thread|join|resume|suspend" holepunchto/bare-worker holepunchto/bare-thread`
- `rg "BareKit|react-native-bare-kit|IPC" holepunchto/bare-kit holepunchto/react-native-bare-kit`
- `rg "update|auto.?update|runtime updater|bundle|pack|unpack" holepunchto/pear holepunchto/pear-updates holepunchto/pear-runtime-updater holepunchto/bare-build holepunchto/bare-pack holepunchto/bare-unpack`
- `rg "blind-peer|blind-peering|relay" holepunchto/blind-peer holepunchto/blind-peering holepunchto/blind-peer-muxer holepunchto/blind-relay-service`

## Docs
If Pear docs are mirrored:
- `~/.codex/skills-cache/holepunch-p2p-architect/docs/pears`
