# Travelling Salesman Problem — Name & Idea Only

#### 1. Definition — Must Know

The **Travelling Salesman Problem (TSP)**: given a list of cities and the distances between every pair, find the shortest possible route that visits every city exactly once and returns to the start.

#### 2. Why It Is Used — Must Know

1. It's the most famous example of a problem that is easy to *state* but has no known fast (polynomial-time) exact solution — a key example for Complexity Classes (`11-Complexity Classes`, its own folder).
2. Recognising a problem as "TSP-shaped" (visit everything once, minimise total cost, order matters) is a valuable interview skill, even without implementing a solver.

#### 3. How It Works — Must Know

```text
Brute force: try every possible ordering of cities, compute total distance
             for each, keep the shortest. That's (n-1)! possible routes
             (fixing the start city) — explodes fast: 10 cities → 362,880
             routes; 20 cities → over 10^17 routes.

Backtracking + branch and bound: build a route city by city, pruning any
             partial route whose cost already exceeds the best found so far
             (see `06-Branch and Bound`). Much faster in practice, still
             exponential in the worst case.

Bitmask DP (small n, exact): dp[mask][i] = shortest route visiting exactly
             the cities in `mask`, ending at city i (see `12-Interval DP
             & Bitmask DP — Names Only` in `05-Dynamic Programming`).
             Reduces the brute-force (n-1)! down to O(2ⁿ × n²) — still
             exponential, but usable for n up to about 15-20.
```

#### 4. Algorithm — Must Know

*(Name and shape only — not expected to be implemented from memory.)*

```text
For small n (≤ ~20): bitmask DP gives an exact answer in O(2ⁿ × n²).
For larger n: use an approximation algorithm or a heuristic (nearest
              neighbour, genetic algorithms, simulated annealing) — these
              give a good, not necessarily optimal, answer quickly.
```

#### 5. Kotlin Implementation — Must Know

*(Not expected — knowing the problem shape and the general approaches is the goal at this level.)*

#### 6. Complexity — Must Know

| Approach | Complexity | Gives the exact optimum? |
|---|---|---|
| Brute force | O(n!) | Yes |
| Backtracking + branch and bound | Exponential, faster in practice | Yes |
| Bitmask DP | O(2ⁿ × n²) | Yes, but only usable for small n |
| Approximation / heuristics | Polynomial | No — a good, not guaranteed-best, answer |

#### 7. Common Mistakes — Must Know

1. Trying to design an exact, fast (polynomial) algorithm for TSP in an interview — none is known to exist; this is expected, not a personal failure to solve it.
2. Not recognising a disguised TSP-shaped problem (for example, "visit every location once with minimum total travel time") and wasting time looking for a simple greedy or DP trick that doesn't apply at scale.
3. Forgetting to mention approximation approaches when n is large — an interviewer often wants to hear "here's what I'd do practically", not just "this is NP-hard, I give up".

#### 8. Related Topics

1. `11` Complexity Classes (P, NP, NP-Complete) (its own folder) — why TSP has no known fast exact solution
2. `12` Interval DP & Bitmask DP — Names Only (in `05-Dynamic Programming`) — the exact small-n solution
3. `06` Branch and Bound — Tracking a Best-So-Far Bound — the practical exact approach for moderate n

#### 9. Interview Must Remember

1. TSP = **visit every node once, minimise total cost, return to start.**
2. No known algorithm solves it exactly in polynomial time — say this directly, it's the expected, correct answer.
3. For small n, bitmask DP gives an exact answer; for large n, mention approximation or heuristic approaches instead.
