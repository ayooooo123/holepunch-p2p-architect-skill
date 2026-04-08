---
name: holepunch-p2p-architect
description: Design, implement, debug, and test production-ready P2P apps using the Holepunch stack (Hypercore/Hyperdrive/Hyperbee/Hyperdb/Autobase, Hyperswarm/HyperDHT/Protomux) plus Pear Runtime and Bare JS Runtime. Use for architecture design, feature implementation (e.g., comments/feeds), performance and reliability tuning, sync failures, and unit/integration test enablement; also when building multi-platform Pear/BareKit apps with IPC/concurrency (pear-ipc, bare-ipc, bare-atomics, bare-workers, bare-thread) or mining Holepunch/Pear/Bare repos, docs, or pear:// app dumps.
---

# Holepunch P2P Architect

## Overview
Design and deliver P2P features and systems on the Holepunch stack end-to-end, using local mirrors of upstream repos/docs and pear:// app dumps to stay current.

## IPC and Runtime Concurrency
- Use when designing IPC between Pear renderer, Pear workers, and BareKit worklets.
- Prefer pear-ipc (Pear apps) or bare-ipc + bare-pipe (Bare apps) for transport, bare-atomics for shared state, and bare-workers/bare-thread for isolation.
- Community guidance: wrap worker IPC in HRPC, and reference `holepunchto/bare-worker` examples first for thread/pipe usage.
- Validate message schemas, backpressure, and reconnect behavior.
- Use `references/ipc-runtime.md` for envelope, backpressure, and reconnect guidance.
- Use `references/ipc-repos.md` to locate IPC/concurrency examples in upstream repos.
- Use `assets/ipc-scaffold/` for a minimal protocol/router + transport adapter starter.
- Prefer pearopen examples first; only dive into tool repos for missing low-level details.

## Workflow Decision Tree
- If asked to generate a complete working app, follow the One-Shot App Generation Contract.
- If asked to design architecture, follow Architecture Workflow.
- If asked to implement a feature (comments, feeds, reactions, indexing), follow Feature Workflow.
- If asked to improve performance or reliability, follow Performance Workflow.
- If asked to debug sync failures, follow Debugging Workflow.
- If asked to enable tests, follow Testing Workflow.
- If asked to become an expert or survey the ecosystem, run the Knowledge Sync Workflow first.

## One-Shot App Generation Contract

When asked to generate a complete working P2P app, always produce a fully runnable repo shape. Never stop at architecture alone.

