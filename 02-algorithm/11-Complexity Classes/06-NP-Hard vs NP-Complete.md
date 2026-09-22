# NP-Hard vs NP-Complete

#### 1. Definition — Must Know

1. **NP-Complete** = in NP (a proposed solution can be checked fast, topic 2), **and** at least as hard as every other problem in NP.
2. **NP-Hard** = at least as hard as every problem in NP (same difficulty bar), **but not necessarily in NP itself** — meaning a proposed solution might not even be checkable quickly.
3. Every NP-Complete problem is NP-Hard, but not every NP-Hard problem is NP-Complete.

#### 2. Why It Is Used — Must Know

This distinction is a small but real vocabulary trap — using "NP-Hard" and "NP-Complete" interchangeably is technically incorrect, and precise language here signals real understanding rather than memorised buzzwords.

#### 3. How It Works — Must Know

```text
NP-Complete example: Travelling Salesman Problem (decision version —
  "is there a route under length X?")
  - Checking a proposed route: fast (add up distances) → it's in NP
  - At least as hard as every NP problem → NP-Complete

NP-Hard but NOT NP-Complete example: Travelling Salesman Problem
  (OPTIMIZATION version — "what is the shortest possible route?",
  not just yes/no)
  - This version doesn't have a simple yes/no answer to "check" in the
    same way — you'd need to somehow verify a number IS the true minimum,
    which isn't obviously fast
  - Still at least as hard as NP → NP-Hard
  - But not cleanly verifiable in polynomial time the way the yes/no
    "decision" version is → not classified as NP-Complete (it isn't
    even confirmed to be IN NP at all)
```

```text
Rough picture:

   NP-Hard  ─────────────────────────────
   │                                       │
   │        NP ─────────────────           │
   │        │                    │          │
   │        │   NP-Complete       │          │
   │        │  ┌──────────┐      │          │
   │        │  │TSP(yes/no│      │          │
   │        │  └──────────┘      │          │
   │        └────────────────────           │
   │   TSP (optimization version) lives HERE, outside NP but still NP-Hard
   └───────────────────────────────────────
```

#### 4. Algorithm — Must Know

```text
To classify a problem:
1. Can a proposed solution be VERIFIED in polynomial time?
     Yes → it's in NP
     No / unclear → it might still be NP-Hard, but not NP-Complete
2. Is it at least as hard as every problem in NP (provable by reduction)?
     Yes → it's NP-Hard (and NP-Complete too, if step 1 was also yes)
```

#### 5. Kotlin Implementation — Must Know

*(Not applicable — this is a classification concept.)*

#### 6. Complexity — Must Know

Not applicable directly — both categories describe problems with no known polynomial-time exact algorithm, same as NP-Complete (topic 3).

#### 7. Common Mistakes — Must Know

1. Using "NP-Hard" and "NP-Complete" as if they mean exactly the same thing — they're related but distinct, as shown by the TSP example above.
2. Assuming "NP-Hard" is somehow a stronger or scarier label than "NP-Complete" — it's actually the *broader* category; NP-Complete is the more specific overlap with NP.
3. Getting stuck trying to precisely classify every problem during an interview — for practical purposes, "this looks NP-Hard/NP-Complete, so I expect no fast exact solution" is usually the useful-enough takeaway (see topic 5).

#### 8. Related Topics

1. `3` NP-Complete — the Hardest Problems in NP
2. `2` NP — Checkable in Polynomial Time
3. `4` Recognising an NP-Complete Shape in an Interview

#### 9. Interview Must Remember

1. **NP-Complete = NP-Hard AND in NP. NP-Hard alone just means "at least as hard as NP", with no promise about verification speed.**
2. The optimization version of a problem (find the *best* answer) is often NP-Hard without necessarily being NP-Complete; the decision version (yes/no, under some threshold) usually is NP-Complete.
3. In practice, both labels lead to the same next step (topic 5) — knowing the distinction is about precision, not changing your approach.
