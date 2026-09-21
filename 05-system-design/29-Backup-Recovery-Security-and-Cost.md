# Backup, Recovery, Security & Cost

Roadmap topic 29 · Stage 6: Architecture & Production

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** plan for the day something goes badly wrong. Have backups you have tested, know how much data and time you can afford to lose, protect data, and keep an eye on cost.

---

#### 1. Backups and Tested Restores — 🟢 Must Know

*A backup only counts if you can restore it.*

1. Take **regular backups** of the database and important files, and store them **separately** (another location or account).
2. **Test restoring.** A backup you have never restored is only a guess.
3. **Point-in-time recovery** — restore the database to a specific moment (for example, just before a bad deploy).
4. Replication is not a backup (topic `18`).
5. Rule of thumb: **3 copies, 2 kinds of storage, 1 off-site.**

---

#### 2. RPO and RTO — 🟢 Must Know

*Two numbers that drive every recovery plan.*

```text
   last good backup          disaster           service restored
────────────●──────────────────✕─────────────────────●──────────►
            |←──── RPO ───────→|←────── RTO ─────────→|
```

1. **RPO (recovery point objective)** — how much **data** you can afford to lose (for example, 5 minutes).
2. **RTO (recovery time objective)** — how long you can be **down** (for example, 1 hour).
3. Smaller RPO/RTO = more expensive (more frequent backups, standby systems).
4. Ask the business what is acceptable, then design for it.

---

#### 3. Multi-AZ vs Multi-Region — 🟡 Good to Know

*Survive one data center failing, or a whole region.*

| | Multi-AZ | Multi-region |
|---|---|---|
| Protects from | One data center failing | A whole region failing |
| Complexity | Low (often built in) | High (data sync, latency, cost) |
| Use | Standard for production | Only when the requirements justify it |

Multi-region options: **active–passive** (a standby region takes over) or **active–active** (both serve traffic; harder data consistency).

---

#### 4. Security Basics for Production — 🟡 Good to Know

*The minimum safety rules for production.*

1. **Encryption** in transit (HTTPS/TLS) and at rest (disks, backups).
2. **Least privilege** — each service and person gets only the access they need.
3. **Secrets manager** for keys and passwords. Rotate them.
4. **Audit logs** — who did what.
5. Personal data: collect the minimum, allow deletion.

---

#### 5. Cost Trade-Offs — 🟡 Good to Know

*Every design choice has a price. Mention it.*

1. **Compute** — right-size servers, use auto-scaling, don't overprovision.
2. **Storage** — set retention rules, and move old data to cheaper storage.
3. **Bandwidth** — data leaving the cloud costs money; a **CDN** reduces origin traffic.
4. A cache is often cheaper than a bigger database.
5. Mention cost in an interview when you choose between options.

---

#### 6. Common Interview Questions

1. **What are your RPO and RTO for this system, and how do you meet them?**
   State numbers (for example, RPO 5 min, RTO 1 hour). Meet them with frequent backups or point-in-time recovery, replication, a tested restore process, and a standby.
2. **Is replication a backup?**
   No. Bad deletes and corruption replicate too.
3. **How do you protect against a data center or region failure?**
   Multi-AZ for standard cases, multi-region (active–passive or active–active) if required.
4. **How do you know your backups work?**
   Regularly restore them in a test environment.
5. **How do you reduce cost?**
   Right-size compute, use caching and a CDN, set retention, and use cheaper storage tiers for old data.

---

#### 7. Common Mistakes

1. Never testing a restore.
2. Backups stored next to the original data.
3. No agreed RPO or RTO.
4. Over-engineering multi-region with no requirement.
5. Ignoring bandwidth costs.
6. Broad access permissions for everyone.

---

#### 8. Related Topics

1. `18` Replication
2. `27` Observability
3. `28` Deployment & Release
4. `06` Backend Security Essentials (in `04-backend-engineering`)
5. `33` Follow-Up Topics (multi-region)

---

#### 9. Interview Must Remember

1. **Backups + tested restores.**
2. **RPO** = data you can lose. **RTO** = time you can be down.
3. **Multi-AZ** is normal. **Multi-region** only when needed.
4. **Least privilege, encryption, secrets manager.**
5. **Mention cost** when you compare options.
