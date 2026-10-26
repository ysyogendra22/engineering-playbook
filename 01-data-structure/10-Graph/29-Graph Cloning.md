# Graph Cloning

#### 1. What Is It?

**Graph cloning** means making a **deep copy** of a graph: new node objects with the same values and the same connections. Changing the copy must not change the original.

It is *Clone Graph* (LeetCode 133). Its trick is simple:

> Keep a **map from each original node to its clone**. The map is also your **visited** set.

Why a map?

- A node can be reached from many neighbours. You must create its clone **only once**.
- Graphs have cycles. Without the map you would clone the same nodes forever.

The same idea copies a linked list with random pointers (LeetCode 138).

#### 2. How It Works

Graph: `1 — 2`, `2 — 3`, `3 — 1` (a triangle). Each node stores its neighbours.

```text
clone(1):
   no clone of 1 yet → create 1', put 1 → 1' in the map            (before visiting neighbours!)
   neighbours of 1: 2 and 3
      clone(2): create 2', map 2 → 2'
         neighbours of 2: 1 (already in the map → use 1'), 3
         clone(3): create 3', map 3 → 3'
            neighbours of 3: 2 (in the map → 2'), 1 (in the map → 1')
         ...
```

Two rules:

1. **Put the clone in the map before visiting the neighbours.** Otherwise a cycle sends you back to the same node with no clone yet.
2. **If the node is already in the map, return its clone** without creating a new one.

Works with DFS (recursion) or BFS (queue).

#### 3. Kotlin Code

```kotlin
class Node(var `val`: Int) {
    var neighbors: MutableList<Node> = mutableListOf()
}

// DFS
fun cloneGraph(node: Node?): Node? {
    if (node == null) return null
    val clones = HashMap<Node, Node>()                 // original → clone

    fun dfs(original: Node): Node {
        clones[original]?.let { return it }            // already cloned → reuse it
        val clone = Node(original.`val`)
        clones[original] = clone                       // register BEFORE visiting the neighbours
        for (neighbour in original.neighbors) {
            clone.neighbors.add(dfs(neighbour))
        }
        return clone
    }

    return dfs(node)
}

// BFS
fun cloneGraphBfs(node: Node?): Node? {
    if (node == null) return null
    val clones = HashMap<Node, Node>()
    clones[node] = Node(node.`val`)
    val queue = ArrayDeque<Node>()
    queue.addLast(node)
    while (queue.isNotEmpty()) {
        val original = queue.removeFirst()
        for (neighbour in original.neighbors) {
            if (neighbour !in clones) {
                clones[neighbour] = Node(neighbour.`val`)     // create the clone when first seen
                queue.addLast(neighbour)
            }
            clones.getValue(original).neighbors.add(clones.getValue(neighbour))
        }
    }
    return clones.getValue(node)
}
```

Check: for the triangle `1—2—3—1`, the clone has 3 new nodes, each with 2 neighbours, none of them an original node.

Copy a linked list with random pointers (LeetCode 138) in the same way:

```kotlin
class ListNode(var `val`: Int) { var next: ListNode? = null; var random: ListNode? = null }

fun copyRandomList(head: ListNode?): ListNode? {
    if (head == null) return null
    val copy = HashMap<ListNode, ListNode>()
    var cur: ListNode? = head
    while (cur != null) { copy[cur] = ListNode(cur.`val`); cur = cur.next }     // pass 1: create copies
    cur = head
    while (cur != null) {                                                        // pass 2: connect them
        val c = copy.getValue(cur)
        c.next = cur.next?.let { copy[it] }
        c.random = cur.random?.let { copy[it] }
        cur = cur.next
    }
    return copy[head]
}
```

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Clone Graph | `O(V + E)` | `O(V)` (the map + the recursion or queue) |
| Copy List with Random Pointer | `O(n)` | `O(n)` |

#### 5. Common Mistakes

1. **Adding the clone to the map after visiting the neighbours.** A cycle loops forever.
2. **Creating a new clone for a node that already has one.**
3. **Giving the clone the original's neighbour objects.** That is a shallow copy.
4. **Giving the node class an `equals()` based on the value.** Two different nodes with the same value would share one map entry. Keep identity equality.
5. **Forgetting the empty graph** (`null`).

#### 6. Say This in the Interview

1. "I use a HashMap from each original node to its clone. It also works as my visited set."
2. "I put the clone in the map before visiting the neighbours, so cycles do not cause an infinite loop."
3. "Time `O(V + E)`, space `O(V)`."

#### 7. Quick Check

1. Why do we need the map?
2. When must the clone be stored in the map?

<details>
<summary>Answers</summary>

1. To create each clone only once and to avoid looping forever on cycles.
2. Before visiting the neighbours.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 133 | Clone Graph (Medium) | map original → clone |
| 138 | Copy List with Random Pointer (Medium) | map original → copy |
| 1485 | Clone Binary Tree With Random Pointer (Medium, premium) | map original → clone |
| 1490 | Clone N-ary Tree (Medium, premium) | map original → clone |