Required output order:
1. Pick the target platform(s) and runtime(s). State tradeoffs if defaulting.
2. Choose the primary P2P primitive(s). Explain the split between shared core and platform adapters using `references/runtime-abstraction.md`.
3. Emit a concrete file tree. Use the canonical shapes in `assets/templates/` and `references/app-scaffold.md` as the base.
4. Generate the shared core module(s) first. No direct dependence on platform globals (no `Pear`, `Bare`, `process.env`, DOM, or React Native globals in core).
5. Generate platform adapters for each target runtime (storage adapter, transport adapter, UI/IPC adapter).
6. Add platform-specific config and package scripts (package.json, pear.config.js or package.json#pear, build scripts).
7. Add build, test, and run commands. See `references/build-deploy.md` for the canonical command matrix.
8. Add a short acceptance checklist covering: app starts, peer discovery fires, replication completes, data persists across restart, update check runs, app packages cleanly.
9. Call out assumptions and missing product decisions explicitly at the end.

Hard rules:
- Never stop at architecture alone when the request is to build an app.
- Never mix transport, UI, storage, and packaging concerns in the shared core.
- Prefer the smallest fully working app over a broad but incomplete design.
- If a platform is not specified, default to Pear terminal (fastest to validate) and state the tradeoff.
- If a target needs native runtime behavior, prefer Bare/BareKit guidance over browser or Node assumptions.
- Always include a package.json with all required dependencies listed by name.
- Always include a working test entry point, even if minimal.

Starter app matrix (map problem to template):

| App type | Template | Primary primitive |
| --- | --- | --- |
| Feed / activity log | `assets/templates/shared-core/` + terminal or desktop | Hypercore + Hyperbee |
| Collaborative document / comments | `assets/templates/shared-core/` + terminal or desktop | Autobase |
| File sync / archive | `assets/templates/desktop/` | Hyperdrive + Localdrive |
| Encrypted one-to-one pipe | `assets/templates/terminal/` | Hyperbeam |
| Mobile companion app | `assets/templates/mobile/` | Bare + BareKit + Hyperswarm |
| Multi-platform (desktop + mobile) | `assets/templates/shared-core/` + desktop + mobile | Choose per data need |

## Knowledge Sync Workflow
1. Sync upstream repos for source-of-truth patterns and tests.
   - Run `scripts/sync_holepunch_repos.py` to mirror orgs locally (e.g., `--org holepunchto --org tetherto --org pearopen`).
   - Repos are stored under `~/.codex/skills-cache/holepunch-p2p-architect/repos/<org>/<repo>`.
   - Use `--shallow` or `--repo-list` to limit clone size when needed.
   - Start with `pearopen/*` examples for best-practice patterns; pull `holepunchto/*` or `tetherto/*` only to fill API gaps.
2. Mirror Pear docs for offline reference.
   - Run `scripts/fetch_pears_docs.sh`.
3. Dump reference Pear apps for real-world patterns.
   - Run `scripts/pear_dump_app.sh` with a `pear://` app key.
4. Use `rg` against the local mirrors for examples, tests, and API usage.

## Architecture Workflow
1. Identify runtime targets (Pear desktop, Bare mobile, Node) and constraints (storage, backgrounding, NAT/firewalls, offline requirements).
2. Choose data model primitives using `references/stack-map.md`.
3. Define discovery and replication surfaces (topics, protocols, membership, access control).
4. Specify sync strategy (eventual vs real-time, public vs private data, caching/prefetching, migrations).
5. Produce outputs:
   - Architecture overview (1-2 pages)
   - Data model and replication diagram (Mermaid/ASCII)
   - Key protocol/topic names and invariants

## Feature Workflow (e.g., comments via Autobase)
1. Clarify feature semantics: multi-writer vs single-writer, moderation, ordering, offline behavior.
2. Pick the primitive (Autobase vs Hyperbee/Hyperdrive/Hyperdb) and justify tradeoffs.
3. Define storage schema, indexes, and migration/backfill strategy.
4. Wire replication and discovery with explicit topic joins and protocol channels.
5. Add RPC surface, UI integration, and telemetry/logging.
6. Validate with multi-peer tests and version-skew scenarios.

## Performance Workflow
1. Collect metrics: peer counts, DHT state, replication backlog, data sizes, update times.
2. Map bottlenecks to layers (discovery, replication, storage, UI/runtime).
3. Apply targeted fixes (topic joins, caching, public mirrors, backpressure).
4. Re-test with controlled conditions and real network variability.

## Debugging Workflow (Sync/Discovery)
1. Capture environment: versions, runtime, storage paths, keys, repro steps.
2. Verify discovery joins and retained handles (prevent GC of discovery handles).
3. Confirm replication wiring (store.replicate, Autobase replicate, protocol pairing).
4. Inspect DHT/Swarm status and connection events.
5. Isolate with minimal two-peer reproduction.
6. Use `references/debug-playbook.md` for checklist and symptom mapping.

## Testing Workflow
1. Identify test layers: unit (pure logic), integration (replication), end-to-end (multi-peer).
2. Prefer deterministic storage and controlled networks in tests.
3. Add regression tests around version skew, unknown commands, and partial data.
4. Use `references/testing.md` for patterns and coverage checklist.

## Local Knowledge Sources
- `scripts/sync_holepunch_repos.py` -> Mirror `holepunchto/*` and `tetherto/*` repos to a local cache.
- `scripts/fetch_pears_docs.sh` -> Mirror https://docs.pears.com for offline reference.
- `scripts/pear_dump_app.sh` -> Dump Pear apps for real-world pattern analysis.
- `references/stack-map.md` -> Data model, networking decision matrix, and problem-first repo index.
- `references/ipc-runtime.md` -> IPC envelopes, backpressure, and reconnection patterns.
- `references/ipc-repos.md` -> Expanded repo index and rg patterns for all ecosystem areas.
- `references/app-scaffold.md` -> Canonical one-shot app structure and per-target file trees.
- `references/runtime-abstraction.md` -> Shared-core and platform-adapter boundaries with code shapes.
- `references/build-deploy.md` -> Build, test, package, and release command matrix per target.
- `references/debug-playbook.md` -> Sync and discovery troubleshooting checklist.
- `references/testing.md` -> Test strategy and patterns.
- `assets/templates/shared-core/` -> Shared domain logic scaffold.
- `assets/templates/desktop/` -> Pear desktop app scaffold.
- `assets/templates/terminal/` -> Pear terminal app scaffold.
- `assets/templates/mobile/` -> Bare/BareKit mobile app scaffold.
- `assets/ipc-scaffold/` -> Minimal IPC scaffold (protocol + router + adapters).
- `.github/workflows/` -> CI validate and release workflow templates.

## Example Requests
- "Build a minimal P2P chat app for Pear desktop."
- "Generate a complete Bare mobile app that syncs a feed with a desktop peer."
- "Set up IPC between Pear renderer and a Bare worker with typed messages and reconnect logic."
- "Show a safe pattern for spinning up a Bare worker and bare-thread and coordinating with bare-atomics."
- "Debug a deadlock in bare-ipc or pear-ipc and propose a fix with instrumentation."
- "Design a multi-platform app architecture that shares IPC code between Pear and BareKit."
- "Create a minimal example that streams data between a Bare worker and the UI with backpressure."
