# Observability

Roadmap topic 27 · Stage 6: Architecture & Production

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** once your system is live, you can't attach a debugger. Logs, metrics, and traces tell you what is happening, and alerts tell you when something is wrong.

---

#### 1. Logs, Metrics, Traces — 🟢 Must Know

| | What it is | Answers |
|---|---|---|
| **Logs** | Text records of events | "What happened in this request?" |
| **Metrics** | Numbers over time (counts, rates, latency) | "Is the system healthy? Is it getting worse?" |
| **Traces** | One request followed across services | "Where did the time go?" |

1. **Structured logs** (JSON) with a **request ID** on every line, so you can follow one request through all services.
2. **Never** log passwords, tokens, or personal data.
3. Pass the request ID (correlation ID) from service to service, and even from the app.

---

#### 2. What to Measure — 🟢 Must Know

The three signals for any service (**RED**):

1. **R**ate — requests per second.
2. **E**rrors — how many fail (4xx/5xx).
3. **D**uration — latency, using p50, p95, p99.

Also: CPU, memory, DB connections, queue length, cache hit rate.

---

#### 3. Health and Readiness Checks — 🟢 Must Know

1. **Health (liveness)** — is the process alive? If not, restart it.
2. **Readiness** — can it serve traffic now (database connected, cache warm)? If not, the load balancer stops sending requests.
3. Load balancers and orchestrators use these to remove bad servers automatically.

---

#### 4. Actionable Alerts — 🟢 Must Know

1. Alert on **symptoms users feel** (error rate, latency), not every small metric.
2. Every alert must have a clear **action**. Too many alerts = people ignore them (alert fatigue).
3. Use severity: page someone at night only for real user impact.

---

#### 5. SLI, SLO — 🟢 Must Know

1. **SLI** (indicator) — what you measure: percentage of successful requests, p95 latency.
2. **SLO** (objective) — the target: "99.9% of requests succeed", "p95 < 300 ms".
3. **SLA** — a contract with customers, with penalties.
4. The gap between 100% and the SLO is your **error budget**. It tells you how much risk you can take with new releases.

---

#### 6. Incident Debugging — 🟡 Good to Know

```text
1. Symptom     → alert: error rate up, latency doubled
2. Scope       → which endpoint, region, version, user group?
3. Recent change → a deploy, config change, traffic spike?
4. Metrics → logs → traces  → find the failing component
5. Mitigate    → roll back, scale up, disable a feature
6. Fix root cause, then write a blameless post-mortem
```

Mitigate first (stop the pain), investigate after.

---

#### 7. Mobile Crash Reporting — 🟡 Good to Know

1. Use crash reporting and analytics in the app (Crashlytics or similar).
2. Send the request ID or app version with errors to connect app problems with backend logs.
3. Track app-side latency and error rates by version, because the user's experience includes the network.

---

#### 8. Common Interview Questions

1. **Latency doubled at 2 a.m. How do you find the cause?**
   Check metrics for which endpoint and when it started. Compare with recent deploys or traffic changes. Use traces to find the slow component, then logs for details. Mitigate (rollback or scale), then fix the root cause.
2. **Logs vs metrics vs traces?**
   Logs are events, metrics are numbers over time, traces follow one request across services.
3. **What is a request ID and why use it?**
   A unique ID on every log line of a request, so you can follow it across services.
4. **What are SLI and SLO?**
   The measurement (for example, success rate) and the target for it (99.9%).
5. **What makes a good alert?**
   It reflects user impact and points to an action.

---

#### 9. Common Mistakes

1. No request ID in logs.
2. Only average latency, no percentiles.
3. Too many alerts, or alerts nobody can act on.
4. Logging sensitive data.
5. No health checks, so bad servers stay in rotation.
6. Debugging before mitigating during an outage.

---

#### 10. Related Topics

1. `04` Backend Building Blocks (logging basics, in `04-backend-engineering`)
2. `13` Requirements & Estimation (percentiles)
3. `28` Deployment & Release (rollback)
4. `29` Backup, Recovery, Security & Cost

---

#### 11. Interview Must Remember

1. **Logs, metrics, traces**, with a **request ID**.
2. **RED:** rate, errors, duration (use percentiles).
3. **Health vs readiness** checks.
4. **SLI** = measurement, **SLO** = target.
5. **Alert on user impact.** Mitigate first, root-cause after.
