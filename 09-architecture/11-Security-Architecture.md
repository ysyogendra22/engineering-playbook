# Security Architecture

Roadmap topic 11 · Stage 3: Cross-Cutting Concerns

**Marks:** 🟢 Must Know · 🟡 Good to Know · (New) for a mobile engineer moving into architecture, or still changing

**In simple words:** security architecture isn't one wall around the system — it's many layers, each assuming the others might fail. The goal isn't making a breach impossible; it's making one costly, limited in blast radius, and detectable.

---

#### 1. Defense in Depth — 🟢 Must Know

*The core mindset for this entire topic.*

Many layers of protection — network, authentication, authorization, encryption, monitoring — rather than one strong perimeter. If any single layer is bypassed, the others still limit the damage. Never design as if one control (a firewall, a login screen) is sufficient on its own.

---

#### 2. Least Privilege — 🟢 Must Know

Every person, service, and token gets **only** the access it actually needs, nothing more — the same principle that shows up concretely in `BE 6`, `DB 18`, and `MOB 13`. Reduces both the attack surface (item 5) and the blast radius if any one credential is compromised.

---

#### 3. Authentication and Authorization Design — 🟢 Must Know

**Authentication** (who are you?) and **authorization** (what are you allowed to do?) are separate concerns that need separate, deliberate design — full concrete detail in `BE 5`. At the architecture level, decide where these checks live (a gateway, each service, both) and keep that decision consistent system-wide.

---

#### 4. Threat Modelling — 🟢 Must Know

*A structured way to ask "what can go wrong, and where?" before it happens for real.*

**STRIDE** is a common checklist for threat categories: **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege. Walk through a design (or a specific feature) against each category to systematically find gaps, rather than relying on ad hoc intuition alone.

---

#### 5. Attack Surface — 🟢 Must Know

**Keep it small.** Every exposed endpoint, every open port, every accepted input format is a potential entry point — minimise what's actually exposed to what's genuinely needed, and question anything exposed "just in case".

---

#### 6. Secrets Management and Key Rotation — 🟢 Must Know

Secrets (API keys, database credentials, signing keys) belong in a dedicated secrets manager, never in code or config files committed to a repo — and they should be **rotated** periodically, so a leaked or stale credential has a limited window of usefulness.

---

#### 7. Encryption in Transit and at Rest — 🟢 Must Know

**In transit** — TLS/HTTPS for all network communication. **At rest** — encrypted storage for data on disk, including backups. Both are close to non-negotiable baselines for any real production system, not an optional hardening step.

---

#### 8. Zero Trust — 🟡 Good to Know

Never trust a request just because it originates from inside the network perimeter — verify identity and authorization on every request, regardless of source. A response to the reality that internal networks get breached too, and a perimeter alone is an increasingly weak assumption.

---

#### 9. Secure Development Lifecycle — 🟡 Good to Know

Security woven into the development process itself: security-focused code reviews, automated **dependency scanning** (catching known-vulnerable libraries), and **secret scanning** (catching accidentally committed credentials) — catching problems before they reach production, not just auditing after the fact.

---

#### 10. Compliance and Audit Trails — 🟡 Good to Know

Regulatory requirements (industry- or region-specific) often mandate not just security controls themselves, but **provable records** of who accessed or changed what, and when — an audit trail is itself a security-architecture requirement, not just a logging nicety.

---

#### 11. Mobile-Specific Security — 🟡 Good to Know

**Token storage** (Keystore-backed encrypted storage), **certificate pinning** (and its rollout risk), and **app attestation** (Play Integrity API / App Attest) — the mobile-client-side half of security architecture, covered in full depth in `SD 30` and `MOB 13`.

---

#### 12. Common Interview Questions

1. **What does "defense in depth" mean, and why does it matter?**
   Many independent layers of protection instead of relying on one — if any single layer is bypassed, the others still limit the damage; never architect around a single point of security failure.
2. **How would you threat-model a new feature?**
   Walk through it against a checklist like STRIDE — spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege — to systematically surface gaps rather than relying on intuition alone.
3. **What's the difference between authentication and authorization, architecturally?**
   Authentication verifies identity; authorization decides what that identity is allowed to do. They're separate concerns, and the architecture should decide deliberately where each check lives.
4. **What does zero trust change compared to a traditional perimeter model?**
   Every request is verified on its own merits, regardless of whether it originates inside or outside the network — because internal networks get breached too, and trusting requests by location alone is an increasingly weak assumption.

---

#### 13. Common Mistakes

1. Relying on one control (a firewall, a login page) as if it were sufficient on its own.
2. Broad, standing access granted "to be safe" instead of least privilege.
3. Secrets committed to a repository or left in plain config files.
4. Treating mobile client security as separate from, rather than part of, the overall security architecture.

---

#### 14. Related Topics

1. `BE 5`, `BE 6` — authentication/authorization and backend security essentials in concrete detail
2. `9` Data Architecture — privacy and encryption overlap directly here
3. `SD 30`, `MOB 13` — mobile-specific security detail

---

#### 15. Interview Must Remember

1. **Defense in depth** — many layers, never one wall.
2. **Least privilege** for people, services, and tokens.
3. **STRIDE** as a structured threat-modelling checklist.
4. **Encryption in transit and at rest** are baseline, not optional hardening.
