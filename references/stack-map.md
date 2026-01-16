# Holepunch Stack Map

Use this as a quick decision matrix for data model, replication, and runtime choices.

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

## Runtime Considerations
- Pear Runtime (desktop): Browser-like UI + worker runtime; IPC and worker setup are critical.
- Bare Runtime (mobile): Restricted environment; avoid blocking joins, retain discovery handles, and expect stricter lifecycle constraints.

## Decision Prompts
- Need multi-writer? Choose Autobase.
- Need fast indexed reads, single writer? Choose Hyperbee.
- Need file tree semantics? Choose Hyperdrive.
- Need append-only history? Choose Hypercore.
- Need legacy compatibility? Consider Hyperdb, but validate current guidance first.

## Common Patterns
- Public feed: Gossip discovery via Hyperswarm topic + read-only public index (often Hyperbee).
- Comments: Autobase for open participation; publish key via metadata so viewers can load it.
- Performance: Cache hot metadata in Hyperbee; avoid blocking on network for UI paths.
