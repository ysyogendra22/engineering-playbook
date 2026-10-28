# Singly Linked List

#### 1. What Is It?

A **singly linked list** is the basic linked list: every node has a `value` and **one** pointer, `next`. You can only move forward.

```text
head → [10] → [20] → [30] → null
```

Interviews ask you to **build one yourself** (*Design Linked List*, LeetCode 707). The goal is to show that you handle pointers and edge cases cleanly.

The best way to build it: keep a **dummy node** before the real head and a **size** counter. Then adding or deleting at index 0 works like any other index.

#### 2. How It Works

Insert `15` at index `1`:

```text
before:   dummy → [10] → [20] → [30]
find the node BEFORE the position: prev = dummy → [10]   (walk `index` steps from the dummy)

new node 15:  15.next = prev.next   (15 → 20)
              prev.next = 15        (10 → 15)

after:    dummy → [10] → [15] → [20] → [30]
```

Delete the node at index `1`:

```text
find prev (the node before index 1): [10]
prev.next = prev.next.next        (10 → 30, skipping 20)
```

Both need the **previous** node. That is why the dummy helps: index 0 also has a "previous" node (the dummy).

#### 3. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (defined in note 01)

// Design Linked List (LeetCode 707)
class MyLinkedList {
    private val dummy = ListNode(0)
    private var size = 0

    fun get(index: Int): Int {
        if (index < 0 || index >= size) return -1
        var cur = dummy.next
        repeat(index) { cur = cur!!.next }
        return cur!!.`val`
    }

    fun addAtHead(value: Int) = addAtIndex(0, value)

    fun addAtTail(value: Int) = addAtIndex(size, value)

    fun addAtIndex(index: Int, value: Int) {
        if (index < 0 || index > size) return
        var prev = dummy
        repeat(index) { prev = prev.next!! }                 // the node before the position
        val node = ListNode(value)
        node.next = prev.next
        prev.next = node
        size++
    }

    fun deleteAtIndex(index: Int) {
        if (index < 0 || index >= size) return
        var prev = dummy
        repeat(index) { prev = prev.next!! }
        prev.next = prev.next!!.next
        size--
    }
}

// Usage
val list = MyLinkedList()
list.addAtHead(1); list.addAtTail(3); list.addAtIndex(1, 2)   // 1 → 2 → 3
println(list.get(1))                                           // 2
list.deleteAtIndex(1)                                          // 1 → 3
println(list.get(1))                                           // 3
```

Kotlin and Java already have `LinkedList`. In interviews you write your own node class.

#### 4. Complexity

| Action | Time | Space |
|---|---|---|
| `get(i)`, `addAtIndex(i)`, `deleteAtIndex(i)` | `O(i)` (walk to the position) | `O(1)` |
| `addAtHead` | `O(1)` | `O(1)` |
| `addAtTail` (no tail pointer) | `O(n)` | `O(1)` |
| `addAtTail` (with a tail pointer) | `O(1)` | `O(1)` |

#### 5. Common Mistakes

1. **Stopping at the node, not the node before it.** To insert or delete you need `prev`.
2. **`index > size` vs `index >= size`.** Adding is valid at `index == size` (the tail). Reading and deleting are not.
3. **Forgetting to update `size`.**
4. **Not using a dummy node,** which makes the head a special case.
5. **Losing the rest of the list** (set `node.next = prev.next` **before** `prev.next = node`).

#### 6. Say This in the Interview

1. "I keep a dummy node and a size counter, so head and tail need no special case."
2. "To insert or delete at an index I walk to the node before it. That is `O(index)`."
3. "Adding at the head is `O(1)`. With a tail pointer, adding at the tail is also `O(1)`."

#### 7. Quick Check

1. In `addAtIndex(0, x)`, which node is `prev`?
2. Which order is correct when inserting `node` after `prev`?

<details>
<summary>Answers</summary>

1. The dummy node.
2. `node.next = prev.next` first, then `prev.next = node`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) (Medium) | this note |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) (Easy) | delete with a dummy |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) (Medium) | copy the next value |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) (Easy) | skip equal nodes |
