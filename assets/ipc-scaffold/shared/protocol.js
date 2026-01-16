// Minimal message envelope to standardize IPC across transports.
export const PROTOCOL_VERSION = 1;

export function makeMessage(type, payload, opts = {}) {
  return {
    v: PROTOCOL_VERSION,
    id: opts.id ?? `${Date.now()}-${Math.random().toString(16).slice(2)}`,
    replyTo: opts.replyTo ?? null,
    ts: Date.now(),
    type,
    payload,
    meta: opts.meta ?? {},
  };
}

export function isProtocolMessage(msg) {
  return Boolean(msg && msg.v === PROTOCOL_VERSION && msg.type);
}
