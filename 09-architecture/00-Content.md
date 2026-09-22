# Architecture: Roadmap for an Architect

For a mobile engineer growing into an architect: what to do on any project, which decisions matter most, and which terms to know first.
This folder has **its own numbering, 1 to 22**. Each topic gets its own doc later.

**How to read references:** a plain number (`7`) is a topic in this folder. `BE 3` is topic 3 in `04-backend-engineering`. `SD 21` is topic 21 in `05-system-design`. `AI 7` is topic 7 in `08-artificial-intelligence`. Mobile platform details live in `06-mobile-engineering`, and interview stories in `07-behavioral-leadership`.

**What you need first:** `BE 1–4` (backend basics) and `SD 13–15`, `SD 26` (scale, caching, service boundaries). This folder builds on them and does not repeat them.

**Marks:**

| Mark | Meaning |
|---|---|
| 🟢 | **Must have.** An architect is expected to know this. Learn first. |
| 🟡 | **Good to have.** Learn after the 🟢 items are solid. |
| (New) | Added for a mobile engineer moving into architecture, or a newer idea that is still changing. |

---

## Index

| #   | Topic                                        | Stage                          |
| --- | -------------------------------------------- | ------------------------------ |
| 1   | What an Architect Does                       | 1. Role & Mindset              |
| 2   | Requirements, Constraints & Quality Attributes | 1. Role & Mindset            |
| 3   | Trade-Offs & Decision Making                 | 1. Role & Mindset              |
| 4   | Design Principles                            | 2. Design Foundations          |
| 5   | Architectural Styles                         | 2. Design Foundations          |
| 6   | Architecture & Design Patterns               | 2. Design Foundations          |
| 7   | Domain-Driven Design Essentials              | 2. Design Foundations          |
| 8   | Modularity, Coupling & Boundaries            | 2. Design Foundations          |
| 9   | Data Architecture                            | 3. Cross-Cutting Concerns      |
| 10  | Integration & API Architecture               | 3. Cross-Cutting Concerns      |
| 11  | Security Architecture                        | 3. Cross-Cutting Concerns      |
| 12  | Scalability, Performance & Resilience        | 3. Cross-Cutting Concerns      |
| 13  | Operations, Deployment & Cost                | 3. Cross-Cutting Concerns      |
| 14  | Documentation & Diagrams                     | 4. Documenting & Communicating |
| 15  | Communicating & Influencing                  | 4. Documenting & Communicating |
| 16  | Evolutionary Architecture & Technical Debt   | 5. Evolving & Governing        |
| 17  | Architecture Governance & Quality            | 5. Evolving & Governing        |
| 18  | Teams & Delivery                             | 5. Evolving & Governing        |
| 19  | Mobile App Architecture (New)                | 6. Your Domain                 |
| 20  | Architecting AI-Enabled Systems (New)        | 6. Your Domain                 |
| 21  | Architecture Interview Answers (New)         | 7. Interview & Practice        |
| 22  | Practice: Case Studies & Exercises           | 7. Interview & Practice        |

**Short on time:** 1, 2, 3, 4, 5, 8, 10, 12, 14, 16, 19, 21. 🟢 items only.

**Glossary:** the terms to learn first are listed at the end, each with a priority mark and the topic that explains it.

---

# What to Follow on Any Project

*The same nine steps work for a new app, a rewrite, or a new feature. Do them in order and keep each output short.*

