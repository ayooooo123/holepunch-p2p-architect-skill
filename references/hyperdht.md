# HyperDHT Deep-Dive Guide

Use this when the app needs direct peer discovery, encrypted DHT-backed connections, or custom server/client key connections outside the higher-level swarm layer.

Last reviewed: Wednesday, April 8, 2026.

## What HyperDHT is for
HyperDHT powers peer discovery and distributed hole punching. It is the lower-level DHT underneath Hyperswarm and is useful when you need direct key-based connections, isolated DHT networks, or custom discovery/announce behavior.

Use HyperDHT when you need:
- direct connect-by-key workflows
- custom DHT bootstrap networks
- hole punching and peer discovery
- a transport or discovery layer inside a worker host

## API surface to know

### Constructor and identity
```js
const node = new DHT([options])
const keyPair = DHT.keyPair([seed])
```

Notable options:
- `bootstrap`
- `keyPair`
- `connectionKeepAlive`
- `randomPunchInterval`

### Server-side APIs
- `const server = node.createServer([options], [onconnection])`
- `await server.listen(keyPair)`
- `server.refresh()`
- `server.address()`
- `await server.close()`
- `server.on('connection', socket)`
- `server.on('listening')`
- `server.on('close')`

### Client-side APIs
- `const socket = node.connect(remotePublicKey, [options])`
- `socket.on('open')`
- `socket.remotePublicKey`
- `socket.publicKey`

### Discovery and announcement
- `const stream = node.lookup(topic, [options])`
- `const stream = node.announce(topic, keyPair, [relayAddresses], [options])`
- `await node.unannounce(topic, keyPair, [options])`
- `await node.destroy([options])`
- `await node.ready(callback)`
- `await node.bootstrap([callback])`
- `node.listen(port, callback)`
- `node.remoteAddress()` for diagnostics
- `DHT.bootstrapper(port, host, [options])` to create a bootstrap node

### Mutable/immutable records
- `await node.immutablePut(value, [options])`
- `await node.immutableGet(hash, [options])`
- `await node.mutablePut(keyPair, value, [options])`
- `await node.mutableGet(publicKey, [options])`

## Common usage patterns

### 1) Bootstrap a private or isolated DHT
Create one bootstrap node, then point all app nodes at it. For private networks, keep at least one persistent node alive.

### 2) Connect peers by public key
Use `createServer` + `connect` when you know the peer key and want a direct encrypted connection.

### 3) Announce a topic, then look up peers
Use `announce` and `lookup` for topic-based discovery. This is the lower-level form of what Hyperswarm wraps.

### 4) Keep discovery stable across lifecycle changes
If the runtime suspends, the worker host should refresh, resume, or recreate discovery and server state as needed.

## HyperDHT in the Bare worker-based architecture

### Recommended placement
- shared core: topic naming, peer policy, message schema
- worker host: DHT node, server/client setup, discovery, retries
- shell adapter: lifecycle signals and status display

### Worker-host responsibilities
The worker host should:
- own the DHT node instance
- manage bootstrap addresses
- maintain discovery and announce state
- keep direct peer connections alive as needed
- cleanly destroy or resume the node on shutdown/suspend

### Shell responsibilities
The shell should:
- pass lifecycle events to the worker host
- avoid direct DHT manipulation
- only render status or collect user actions

## Minimal worker-host shape
```js
import DHT from 'hyperdht'

export async function createDhtHost ({ bootstrap, log }) {
  const dht = new DHT({ bootstrap })
  await dht.ready()

  return {
    dht,
    async stop () {
      await dht.destroy()
    }
  }
}
```

## Practical rules
- Use one DHT node per app host when possible
- Keep bootstrap nodes persistent for isolated networks
- Use topic lookup for discovery and direct keys for private server connections
- Keep hole-punching state inside the worker host
- Prefer Hyperswarm when you want higher-level topic management

## Good fit app types
- peer discovery
- private or isolated networks
- direct encrypted peer connections
- relay/bootstrap infrastructure
- worker-host networking layers
