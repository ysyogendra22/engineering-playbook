# Reductions — Name Only

#### 1. Definition — Must Know

A **reduction** transforms one problem into another, so that solving the second problem also solves the first. If problem A can be reduced to problem B in polynomial time, then B is "at least as hard as" A — because any algorithm for B could also solve A (just do the transformation first, then use B's algorithm).

#### 2. Why It Is Used — Must Know

Reductions are the actual mechanism behind everything in this folder's Complexity Classes topics: they're how NP-Completeness is *proven* for new problems (topic 3), and recognising when your own problem can be reduced to a known one is a genuinely useful interview skill, even without formal proof.

#### 3. How It Works — Must Know

```text
Example: reducing "Is there a Hamiltonian Cycle?" (visit every node exactly
once and return to start) to the Travelling Salesman decision problem
("is there a route of length ≤ X?"):

  Take the Hamiltonian Cycle graph.
  Build a TSP instance: same nodes, edge weight 1 if the edge exists in
  the original graph, edge weight 2 (or any large value) if it doesn't.
  Ask: "is there a TSP route of length ≤ n?" (n = number of nodes)

  If yes → that route only used weight-1 edges → it's a Hamiltonian Cycle.
  If no  → no Hamiltonian Cycle exists.

This transformation is fast (polynomial time) and shows: if you could
solve TSP fast, you could solve Hamiltonian Cycle fast too — so TSP is
"at least as hard as" Hamiltonian Cycle.
```

A more everyday, practical use of the same idea: recognising "oh, this new interview problem is really just Subset Sum wearing a disguise" — that's an informal reduction, and it immediately tells you what techniques to reach for.

#### 4. Algorithm — Must Know

```text
To reduce problem A to problem B:
1. Write a transformation that turns any instance of A into an
   instance of B, in polynomial time.
2. Show that solving the transformed instance of B tells you the
   answer to the original instance of A.

If this is possible, A is "no harder than" B — an algorithm for B
gives you one for A for free.
```

#### 5. Kotlin Implementation — Must Know

*(Not applicable — reductions are a proof and recognition technique, not something coded directly for most interview purposes.)*

#### 6. Complexity — Must Know

| | Requirement |
|---|---|
| The reduction itself | Must run in polynomial time (otherwise it doesn't prove anything about relative difficulty) |

#### 7. Common Mistakes — Must Know

1. Trying to formally construct and prove a reduction live in an interview — this is a research-level skill; the practical version ("this looks like Subset Sum in disguise") is what's actually expected.
2. Forgetting that the reduction itself must be **fast** (polynomial time) — a slow transformation wouldn't prove anything useful about the target problem's difficulty.
3. Confusing "reduction" (transforming one problem into another) with simply "this problem reminds me of that one" — a real reduction is a precise, checkable transformation, even if you only sketch it informally.

#### 8. Related Topics

1. `3` NP-Complete — the Hardest Problems in NP — reductions are exactly how these are formally proven
2. `4` Recognising an NP-Complete Shape in an Interview — the informal, practical version of this skill

#### 9. Interview Must Remember

1. A reduction = **transform problem A into problem B (fast), so that solving B solves A.**
2. It's the formal tool behind proving NP-Completeness — and informally, it's just "recognising this problem is really a known one in disguise".
3. Name-and-idea depth is the expectation here — informally spotting a reduction ("this is Subset Sum again") is the practical skill worth having.