| Step                    | Question to answer                                                                         | Output                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| 1. Understand           | Why are we building this? Who are the users and stakeholders? What does success look like? | One-page goal, scope, success metrics                               |
| 2. Capture what matters | Which requirements and limits shape the design most?                                       | Top 5–8 quality attributes with numbers, plus constraints (topic 2) |
| 3. Find the risks       | What could hurt us: unknowns, hard requirements, weak spots?                               | Risk list, ranked (topic 3)                                         |
| 4. Choose the approach  | Which style and technologies fit? What are the options and trade-offs?                     | Options with a recommendation, recorded as ADRs (topics 3, 5)       |
| 5. Draw the design      | What are the parts, and how do they connect?                                               | C4 diagrams: context, containers, key flows (topic 14)              |
| 6. Check it             | Will it meet the numbers? Does the risky part work?                                        | Spike or prototype, estimates, review with the team (topics 3, 17)  |
| 7. Plan delivery        | What is the smallest slice that proves the design?                                         | Walking skeleton, milestones, thin vertical slices (topic 18)       |
| 8. Guide the build      | How do we keep the design from drifting?                                                   | Standards, reviews, automated checks (topics 16, 17)                |
| 9. Operate and evolve   | How do we see problems and change safely?                                                  | Monitoring, SLOs, debt list, regular reviews (topics 13, 16)        |

**Priority order when time is short:** steps 2, 4, and 5. Most project trouble comes from unclear quality requirements, undocumented decisions, and a design nobody can see.

---

# Stage 1: Role & Mindset

## 1. What an Architect Does

- 🟢 Architecture = the important decisions that are costly to change
- 🟢 The architect's job: make the key decisions, keep them consistent, and help the team follow them
- 🟢 Architect vs tech lead vs senior engineer: scope, and how close to the code
- 🟢 Stay hands-on: read code, build spikes, join reviews
- 🟢 Breadth over depth: know a little of many areas, and go deep where the risk is
- 🟡 Types of architect: solution, software, enterprise, cloud, mobile (roles differ by company)
- 🟡 Common failure: the "ivory tower" architect who draws but does not build or listen

## 2. Requirements, Constraints & Quality Attributes

- 🟢 Functional requirements (what it does) vs quality attributes (how well)
- 🟢 Key quality attributes: performance, scalability, availability, reliability, security, maintainability, testability, observability, usability, cost
- 🟢 Architecturally significant requirements (ASRs): the few that shape the design
- 🟢 Make them measurable: "p95 under 300 ms", not "fast"
- 🟢 Constraints: budget, deadline, team skills, existing systems, regulation, vendor rules
- 🟢 Rank the quality attributes: you cannot maximise them all
- 🟡 Quality attribute scenarios: stimulus, response, measure
- 🟡 Business drivers and stakeholder needs
- 🟡 Standards for quality models (names only)

## 3. Trade-Offs & Decision Making

- 🟢 There is no best architecture, only trade-offs for a given context. Say "it depends on ..." and name what
- 🟢 ADR (architecture decision record): context, options, decision, consequences
- 🟢 One-way vs two-way decisions: spend effort on the hard-to-reverse ones
- 🟢 Risk-driven design: attack the biggest unknowns first (spike, proof of concept, prototype)
- 🟢 Build vs buy vs open source: cost, control, speed, lock-in
- 🟢 Technology selection criteria: fit, team skills, maturity, community, cost, exit path
- 🟡 Last responsible moment: decide late enough to know more, early enough not to block
- 🟡 Avoid resume-driven and hype-driven choices
- 🟡 Cost of delay and cost of change

---

# Stage 2: Design Foundations

## 4. Design Principles

- 🟢 Separation of concerns
- 🟢 High cohesion, low coupling
- 🟢 SOLID (single responsibility, open–closed, Liskov substitution, interface segregation, dependency inversion)
- 🟢 Abstraction and information hiding
- 🟢 KISS, YAGNI, DRY (and when DRY hurts: wrong abstractions)
- 🟢 Design for failure: assume parts will break
- 🟡 Composition over inheritance
- 🟡 Law of Demeter (least knowledge)
- 🟡 Single source of truth
- 🟡 Principle of least astonishment

## 5. Architectural Styles

