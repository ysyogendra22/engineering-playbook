# Union Find

> Track groups. `find` tells you which group an item is in, and `union` merges two groups, both in nearly `O(1)`.

#### 1. What Is It?

**Union Find** (Disjoint Set Union, DSU) keeps a set of groups. Each group has one **root**. Two items are connected if they have the same root.

**Signals**

- "Are `a` and `b` **connected**?"
- Edges arrive one by one and you **merge groups** (accounts, friends, stones)
- "**Number of components**" that changes as you add edges
- "Which edge **creates a cycle**?" in an undirected graph (Redundant Connection)
- Kruskal's minimum spanning tree
- Equality constraints (`a == b`, `b != c`)

**Operations**

| Operation | Meaning |
|---|---|
| `find(x)` | root of `x`'s group, with **path compression** |
| `union(a, b)` | join the two groups (smaller under larger = **union by size**); returns `false` if they were already joined |
| `count` | number of groups, reduced by 1 on every successful `union` |

**Union Find vs DFS**

| | Union Find | DFS / BFS |
|---|---|---|
| Edges added over time (dynamic) | great | rerun each time |
| One-time component count | fine | fine |
| Need the path itself | no | yes |
| Cycle in an undirected graph | `find(a) == find(b)` before union | parent check |

#### 2. How It Works

```text
n = 5, parent = [0,1,2,3,4]   (every item is its own group)
union(0,1): parent[1] = 0       groups: {0,1} {2} {3} {4}
union(3,4): parent[4] = 3       groups: {0,1} {2} {3,4}
find(1) = 0, find(4) = 3        different → not connected
union(1,4): roots 0 and 3 merge → {0,1,3,4} {2}
```

**Path compression.** While walking up to the root, point each node closer to the root. Later `find` calls are faster.

**Union by size.** Hang the smaller tree under the larger one. Keeps trees shallow.

With both tricks the cost per operation is the inverse Ackermann function: below 5 for any real input.

**Cycle detection.** Before `union(a, b)`, if `find(a) == find(b)` they are already connected, so this edge closes a cycle. That edge is the "redundant connection".

**Kruskal MST.** Sort edges by weight. Add an edge if its ends are in different groups. Stop at `n − 1` edges.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Union Find |
|---|---|---|
| Connected after each edge | rerun DFS each time, `O(E · (V + E))` | `O(E · α(V))` |
| Redundant edge | DFS from `a` to `b` before adding each edge | `find` comparison |
| Merge accounts | repeatedly merge lists until stable | union by shared emails |

```kotlin
// Brute force: is `a` connected to `b`? BFS each time
fun connectedBrute(graph: Array<MutableList<Int>>, a: Int, b: Int): Boolean {
    val seen = BooleanArray(graph.size)
    val queue = ArrayDeque<Int>()
    queue.addLast(a)
    seen[a] = true
    while (queue.isNotEmpty()) {
        val node = queue.removeFirst()
        if (node == b) return true
        for (next in graph[node]) if (!seen[next]) { seen[next] = true; queue.addLast(next) }
    }
    return false
}
```

#### 4. Kotlin Code

