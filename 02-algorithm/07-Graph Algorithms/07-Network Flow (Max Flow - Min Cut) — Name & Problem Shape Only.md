# Network Flow (Max Flow / Min Cut) — Name & Problem Shape Only

#### 1. Definition — Must Know

**Network flow** problems model a graph where edges have **capacities** (a maximum amount that can flow through them), and ask: what's the maximum total amount that can flow from a source node to a sink node, respecting every edge's capacity?

#### 2. Why It Is Used — Must Know

It's a name worth recognising because many real problems are secretly network flow: matching problems (assigning workers to tasks), scheduling with resource limits, and bipartite matching all reduce to it. You're not expected to implement a solver from memory — knowing the shape is the goal.

#### 3. How It Works — Must Know

```text
Source (S) → A (capacity 3) → Sink (T)
Source (S) → B (capacity 2) → Sink (T)

Max flow from S to T = 3 + 2 = 5
(each path's flow is limited by its smallest/"bottleneck" capacity)

A more connected example, with a shared bottleneck edge:
S → A (cap 10) → T
S → B (cap 10) → A (cap 1) → T   ← the A→T edge might already be full

The maximum flow is limited by whatever the tightest "cut" through the
graph is — this is the core idea behind the Max-Flow Min-Cut theorem:
the maximum possible flow always equals the minimum total capacity of
edges you'd need to remove to fully disconnect source from sink.
```

#### 4. Algorithm — Must Know

*(Name only — full augmenting-path algorithms like Ford-Fulkerson or Edmonds-Karp are out of scope to reproduce from memory.)*

```text
General shape (Ford-Fulkerson idea):
while a path from source to sink with spare capacity exists:
    find that path (an "augmenting path")
    push as much flow through it as its tightest edge allows
    reduce the remaining capacity along that path
return the total flow pushed
```

#### 5. Kotlin Implementation — Must Know

*(Not expected at this level — recognise the problem shape and name the general approach, rather than coding a solver.)*

#### 6. Complexity — Must Know

| Algorithm (name only) | Rough complexity |
|---|---|
| Ford-Fulkerson (basic) | Depends on the capacities themselves — can be slow on adversarial inputs |
| Edmonds-Karp (a specific, more careful version) | O(V · E²) |

#### 7. Common Mistakes — Must Know

1. Trying to reinvent max flow from scratch under interview time pressure — for most roles, naming the technique and the theorem (Max-Flow Min-Cut) is the expected depth.
2. Not recognising a disguised flow problem — "assign each worker to at most one task, each task to at most one worker" is bipartite matching, solvable as a flow problem.
3. Confusing this with shortest-path problems — flow is about **capacity and quantity**, not distance.

#### 8. Related Topics

1. `11` Complexity Classes (P, NP, NP-Complete) (its own folder) — max flow is actually solvable in polynomial time, unlike TSP, worth contrasting
2. `1` Dijkstra's Algorithm, `2` Kruskal's & Prim's Algorithms — other named graph algorithms in this folder

#### 9. Interview Must Remember

1. Network flow = **edges have capacities; find the max total flow from source to sink.**
2. The **Max-Flow Min-Cut theorem**: maximum flow equals the minimum total capacity of edges separating source from sink — a good one-liner to know.
3. This is a name-and-shape topic — recognise it and describe the approach, without expecting to code a full solver live.
