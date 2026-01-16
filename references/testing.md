# Testing Patterns for Holepunch P2P Apps

Use this guide to add unit and integration tests for Holepunch-based systems.

## Test Layers
- Unit tests: Pure logic (schema validation, message parsing, UI state).
- Integration tests: Two or more peers with replication enabled.
- End-to-end tests: Full app runtime (Pear/Bare) with realistic lifecycle.

## Deterministic Storage
- Prefer temporary or in-memory stores for tests.
- Ensure each test uses a unique storage path to avoid cross-test contamination.

## Replication Tests
- Create two stores and connect them directly through a swarm connection.
- Write data on peer A and assert peer B eventually sees it.
- Include timeouts and retries to handle network variance.

## Version Skew and Unknown Commands
- Add tests that send unknown RPC commands or old schema payloads.
- Ensure handlers ignore or log unsupported commands instead of crashing.

## Coverage Checklist
- Discovery: topic joins and handle retention.
- Replication: store-level and Autobase-level replication.
- Data consistency: idempotent updates and backfill behavior.
- Error handling: timeouts, missing peers, partial data.

## Where to Find Upstream Examples
- Use `scripts/sync_holepunch_repos.py` and search local mirrors for test patterns.
- Prefer upstream tests as the reference for current API usage.