```kotlin
class UnionFind(n: Int) {
    private val parent = IntArray(n) { it }
    private val size = IntArray(n) { 1 }
    var count = n
        private set

    fun find(x: Int): Int {
        var root = x
        while (parent[root] != root) {
            parent[root] = parent[parent[root]]          // path halving
            root = parent[root]
        }
        return root
    }

    fun union(a: Int, b: Int): Boolean {
        var ra = find(a)
        var rb = find(b)
        if (ra == rb) return false                       // already connected
        if (size[ra] < size[rb]) { val t = ra; ra = rb; rb = t }
        parent[rb] = ra                                  // smaller under larger
        size[ra] += size[rb]
        count--
        return true
    }
}

// Number of Connected Components in an Undirected Graph (LeetCode 323; free alternative: 547)
fun countComponents(n: Int, edges: Array<IntArray>): Int {
    val uf = UnionFind(n)
    for ((a, b) in edges) uf.union(a, b)
    return uf.count
}

// Number of Provinces (LeetCode 547)
fun findCircleNum(isConnected: Array<IntArray>): Int {
    val n = isConnected.size
    val uf = UnionFind(n)
    for (i in 0 until n) for (j in i + 1 until n) if (isConnected[i][j] == 1) uf.union(i, j)
    return uf.count
}

// Redundant Connection (LeetCode 684): the edge that closes a cycle (nodes are 1..n)
fun findRedundantConnection(edges: Array<IntArray>): IntArray {
    val uf = UnionFind(edges.size + 1)
    for (e in edges) if (!uf.union(e[0], e[1])) return e
    return intArrayOf()
}

// Accounts Merge (LeetCode 721)
fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
    val uf = UnionFind(accounts.size)
    val owner = HashMap<String, Int>()                   // email -> first account index that has it
    for ((i, account) in accounts.withIndex()) {
        for (j in 1 until account.size) {
            val email = account[j]
            val first = owner[email]
            if (first == null) owner[email] = i else uf.union(i, first)
        }
    }
    val groups = HashMap<Int, java.util.TreeSet<String>>()
    for ((email, i) in owner) groups.getOrPut(uf.find(i)) { java.util.TreeSet() }.add(email)
    return groups.map { (root, emails) -> listOf(accounts[root][0]) + emails.toList() }
}

// Satisfiability of Equality Equations (LeetCode 990)
fun equationsPossible(equations: Array<String>): Boolean {
    val uf = UnionFind(26)
    for (eq in equations) if (eq[1] == '=') uf.union(eq[0] - 'a', eq[3] - 'a')
    for (eq in equations) {
        if (eq[1] == '!' && uf.find(eq[0] - 'a') == uf.find(eq[3] - 'a')) return false
    }
    return true
}

// Most Stones Removed with Same Row or Column (LeetCode 947)
fun removeStones(stones: Array<IntArray>): Int {
    val offset = 10001                                   // columns live after rows
    val uf = UnionFind(20002)
    for ((r, c) in stones) uf.union(r, c + offset)
    val roots = HashSet<Int>()
    for ((r, _) in stones) roots.add(uf.find(r))
    return stones.size - roots.size                      // keep one stone per component
}

// Kruskal's MST: total weight of the minimum spanning tree, or -1 if the graph is not connected
fun kruskal(n: Int, edges: Array<IntArray>): Int {       // edge = [u, v, weight]
    val uf = UnionFind(n)
    var total = 0
    for (e in edges.sortedBy { it[2] }) {
        if (uf.union(e[0], e[1])) total += e[2]
    }
    return if (uf.count == 1) total else -1
}
```

Checks: `countComponents(5, [[0,1],[1,2],[3,4]])` → `2`. `findCircleNum([[1,1,0],[1,1,0],[0,0,1]])` → `2`. `findRedundantConnection([[1,2],[1,3],[2,3]])` → `[2,3]`; `([[1,2],[2,3],[3,4],[1,4],[1,5]])` → `[1,4]`. `accountsMerge` of John's two accounts sharing `johnsmith@mail.com`, Mary, and a separate John → three groups; the merged John group is `[John, john00@mail.com, john_newyork@mail.com, johnsmith@mail.com]` (groups can come back in any order). `equationsPossible(["a==b","b!=a"])` → `false`; `(["b==a","a==b"])` → `true`; `(["a==b","b!=c","c==a"])` → `false`. `removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])` → `5`; `([[0,0],[0,2],[1,1],[2,0],[2,2]])` → `3`. `kruskal(4, [[0,1,1],[1,2,2],[0,2,3],[2,3,4]])` → `7`.

#### 5. Complexity

| Operation | Time | Space |
|---|---|---|
| `find` / `union` (both tricks) | `O(α(n))`, about `O(1)` | `O(n)` |
| Build from `E` edges | `O(E · α(n))` | `O(n)` |
| Kruskal | `O(E log E)` (the sort) | `O(n)` |

#### 6. Common Mistakes

1. **Forgetting path compression** or union by size. Long chains make `find` `O(n)`.
2. **Union on the items instead of the roots** (`parent[a] = b`). Always join the roots.
3. **Wrong size.** Redundant Connection nodes are `1..n`, so the array needs `n + 1` slots.
4. **Not decrementing `count`** only on a successful merge.
5. **Accounts Merge:** using the name to merge. Names can repeat for different people. Merge by email.
6. **Equality equations:** processing `!=` before all `==` are done.
7. **Using Union Find when you need the path** or the shortest distance. Use BFS/DFS.

#### 7. Say This in the Interview

1. "I need to merge groups and ask if two items are connected, as edges arrive. Union Find does both in nearly constant time."
2. "I use path compression and union by size, so each operation is about `O(α(n))`."
3. "If `find(a) == find(b)` before I union them, adding this edge would create a cycle."

#### 8. Quick Check

1. In a graph with 6 nodes and 3 successful unions, how many components are left?
2. Why does `union` return a Boolean?

<details>
<summary>Answers</summary>

1. `6 − 3 = 3`.
2. A `false` means the two were already connected. That signals a cycle or redundant edge, and it lets you update `count` only when a real merge happens.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (Medium) | count after unions |
| 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Medium) | `union` returns false |
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) (Medium) | `==` first, then `!=` |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) (Medium) | union by shared email |
| 947 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) (Medium) | rows and columns as nodes |
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium) | Kruskal |
| 323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Medium, premium) | use 547 instead |