- 🟢 Layered architecture
- 🟢 Monolith, modular monolith, microservices: when each fits ("monolith first" is often right)
- 🟢 Client–server and API-first design
- 🟢 Event-driven architecture (`SD 21`)
- 🟢 Hexagonal (ports and adapters) and clean architecture: business rules at the centre, details at the edge
- 🟡 Serverless and functions
- 🟡 Service-based architecture (fewer, larger services)
- 🟡 Microkernel (plugin), pipe-and-filter
- 🟡 Space-based and other styles (names only)
- 🟡 How to choose a style from your ranked quality attributes

## 6. Architecture & Design Patterns

- 🟢 Creational and structural basics: factory, builder, adapter, facade, decorator
- 🟢 Behavioural basics: strategy, observer
- 🟢 Dependency injection and inversion of control
- 🟢 Repository pattern and the data access layer
- 🟢 UI patterns: MVC, MVP, MVVM, MVI (topic 19)
- 🟢 Resilience patterns: timeout, retry, circuit breaker, bulkhead (`SD 22`, `SD 25`)
- 🟢 API gateway and BFF (`SD 26`)
- 🟡 CQRS and event sourcing (name and purpose)
- 🟡 Saga and transactional outbox (`SD 26`)
- 🟡 Strangler fig, anti-corruption layer, sidecar
- 🟡 Anti-patterns: God class, big ball of mud, distributed monolith, golden hammer

## 7. Domain-Driven Design Essentials

- 🟢 Ubiquitous language: the same words in code, docs, and talk
- 🟢 Bounded context: one model, one meaning, clear edges
- 🟢 Entities, value objects, aggregates
- 🟢 Core, supporting, and generic subdomains: spend design effort on the core
- 🟡 Domain events
- 🟡 Context map: how contexts relate (shared kernel, customer–supplier, anti-corruption layer)
- 🟡 When DDD is overkill (simple CRUD)

## 8. Modularity, Coupling & Boundaries

- 🟢 Module boundaries: small public API, hidden inside
- 🟢 Dependency direction: depend on stable abstractions, not on details
- 🟢 Package by feature vs by layer
- 🟢 Conway's law: your system copies your team structure
- 🟢 Contracts between modules and services, and how they change over time
- 🟡 Monorepo vs polyrepo
- 🟡 Shared code and shared libraries: the cost of sharing
- 🟡 Measuring coupling: dependency graphs, cyclic dependencies
- 🟡 Boundaries inside a monolith (the modular monolith)

---

# Stage 3: Cross-Cutting Concerns

## 9. Data Architecture

- 🟢 Data ownership and the single source of truth
- 🟢 Choose the store by data shape and access pattern (`SD 17`)
- 🟢 Consistency needs per feature: strong vs eventual (`SD 23`)
- 🟢 Schema evolution and migrations without downtime
- 🟢 Data lifecycle: retention, archiving, deletion
- 🟢 Privacy and compliance shaping data design (GDPR-style rules)
- 🟡 OLTP vs OLAP, data warehouse and data lake (names)
- 🟡 Data flow diagrams and data lineage
- 🟡 Caching and read models as part of the design (`SD 15`)
- 🟡 Data governance and master data (names)

## 10. Integration & API Architecture

- 🟢 Synchronous vs asynchronous integration (`SD 26`)
- 🟢 API-first: design the contract before the code (`BE 3`)
- 🟢 API versioning and backward compatibility (old app versions never go away)
- 🟢 Idempotency and retries across service boundaries
- 🟢 Third-party integration: rate limits, failure, webhooks, reconciliation (`SD 22`)
- 🟡 REST, GraphQL, gRPC: when each fits
- 🟡 Events and messaging contracts, schema registries (name)
- 🟡 API gateway responsibilities
- 🟡 Anti-corruption layer around external systems

## 11. Security Architecture

