// Placeholder transport adapter for Pear IPC.
// Wire this to pear-ipc once you pick transport/channel primitives.
export function createPearTransport({ send, onMessage }) {
  return {
    send: (msg) => send(msg),
    onMessage: (handler) => onMessage(handler),
  };
}
