from poster_lib import *
from poster_svg import *

boxes = [
 box(1, "What an Architect Does", "r", ul(["Important, costly-to-change decisions", "Decides **with** the team", "Records, keeps consistent, enables", "Stays hands-on"]) + callout("No best architecture,\nonly trade-offs.", "")),
 box(2, "Quality Attributes", "g", ul(["Performance · scalability", "Availability · reliability", "Security · maintainability", "Testability · observability · cost", "Measurable + **ranked**", "A few ASRs shape the design", "Constraints: budget, date, skills, rules"])),
 box(3, "Decisions & ADRs", "b", flow(["Options", "Criteria", "Spike", "ADR"]) + ul(["2–4 options", "One-way vs two-way doors", "Build the core, buy the rest", "Decision score = Σ weight × score"]) + mut("Argue the weights, not the arithmetic.")),
 box(4, "Principles", "p", kv([("S", "one reason to change"), ("O", "extend, don't edit"), ("L", "subtypes substitute"), ("I", "small interfaces"), ("D", "depend on abstractions")], True) + mut("High cohesion · low coupling · KISS · YAGNI · DRY (rule of three)")),

 box(5, "Styles", "r", ul(["**Modular monolith first**", "Microservices for real needs, else distributed monolith", "Event-driven: decouple, fan-out", "Hexagonal / clean: protect the core", "Choose from ranked attributes + team"])),
 box(6, "Patterns", "g", ul(["Adapter, decorator, strategy", "Repository; MVVM / MVI", "Timeout, retry, circuit breaker, bulkhead", "BFF", "Saga + outbox", "Strangler + anti-corruption layer", "CQRS / event sourcing only with a need"])),
 box(7, "DDD", "b", ul(["Ubiquitous language", "**Bounded contexts** = module / service boundaries", "Entity · value object · aggregate", "Invest in the core subdomain"])),
 box(8, "Boundaries & Coupling", "p", ul(["Small public API, hidden insides", "No cycles; package by feature", "Conway's law"]) + callout("Instability I = Ce ÷ (Ca + Ce)\nCa = 3, Ce = 1 → I = 0.25\nDepend toward lower I", "b")),

 box(9, "Data Architecture", "r", ul(["One owner per data set", "Store by shape + access pattern", "Consistency per feature", "Expand → migrate → contract", "Retention + deletion up front"])),
 box(10, "Integration & APIs", "g", ul(["Contract first; add-only", "Sync vs async", "Idempotency keys", "Webhooks: verified, stored, async", "Reconcile", "Adapter around third parties"])),
 box(11, "Security (STRIDE)", "b", kv([("S", "Spoofing"), ("T", "Tampering"), ("R", "Repudiation"), ("I", "Info disclosure"), ("D", "Denial of service"), ("E", "Elevation of privilege")], True) + mut("Defense in depth · least privilege · server-side authz")),
 box(12, "Scale & Resilience", "p", ul(["Numbers first; find the bottleneck", "Stateless; remove SPOFs", "Timeouts, retries, breakers, fallbacks", "SLO → error budget → burn rate", "RTO / RPO; load + chaos tests"])),

 box(13, "Availability Maths", "r", table(["SLA", "Down / month"], [["99%", "7.2 h"], ["99.9%", "43 min"], ["99.99%", "4.3 min"]]) + ul(["Series multiplies: 0.999⁵ ≈ 99.5%", "Parallel: 1 − (1 − a)ⁿ", "Two 99% → 99.99%"])),
 box(14, "Ops, Cost, Docs", "g", ul(["CI/CD, canary, rollback", "Logs, metrics, traces", "Infrastructure as code", "Cost is a requirement with a number", "**C4** diagrams as text, ADRs, short docs"])),
 box(15, "Evolution", "b", ul(["Make change cheap", "Debt register with interest", "Small safe refactors", "Strangler migrations: 1% → 10% → 50% → 100%", "**Fitness functions**", "Avoid big-bang rewrites"])),
 box(16, "Teams & Governance", "p", ul(["Inverse Conway", "Stream-aligned + platform teams", "Team size 5–9", "Guardrails over gates", "Paved road + tech radar", "DORA: frequency, lead time, change-fail rate, time to restore"])),

 box(17, "Code-Level Foundations: OOP, SOLID, Patterns", "o", row(
     ul(["**OOP:** encapsulation, abstraction, inheritance, polymorphism", "Interface = capability; abstract class = shared state", "Overriding: runtime · overloading: compile time", "`equals` + `hashCode` together", "Java `==` compares references", "Java is pass-by-value", "Prefer immutable objects"]),
     ul(["**SOLID in code:**", "S: one reason to change", "O: add a strategy, don't edit a `when`", "L: Square is not a safe Rect (setters)", "I: `NotesReader` + `NotesWriter`", "D: depend on an interface, inject it, test with a fake"]),
     ul(["**Patterns:** start from the problem", "Singleton → DI scope or `object`", "Factory hides the class · Builder validates", "Adapter fits · Decorator wraps · Facade simplifies", "Strategy swaps · State owns transitions", "Observer notifies (unsubscribe!) · Command undoes", "Template Method fixes the steps"])), 4),

 box(0, "Mobile & AI Angles", "o", table(["Area", "Architecture answer"], [["Mobile", "offline-first, Room = truth; UI → ViewModel → repository; modules by feature; add-only API + min version; flags + staged rollout"], ["AI", "model behind a gateway; design for wrong answers; cost/latency/reliability are ASRs; control data flow; eval-gated upgrades"]]) + mut("Little's law: in-flight = throughput × latency (2,000 rps × 0.1 s = 200)"), 2),
 box(0, "Golden Rules", "t", ul(["Clarify the attributes", "2–4 options + trade-offs", "Record the decision", "Modular monolith first", "Fitness functions guard it"], ok=True)),
 box(0, "Say Out Loud", "r", '<div class="big">"Requirements → attributes →<br>options → decision with the<br>trade-off → risks."</div>'),
]
meta = dict(left="Trade-offs, not best<br>Decide. Record.", right="Clarify. Choose.<br>Evolve! ☺", title="<b>ARCHITECTURE</b> CHEATSHEET", sub="for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
