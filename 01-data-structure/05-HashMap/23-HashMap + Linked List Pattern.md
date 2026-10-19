# HashMap + Linked List Pattern

#### 1. Definition — Must Know

1. A linked list gives `O(1)` insert/remove **when you hold the node**, but finding a node takes `O(n)`.
2. A HashMap gives `O(1)` find by key.
3. Combine them: **the map finds the node, the list does the cheap reordering or linking**.

#### 2. Why It Is Used — Must Know

1. It fixes the slow part of a linked list (search) with a map lookup.
2. It is used to **copy** linked structures with extra pointers, to **clone graphs**, and to build caches (LRU, next topic group).
3. It is a medium-level interview pattern that checks you understand both structures.

#### 3. How It Works — Must Know

*Copy List with Random Pointer* (LeetCode 138): each node has `next` and a `random` pointer to any node (or null). Make a deep copy.

```text
Original:  A → B → C        A.random = C,  B.random = A,  C.random = B

Pass 1: create a copy of each node and remember it in a map:   A→A', B→B', C→C'
Pass 2: for each original node X:
            X'.next   = map[X.next]
            X'.random = map[X.random]

The map answers "which copy belongs to this original?" in O(1).
```

The map is the bridge between the old structure and the new one.

#### 4. Core Concepts — Must Know

1. **Map old → new** to copy or clone structures where nodes point to each other.
2. **Two passes:** (1) create all nodes, (2) connect them. This avoids "node not created yet" problems.
3. **Map key → node** to jump straight to a node in a list (the LRU idea).
4. **`LinkedHashMap`** is a ready-made HashMap + doubly linked list. It keeps insertion order or access order.
5. **Node identity as the key.** A node class without `equals`/`hashCode` uses identity, which is exactly what you want when copying.
6. **Other users of the idea:** Clone Graph (`old node → clone`), remembering visited nodes by identity, finding the entry point of a cycle with a set.

| Need | Combination |
|---|---|
| Deep copy with random pointers | `HashMap<Node, Node>` |
| Clone a graph | `HashMap<Node, Node>` + DFS/BFS |
| LRU cache | `HashMap<Key, Node>` + doubly linked list |
| Keep insertion order of keys | `LinkedHashMap` |
| Detect a cycle (simple) | `HashSet<Node>` (or Floyd's pointers) |

#### 5. Algorithm — Must Know

```text
copyRandomList(head):
    map = empty
    cur = head
    while cur != null:  map[cur] = Node(cur.val);  cur = cur.next
    cur = head
    while cur != null:
        map[cur].next = map[cur.next]       (null stays null)
        map[cur].random = map[cur.random]
        cur = cur.next
    return map[head]
```

#### 6. Kotlin Implementation — Must Know

```kotlin
class Node(var `val`: Int) {
    var next: Node? = null
    var random: Node? = null
}

// Copy List with Random Pointer
fun copyRandomList(head: Node?): Node? {
    if (head == null) return null
    val copy = HashMap<Node, Node>()                 // original → copy (identity keys)

    var cur: Node? = head
    while (cur != null) {                            // pass 1: create copies
        copy[cur] = Node(cur.`val`)
        cur = cur.next
    }

    cur = head
    while (cur != null) {                            // pass 2: connect copies
        val clone = copy.getValue(cur)
        clone.next = cur.next?.let { copy[it] }
        clone.random = cur.random?.let { copy[it] }
        cur = cur.next
    }
    return copy[head]
}

// Clone Graph — same idea with DFS
class GraphNode(val `val`: Int) {
    val neighbors = mutableListOf<GraphNode>()
}

fun cloneGraph(node: GraphNode?): GraphNode? {
    if (node == null) return null
    val clones = HashMap<GraphNode, GraphNode>()
    fun dfs(original: GraphNode): GraphNode {
        clones[original]?.let { return it }          // already cloned
        val clone = GraphNode(original.`val`)
        clones[original] = clone                     // register BEFORE visiting neighbours
        for (n in original.neighbors) clone.neighbors.add(dfs(n))
        return clone
    }
    return dfs(node)
}

// LinkedHashMap keeps insertion order (and can keep access order — see the LRU note)
val ordered = LinkedHashMap<String, Int>()
ordered["b"] = 1; ordered["a"] = 2
println(ordered.keys)                                // [b, a]
```

The `O(1)`-space alternative for the random pointer problem weaves the copies between the originals, then splits the lists. It is clever but easier to get wrong; the map version is the safe interview answer.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Copy List with Random Pointer (map) | `O(n)` | `O(n)` |
| Weaving trick | `O(n)` | `O(1)` extra |
| Clone Graph | `O(V + E)` | `O(V)` |

#### 8. Common Map + Linked List Patterns — Must Know

1. **Copy List with Random Pointer** (LeetCode 138).
2. **Clone Graph** (LeetCode 133).
3. **LRU Cache** (LeetCode 146) — next topic group.
4. **LFU Cache** (LeetCode 460) — map of frequency → list.
5. **All O(1) Data Structure** (LeetCode 432) — map plus a list of buckets.
6. **Linked List Cycle** (LeetCode 141) — a set of nodes (or Floyd's pointers).
7. **Intersection of Two Linked Lists** (LeetCode 160) — set of nodes (or two pointers).

#### 9. Edge Cases / Common Mistakes

1. Using `copy[cur.next]` for a null `next` without handling it. Use `cur.next?.let { copy[it] }`.
2. Registering the clone **after** the recursion in Clone Graph, which loops forever on cycles.
3. Giving the node class an `equals` based on `val`. Equal values would then collide as keys. Keep identity equality for nodes.
4. Returning the original head instead of the copied head.
5. Empty list (`head == null`).
6. A single node pointing to itself via `random`.
7. Creating copies in the second pass and getting `null` for nodes that do not exist yet.

#### 10. When to Use / When Not to Use

**Use when:**

1. You copy or clone linked structures with extra pointers.
2. You need a quick jump to a node in a list.

**Avoid when:**

1. The list is plain (`next` only). Copy it with a simple loop.
2. Memory is tight and the `O(1)` weaving trick is allowed.

#### 11. Related Topics

1. HashMap + Doubly Linked List — LRU Pattern
2. Linked List (`01-data-structure/02-LinkedList`)
3. Graph (`01-data-structure/10-Graph`)
4. Visited / Seen Pattern (`01-data-structure/06-HashSet/10-Visited - Seen Pattern.md`)

#### 12. Interview Must Remember

1. **Map `old node → new node`.** Two passes: create, then connect.
2. For graphs, register the clone **before** visiting neighbours.
3. Map gives `O(1)` find; list gives `O(1)` re-link.
4. Node keys should use identity equality.
