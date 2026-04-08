# Autobase Deep-Dive Guide

Use this when the app needs a multi-writer replicated data structure, eventually consistent ordering, or a worker-hosted materialized view.

Last reviewed: Wednesday, April 8, 2026.

## What Autobase is for
Autobase combines multiple writer cores into a single ordered view of the system. It fits the worker-host pattern well because the worker can own the writers, the view store, and the replication lifecycle while shells stay thin.

Use Autobase when you need:
- multi-writer comments, feeds, reactions, or activity streams
- deterministic materialization of concurrent writes
- a view that can be rebuilt from writer history
- local user data that should stay off the replicated log

## API surface to know

### Constructor and readiness
```js
const base = new Autobase(store, bootstrap, { open, apply })
await base.ready()
```

Key concepts:
- `store` is usually a single Corestore for the whole app
- `bootstrap` is the bootstrap core or bootstrap key for the Autobase
- `open(store)` creates the view core(s)
- `apply(nodes, view, host)` deterministically applies writer nodes into the view

### Core methods and properties
- `await base.append(value)` appends a local writer value
- `await base.update()` advances the materialized view
- `base.replicate(isInitiatorOrStream, opts)` replicates the base
- `base.view` is the current materialized view
- `base.discoveryKey` is what you join in discovery
- `base.getUserData(key)` / `base.setUserData(key, value)` for local-only state
- `Autobase.isAutobase(core, opts)` checks whether a core belongs to Autobase

### AutoStore helpers
Autobase creates an AutoStore for view creation.
- `store.get(nameOrOptions)` loads or creates a named Hypercore view

## Common usage patterns

### 1) Event-sourced multiwriter data
Represent each user action as an append to a writer core. The `apply` function merges those nodes into a view in a deterministic way.

### 2) Add-writer protocol
The common pattern is to append a control record such as `{ addWriter: writerKey }`, then have `apply` call `host.addWriter(...)` before processing normal records.

### 3) Materialized views in the worker host
The worker host should own:
- the Corestore
- the Autobase instance
- the `open` and `apply` functions
- the replication and discovery handles

### 4) User data for local-only secrets
Autobase uses Hypercore user data for local metadata like encryption keys and writer/bootstrap relationships. Keep that data in the worker host, not in the shell.

## Autobase in the Bare worker-based architecture

### Recommended placement
- shared core: record schema, validation, conflict rules, projection logic
- worker host: Autobase instance, Corestore, discovery, replication, materialization
- shell adapter: UI rendering, user input, and lifecycle signals

### Worker-host responsibilities
The worker host should:
- create one Corestore for the app
- create Autobase with explicit `open` and `apply`
- keep discovery handles alive
- call `update()` when the swarm or data changes
- persist any local-only operational state via user data

### Shell responsibilities
The shell should:
- boot the worker host
- show view state
- forward edits and lifecycle changes
- avoid owning replication logic

## Minimal worker-host shape
```js
import Corestore from 'corestore'
import Autobase from 'autobase'
import Hyperswarm from 'hyperswarm'

export async function createAutobaseHost ({ storage, topic, log }) {
  const store = new Corestore(storage)
  const swarm = new Hyperswarm()

  const base = new Autobase(store, null, {
    open (store) {
      return store.get({ name: 'view' })
    },
    async apply (nodes, view, host) {
      for (const node of nodes) {
        const { value } = node
        if (value?.addWriter) {
          await host.addWriter(value.addWriter, { indexer: true })
          continue
        }
        await view.append(value)
      }
    }
  })

  await base.ready()
  const discovery = swarm.join(base.discoveryKey, { client: true, server: true })

  swarm.on('connection', socket => {
    store.replicate(socket)
  })

  return {
    async append (value) {
      await base.append(value)
      await base.update()
    },
    async stop () {
      discovery.destroy()
      await swarm.destroy?.()
      await base.close?.()
      await store.close?.()
    }
  }
}
```

## Practical rules
- Use a single Corestore per app
- Keep `apply` deterministic and side-effect free except for explicit host actions
- Use Autobase when multiple peers can author records
- Keep writer identity and view storage in the worker host
- Do not put UI-specific code inside `apply`

## Good fit app types
- collaborative docs
- comments and replies
- shared feeds
- moderation queues
- multi-writer activity timelines
