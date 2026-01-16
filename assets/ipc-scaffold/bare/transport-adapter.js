// Placeholder transport adapter for Bare IPC.
// Wire this to bare-ipc or BareKit IPC primitives.
export function createBareTransport({ send, onMessage }) {
  return {
    send: (msg) => send(msg),
    onMessage: (handler) => onMessage(handler),
  };
}
