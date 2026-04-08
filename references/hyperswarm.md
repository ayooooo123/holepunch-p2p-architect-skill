# Hyperswarm Deep-Dive Guide

Use this when the app needs peer discovery, NAT traversal, encrypted peer connections, or a network lifecycle that can be paused and resumed by a worker host.

Last reviewed: Wednesday, April 8, 2026.

## What Hyperswarm is for
Hyperswarm is the discovery and connection layer for peers interested in the same topic. In worker-first apps, the worker host should own the swarm and manage joins, connections, suspension, and resumption. Shells should only trigger lifecycle changes and render state.

Use Hyperswarm when you need:
- topic-based peer discovery
- encrypted peer connections over the DHT
- client/server style participation on the same topic
- a connection manager that can survive app lifecycle transitions

## API surface to know

### Constructor
```js
const swarm = new Hyperswarm(opts = {})
```

Notable options:
- `keyPair`: Noise keypair for identity
- `seed`: deterministic seed for the keypair
- `maxPeers`: connection cap
- `firewall(remotePublicKey)`: reject unwanted peers
- `dht`: lower-level DHT instance when you need custom networking control

### Topic discovery
```js
const discovery = swarm.join(topic, { client: true, server: true })
```

Key concepts:
- `topic` must be a 32-byte Buffer
- `client: true` means actively discover and connect
- `server: true` means announce yourself so others can connect
- `discovery.flushed()` waits for announcements to finish
- `discovery.refresh({ client, server })` updates discovery mode
- `discovery.destroy()` leaves the topic

### Connections and peer info
- `swarm.on('connection', (socket, peerInfo) => {})` fires for new peer connections
- `peerInfo.publicKey` identifies the peer
- `peerInfo.topics` is only populated when the peer is in client mode
- `peerInfo.prioritized` tells the swarm to reconnect faster
- `peerInfo.ban()` can ban or unban a peer

### Lifecycle and control
- `await swarm.flush()` waits for pending announces and connections
- `await swarm.leave(topic)` stops discovery for a topic
- `swarm.joinPeer(noisePublicKey)` forces a direct connection to a known peer
- `swarm.leavePeer(noisePublicKey)` stops that direct connection effort
- `await swarm.suspend()` and `await swarm.resume()` are useful in runtime suspend/resume flows
- `swarm.on('update')` is useful for UI status updates

## Common usage patterns

### 1) Join once, keep the discovery handle alive
Store the `discovery` object in the worker host. Do not let it get garbage-collected while the app still needs network presence.

### 2) Use client/server modes intentionally
- client mode: find peers and connect
- server mode: announce a peer target
- use both for symmetric network participation

### 3) Pair with Hypercore replication
On `connection`, pipe the socket into the Hypercore replication stream for the core or cores managed by the worker host.

### 4) Suspend and resume with lifecycle changes
Mobile and desktop shells should tell the worker host when the app is backgrounded, suspended, or restarted. The worker host should call `swarm.suspend()`/`swarm.resume()` or rejoin topics as needed.

## Hyperswarm in the Bare worker-based architecture

### Recommended placement
- shared core: topic names, protocol versioning, message schema, join policy
- worker host: swarm instance, discovery handles, connection lifecycle, replication wiring
- shell adapter: lifecycle signals, UI state, and user actions

### Worker-host responsibilities
The worker host should:
- create and own the swarm
- join the app topic(s)
- keep discovery handles alive
- connect peers and route sockets to replication or custom protocol handlers
- handle suspend/resume, reconnect, and leave/join transitions

### Shell responsibilities
The shell should:
- launch the worker host
- surface connection state to the user
- forward foreground/background or focus changes

## Minimal worker-host shape
```js
import Hyperswarm from 'hyperswarm'
import Hypercore from 'hypercore'

export async function createSwarmHost ({ storage, log, topic }) {
  const swarm = new Hyperswarm()
  const core = new Hypercore(storage)
  await core.ready()

  const discovery = swarm.join(topic, { client: true, server: true })
  await discovery.flushed()

  swarm.on('connection', (socket, peerInfo) => {
    const stream = core.replicate(peerInfo.client, { live: true })
    socket.pipe(stream).pipe(socket)
  })

  return {
    async suspend () {
      await swarm.suspend({ log })
    },
    async resume () {
      await swarm.resume({ log })
    },
    async stop () {
      discovery.destroy()
      await swarm.destroy?.()
      await core.close()
    }
  }
}
```

## Practical rules
- Topic identifiers must be 32 bytes
- Use `discovery.flushed()` when you need to know the server announcement has completed
- Prefer `swarm.flush()` only when you need to wait for all pending connection work
- Keep the swarm in the worker host, not in the UI layer
- Use `swarm.suspend()` and `swarm.resume()` for lifecycle-aware runtimes
- If the app already knows a peer, use `joinPeer()` for direct reconnection behavior

## Good fit app types
- live peer discovery
- replicated feeds and comments
- chat and coordination apps
- direct encrypted pipes
- runtime-aware apps that must survive suspend/resume
