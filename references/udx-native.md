# udx-native Deep-Dive Guide

Use this when the app needs raw UDP transport, multiplexed message streams, or a lower-level transport layer beneath discovery and replication.

Last reviewed: Wednesday, April 8, 2026.

## What udx-native is for
udx-native provides reliable, multiplexed, congestion-controlled streams over UDP. It is a transport protocol, not a full discovery or application layer.

Use udx-native when you need:
- raw peer transport
- multiplexed custom streams
- message-oriented UDP communication
- a foundation for discovery or sync layers in a worker host

## API surface to know

### Core instance
```js
const u = new UDX()
```

Helpful helpers:
- `UDX.isIPv4(host)`
- `UDX.isIPv6(host)`
- `UDX.isIP(host)`
- `u.networkInterfaces()`
- `u.watchNetworkInterfaces([onchange])`
- `await u.lookup(host, [options])`

### Socket APIs
- `const socket = u.createSocket([options])`
- `socket.bind([port], [host])`
- `socket.address()`
- `await socket.send(buffer, port, [host], [ttl])`
- `socket.trySend(buffer, port, [host], [ttl])`
- `await socket.close()`
- `socket.setTTL(ttl)`
- `socket.on('message', (msg, from) => {})`
- `socket.on('listening')`, `socket.on('close')`, `socket.on('idle')`, `socket.on('busy')`

### Stream APIs
- `const stream = u.createStream(id, [options])`
- `stream.connect(socket, remoteId, port, [host], [options])`
- `await stream.changeRemote(remoteId, port, [host])`
- `stream.relayTo(destination)`
- `await stream.send(buffer)`
- `stream.trySend(buffer)`
- `await stream.flush()`
- `stream.on('connect')`, `stream.on('message')`, `stream.on('remote-changed')`, `stream.on('mtu-exceeded')`

## Common usage patterns

### 1) Use udx-native as the transport layer
Pair it with discovery or protocol code. It is intentionally low-level so higher layers can decide what messages mean.

### 2) Keep streams and sockets in the worker host
The worker host should own UDP sockets, stream IDs, and lifecycle cleanup.

### 3) Watch interfaces when networking can change
For mobile or laptop apps, use `watchNetworkInterfaces()` so the worker host can react to network changes.

### 4) Flush when you need delivery guarantees
Use `stream.flush()` when the app needs to know queued writes were acknowledged.

## udx-native in the Bare worker-based architecture

### Recommended placement
- shared core: message schema, retry rules, protocol versioning
- worker host: sockets, stream registry, interface watching, transport retries
- shell adapter: lifecycle notifications and status UI

### Worker-host responsibilities
The worker host should:
- create the UDX instance
- manage sockets and streams
- keep transport logic out of the UI
- bridge the transport to Hyperswarm, HyperDHT, or custom protocols

### Shell responsibilities
The shell should:
- report connectivity state
- forward lifecycle changes
- avoid manipulating UDP sockets directly

## Minimal worker-host shape
```js
import UDX from 'udx-native'

export async function createTransportHost ({ log }) {
  const udx = new UDX()
  const socket = udx.createSocket()
  socket.bind(0)

  return {
    udx,
    socket,
    async stop () {
      await socket.close()
    }
  }
}
```

## Practical rules
- Use udx-native for transport, not discovery
- Keep UDP state inside the host
- Use stream IDs to multiplex logical channels
- Watch network interfaces if the app must survive network changes
- Prefer higher-level layers when you do not need raw transport control

## Good fit app types
- custom peer transport
- NAT-friendly transports
- protocol multiplexing
- relay layers
- transport experiments inside a worker host
