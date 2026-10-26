# Union-Find / Disjoint Set Union (DSU)

> A must-know structure for FAANG. It answers "are these two connected?" very fast, and it is short to code.

#### 1. What Is It?

**Union-Find** (also called **Disjoint Set Union**, DSU) keeps track of **groups** of items. It has two main operations:

| Operation | Meaning |
|---|---|
| **`find(x)`** | which group does `x` belong to? Returns a group **leader** (root). |
| **`union(a, b)`** | merge the group of `a` and the group of `b` |

Two items are in the same group when `find(a) == find(b)`.

Use it when:

- **edges arrive one by one** and you must know if two nodes are connected,
- you need to **count groups** (components) as they merge,
- you must find the **edge that creates a cycle**,
- you build a **minimum spanning tree** (Kruskal).

Each group is a small tree. Each node points to a **parent**. The root points to itself.

#### 2. How It Works

Start with each item alone: `parent[i] = i`.

```text
Items 0..4, each its own group:    parent = [0, 1, 2, 3, 4]

union(0, 1): root of 0 is 0, root of 1 is 1 → make 1's root point to 0:   parent = [0, 0, 2, 3, 4]
union(2, 3): parent = [0, 0, 2, 2, 4]
union(1, 3): find(1) = 0, find(3) = 2 → different groups → link: parent = [0, 0, 0, 2, 4]

find(3): 3 → 2 → 0     root is 0
find(4): 4             root is 4 (alone)
Same group? find(1) == find(3)? 0 == 0 → yes
Groups: {0,1,2,3} and {4}  → count = 2
```

Two small tricks make it almost constant time (see notes 24 and 25):

1. **Path compression:** while finding the root, point every node directly at the root.
2. **Union by size/rank:** attach the smaller tree under the bigger tree.

With both, each operation costs `O(α(n))`, which is below 5 for any real input. Treat it as constant.

#### 3. Kotlin Code

```kotlin
class UnionFind(n: Int) {
    private val parent = IntArray(n) { it }          // each node is its own root at the start
    private val size = IntArray(n) { 1 }
    var count = n                                    // number of groups
        private set

    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])    // path compression
        return parent[x]
    }

    fun union(a: Int, b: Int): Boolean {
        var rootA = find(a)
        var rootB = find(b)
        if (rootA == rootB) return false                   // already in the same group
        if (size[rootA] < size[rootB]) { val t = rootA; rootA = rootB; rootB = t }
        parent[rootB] = rootA                              // the smaller tree goes under the bigger one
        size[rootA] += size[rootB]
        count--
        return true
    }

    fun connected(a: Int, b: Int) = find(a) == find(b)
}

// Number of Provinces (LeetCode 547)
fun findCircleNum(isConnected: Array<IntArray>): Int {
    val n = isConnected.size
    val uf = UnionFind(n)
    for (i in 0 until n) for (j in i + 1 until n) {
        if (isConnected[i][j] == 1) uf.union(i, j)
    }
    return uf.count
}

// Redundant Connection (LeetCode 684): the edge that creates a cycle
fun findRedundantConnection(edges: Array<IntArray>): IntArray {
    val uf = UnionFind(edges.size + 1)
    for ((a, b) in edges) {
        if (!uf.union(a, b)) return intArrayOf(a, b)      // a and b were already connected
    }
    return intArrayOf()
}

// Satisfiability of Equality Equations (LeetCode 990): ["a==b", "b!=a"] ...
fun equationsPossible(equations: Array<String>): Boolean {
    val uf = UnionFind(26)
    for (e in equations) {
        if (e[1] == '=') uf.union(e[0] - 'a', e[3] - 'a')   // first handle all "=="
    }
    for (e in equations) {
        if (e[1] == '!' && uf.connected(e[0] - 'a', e[3] - 'a')) return false
    }
    return true
}
```

Checks: `findCircleNum([[1,1,0],[1,1,0],[0,0,1]])` → `2`. `findRedundantConnection([[1,2],[1,3],[2,3]])` → `[2, 3]`. `equationsPossible(["a==b","b!=a"])` → `false`.

**Accounts Merge (LeetCode 721):** give every email an id, union the emails of one account, then group the emails by root. Use a map from email to id.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| `find`, `union` (with both tricks) | `O(α(n))` — almost constant | |
| Build with `n` items | `O(n)` | `O(n)` |
| Process `E` edges | `O(E · α(n))` | |

#### 5. Common Mistakes

1. **Merging the items instead of the roots.** Always `union(find(a), find(b))`.
2. **Forgetting to check `rootA == rootB`** before decreasing `count`.
3. **No path compression**, so a long chain makes `find` slow.
4. **Arrays too small** when nodes start at 1. Allocate `n + 1`.
5. **Reading `parent[x]` as the root.** It is only the parent. Use `find(x)`.
6. **Using it on directed problems** (it ignores direction). Use DFS/Kahn there.

#### 6. Say This in the Interview

1. "Union-find keeps groups. `find` returns the group leader and `union` merges two groups."
2. "With path compression and union by size, each operation is almost `O(1)`."
3. "If `union` finds both nodes already in the same group, that edge makes a cycle."

#### 7. Quick Check

1. How do you check whether `a` and `b` are in the same group?
2. What does `union` return if they already are?

<details>
<summary>Answers</summary>

1. `find(a) == find(b)`.
2. `false`. Nothing is merged and the group count does not change.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 547 | Number of Provinces (Medium) | count groups |
| 684 | Redundant Connection (Medium) | the edge that closes a cycle |
| 990 | Satisfiability of Equality Equations (Medium) | union `==`, then check `!=` |
| 721 | Accounts Merge (Medium) | union emails of one account |
| 1319 | Number of Operations to Make Network Connected (Medium) | groups − 1 |
| 323 | Number of Connected Components (Medium, premium) | count groups |
| 1584 | Min Cost to Connect All Points (Medium) | Kruskal (note 27) |
