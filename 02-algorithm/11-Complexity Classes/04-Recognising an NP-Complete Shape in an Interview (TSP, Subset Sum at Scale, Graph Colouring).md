# Recognising an NP-Complete Shape in an Interview (TSP, Subset Sum at Scale, Graph Colouring)

#### 1. Definition — Must Know

A practical checklist for spotting, during an interview, when a problem is very likely NP-Complete — so you can confidently say so and move straight to a practical approach, instead of burning time hunting for a fast exact algorithm that doesn't exist.

#### 2. Why It Is Used — Must Know

This is arguably the most useful topic in this whole folder for a **real interview**: knowing the theory (topics 1–3) is only valuable if you can apply it live, under time pressure, to recognise "wait, this smells NP-Complete" within the first minute or two of hearing a problem.

#### 3. How It Works — Must Know

```text
Common NP-Complete "smells" to listen for:

"Visit every X exactly once, minimize total cost"
  → sounds like TSP

"Select a subset of items whose values sum to exactly/at most a target"
  (with large numbers, not small bounded ones)
  → sounds like Subset Sum

"Assign each item to a group such that no two connected/conflicting
  items share a group, using the fewest groups"
  → sounds like Graph Coloring

"Find the largest subset where every pair satisfies some relationship"
  → sounds like a Clique problem (a well-known NP-Complete problem)

"Schedule tasks on limited resources to minimize total time,
  with complex dependency/conflict rules"
  → often NP-Complete in its general form (though many practical
    restricted versions ARE solvable in P — read the constraints carefully)
```

**Important nuance**: constraints matter a lot. Subset Sum with a **small** target value has a perfectly good DP solution (`05-Dynamic Programming/06`) in pseudo-polynomial time. The same problem with numbers up to 10^18 does not. Read the actual bounds before concluding a problem is NP-Complete.

#### 4. Algorithm — Must Know

```text
When a problem "smells" NP-Complete:
1. Check the actual constraints given (n, value ranges) — could a DP or
   backtracking solution realistically finish within them?
2. If n is small (roughly ≤ 20-25), say so, and propose bitmask DP or
   backtracking with pruning — a genuinely correct, exact approach.
3. If n is large, say directly: "this looks NP-Complete, so I don't
   expect a fast exact solution — here's what I'd do instead"
   → go to topic 5.
4. Never go silent or stuck trying to force a fast exact answer that
   likely doesn't exist — recognising the shape IS the correct answer.
```

#### 5. Kotlin Implementation — Must Know

*(Not applicable — this is a recognition skill, not an algorithm.)*

#### 6. Complexity — Must Know

Not applicable to this topic directly — see topics 1-3 for the complexity classes themselves.

#### 7. Common Mistakes — Must Know

1. Panicking or going quiet when a problem seems impossibly hard, instead of naming what it looks like and proposing a practical path forward.
2. Declaring a problem NP-Complete without checking the actual given constraints — many problems that *sound* similar to famous NP-Complete ones have a small, bounded input size that makes exponential approaches perfectly fine in practice.
3. Assuming every graph/scheduling/selection problem is automatically NP-Complete — plenty of very similar-sounding problems (shortest path, bipartite matching, interval scheduling) are actually in P; check carefully rather than pattern-matching too loosely.

#### 8. Related Topics

1. `3` NP-Complete — the Hardest Problems in NP — the theory behind this recognition skill
2. `5` What to Do Instead — Approximation, Heuristics, Smaller Exact Inputs — the next step once you've recognised the shape
3. `06-Backtracking & Branch and Bound/08` Travelling Salesman Problem — the canonical worked example

#### 9. Interview Must Remember

1. **"Visit everything once", "select a subset summing to a large target", "color with the fewest groups, no conflicts"** — the three go-to smells.
2. **Always check the actual constraints** — small n changes everything, even for famously hard problem shapes.
3. Confidently naming "this looks NP-Complete" and pivoting to a practical approach is a **strong** answer, not a failure to solve the problem.
