# P — Solvable in Polynomial Time

#### 1. Definition — Must Know

**P** is the set of problems that can be **solved** by an algorithm whose running time is a polynomial function of the input size — O(n), O(n log n), O(n²), O(n³), and so on (as opposed to O(2ⁿ) or O(n!), which grow far faster).

#### 2. Why It Is Used — Must Know

"Is this problem in P?" is really asking "does a reasonably fast, exact algorithm exist for this?" — nearly every algorithm covered elsewhere in this folder (sorting, searching, shortest paths, DP problems) is in P. Knowing this category by name gives you the vocabulary to talk about *why* some problems (topic 3) are fundamentally harder.

#### 3. How It Works — Must Know

```text
In P (a fast algorithm exists and is known):
  Sorting               — O(n log n)
  Binary search         — O(log n)
  Shortest path (Dijkstra's, non-negative weights) — O((V+E) log V)
  Most Dynamic Programming problems from `05-Dynamic Programming` — polynomial

NOT known to be in P (no fast exact algorithm is known):
  Travelling Salesman Problem (exact answer)  — see `06-Backtracking/08`
  General Subset Sum (with large numbers)     — technically NP-complete
```

`n log n`, `n²`, and even `n^10` all count as "polynomial", and are all considered "efficient" in this classification — even though `n^10` is very slow in practice for large `n`. The P vs NP distinction is about a different, more fundamental line: "is there *any* polynomial algorithm at all", not "is the polynomial small".

#### 4. Algorithm — Must Know

```text
To check "is my problem in P?":
  Have I (or has anyone) found an algorithm whose worst-case time is
  bounded by SOME polynomial in the input size, for ALL valid inputs?

  Yes → the problem is in P (or at least, a known algorithm proves it's
        at least as easy as P; formally "in P" requires this to be provably
        always possible)
```

#### 5. Kotlin Implementation — Must Know

*(Not applicable — this is a classification concept about problems in general, not a specific algorithm to implement.)*

#### 6. Complexity — Must Know

| Growth type | In P? |
|---|---|
| O(1), O(log n), O(n), O(n log n), O(n²), O(n^k) for any fixed k | Yes |
| O(2ⁿ), O(n!), O(nⁿ) | No — these are exponential/worse, not polynomial |

#### 7. Common Mistakes — Must Know

1. Assuming "polynomial" means "fast in practice" — O(n^10) is polynomial but can be far slower in practice than a small exponential algorithm on realistic input sizes. P is a theoretical classification, not a promise of practical speed.
2. Assuming every problem you can solve with a loop is automatically "in P" — the classification requires the algorithm's worst case to be bounded by a polynomial for **all** valid inputs, not just typical ones.
3. Confusing "I don't currently know a polynomial algorithm" with "provably no polynomial algorithm exists" — for most problems (including TSP), it's genuinely unknown whether a fast algorithm could exist; this is exactly what the open P vs NP question (topic 7) is about.

#### 8. Related Topics

1. `2` NP — Checkable in Polynomial Time — the related, larger category
2. `3` NP-Complete — the Hardest Problems in NP — where the genuinely hard problems live
3. `4` Recognising an NP-Complete Shape in an Interview

#### 9. Interview Must Remember

1. **P = a fast (polynomial-time) algorithm is known to exist.**
2. Nearly everything else in this playbook — sorting, searching, DP, shortest paths — is in P.
3. "Polynomial" is a theoretical bar, not a guarantee of practical speed — O(n^10) still counts, even though it's slow for large n.
