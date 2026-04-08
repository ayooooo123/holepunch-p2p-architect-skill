# IPC Runtime Patterns (Pear/Bare)

## When to read this
- Use when designing IPC between a shell and a Bare worker host, wiring bare-workers or bare-threads, or adding shared-state protocols with bare-atomics.
- Use for reliability/perf issues (reconnect, ordering, backpressure).

## Core patterns
- **Message envelope**: `{ type, id, replyTo, ts, payload, meta }` with monotonic `id` and `replyTo` for RPC-style replies.
- **Capability handshake**: on connect, exchange `{ protocolVersion, features, maxFrame }` and branch behavior on feature flags.
- **Ack + retry**: for non-idempotent commands, require ACK; add jittered retry + timeout.
- **Backpressure**: limit in-flight messages; use credits or windowed send (e.g., max 128 in-flight).
- **Reconnect safety**: clear pending requests on disconnect; re-emit subscriptions after rejoin.

## Worker-host guidance
- Keep the shell thin and let the worker host own application state.
- Treat shell-to-worker messaging as a control plane, not a place to implement business logic.
- Avoid implicit globals; pass config over IPC during init.
- Keep initialization idempotent so reconnects rehydrate safely.

## bare-atomics ring buffer guidance
- Use ring buffers for high-frequency telemetry (stats, metrics) not for RPC.
- Store fixed-size records; publish write index via Atomics.store; read via Atomics.load.
- Always reserve space first; drop oldest or newest if buffer full.

## Debugging checklist
- Verify single source of truth for connection state.
- Log connect/disconnect events with transport IDs.
- Trace message IDs at send/recv to detect duplication/loss.
- Confirm the worker host is still alive after shell resume or update handoff.
