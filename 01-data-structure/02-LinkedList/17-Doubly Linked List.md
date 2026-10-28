# Doubly Linked List

#### 1. What Is It?

In a **doubly linked list** each node has **two** pointers: `prev` (the node before) and `next` (the node after). You can walk **both ways**.

```text
null ⇄ [10] ⇄ [20] ⇄ [30] ⇄ null
```

Why it is used:

- **Delete a node in `O(1)` when you hold it.** It knows its `prev`, so you do not search for the previous node.
- Moving a node to the front or back in `O(1)`. This is the heart of the **LRU cache** (note 25).
- Browser history (back / forward), undo/redo, and music playlists.

The cost is more memory (an extra pointer per node) and more pointers to keep correct.

#### 2. How It Works

Use two **sentinel (dummy) nodes**, `head` and `tail`, that hold no data. Then every real node always has a `prev` and a `next`, and there are no special cases at the ends.

```text
head ⇄ [10] ⇄ [20] ⇄ tail
```

**Insert `15` between `10` and `20`:**

```text
node.prev = a (10);  node.next = b (20)
a.next = node
b.prev = node
→ head ⇄ [10] ⇄ [15] ⇄ [20] ⇄ tail
```

**Remove a node `x`** (you hold `x`):

```text
x.prev.next = x.next
x.next.prev = x.prev
```

That is 2 pointer changes and no search: `O(1)`.

#### 3. Kotlin Code

```kotlin
class DNode(var `val`: Int) {
    var prev: DNode? = null
    var next: DNode? = null
}

class DoublyLinkedList {
    private val head = DNode(0)                    // sentinel
    private val tail = DNode(0)                    // sentinel
    var size = 0
        private set

    init {
        head.next = tail
        tail.prev = head
    }

    fun addFirst(value: Int): DNode = insertAfter(head, value)

    fun addLast(value: Int): DNode = insertAfter(tail.prev!!, value)

    private fun insertAfter(node: DNode, value: Int): DNode {
        val newNode = DNode(value)
        newNode.prev = node
        newNode.next = node.next
        node.next!!.prev = newNode
        node.next = newNode
        size++
        return newNode
    }

    // O(1): remove a node you already hold
    fun remove(node: DNode) {
        node.prev!!.next = node.next
        node.next!!.prev = node.prev
        size--
    }

    fun removeFirst(): Int? {
        val first = head.next
        if (first === tail) return null            // empty
        remove(first!!)
        return first.`val`
    }

    fun removeLast(): Int? {
        val last = tail.prev
        if (last === head) return null
        remove(last!!)
        return last.`val`
    }

    // Move a node to the front in O(1) (used by an LRU cache)
    fun moveToFront(node: DNode) {
        remove(node)
        node.prev = head
        node.next = head.next
        head.next!!.prev = node
        head.next = node
        size++
    }

    fun toList(): List<Int> {
        val result = mutableListOf<Int>()
        var cur = head.next
        while (cur !== tail) { result.add(cur!!.`val`); cur = cur.next }
        return result
    }
}

// Usage
val list = DoublyLinkedList()
list.addLast(10); list.addLast(20); val n = list.addLast(30)
list.moveToFront(n)
println(list.toList())          // [30, 10, 20]
list.removeLast()
println(list.toList())          // [30, 10]
```

#### 4. Complexity

| Action | Singly | Doubly |
|---|---|---|
| Delete a node you hold | `O(n)` (find the previous node) | **`O(1)`** |
| Insert before a node you hold | `O(n)` | `O(1)` |
| Add / remove at the head or tail (with sentinels) | `O(1)` | `O(1)` |
| Walk backwards | not possible | `O(n)` |
| Memory per node | 1 pointer | 2 pointers |

#### 5. Common Mistakes

1. **Updating only one direction** (`next` but not `prev`). The list breaks when you walk backwards.
2. **Wrong order of updates** that loses a pointer. Set the new node's pointers first, then the neighbours'.
3. **No sentinel nodes,** which creates `null` checks at both ends.
4. **Forgetting to update `size`.**
5. **Removing a sentinel** by mistake.
6. **Not handling the empty list** (`head.next === tail`).

#### 6. Say This in the Interview

1. "A doubly linked list lets me delete a node I hold in `O(1)`, because the node knows its previous node."
2. "I use sentinel head and tail nodes, so there are no special cases at the ends."
3. "That is why an LRU cache uses a HashMap plus a doubly linked list."

#### 7. Quick Check

1. How many pointers change when you remove a node from the middle?
2. What does a sentinel node do?

<details>
<summary>Answers</summary>

1. Two (`prev.next` and `next.prev`).
2. It removes the special cases for the first and last node.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | doubly list + HashMap (note 25) |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) | back / forward |
| 641 | [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) (Medium) | two-ended structure |
| 430 | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) (Medium) | prev and child pointers (note 24) |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) (Hard) | lists of equal frequency |
