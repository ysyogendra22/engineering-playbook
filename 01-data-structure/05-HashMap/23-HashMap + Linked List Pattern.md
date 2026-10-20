# HashMap + Linked List Pattern

#### 1. What Is It?

A linked list can add or remove a node in `O(1)` **if you already hold the node**. But finding a node takes `O(n)`.

A HashMap finds a value in `O(1)`.

**Combine them: the map finds the node, the list does the cheap re-linking.** The map is also a **bridge between an old structure and its copy**.

Where it is used:

- **Copy List with Random Pointer** (LeetCode 138): map old node → new node.
- **Clone Graph** (LeetCode 133): map old node → clone.
- **LRU Cache** (LeetCode 146): map key → node in a doubly linked list (note 25).
- `LinkedHashMap`: a ready-made HashMap + linked list that keeps insertion or access order.

#### 2. How It Works

*Copy List with Random Pointer* (LeetCode 138): each node has `next` and a `random` pointer to any node (or `null`). Make a deep copy.

```text
Original:  A → B → C       A.random = C,  B.random = A,  C.random = B

Pass 1: create a copy of every node and remember it in a map:   A→A',  B→B',  C→C'
Pass 2: for each original node X:
            X'.next   = map[X.next]
            X'.random = map[X.random]
```

The map answers "which copy belongs to this original?" in `O(1)`.

Why **two passes**? When you set `A'.random = C'`, the copy `C'` must already exist.

For **Clone Graph**: the map also works as the "visited" set. **Put the clone in the map before visiting the neighbours**, or a cycle makes the code loop forever.

Keys are **node objects**. A node class without `equals()` uses identity, which is exactly what you want here.

#### 3. Kotlin Code

```kotlin
class Node(var `val`: Int) {
    var next: Node? = null
    var random: Node? = null
}

// Copy List with Random Pointer
fun copyRandomList(head: Node?): Node? {
    if (head == null) return null
    val copy = HashMap<Node, Node>()                   // original → copy

    var cur: Node? = head
    while (cur != null) {                              // pass 1: create all copies
        copy[cur] = Node(cur.`val`)
        cur = cur.next
    }

    cur = head
    while (cur != null) {                              // pass 2: connect the copies
        val clone = copy.getValue(cur)
        clone.next = cur.next?.let { copy[it] }
        clone.random = cur.random?.let { copy[it] }
        cur = cur.next
    }
    return copy[head]
}

// Clone Graph
class GraphNode(val `val`: Int) {
    val neighbors = mutableListOf<GraphNode>()
}

fun cloneGraph(node: GraphNode?): GraphNode? {
    if (node == null) return null
    val clones = HashMap<GraphNode, GraphNode>()
    fun dfs(original: GraphNode): GraphNode {
        clones[original]?.let { return it }            // already cloned
        val clone = GraphNode(original.`val`)
        clones[original] = clone                       // register BEFORE visiting the neighbours
        for (n in original.neighbors) clone.neighbors.add(dfs(n))
        return clone
    }
    return dfs(node)
}
```

The `O(1)`-space alternative for the random-pointer problem weaves the copies between the originals, then splits the lists. It is clever but easy to get wrong. The map version is the safe interview answer. Mention that the weaving trick exists.

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| Copy List with Random Pointer (map) | `O(n)` | `O(n)` |
| Same, with the weaving trick | `O(n)` | `O(1)` extra |
| Clone Graph | `O(V + E)` | `O(V)` |

#### 5. Common Mistakes

1. **Using `copy[cur.next]` with a `null` `next`.** Use `cur.next?.let { copy[it] }`.
2. **Clone Graph: adding the clone to the map after visiting the neighbours.** A cycle loops forever.
3. **A node class with `equals` based on its value.** Nodes with the same value would share one map entry.
4. **Returning the original head** instead of the copy of the head.
5. **An empty list** (`head == null`).
6. **Trying to connect copies in pass 1**, before they all exist.

#### 6. Say This in the Interview

1. "I use a map from each original node to its copy. Pass 1 creates all copies. Pass 2 connects `next` and `random` using the map."
2. "For a graph, the map is also my visited set, and I add the clone before visiting neighbours."
3. "`O(n)` time and space. There is an `O(1)` space weaving trick if needed."

#### 7. Quick Check

1. Why do we need two passes in Copy List with Random Pointer?
2. In Clone Graph, why add the clone to the map before visiting its neighbours?

<details>
<summary>Answers</summary>

1. A node's `random` may point to a node that comes later. That copy must already exist when you link it.
2. A neighbour may point back to this node. If the clone is not in the map yet, you would clone it again and loop forever.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 138 | Copy List with Random Pointer (Medium) | old → new map |
| 133 | Clone Graph (Medium) | old → clone map |
| 146 | LRU Cache (Medium) | map + doubly linked list (note 25) |
| 141 | Linked List Cycle (Easy) | a set of nodes (or two pointers) |
| 160 | Intersection of Two Linked Lists (Easy) | a set of nodes (or two pointers) |