- 🟢 Defense in depth: many layers, not one wall
- 🟢 Least privilege for people, services, and tokens
- 🟢 Authentication and authorization design (`BE 5`)
- 🟢 Threat modelling: what can go wrong, and where (STRIDE as a checklist)
- 🟢 Attack surface: keep it small
- 🟢 Secrets management and key rotation
- 🟢 Encryption in transit and at rest
- 🟡 Zero trust (never trust the network)
- 🟡 Secure development lifecycle: reviews, dependency scanning, secret scanning
- 🟡 Compliance and audit trails
- 🟡 Mobile-specific: token storage, certificate pinning, app attestation (`SD 30`)

## 12. Scalability, Performance & Resilience

- 🟢 Capacity planning: numbers first (`SD 13`)
- 🟢 Stateless services and horizontal scaling (`SD 14`)
- 🟢 Find the bottleneck before optimising
- 🟢 Single points of failure and redundancy
- 🟢 Timeouts, retries, circuit breakers, graceful degradation (`SD 25`)
- 🟢 SLI, SLO, SLA and error budgets
- 🟢 RTO and RPO (`SD 29`)
- 🟡 Multi-AZ and multi-region design
- 🟡 Load testing and chaos testing (names and purpose)
- 🟡 Performance budgets for latency and payload size
- 🟡 Back-pressure and load shedding

## 13. Operations, Deployment & Cost

- 🟢 CI/CD and safe release strategies (`SD 28`)
- 🟢 Observability: logs, metrics, traces (`SD 27`)
- 🟢 Environments and configuration
- 🟢 Infrastructure as code
- 🟢 Cost as a design constraint: cloud bills, build vs buy, right-sizing
- 🟡 Containers and orchestration (concepts, not Kubernetes internals)
- 🟡 Cloud service models: IaaS, PaaS, SaaS, and managed services
- 🟡 Twelve-factor app principles
- 🟡 Runbooks, on-call, incident review
- 🟡 Cloud well-architected frameworks (names)
- 🟡 FinOps basics: tagging, budgets, cost per feature

---

# Stage 4: Documenting & Communicating

## 14. Documentation & Diagrams

- 🟢 C4 model: system context, containers, components (and code, rarely)
- 🟢 Draw for your audience: business, developers, operations
- 🟢 Key flow diagrams: sequence diagrams for the main use cases
- 🟢 ADRs kept next to the code
- 🟢 Design docs / RFCs: problem, options, decision, risks
- 🟡 Views: logical, process, deployment, data
- 🟡 UML basics: sequence, component, class
- 🟡 Docs as code: text-based diagrams in the repo
- 🟡 arc42 or similar templates (names)
- 🟡 Keep docs short and current: delete what is stale

## 15. Communicating & Influencing

- 🟢 Know your stakeholders: what each cares about
- 🟢 Explain trade-offs in the listener's language: cost, risk, time, user impact
- 🟢 Present options and a recommendation, not only a problem
- 🟢 Run design reviews that are useful and kind
- 🟢 Disagree and commit; handle pushback with data
- 🟡 Say no with alternatives
- 🟡 Risk registers and status for leadership
- 🟡 Estimates and roadmaps: ranges, assumptions, confidence
- 🟡 Working with product, QA, security, and operations
- 🟡 Storytelling for interviews (`07-behavioral-leadership`)

---

# Stage 5: Evolving & Governing

## 16. Evolutionary Architecture & Technical Debt

- 🟢 Architecture changes over time: design so change is cheap
- 🟢 Technical debt: deliberate vs accidental, and how to track it
- 🟢 Refactoring in small, safe steps
- 🟢 Strangler fig migration: replace a system piece by piece
- 🟢 Fitness functions: automated checks that a quality still holds
- 🟢 Deprecation and removal plans
- 🟡 Architecture drift and erosion: why designs decay
- 🟡 Large migrations without downtime (`SD 33`)
- 🟡 Rewrite vs refactor: why rewrites often fail
- 🟡 Versioning strategy for APIs, data, and apps

## 17. Architecture Governance & Quality

