# Path Compression

#### 1. What Is It?

**Path compression** is a small trick that makes `find` in Union-Find fast.

When `find(x)` walks up from `x` to the root, it **re-points every node it passed directly to the root**. The next `find` on those nodes takes one step.

Without it, a chain like `4 → 3 → 2 → 1 → 0` makes every `find(4)` walk 4 steps. With it, the chain flattens after the first call.

It is a very common interview follow-up: "how do you make union-find fast?".

#### 2. How It Works

```text
Before find(4):                  After find(4) with path compression:

0 ← 1 ← 2 ← 3 ← 4                0 ← 1,  0 ← 2,  0 ← 3,  0 ← 4
(a long chain)                   (every node points straight to the root 0)

find(4): walk 4 → 3 → 2 → 1 → 0 (root). On the way back, set parent[4], parent[3], parent[2], parent[1] = 0.
Next find(4): 4 → 0   (one step)
```

Two ways to write it:

| Way | Idea |
|---|---|
| **Recursive** | `parent[x] = find(parent[x])` |
| **Iterative** | walk up to find the root, then walk again and set each parent to the root |

(There is also "path halving": `parent[x] = parent[parent[x]]` while walking.)

#### 3. Kotlin Code

```kotlin
// Recursive (the shortest)
fun find(parent: IntArray, x: Int): Int {
    if (parent[x] != x) parent[x] = find(parent, parent[x])   // point directly to the root
    return parent[x]
}

// Iterative (no recursion, safe for very long chains)
fun findIterative(parent: IntArray, x: Int): Int {
    var root = x
    while (parent[root] != root) root = parent[root]          // 1. find the root
    var cur = x
    while (parent[cur] != root) {                             // 2. point everyone on the path to the root
        val next = parent[cur]
        parent[cur] = root
        cur = next
    }
    return root
}

// Demo: a chain 0 ← 1 ← 2 ← 3 ← 4
val parent = intArrayOf(0, 0, 1, 2, 3)
println(find(parent, 4))          // 0
println(parent.toList())          // [0, 0, 0, 0, 0]  (the chain is flat now)
```

Without union by size, path compression alone already gives `O(log n)` amortized per operation. Together with union by size (note 25), it gives `O(α(n))`.

#### 4. Complexity

| | Time per `find` |
|---|---|
| No tricks | `O(n)` worst case |
| Path compression only | `O(log n)` amortized |
| Path compression + union by size | `O(α(n))`, almost constant |

#### 5. Common Mistakes

1. **Writing `return find(parent[x])` without setting `parent[x]`.** Then nothing is compressed.
2. **Compressing a copy** of the array instead of the real one.
3. **Recursion depth** on a very long chain with the recursive version. Use the iterative one for huge inputs.
4. **Mixing it up with union by size.** They are two different tricks.

#### 6. Say This in the Interview

1. "Path compression re-points each node I visit in `find` to the root, so later finds are one step."
2. "Together with union by size, each operation is almost constant, `O(α(n))`."

#### 7. Quick Check

1. What changes in the array during `find(4)` on the chain above?
2. Does path compression change which group a node belongs to?

<details>
<summary>Answers</summary>

1. Every node on the path now has the root as its parent.
2. No. It only changes the tree shape, not the groups.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 684 | Redundant Connection (Medium) | union-find with compression |
| 547 | Number of Provinces (Medium) | count groups |
| 990 | Satisfiability of Equality Equations (Medium) | union-find |
| 721 | Accounts Merge (Medium) | union-find on emails |
