# Linked List Operations

#### 1. What Is It?

The four basic operations: **traversal**, **search**, **insert** and **delete**. Every other linked list solution is built from them.

| Operation | Idea | Time |
|---|---|---|
| **Traversal** | follow `next` from the head until `null` | `O(n)` |
| **Search** | traverse and compare each value | `O(n)` |
| **Insert** at the head | new node points to the old head | `O(1)` |
| **Insert** after a node | new node takes over `prev.next` | `O(1)` (once you hold the node) |
| **Delete** the head | `head = head.next` | `O(1)` |
| **Delete** a node (you hold the previous one) | `prev.next = prev.next.next` | `O(1)` |
| **Delete** by value | find the previous node, then skip | `O(n)` |

Use a **dummy node** for any operation that may change the head.

#### 2. How It Works

Delete all nodes with value `6` from `1 → 6 → 6 → 3` (LeetCode 203):

```text
dummy → 1 → 6 → 6 → 3
prev = dummy, cur = 1
cur=1: keep it → prev = 1, cur = 6
cur=6: remove it → prev.next = cur.next (1 → 6), cur = 6 (the second)
cur=6: remove it → prev.next = cur.next (1 → 3), cur = 3
cur=3: keep it
result: 1 → 3
```

Rule: **only move `prev` when you keep a node.** When you delete, `prev` stays and only `cur` moves.

Delete a node when you are **given only that node** (LeetCode 237): you cannot reach the previous node. So copy the next node's value into this node, and skip the next node.

```text
delete the node 5 in 4 → 5 → 1 → 9:
  copy 1 into this node → 4 → 1 → 1 → 9, then skip the second 1 → 4 → 1 → 9
```

#### 3. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Search
fun contains(head: ListNode?, target: Int): Boolean {
    var cur = head
    while (cur != null) {
        if (cur.`val` == target) return true
        cur = cur.next
    }
    return false
}

// Insert at the head: O(1)
fun insertAtHead(head: ListNode?, value: Int): ListNode {
    val node = ListNode(value)
    node.next = head
    return node                                   // the new head
}

// Remove Linked List Elements (LeetCode 203)
fun removeElements(head: ListNode?, value: Int): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var prev = dummy
    var cur = head
    while (cur != null) {
        if (cur.`val` == value) prev.next = cur.next      // skip it, prev stays
        else prev = cur                                    // keep it, prev moves
        cur = cur.next
    }
    return dummy.next
}

// Delete Node in a Linked List (LeetCode 237): you only get the node itself
fun deleteNode(node: ListNode) {
    node.`val` = node.next!!.`val`
    node.next = node.next!!.next
}

// Remove Duplicates from Sorted List (LeetCode 83)
fun deleteDuplicates(head: ListNode?): ListNode? {
    var cur = head
    while (cur?.next != null) {
        if (cur.`val` == cur.next!!.`val`) cur.next = cur.next!!.next    // skip the duplicate
        else cur = cur.next
    }
    return head
}
```

Checks: `removeElements(1→2→6→3→4→5→6, 6)` → `1→2→3→4→5`. `deleteDuplicates(1→1→2→3→3)` → `1→2→3`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Traversal, search, remove by value | `O(n)` | `O(1)` |
| Insert / delete with the node in hand | `O(1)` | `O(1)` |

#### 5. Common Mistakes

1. **Moving `prev` after a delete.** Only move it when you keep the node.
2. **Deleting the head without a dummy node.** The head changes.
3. **`cur.next.next` when `cur.next` is `null`.**
4. **Using `==` for node identity.** Use `===` when comparing nodes themselves.
5. **Deleting while forgetting to move `cur`** (infinite loop).

#### 6. Say This in the Interview

1. "I use a dummy node because the head may be deleted."
2. "When I delete, `prev` stays and `cur` moves. When I keep a node, both move."
3. "Time `O(n)`, space `O(1)`."

#### 7. Quick Check

1. In Remove Elements, when does `prev` move?
2. Why can't you delete a node you hold from the middle of a list in `O(1)` normally?

<details>
<summary>Answers</summary>

1. Only when the current node is kept.
2. You need the previous node to change its `next`, and a singly linked node cannot reach its previous node. (The copy trick works for non-tail nodes.)

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) (Easy) | delete by value |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) (Easy) | skip equal neighbours |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) (Medium) | copy the next value |
| 82 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) (Medium) | remove all copies, dummy node |
| 1290 | [Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) (Easy) | traversal |