- 🟢 Guardrails over gates: make the right way the easy way
- 🟢 Architecture reviews: when, who, and what to look for
- 🟢 Automated architecture tests: dependency rules, layer rules, cycle checks
- 🟢 Coding standards and definition of done
- 🟡 Paved road (golden path): approved default stacks and templates
- 🟡 Tech radar: adopt, trial, assess, hold
- 🟡 Balance standards with team autonomy
- 🟡 ATAM-style reviews (name and purpose)
- 🟡 Ownership: who owns each service, module, and data set

## 18. Teams & Delivery

- 🟢 Conway's law and the inverse Conway manoeuvre
- 🟢 Build the thinnest end-to-end slice first (walking skeleton)
- 🟢 Vertical slices vs horizontal layers of work
- 🟢 DevOps mindset: you build it, you run it
- 🟢 Delivery metrics (DORA): deployment frequency, lead time, change failure rate, time to restore
- 🟡 Team Topologies: stream-aligned, platform, enabling, complicated-subsystem teams
- 🟡 Architecture in agile teams: just enough design up front
- 🟡 MVP thinking: what to build now, what to defer
- 🟡 Onboarding: docs, diagrams, and code that new people can read

---

# Stage 6: Your Domain

## 19. Mobile App Architecture (New)

- 🟢 Layers: UI, domain (optional), data
- 🟢 Patterns: MVVM, MVI, and clean architecture on mobile
- 🟢 Unidirectional data flow and a single source of truth for state
- 🟢 Dependency injection (Hilt, Koin, or manual)
- 🟢 Modularization: by feature, with clear module APIs
- 🟢 Offline-first: a local database as the source of truth, with sync (`SD 30`)
- 🟢 Backward compatibility with old app versions (`SD 30`)
- 🟡 Networking layer, caching, and error handling
- 🟡 Navigation, and how features are wired together
- 🟡 Feature flags, remote config, and staged rollouts
- 🟡 Security: token storage, certificate pinning, obfuscation
- 🟡 Testing strategy for apps
- 🟡 Cross-platform options (Kotlin Multiplatform, others) and their trade-offs
- 🟡 Details for each platform live in `06-mobile-engineering`

## 20. Architecting AI-Enabled Systems (New)

- 🟢 Where the model sits: behind your backend, never a key in the app (`AI 5`)
- 🟢 Building blocks: prompts, retrieval, tools, agents, evals (`AI 7`, `AI 10`, `AI 15`)
- 🟢 Design for wrong answers: grounding, validation, human approval (`AI 16`)
- 🟢 Cost, latency, and reliability as first-class requirements (`AI 17`)
- 🟢 Privacy and data flow to third-party models
- 🟡 Model gateway: one place for keys, limits, routing, logging
- 🟡 Swappable providers and model versions (`AI 18`)
- 🟡 On-device vs cloud (`AI 19`)
- 🟡 Evaluation as part of the delivery pipeline

---

# Stage 7: Interview & Practice

## 21. Architecture Interview Answers (New)

- 🟢 Answer structure: clarify → quality attributes → options → decision → risks → evolution
- 🟢 Name the trade-off in every choice ("I choose X because ...; the cost is ...")
- 🟢 Ready answers: monolith vs microservices, how you choose a stack, how you handle change
- 🟢 Ready answers: how you document decisions, how you keep a design from drifting
- 🟢 Tell one or two real decision stories with context, options, result, and what you would change
- 🟡 Handling disagreement and pushback
- 🟡 Questions you can ask about the company's architecture
- 🟡 Common traps: naming tools first, ignoring constraints, only the happy path

## 22. Practice: Case Studies & Exercises

**Do these (in order)**

- 🟢 Write three ADRs for a real decision you made or could make
- 🟢 Draw C4 context and container diagrams for the Notes app (`BE 12`)
- 🟢 List the top 5 quality attributes for three different apps, with numbers
- 🟢 Compare monolith, modular monolith, and microservices for one case, with a recommendation
- 🟢 Threat-model one feature (login or sharing) with STRIDE
- 🟡 Review the architecture of an app you know: strengths, risks, debt
- 🟡 Plan a strangler-fig migration for a legacy screen or service
- 🟡 Design the mobile and backend architecture for one AI feature (`AI 22`)
- 🟡 Run a mock design review with a friend

