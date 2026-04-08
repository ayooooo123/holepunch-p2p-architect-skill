# Holepunch Stack Map

Use this as a quick decision matrix for data model, replication, runtime choices, and repo discovery.

## Data Model Choices
- Hypercore: Append-only log. Use for ordered event streams, durable logs, or building higher-level structures.
- Hyperbee: Single-writer key/value store. Use for indexed metadata, lookup tables, and fast reads.
- Hyperdrive: Single-writer file tree abstraction. Use when you want file-like semantics.
- Autobase: Multi-writer log with a materialized view. Use for collaborative or multi-device writes where a linearized view is required.
- Hyperdb: Legacy multi-writer key/value. Use only for compatibility or specific requirements; confirm current status in upstream docs/repo before choosing.

## Networking and Discovery
- Hyperswarm: Peer discovery and encrypted transport. Use for joining topics, connecting peers, and replicating cores.
- HyperDHT: Underlying DHT used by Hyperswarm for discovery and holepunching.
- Protomux: Multiplex custom protocols over a single connection.
- worker IPC: Use when the app runtime is split between a shell and a Bare worker host.
- udx-native: Raw UDP transport for custom streams and low-level protocol work.

## Runtime Considerations
- Pear Runtime (desktop): Shell + worker orchestration belongs in the Pear runtime/bootstrap layer; do not build the app around `pear run`.
- Bare Runtime (mobile/native): Restricted environment; avoid blocking joins, retain discovery handles, and expect stricter lifecycle constraints.
- BareKit / react-native-bare-kit: Use for native mobile work when you need Bare semantics inside Android or iOS apps.
- Bare worker host: Default architecture for one-shot app generation; keep business logic and replication state here instead of in the shell.
- bare-runtime: Use as the launcher/locator for the correct Bare binary on each target.

## Decision Prompts
- Need multi-writer data? Choose Autobase.
- Need fast indexed reads, single writer? Choose Hyperbee.
- Need file tree semantics? Choose Hyperdrive.
- Need append-only history? Choose Hypercore.
- Need legacy compatibility? Consider Hyperdb, but validate current guidance first.
- Need on-device native runtime behavior? Prefer Bare or BareKit before reaching for browser assumptions.
- Need one-shot generation that works across platforms? Default to the Bare worker host and add thin shells on top.

## Problem-first repo index

| User problem | Start here | Then inspect |
| --- | --- | --- |
| Peer discovery / NAT traversal | `hyperswarm`, `hyperdht` | `blind-peer`, `blind-peering`, `blind-peer-muxer`, `blind-relay-service` |
| Append-only activity log | `hypercore` | `corestore`, `hyperbee`, `autobase` |
| Collaborative writable data | `autobase` | `hyperbee`, `hypercore`, `hyperdb` |
| Distributed file sync | `hyperdrive` | `localdrive`, `mirrordrive`, `drives` |
| Encrypted one-to-one transport | `hyperbeam` | `protomux`, `secretstream` |
| Desktop Pear app shell | `pear` | `pear-runtime`, `pear-run`, `pear-electron`, `pear-inspect`, `pear-hotmods` |
| Pear updates / runtime delivery | `pear-updates`, `pear-runtime-updater` | `pear-runtime`, `pear-run`, `pear-api`, `pear-constants` |
| Native/Bare mobile app | `bare`, `bare-kit` | `react-native-bare-kit`, `bare-ipc`, `bare-atomics`, `bare-worker`, `bare-thread` |
| Bare worker host / worker lifecycle | `bare-worker`, `bare-thread` | `bare-ipc`, `bare-atomics`, `bare-kit` |
| Bare standard-library behavior | `bare-fs`, `bare-http1`, `bare-fetch`, `bare-zlib` | `bare-stream`, `bare-console`, `bare-readline`, `bare-repl` |
| Packaging / bundling / app delivery | `bare-bundle`, `bare-pack`, `bare-unpack`, `bare-build`, `bare-link` | `pear-runtime`, `pear-updates`, `pear-runtime-updater` |
| Terminal / CLI UX | `pear-terminal`, `bare-readline` | `bare-repl`, `bare-console` |
| Debugging / inspection | `pear-inspect`, `bare-inspector` | `bare-repl`, `bare-readline`, `pear-hotmods` |
| Native addon development | `bare-addon`, `bare-link` | `bare-make`, `cmake-fetch`, `bare-pack` |
| Raw UDP transport | `udx-native` | `hyperdht`, `hyperswarm`, `protomux` |

## Common Patterns
- Public feed: Gossip discovery via Hyperswarm topic + read-only public index, often Hyperbee.
- Comments: Autobase for open participation; publish the key in metadata so viewers can load it.
- Mobile app lifecycle: Keep discovery handles alive, avoid blocking startup, and make sure reconnect logic survives suspend/resume.
- Worker-host apps: Keep shell code thin, move state and replication into the worker host, and test worker startup separately.
- Performance: Cache hot metadata in Hyperbee; avoid blocking on network for UI paths.
- Update-aware apps: Route through Pear runtime bootstrap modules and use Bare-native packaging when the app must bootstrap itself cleanly on device.

## Selection Notes
- When the question is "which repo should I inspect?", use the problem-first repo index above.
- When the question is "which primitive should I use?", use the decision prompts above.
- When the question is "is this stable enough?", check the Pear docs stability labels before copying a pattern into the skill.
