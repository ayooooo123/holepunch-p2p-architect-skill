# IPC Runtime Patterns (Pear/Bare)

## When to read this
- Use when designing IPC between renderer/worker/processes, wiring bare-workers or bare-threads, or adding shared-state protocols with bare-atomics.
- Use for reliability/perf issues (reconnect, ordering, backpressure).

## Core patterns
- **Message envelope**: `{ type, id, replyTo, ts, payload, meta }` with monotonic `id` and `replyTo` for RPC-style replies.
- **Capability handshake**: on connect, exchange `{ protocolVersion, features, maxFrame }` and branch behavior on feature flags.
- **Ack + retry**: for non-idempotent commands, require ACK; add jittered retry + timeout.
- **Backpressure**: limit in-flight messages; use credits or windowed send (e.g., max 128 in-flight).
- **Reconnect safety**: clear pending requests on disconnect; re-emit subscriptions after rejoin.

## bare-atomics ring buffer guidance
- Use ring buffers for high-frequency telemetry (stats, metrics) not for RPC.
- Store fixed-size records; publish write index via Atomics.store; read via Atomics.load.
- Always reserve space first; drop oldest or newest if buffer full.

## Worker isolation notes
- bare-workers are fully isolated; shared state must go through explicit IPC.
- Avoid implicit globals; pass config over IPC during init.
- Keep initialization idempotent so reconnects rehydrate safely.

## Debugging checklist
- Verify single source of truth for connection state.
- Log connect/disconnect events with transport IDs.
- Trace message IDs at send/recv to detect duplication/loss.