**Case studies to think through**

- 🟢 Notes app with sync and offline support
- 🟢 Chat app
- 🟢 Payments or checkout flow
- 🟡 Startup outgrowing its monolith
- 🟡 A migration from a legacy backend

---

# Glossary: Terms to Learn First

Plain meanings, with a priority. The last column is the topic that explains the term.

**Decisions and requirements**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Architecture | The important decisions about structure that are costly to change | 1 |
| 🟢 | Quality attributes (NFRs, "-ilities") | How well the system must work: speed, scale, availability, security, maintainability | 2 |
| 🟢 | ASR | Architecturally significant requirement: a requirement that strongly shapes the design | 2 |
| 🟢 | Constraint | A fixed limit you must accept: budget, deadline, skills, regulation, existing systems | 2 |
| 🟢 | Trade-off | Improving one quality costs another | 3 |
| 🟢 | ADR | Architecture decision record: a short note of context, options, decision, consequences | 3 |
| 🟢 | Spike / proof of concept | A small experiment to reduce a risk or unknown | 3 |
| 🟡 | One-way vs two-way decision | Hard to reverse vs easy to reverse | 3 |
| 🟡 | Last responsible moment | Delay a decision until waiting costs more than deciding | 3 |
| 🟡 | Build vs buy | Make it yourself, or use a product or service | 3 |

**Structure and design**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Coupling / cohesion | How tied modules are to each other / how focused each one is. Aim for low and high | 4, 8 |
| 🟢 | Separation of concerns | Each part has one clear job | 4 |
| 🟢 | SOLID | Five object-oriented design principles | 4 |
| 🟢 | Abstraction | Hide the details behind a simple interface | 4 |
| 🟢 | Layered architecture | Code split into layers, each using the one below | 5 |
| 🟢 | Monolith / modular monolith / microservices | One deployable / one deployable with strict modules / many small deployables | 5 |
| 🟢 | Hexagonal / clean architecture | Business rules in the centre; outside details plug in through interfaces | 5 |
| 🟢 | Event-driven architecture | Parts communicate by publishing and reacting to events | 5 |
| 🟢 | Dependency injection | Give a class what it needs instead of letting it create it | 6 |
| 🟢 | Bounded context | An area where one model and one set of words have one meaning | 7 |
| 🟢 | Ubiquitous language | The same words used in code, docs, and conversations | 7 |
| 🟢 | Conway's law | A system's design mirrors the communication structure of the team that builds it | 8, 18 |
| 🟡 | Aggregate | A group of objects changed together as one unit, with one entry point | 7 |
| 🟡 | Domain event | A fact that happened in the business ("order placed") | 7 |
| 🟡 | CQRS | Separate models for writing and for reading | 6 |
| 🟡 | Saga / outbox | Multi-step process with compensation / reliable event publishing from the database | 6 |
| 🟡 | Anti-corruption layer | A translation layer that protects your model from an outside system | 6, 10 |
| 🟡 | Distributed monolith | Microservices that must still be deployed and changed together | 6 |

**Data, integration, and security**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Single source of truth | One place owns each piece of data | 9 |
| 🟢 | API contract | The agreed shape of requests and responses between systems | 10 |
| 🟢 | Backward compatibility | New versions keep working with old clients | 10 |
| 🟢 | Idempotency | Doing the same request twice has the same effect as once | 10 |
| 🟢 | Defense in depth | Many layers of protection instead of one | 11 |
| 🟢 | Least privilege | Give only the access that is needed | 11 |
| 🟢 | Threat model / STRIDE | Listing what can go wrong; STRIDE is a checklist of threat types | 11 |
| 🟢 | Attack surface | All the ways an attacker could reach the system | 11 |
| 🟡 | Zero trust | Never trust a request just because it is inside the network | 11 |
| 🟡 | OLTP vs OLAP | Everyday transactions vs large-scale analysis | 9 |

