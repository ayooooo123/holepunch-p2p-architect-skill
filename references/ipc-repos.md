# IPC/Runtime Repos & Grep Patterns

## Repo sync
Use the skill cache:
- `scripts/sync_holepunch_repos.py --org holepunchto --org tetherto --org pearopen`

Local cache:
- `~/.codex/skills-cache/holepunch-p2p-architect/repos/<org>/<repo>`

## Key repos to inspect
- pearopen/* (up-to-date cross-platform examples: desktop, mobile, CLI)
- tetherto/* (Pear/Bare examples)
- holepunchto/pear-ipc
- holepunchto/bare-ipc
- holepunchto/bare-atomics
- holepunchto/bare-workers
- holepunchto/bare-thread
- holepunchto/bare-kit
- holepunchto/pear

## Priority guidance
- Start with pearopen examples for realistic patterns and best practices.
- Use holepunchto repos only when you need lower-level API details or missing behavior.

## Grep patterns
Run in the local cache:
- `rg "ipc|rpc|request|response" holepunchto/pear-ipc`
- `rg "SharedArrayBuffer|Atomics" holepunchto/bare-atomics`
- `rg "worker|thread" holepunchto/bare-workers holepunchto/bare-thread`
- `rg "BareKit|IPC" holepunchto/bare-kit`

## Docs
If Pear docs are mirrored:
- `~/.codex/skills-cache/holepunch-p2p-architect/docs/pears`
