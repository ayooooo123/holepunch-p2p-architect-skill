# Sync and Discovery Debug Playbook

Use this checklist when data is not syncing between peers or discovery appears stalled.

## 1) Capture Context
- Record runtime (Pear/Bare/Node), OS, and app version.
- Capture storage paths and whether stores are fresh or reused.
- Gather key IDs (channel key, drive key, public bee key, comments autobase key).
- Note repro steps and which peers are involved.

## 2) Verify Swarm/DHT State
- Confirm DHT bootstrapped and online.
- Check firewalled status and peer count.
- Log swarm connections and peer discovery events.

## 3) Verify Discovery Joins
- Ensure all topics are joined (public feed topic, channel discovery keys, public bee keys).
- Retain discovery handles returned by `swarm.join()` to avoid GC on mobile.
- Avoid awaiting `flushed()` in critical paths on constrained runtimes.

## 4) Verify Replication Wiring
- Confirm `store.replicate(conn)` is called for each connection.
- For Autobase, ensure `base.replicate(conn)` is registered for existing and new connections.
- Ensure protocol channels (Protomux) open on both sides.

## 5) Protocol and Message Sanity
- Confirm protocol name matches exactly on both ends.
- Guard unknown/unsupported commands to avoid dropping connections.
- Check for version skew in HRPC schemas.

## 6) Data Layer Checks
- Validate keys and encoding (hex length, prefixes, encryption keys).
- Verify local writes are actually appended before expecting remote reads.
- Check for migrations or schema changes that might block reads.

## 7) Minimal Repro
- Reproduce with two peers and a fresh store.
- Start one peer, wait for DHT bootstrap, then start the second peer.
- Join a single topic and verify a single data write replicates.

## Useful Search Patterns (local repo mirrors)
- `rg "swarm.join|protomux|Autobase|Hyperbee" resources/repos`
- `rg "replicate\(|store.replicate" resources/repos`
- `rg "dht|bootstrapped|firewalled" resources/repos`
