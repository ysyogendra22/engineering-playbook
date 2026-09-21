# Networking & HTTP

Roadmap topic 2 · Stage 1: Foundations

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** the road your request travels on. DNS finds the server, TCP and TLS build a safe connection, and HTTP is the language used on it.

---

#### 1. IP, Domain, Port, DNS — 🟢 Must Know

*IP = house address. Port = which door of the house. Domain = the name in your contacts. DNS = the phone book that turns the name into the address.*

1. **IP address** — identifies a machine on the network (`142.250.183.14`). IPv6 is the newer, larger format.
2. **Domain name** — human-friendly name (`api.example.com`).
3. **Port** — identifies which program on that machine gets the traffic.
4. **DNS** — turns a domain into an IP address. Results are cached for a while (**TTL**).

```text
api.example.com  →  DNS  →  203.0.113.10
Connect to 203.0.113.10 : 443
```

Common ports:

```text
80   → HTTP
443  → HTTPS
22   → SSH
```

---

#### 2. TCP vs UDP — 🟢 Must Know

*TCP is a phone call that makes sure every word arrives in order. UDP is shouting messages and hoping they arrive.*

| | TCP | UDP |
|---|---|---|
| Delivery | Reliable, in order | May lose or reorder |
| Speed | Slower (setup + checks) | Faster |
| Used for | HTTP, APIs, file download | Video calls, games, live streams |

**Remember:** REST APIs run on TCP.

---

#### 3. HTTP vs HTTPS — 🟢 Must Know

*HTTP is a postcard anyone can read. HTTPS is a sealed, signed envelope.*

1. **HTTP** — plain text. Anyone on the network can read or change it.
2. **HTTPS** = HTTP + **TLS**.
3. TLS gives: **encryption** (nobody can read it), **server identity** (a certificate proves you reached the real server), and **integrity** (data can't be changed on the way).

**Mobile view:** iOS (App Transport Security) and modern Android block plain HTTP by default. Always use HTTPS in production.

---

#### 4. HTTP Request — 🟢 Must Know

*A request says: what do you want (method + URL), who am I (headers), and here is my data (body).*

```http
POST /notes HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
Content-Type: application/json

{ "title": "Buy milk" }
```

Parts:

1. **Method** — the action.
2. **URL** — path (`/notes/42`) and query (`?limit=20`).
3. **Headers** — extra info: token, content type, app version.
4. **Body** — data (POST, PUT, PATCH).

| Method | Use | Safe? | Idempotent? |
|---|---|---|---|
| GET | Read | Yes | Yes |
| POST | Create | No | No |
| PUT | Replace | No | Yes |
| PATCH | Partial update | No | Not guaranteed |
| DELETE | Delete | No | Yes |

*Safe = doesn't change data. Idempotent = repeating gives the same final result.*

---

#### 5. HTTP Response & Status Codes — 🟢 Must Know

*The response says how it went (status code), gives info (headers), and returns data (body).*

```http
HTTP/1.1 201 Created
Content-Type: application/json

{ "id": 42, "title": "Buy milk" }
```

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | Success, no body (often for delete) |
| 400 | Bad request (invalid input) |
| 401 | Not logged in / bad token |
| 403 | Logged in, but not allowed |
| 404 | Not found |
| 409 | Conflict (for example, duplicate) |
| 429 | Too many requests |
| 500 | Server bug |
| 503 | Server unavailable / overloaded |

Groups: **2xx** success · **3xx** redirect · **4xx** client's mistake · **5xx** server's problem.

**401 vs 403:** 401 = "I don't know who you are." 403 = "I know who you are, but you can't do this."

**Retry rule:** 5xx and timeouts can be retried (if the operation is safe). 4xx (except 429) will fail again, so fix the request instead.

---

#### 6. Timeouts & Connection Reuse — 🟢 Must Know

*Never wait forever. And don't rebuild the phone line for every sentence.*

1. **Connect timeout** — max time to open the connection.
2. **Read timeout** — max time to wait for the response.
3. Always set both in the app. Without them, a screen can hang.
4. **Keep-alive** — reuse one connection for many requests. Opening a new one costs extra round trips (TCP + TLS).

```text
New connection:   DNS → TCP → TLS → request
Reused connection:                  request
```

---

#### 7. Full Trace: App Calls `https://api.example.com/notes` — 🟢 Must Know

```text
1. DNS        api.example.com → IP
2. TCP        connect to IP : 443
3. TLS        encrypt, verify certificate
4. HTTP       send request (method, headers, body)
5. Server     process
6. HTTP       receive response (status, headers, body)
7. App        parse JSON, update UI
```

---

#### 8. HTTP/2 and HTTP/3 — 🟡 Good to Know

1. **HTTP/1.1** — one request at a time per connection.
2. **HTTP/2** — many requests at the same time on one connection; smaller headers.
3. **HTTP/3** — runs on UDP (QUIC). Faster to connect and handles switching between Wi-Fi and mobile data better. Good for mobile.

---

#### 9. Cookies, Content Types, Compression — 🟡 Good to Know

1. **Cookie** — small data the server sets; the browser sends it back automatically. Mostly for web. Mobile apps usually send a token in the `Authorization` header.
2. **Content-Type** — format of the body (`application/json`). **Accept** — the format the client wants.
3. **Compression** — `gzip`. Client sends `Accept-Encoding: gzip`, server replies with `Content-Encoding: gzip`. Saves mobile data.

---

#### 10. Reverse Proxy — 🟡 Good to Know

1. Sits in front of your servers (for example, Nginx).
2. Handles TLS, routing, compression, load balancing, and caching.
3. Clients talk to the proxy and never see the real servers.

```text
App → Reverse Proxy → Server A / Server B
```

---

#### 11. Common Interview Questions

1. **What happens when you call `https://api.example.com/notes`?**
   DNS lookup → TCP connection → TLS handshake → HTTP request → server processes → HTTP response → app updates UI.
2. **TCP vs UDP?**
   TCP is reliable and ordered (APIs). UDP is faster but may lose data (video calls, games).
3. **What does HTTPS give you over HTTP?**
   Encryption, server identity, and protection against tampering.
4. **401 vs 403?**
   401 = not authenticated. 403 = authenticated but not allowed.
5. **What is DNS?**
   It converts a domain name into an IP address, and the result is cached.
6. **Why set timeouts? Which ones?**
   To avoid hanging forever. Connect timeout and read timeout.
7. **What is a safe or idempotent method?**
   Safe = no data change (GET). Idempotent = repeating gives the same result (GET, PUT, DELETE).

---

#### 12. Common Mistakes

1. Using HTTP instead of HTTPS.
2. No timeouts in the app.
3. Confusing 401 and 403.
4. Using GET to change data.
5. Retrying non-idempotent requests (like payments) blindly.
6. Thinking a domain and an IP are the same thing.

---

#### 13. Related Topics

1. `01` Client, Server & Request Flow
2. `03` API Design
3. `05` Authentication & Authorization
4. `06` Backend Security Essentials
5. Load balancer, CDN (system design roadmap)

---

#### 14. Interview Must Remember

1. **DNS → TCP → TLS → HTTP** is the path of every request.
2. **TCP** = reliable (APIs). **UDP** = fast, may lose data.
3. **HTTPS = HTTP + TLS** (encrypt, identity, integrity).
4. A request has **method, URL, headers, body**. A response has **status, headers, body**.
5. **4xx = client's fault. 5xx = server's fault.** 401 vs 403.
6. Set **connect and read timeouts**. Reuse connections.
