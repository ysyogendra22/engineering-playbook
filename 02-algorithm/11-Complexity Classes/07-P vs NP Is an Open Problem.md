# P vs NP Is an Open Problem

#### 1. Definition — Must Know

**"Is P equal to NP?"** is one of the most famous unsolved problems in computer science and mathematics. Nobody has ever proven whether every problem whose solution can be *checked* quickly (NP) can also be *solved* quickly (P) — or proven that they're different. It's one of the seven Millennium Prize Problems, with a $1 million reward for a correct proof either way.

#### 2. Why It Is Used — Must Know

This is genuinely good to know as context: when you say "TSP is NP-Complete, so I don't expect a fast exact algorithm", you are relying on the strong **suspicion** (shared by nearly all computer scientists) that P ≠ NP — but it is not, technically, a mathematically proven fact. Knowing this shows real depth of understanding, not just memorised rules.

#### 3. How It Works — Must Know

```text
If P = NP were proven true:
  Every problem whose answer can be checked quickly could ALSO be solved
  quickly. This would mean TSP, Subset Sum, Graph Coloring, and every
  other NP-Complete problem would suddenly have a fast exact algorithm.
  This would also break most of modern cryptography, which relies on
  certain problems (like factoring large numbers) being hard to solve
  but easy to verify.

If P ≠ NP were proven true:
  It would formally confirm what's already strongly suspected: some
  problems are fundamentally harder to solve than to check, no matter
  how clever an algorithm you find.

Current state: neither has been proven. Almost everyone believes P ≠ NP,
  based on decades of failed attempts to find fast algorithms for
  NP-Complete problems, but no one has proven it.
```

#### 4. Algorithm — Must Know

*(Not applicable — there is no algorithm here, this is a statement about the current state of mathematical knowledge.)*

#### 5. Kotlin Implementation — Must Know

*(Not applicable.)*

#### 6. Complexity — Must Know

Not applicable — this topic is about the status of a theoretical question, not a specific algorithm's complexity.

#### 7. Common Mistakes — Must Know

1. Stating "P ≠ NP" as a proven fact rather than a strongly believed, unproven conjecture — precise language matters here ("it is widely believed that...", not "it has been proven that...").
2. Thinking this is purely academic trivia with no practical relevance — it directly underpins why "this is NP-Complete, so I won't look for a fast exact algorithm" is a reasonable, defensible engineering decision, not a guess.
3. Confusing this open question with the (separate, resolved) fact that specific problems like TSP are NP-Complete — that classification itself is proven; whether NP-Complete problems could ever have a fast algorithm is what remains open.

#### 8. Related Topics

1. `1` P — Solvable in Polynomial Time
2. `2` NP — Checkable in Polynomial Time
3. `3` NP-Complete — the Hardest Problems in NP

#### 9. Interview Must Remember

1. **P vs NP is unsolved** — nobody has proven whether they're the same or different.
2. Almost everyone believes **P ≠ NP**, which is *why* "no known fast algorithm exists" for NP-Complete problems is treated as a safe, practical assumption.
3. A precise, honest phrasing ("widely believed, not proven") is a small detail that signals genuine understanding.
