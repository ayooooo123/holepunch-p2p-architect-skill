# Holepunch P2P Architect Skill

An AI skill for designing, implementing, debugging, and testing production-ready P2P applications using the Holepunch stack.

## Overview

This skill provides structured workflows and reference materials for building peer-to-peer applications with:

- **Hypercore** - Append-only logs
- **Hyperdrive** - File system abstraction
- **Hyperbee** - Key-value store
- **Autobase** - Multi-writer consensus
- **Hyperswarm** - Peer discovery and networking
- **HyperDHT** - Distributed hash table
- **Protomux** - Protocol multiplexing
- **Pear Runtime** - Desktop P2P apps
- **Bare Runtime** - Lightweight JS runtime for mobile

## Installation

### For Claude Code / OpenCode

Copy the skill to your skills directory:

```bash
# Clone this repository
git clone https://github.com/ayooooo123/holepunch-p2p-architect-skill.git

# Copy to Claude skills directory
cp -r holepunch-p2p-architect-skill ~/.claude/skills/holepunch-p2p-architect

# Or for OpenCode
cp -r holepunch-p2p-architect-skill ~/.opencode/skills/holepunch-p2p-architect
```

### For other AI tools

Reference `SKILL.md` as a system prompt or context file.

## Skill Structure

```
holepunch-p2p-architect/
  SKILL.md                      # Main skill definition
  references/
    stack-map.md                 # Data model decision matrix
    ipc-runtime.md               # IPC patterns and guidance
    ipc-repos.md                 # Repository grep patterns
    debug-playbook.md            # Sync/discovery troubleshooting
    testing.md                   # Test strategy patterns
  scripts/
    sync_holepunch_repos.py      # Mirror Holepunch repos locally
    fetch_pears_docs.sh          # Mirror Pear documentation
    pear_dump_app.sh             # Dump Pear apps for analysis
  assets/
    ipc-scaffold/                # Minimal IPC starter code
      shared/protocol.js
      shared/router.js
      pear/transport-adapter.js
      bare/transport-adapter.js
```

## Workflows

The skill provides decision-tree workflows for common tasks:

| Task | Workflow |
|------|----------|
| Design architecture | Architecture Workflow |
| Implement features | Feature Workflow |
| Improve performance | Performance Workflow |
| Debug sync issues | Debugging Workflow |
| Add tests | Testing Workflow |
| Learn the ecosystem | Knowledge Sync Workflow |

## Usage Examples

### Architecture Design
> "Design a multi-platform P2P app architecture that works on Pear desktop and BareKit mobile with shared IPC code."

### Feature Implementation
> "Implement a comments feature using Autobase with multi-writer support and moderation."

### IPC Setup
> "Set up IPC between Pear renderer and a Bare worker with typed messages and reconnect logic."

### Debugging
> "Debug why peers aren't discovering each other and replication keeps failing."

### Performance
> "Optimize replication throughput when syncing large Hyperdrive archives."

## Knowledge Sync

Before using the skill, sync local copies of upstream repos and docs:

```bash
# Sync Holepunch repositories
python scripts/sync_holepunch_repos.py --org holepunchto --org pearopen --org tetherto

# Mirror Pear documentation
./scripts/fetch_pears_docs.sh

# Dump a reference Pear app
./scripts/pear_dump_app.sh pear://keet
```

Local mirrors are stored in `~/.codex/skills-cache/holepunch-p2p-architect/`.

## Key Decision Matrix

| Need | Primitive |
|------|-----------|
| Multi-writer data | Autobase |
| Fast indexed reads, single writer | Hyperbee |
| File tree semantics | Hyperdrive |
| Append-only history | Hypercore |
| Legacy compatibility | Hyperdb (validate first) |

## License

MIT

## Contributing

Issues and PRs welcome. This skill is designed to evolve with the Holepunch ecosystem.
