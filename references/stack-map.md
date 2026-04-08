# Holepunch Stack Map

Use this as a quick decision matrix for data model, replication, runtime choices, and repo discovery.

Last reviewed: Wednesday, April 8, 2026.

## Ecosystem updates to keep in mind
- Bare is now the runtime foundation for Pear; Pear docs present Bare as the minimal JS runtime underneath the Pear runtime and module ecosystem.
- Pear docs now organize modules with stability labels and separate sections for P2P modules, Bare modules, and tools. Use those labels when deciding whether something is stable enough for production.
- Bare is especially relevant for desktop/mobile and native embedding. For mobile/native app work, prefer BareKit and related native bindings over assuming a browser-like runtime.
- Pear runtime includes update flows, and the ecosystem now has dedicated update-oriented repos such as `pear-updates` and `pear-runtime-updater`.
- Recent repo activity in the Holepunch org highlights newer connectivity and relay patterns such as `blind-peer`, `blind-peering`, `blind-peer-muxer`, and `blind-relay-service`.

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
- blind-peer / blind-peering / blind-peer-muxer: Useful when the architecture needs blind relays or side-mirror style peer connectivity.
- blind-relay-service: Useful when the problem is to run or inspect a relay service rather than a direct peer mesh.

## Runtime Considerations
- Pear Runtime (desktop): Browser-like UI plus worker/runtime orchestration; IPC, hot reload, and update behavior matter.
- Bare Runtime (mobile/native): Restricted environment; avoid blocking joins, retain discovery handles, and expect stricter lifecycle constraints.
- BareKit / react-native-bare-kit: Use for native mobile work when you need Bare semantics inside Android or iOS apps.
- Bare worker/thread APIs: Prefer these when you need concurrency without depending on browser-style workers.

## Decision Prompts
- Need multi-writer data? Choose Autobase.
- Need fast indexed reads, single writer? Choose Hyperbee.
- Need file tree semantics? Choose Hyperdrive.
- Need append-only history? Choose Hypercore.
- Need legacy compatibility? Consider Hyperdb, but validate current guidance first.
- Need on-device native runtime behavior? Prefer Bare or BareKit before reaching for browser assumptions.

## Problem-first repo index

| User problem | Start here | Then inspect |
| --- | --- | --- |
| Peer discovery / NAT traversal | `hyperswarm`, `hyperdht` | `blind-peer`, `blind-peering`, `blind-peer-muxer`, `blind-relay-service` |
| Append-only activity log | `hypercore` | `corestore`, `hyperbee`, `autobase` |
| Collaborative writable data | `autobase` | `hyperbee`, `hypercore`, `hyperdb` |
| Distributed file sync | `hyperdrive` | `localdrive`, `mirrordrive`, `drives` |
| Encrypted one-to-one transport | `hyperbeam` | `protomux`, `secretstream` |
| Desktop Pear app shell | `pear` | `pear-run`, `pear-electron`, `pear-inspect`, `pear-hotmods` |
| Pear updates / runtime delivery | `pear-updates`, `pear-runtime-updater` | `pear-run`, `pear-api`, `pear-constants` |
| Native/Bare mobile app | `bare`, `bare-kit` | `react-native-bare-kit`, `bare-ipc`, `bare-atomics`, `bare-worker`, `bare-thread` |
| Bare standard-library behavior | `bare-fs`, `bare-http1`, `bare-fetch`, `bare-zlib` | `bare-stream`, `bare-console`, `bare-readline`, `bare-repl` |
| Packaging / bundling / app delivery | `bare-bundle`, `bare-pack`, `bare-unpack`, `bare-build` | `pear`, `pear-updates`, `pear-runtime-updater` |
| Terminal / CLI UX | `pear-terminal`, `bare-readline` | `bare-repl`, `bare-console` |
| Debugging / inspection | `pear-inspect`, `bare-inspector` | `bare-repl`, `bare-readline`, `pear-hotmods` |

## Common Patterns
- Public feed: Gossip discovery via Hyperswarm topic + read-only public index, often Hyperbee.
- Comments: Autobase for open participation; publish the key in metadata so viewers can load it.
- Mobile app lifecycle: Keep discovery handles alive, avoid blocking startup, and make sure reconnect logic survives suspend/resume.
- Performance: Cache hot metadata in Hyperbee; avoid blocking on network for UI paths.
- Update-aware apps: Route through Pear update modules and use Bare-native packaging when the app must bootstrap itself cleanly on device.

## Selection Notes
- When the question is "which repo should I inspect?", use the problem-first repo index above.
- When the question is "which primitive should I use?", use the decision prompts above.
- When the question is "is this stable enough?", check the Pear docs stability labels before copying a pattern into the skill.
