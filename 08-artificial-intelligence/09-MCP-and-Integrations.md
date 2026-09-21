# MCP & Integrations

Roadmap topic 9 · Stage 3: Tools & Agents

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) a newer idea, still changing

**In simple words:** MCP (Model Context Protocol) is a standard way to plug tools and data into AI apps. Build a tool once as an MCP server, and any AI app that speaks MCP can use it. Think of it as a common plug for AI tools. This area is new and changing, so learn the idea, not the details of any product.

---

#### 1. What MCP Is — 🟢 Must Know (New)

*One standard connector between AI apps and the outside world.*

1. **MCP** is an open standard that defines how an AI app talks to tools and data sources.
2. Without it, every AI app needs custom code for every tool (Slack, GitHub, a database, your notes API).
3. With it, you write one **MCP server** for a tool, and any MCP-compatible AI app can use it.

**Mobile view:** like USB-C. One standard plug, instead of a different cable for every device. It is also like a REST API contract, but built for AI apps.

---

#### 2. Roles: Host, Client, Server — 🟢 Must Know (New)

*Who talks to whom.*

```text
AI app (host)  ──[MCP client]──→  MCP server  →  Your API / database / files
 (assistant, IDE,                  (exposes tools,
  your own agent)                   resources, prompts)
```

1. **Host** — the AI application the user uses (an assistant, an IDE, your own agent).
2. **Client** — a connector inside the host. It keeps one connection to one server.
3. **Server** — a program that exposes capabilities and does the real work by calling your systems.
4. The model itself never talks to the server. The host does, on the model's behalf, like normal tool use (topic `08`).

---

#### 3. What a Server Offers — 🟢 Must Know (New)

*Three kinds of things.*

| Type | What it is | Example |
|---|---|---|
| **Tools** | Actions the model can call | `create_note`, `search_notes` |
| **Resources** | Data the app can read | A file, a database row, a note's text |
| **Prompts** | Ready-made prompt templates | "Summarize this note" |

1. **Tools** are the most used part.
2. The host asks the server "what do you offer?" and gets the list with descriptions and schemas. It then gives that list to the model like any tool list.

---

#### 4. Why MCP — 🟢 Must Know (New)

*It turns many custom integrations into a shared one.*

1. **Build once, use in many apps.** One server works with every compatible host.
2. **Fewer custom connectors.** M apps × N tools becomes M + N pieces of work.
3. **A shared ecosystem.** Ready-made servers exist for common services.
4. **Cleaner separation.** The team that owns the notes API can ship its MCP server. AI teams just plug it in.

---

#### 5. Local and Remote Servers — 🟡 Good to Know

*Where the server runs: on the same machine, or over the network.*

1. **Local server** — runs as a process on the same machine as the host (for example, a coding assistant on a laptop reading local files).
2. **Remote server** — runs on a network and is reached over HTTP. Needs authentication.
3. Local is simple to start. Remote is what you use for shared, company-wide, or user-account tools.

---

#### 6. MCP Security — 🟡 Good to Know

*A connected server is code and text you are choosing to trust.*

1. **Trust only servers you trust.** A server can run actions and can return text that the model will read.
2. **Injected text:** tool descriptions and results are text in the model's context. A bad server, or bad data returned by a good one, can carry instructions (prompt injection, topic `16`).
3. **Least privilege:** give a server only the access it needs. Prefer read-only.
4. **Authenticate remote servers** and use per-user credentials, not one shared super-key.
5. **Confirm risky actions** with the user, as with any write tool (topic `08`).
6. Review what a server can do before connecting it.

---

#### 7. MCP vs Function Calling vs REST — 🟡 Good to Know

*Where MCP fits next to tools you already know.*

| | Plain function calling | MCP | Calling a REST API directly |
|---|---|---|---|
| What it is | Tools defined inside one app | A standard for exposing tools to many apps | Your code calls an endpoint |
| Reuse | Only in that app | Any MCP host | Any code, but the model needs a wrapper |
| Best for | One app, a few tools | Sharing tools across apps and teams | Normal backend work |

1. MCP does not replace function calling. It **standardizes how tools are provided** to it.
2. For one small app with two tools, plain function calling is enough. Do not add MCP just because it is popular.

---

#### 8. A2A: Agent-to-Agent Protocol — 🟡 Good to Know

*A different protocol for a different job. Name only.*

1. MCP connects an agent to **tools and data**.
2. **A2A** is a protocol for **agents to talk to other agents**, possibly from different vendors.
3. Name only for interviews (topic `14`). Know that they solve different problems.

---

#### 9. Common Interview Questions

1. **What is MCP?**
   An open standard for connecting AI apps to tools and data. You build a server once and any compatible app can use it.
2. **What are the parts of MCP?**
   A host (the AI app), a client inside it, and a server exposing tools, resources, and prompts.
3. **Why use MCP instead of custom integrations?**
   One reusable server per tool instead of custom code for every app.
4. **How is MCP different from function calling?**
   Function calling is how the model requests a tool. MCP is a standard way to provide and discover tools for many apps.
5. **What are the risks of MCP servers?**
   Untrusted servers, injected instructions in descriptions and results, and over-broad access. Use least privilege and confirmations.
6. **Would you build an MCP server for your backend?**
   If several AI apps need it, yes: wrap the API as tools with clear descriptions and per-user auth. For one app, direct tools are simpler.
7. **What is A2A?**
   A protocol for agents to communicate with each other. MCP is for tools and data.

---

#### 10. Common Mistakes

1. Adding MCP to a tiny app that needs two tools.
2. Connecting servers you have not reviewed.
3. Giving a server broad write access.
4. One shared credential for all users.
5. Assuming tool descriptions and results are safe text.
6. Confusing MCP with A2A.

---

#### 11. Related Topics

1. `08` Tool Use & Function Calling
2. `10` Agents
3. `11` Agent Harness
4. `14` Multi-Agent Systems
5. `16` Safety, Security & Privacy
6. `BE 3` API Design
7. `BE 5` Authentication & Authorization

---

#### 12. Interview Must Remember

1. **MCP = a standard plug for tools and data.**
2. **Host → client → server.** Servers offer **tools, resources, prompts**.
3. **Build once, use in many AI apps.**
4. **Security:** trust, least privilege, injected text, per-user auth.
5. It **does not replace** function calling. It standardizes how tools are supplied.
6. **MCP = tools and data. A2A = agent to agent.**
