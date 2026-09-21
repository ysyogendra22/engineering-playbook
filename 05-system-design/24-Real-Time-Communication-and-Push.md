# Real-Time Communication & Push

Roadmap topic 24 · Stage 5: Async & Reliability

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) added beyond the original roadmaps

**In simple words:** normal HTTP is "client asks, server answers". For chat, live scores, or notifications, the server must send data when something happens. There are several ways, and on mobile the OS limits them.

---

#### 1. Polling, WebSockets, SSE — 🟢 Must Know

*Three ways to get fresh data from the server to the app.*

| Method | How | Good | Bad |
|---|---|---|---|
| **Short polling** | App asks every N seconds | Simplest | Wasteful, delayed, drains battery |
| **Long polling** | Server holds the request until there is news, then answers | Near real-time, plain HTTP | Reconnect after each message |
| **WebSocket** | One persistent **two-way** connection | Low latency both ways | Stateful connections to manage |
| **SSE** (server-sent events) | Persistent connection, **server → client only** | Simple, auto-reconnect | One direction only |

---

#### 2. Choosing a Method — 🟢 Must Know

*Pick by direction, speed, and number of users.*

Ask: **which direction? how fast? how many users?**

```text
Chat, multiplayer game, collaboration → WebSocket (two-way)
Live scores, notifications, stock feed → SSE (server → client)
Occasional updates, simple                → Polling
App is in the background                  → Push notification (section 4)
```

---

#### 3. Connection Management — 🟢 Must Know

*Connections break all the time, especially on mobile.*

1. **Heartbeat / ping** — detect dead connections.
2. **Reconnect with backoff** (with jitter), so a server restart doesn't cause a reconnect storm.
3. **Missed-message recovery** — while disconnected, the client misses messages.
   - Give each message an **ID or sequence number**.
   - On reconnect the client says "my last message was 105", and the server sends everything after it.
4. Authenticate the connection when it opens, and re-check on reconnect.

---

#### 4. Push Notifications (FCM / APNs) — 🟢 Must Know (New)

*How to reach a user whose app is closed.*

1. **FCM** (Firebase Cloud Messaging) for Android, **APNs** (Apple Push Notification service) for iOS.
2. The OS **stops background connections** (like WebSockets), so push wakes the user up.
3. Flow:

```text
App → registers with FCM/APNs → gets a device token → sends token to your server
Server event → your server → FCM/APNs → device → notification
```

4. Delivery is **best effort, not guaranteed.** The payload is small (a few KB).
5. Send a small message or ID, and let the app **fetch the details** when opened.
6. Handle token refresh and remove invalid tokens.

---

#### 5. Scaling WebSockets and Presence — 🟡 Good to Know

*Connections stay open, so servers need extra care.*

1. Each connection holds server memory, so one server handles a limited number (tens of thousands).
2. Users are connected to **different servers**. To send a message to user B on server 2, use a **pub/sub** channel (for example, Redis) between servers.
3. **Presence** (online/offline): use heartbeats with a short TTL in a fast store.
4. Use a load balancer that supports WebSockets.

```text
User A → Server 1 → pub/sub → Server 2 → User B
```

---

#### 6. Common Interview Questions

1. **How do you deliver a chat message to a user who is offline?**
   Store the message. Send a push notification (FCM/APNs). When the app opens, it reconnects and fetches messages after its last known message ID.
2. **WebSocket vs SSE vs polling?**
   WebSocket: two-way. SSE: server to client only. Polling: simplest but wasteful.
3. **How do you handle disconnects?**
   Heartbeat, reconnect with backoff, and recover missed messages by sequence number.
4. **How do you scale WebSockets?**
   Many connection servers behind a load balancer, with pub/sub to route messages between servers.
5. **Why use push notifications when you have WebSockets?**
   The OS closes background connections. Push reaches closed apps.

---

#### 7. Common Mistakes

1. Polling every second.
2. No reconnect strategy, or reconnecting instantly on failure.
3. No way to recover missed messages.
4. Relying on push as guaranteed delivery.
5. Putting large or sensitive data inside push payloads.
6. Ignoring that connections are stateful when scaling.

---

#### 8. Related Topics

1. `21` Queues, Events & Background Jobs
2. `23` Consistency & CAP
3. `30` Mobile-Specific Topics
4. `32` Practice Designs (chat, notification system)

---

#### 9. Interview Must Remember

1. **Polling → long polling → SSE → WebSocket**, by need.
2. **Reconnect with backoff; recover missed messages with a sequence ID.**
3. **Push (FCM/APNs)** reaches closed apps; it's best effort.
4. Scale WebSockets with **pub/sub** between servers.
5. Send small pushes; **fetch details** in the app.
