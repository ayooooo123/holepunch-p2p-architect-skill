# Holepunch P2P Architect Skill

An AI skill for designing, implementing, debugging, and testing production-ready P2P applications using the Holepunch stack.

## Overview

This skill is built for one-shotting: when you ask for a complete P2P app or feature, it should produce the full repo shape, the right runtime boundary, the worker host, the shell adapters, and the build/test/run commands in one pass.

Default architecture: Bare worker-first. Keep the worker as the application core host, keep shells thin, and move platform-specific code behind adapters.

For modern desktop apps, the current v2 standard is an Electron shell that embeds pear-runtime, launches a Bare worker host, and keeps update handling in the shell bridge layer. The shell owns UI and lifecycle; the worker owns peer logic, storage, discovery, and replication.

The skill provides structured workflows and reference materials for building peer-to-peer applications with:

- Hypercore - append-only logs
- Hyperdrive - file system abstraction
- Hyperbee - key-value store
- Hyperdb - legacy compatibility, when validated first
- Autobase - multi-writer consensus
- Hyperswarm - peer discovery and networking
- HyperDHT - distributed hash table
- Protomux - protocol multiplexing
- Pear Runtime - desktop P2P apps and update coordination
- Bare Runtime - lightweight JS runtime and worker host

## Module guides and references

Use the module guides below as the source of truth when choosing primitives or planning the repo shape:

- references/stack-map.md - decision matrix for data model and networking choices
- references/app-scaffold.md - canonical Bare worker-first app structure and v2 desktop shell shape
- references/runtime-abstraction.md - shared-core, worker-host, and shell-adapter boundaries
- references/pear-runtime.md - Pear Runtime API surface, updater lifecycle, and worker launch
- references/pear-v2-architecture.md - Electron + pear-runtime v2 architecture pattern
- references/autobase.md - Autobase API surface and materialization patterns
- references/hypercore.md - Hypercore replication and storage patterns
- references/hyperdrive.md - Hyperdrive file-tree patterns
- references/hyperblob.md - Hyperblob/blob handling patterns
- references/hyperdht.md - HyperDHT announce and lookup patterns
- references/hyperswarm.md - Hyperswarm discovery and lifecycle patterns
- references/bare-runtime.md - Bare runtime bootstrapping and process discovery
- references/bare-build.md - Bare packaging and release workflows
- references/bare-addon.md - Bare native addon workflows
- references/bare-link.md - Bare linker workflows
- references/udx-native.md - transport and worker-host patterns
- references/ipc-runtime.md - shell/worker IPC envelopes and reconnect guidance
- references/ipc-repos.md - repo index and grep patterns for upstream examples
- references/build-deploy.md - build, test, package, and release command matrix
- references/debug-playbook.md - sync and discovery troubleshooting
- references/testing.md - test strategy patterns
- references/holepunch-org-index.md - auto-updating Holepunch org repository index

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

## Skill structure

```
holepunch-p2p-architect/
  SKILL.md                      # Main skill definition
  references/
    app-scaffold.md             # Canonical Bare worker-first scaffold
    autobase.md                 # Autobase guide
    bare-addon.md               # Bare addon guide
    bare-build.md               # Bare packaging guide
    bare-link.md                # Bare linker guide
    bare-runtime.md             # Bare runtime guide
    build-deploy.md             # Build / test / release commands
    debug-playbook.md           # Sync / discovery troubleshooting
    holepunch-org-index.md      # Auto-updating Holepunch org index
    hyperblob.md                # Hyperblob guide
    hypercore-storage.md        # Hypercore storage guide
    hypercore.md                # Hypercore guide
    hyperdht.md                 # HyperDHT guide
    hyperdrive.md               # Hyperdrive guide
    hyperswarm.md               # Hyperswarm guide
    ipc-repos.md                # IPC repo index and grep patterns
    ipc-runtime.md              # IPC runtime guide
    pear-runtime.md             # Pear runtime guide
    pear-v2-architecture.md     # Electron + pear-runtime v2 architecture guide
    runtime-abstraction.md      # Runtime boundary guide
    stack-map.md                # Primitive decision matrix
    testing.md                  # Testing guide
    udx-native.md               # UDX transport guide
  scripts/
    sync_holepunch_repos.py     # Mirror org repos and refresh the org index
    fetch_pears_docs.sh         # Mirror Pear documentation
    pear_dump_app.sh             # Dump Pear apps for analysis
  assets/
    ipc-scaffold/               # Minimal IPC starter code
      shared/protocol.js
      shared/router.js
      pear/transport-adapter.js
      bare/transport-adapter.js
    templates/
      bare-worker.md            # Default one-shot worker-first scaffold
      desktop.md                # Pear desktop scaffold
      electron-v2.md            # Canonical Electron + pear-runtime v2 scaffold
      mobile.md                 # Bare/BareKit mobile scaffold
      shared-core.md            # Shared domain logic scaffold
      terminal.md               # Pear terminal scaffold
```

## One-shotting goal

When asked to generate a working app, aim for a complete, runnable repo in one response:

1. Pick the target platform(s) and runtime(s).
2. Choose the primary P2P primitive(s).
3. Default to a Bare worker-first architecture: shared core first, worker host second, shell adapters third.
4. Emit a concrete file tree based on the canonical scaffold and the platform guides.
5. Generate the shared core modules first, with no direct dependence on platform globals.
6. Generate the worker host, then platform bootstrap files.
7. For Electron desktop targets, use the pear-runtime v2 shell pattern: Electron main process, preload bridge, renderer UI, worker host.
8. Add platform-specific config and package scripts using the build/deploy guide.
9. Add build, test, and run commands.
10. Add a short acceptance checklist covering shell start, worker start, discovery, replication, persistence, and update checks.
11. Call out assumptions and missing product decisions explicitly at the end.

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

## Usage examples

### Architecture design
> "Design a multi-platform P2P app architecture that works on an Electron shell, a Pear terminal shell, and a Bare worker host with shared IPC code."

### Feature implementation
> "Implement a comments feature using Autobase with multi-writer support and moderation."

### IPC setup
> "Set up IPC between an Electron shell and a Bare worker with typed messages and reconnect logic."

### One-shot app generation
> "Generate a complete Bare worker-first chat app with discovery, persistence, tests, and build scripts."

### Desktop v2 app
> "Generate a complete Electron app using pear-runtime v2, preload IPC, worker launch, and update restart flow."

### Debugging
> "Debug why peers aren't discovering each other and replication keeps failing."

### Performance
> "Optimize replication throughput when syncing large Hyperdrive archives."

## Knowledge sync

Before using the skill, sync local copies of upstream repos and docs, then refresh the Holepunch org index:

```bash
# Sync Holepunch-adjacent repositories and refresh references/holepunch-org-index.md
python scripts/sync_holepunch_repos.py --org holepunchto --org pearopen --org tetherto --index-org holepunch

# Mirror the newest v2 architecture examples
# - holepunchto/hello-pear-electron
# - holepunchto/pear-runtime

# Mirror Pear documentation
./scripts/fetch_pears_docs.sh

# Dump a reference Pear app
./scripts/pear_dump_app.sh pear://keet
```

Local mirrors are stored in `~/.codex/skills-cache/holepunch-p2p-architect/`.

## Key decision matrix

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