**Resilience and operations**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | Single point of failure (SPOF) | One part whose failure stops everything | 12 |
| 🟢 | Graceful degradation | Keep the core working when a part fails | 12 |
| 🟢 | Circuit breaker / bulkhead | Stop calling a failing service / isolate resources so one failure does not spread | 6, 12 |
| 🟢 | SLI / SLO / SLA | What you measure / the target you set / the promise to customers | 12 |
| 🟢 | RTO / RPO | How long you can be down / how much data you can lose | 12 |
| 🟢 | Observability | Being able to understand the system from its logs, metrics, and traces | 13 |
| 🟢 | CI/CD | Automatic build, test, and deployment | 13 |
| 🟡 | Infrastructure as code | Servers and cloud resources defined in files and versioned | 13 |
| 🟡 | Twelve-factor app | A set of rules for building cloud-friendly services | 13 |
| 🟡 | FinOps | Managing and lowering cloud cost | 13 |

**Documentation, evolution, and teams**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | C4 model | Four zoom levels of diagram: context, containers, components, code | 14 |
| 🟢 | Design doc / RFC | A written proposal for a change, reviewed before building | 14 |
| 🟢 | Stakeholder | Anyone affected by, or with a say in, the system | 15 |
| 🟢 | Technical debt | Shortcuts that make future change more costly | 16 |
| 🟢 | Strangler fig | Replace an old system piece by piece behind a common front | 16 |
| 🟢 | Fitness function | An automated check that an architecture quality still holds | 16, 17 |
| 🟢 | Walking skeleton | The thinnest end-to-end version that runs through all layers | 18 |
| 🟡 | Architecture drift | The real system slowly moves away from the intended design | 16 |
| 🟡 | Paved road (golden path) | The easy, approved default way to build and deploy | 17 |
| 🟡 | Tech radar | A list of technologies marked adopt, trial, assess, or hold | 17 |
| 🟡 | ATAM | A structured method for reviewing an architecture against its quality goals | 17 |
| 🟡 | DORA metrics | Four delivery measures: deployment frequency, lead time, change failure rate, time to restore | 18 |
| 🟡 | Team Topologies | A model of four team types and how they interact | 18 |

**Mobile and AI**

| Priority | Term | Plain meaning | Topic |
|---|---|---|---|
| 🟢 | MVVM / MVI | UI patterns that separate the screen from its state and logic | 6, 19 |
| 🟢 | Unidirectional data flow | State flows down and events flow up, in one direction | 19 |
| 🟢 | Offline-first | The local database is the source of truth, and it syncs with the server | 19 |
| 🟢 | Modularization | Splitting the app into modules with clear boundaries | 8, 19 |
| 🟡 | Model gateway | One backend layer that holds keys, limits, routing, and logging for AI models | 20 |

---

## Skip for Now

- Heavy enterprise frameworks and certifications (TOGAF, Zachman)
- Detailed UML for every diagram type. Use C4 and sequence diagrams
- Architecture description languages and model-driven tools
- Old-style SOA with enterprise service buses
- Cloud-provider-specific service comparisons

## How to Proceed

1. Read topics 1 to 3 first. They set the mindset: numbers, trade-offs, and written decisions.
2. Learn topics 4 to 8 as a set. Then apply them in exercise 22 (compare monolith, modular monolith, microservices).
3. Learn topics 9 to 13 as a checklist. For any design, ask what each concern needs.
4. Start writing ADRs and C4 diagrams right after topic 3 and topic 14. Do not wait to finish the theory.
5. Do topic 19 alongside your daily mobile work: look at your own app and find its layers, boundaries, and debt.
6. Do topics 21 and 22 last, and tell your decision stories out loud.
7. For each topic: what it is, what problem it solves, how it works, one downside.
