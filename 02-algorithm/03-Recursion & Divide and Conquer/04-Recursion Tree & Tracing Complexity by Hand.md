# Recursion Tree & Tracing Complexity by Hand

#### 1. Definition — Must Know

1. A **recursion tree** is a diagram of every recursive call a function makes, drawn as a tree: the first call at the top (the root), and each call it makes as a child below it.
2. It is a way to **see** an algorithm's complexity instead of just trusting a formula.

#### 2. Why It Is Used — Must Know

1. It turns "what's the complexity of this recursive function?" into a countable diagram: how many nodes, and how much work per node.
2. It shows you exactly *why* naive recursive Fibonacci is slow — the tree is full of the same calls, repeated.

#### 3. How It Works — Must Know

Naive recursive Fibonacci, `fib(4)`:

```text
                    fib(4)
                  /        \
             fib(3)          fib(2)
            /      \        /      \
       fib(2)    fib(1)  fib(1)   fib(0)
      /      \
  fib(1)   fib(0)
```

1. Count the nodes: this small tree already has 9 calls for `fib(4)`.
2. Notice `fib(2)` is computed twice, and `fib(1)` three times — the same work is repeated. This is why naive Fibonacci is O(2ⁿ): the tree roughly doubles in size for every step up.
3. Compare with Merge Sort's tree (topic 3): each level does O(n) total work across all its nodes, and there are O(log n) levels, giving O(n log n) — no repeated work, just a clean, balanced tree.

#### 4. Algorithm — Must Know

*(A method, not code)*

```text
1. Draw the first call as the root.
2. Draw each recursive call it makes as a child node.
3. Repeat for every child, until you reach base cases (the leaves).
4. Count: how many nodes are there, and how much non-recursive work does each node do?
5. Total work ≈ number of nodes × work per node (adjust if work per node varies by level).
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// The function you'd trace with a recursion tree — no extra code needed to draw one,
// it's a technique done on paper, not something you implement.
fun fib(n: Int): Int {
    if (n <= 1) return n
    return fib(n - 1) + fib(n - 2)   // two recursive calls → tree branches in two
}
```

#### 6. Complexity — Must Know

| Function | Tree shape | Complexity |
|---|---|---|
| `factorial(n)` | A single line down (one child per node) | O(n) |
| `fib(n)` (naive) | A full binary tree, roughly doubling each level | O(2ⁿ) |
| `mergeSort(n)` | A balanced tree, log n levels, O(n) work per level | O(n log n) |

The general rule: **total work = number of nodes visited × work done per node** (or, level by level, sum the work across each level of the tree).

#### 7. Common Mistakes — Must Know

1. Only counting the depth of the tree and forgetting how many nodes are at each level.
2. Assuming a recursive function is efficient without checking whether it repeats the same subproblem (a sign that memoization is needed, topic 8).
3. Not accounting for the cost of the **combine step** at each node (relevant for divide and conquer, topic 3).

#### 8. Related Topics

1. `1` Base Case & Recursive Case — where the tree's leaves come from
2. `3` Divide and Conquer — the balanced-tree case
3. `5` Recurrence Relations & the Master Theorem — the formula version of this same idea
4. `8` Memoization — the fix once a tree shows repeated subproblems

#### 9. Interview Must Remember

1. When asked for a recursive function's complexity, **draw the tree** — it rarely lies.
2. Repeated subproblems in the tree are the signal to add memoization.
3. Total work = nodes × work per node, or sum the work level by level.
