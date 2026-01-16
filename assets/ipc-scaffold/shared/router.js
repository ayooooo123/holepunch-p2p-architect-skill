// Simple in-process router for request/response style IPC.
export class IpcRouter {
  constructor() {
    this.handlers = new Map();
  }

  on(type, handler) {
    this.handlers.set(type, handler);
  }

  async handle(message, sendReply) {
    const handler = this.handlers.get(message.type);
    if (!handler) return;
    try {
      const result = await handler(message.payload, message);
      sendReply({ ok: true, result });
    } catch (error) {
      sendReply({ ok: false, error: String(error?.message || error) });
    }
  }
}
