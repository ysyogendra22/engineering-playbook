# Time & Space Complexity

#### 1. What Is It?

Interviewers always ask: "what is the time and space complexity?". For linked lists the answers follow a few simple rules.

| Operation | Time | Why |
|---|---|---|
| Access the `i`-th node | `O(n)` | walk from the head |
| Search for a value | `O(n)` | check each node |
| Insert / delete at the head | `O(1)` | change one pointer |
| Insert / delete after a node you hold | `O(1)` | change a few pointers |
| Insert / delete at the tail | `O(n)`, or `O(1)` with a tail pointer (insert) | must find the previous node |
| Delete a node by value | `O(n)` | find it first |
| Length | `O(n)` | count the nodes (or keep a `size`) |
| Reverse, find the middle, detect a cycle | `O(n)` | one pass |

Space: the list itself uses `O(n)`. What matters in interviews is the **extra** space of your algorithm.

#### 2. How It Works

Extra space of common solutions:

| Approach | Extra space |
|---|---|
| Walk with pointers (reverse, middle, merge, cycle) | `O(1)` |
| Recursion (reverse recursively, merge recursively) | `O(n)` for the **call stack** |
| Copy into an array or `HashSet` | `O(n)` |
| Dummy node | `O(1)` (one node) |

**Recursion uses stack space.** A recursive reverse of 100,000 nodes makes 100,000 nested calls and can crash with `StackOverflowError`. The iterative version uses `O(1)`.

Array versus linked list:

| | Array | Linked list |
|---|---|---|
| Access by index | `O(1)` | `O(n)` |
| Insert / delete in the middle | `O(n)` (shift) | `O(1)` if you hold the node |
| Memory per item | value only | value + pointer |
| Cache-friendly | yes | no (nodes are scattered) |

Because of caching, arrays are usually faster in practice. Linked lists win when you insert and delete often and already hold the nodes (for example in an LRU cache).

#### 3. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Length: O(n) time, O(1) space
fun lengthIterative(head: ListNode?): Int {
    var count = 0
    var cur = head
    while (cur != null) { count++; cur = cur.next }
    return count
}

// The same with recursion: O(n) time, but O(n) stack space
fun lengthRecursive(head: ListNode?): Int =
    if (head == null) 0 else 1 + lengthRecursive(head.next)

// Insert at the tail: O(n) without a tail pointer
fun insertAtTail(head: ListNode?, value: Int): ListNode {
    val node = ListNode(value)
    if (head == null) return node
    var cur: ListNode = head
    while (cur.next != null) cur = cur.next!!             // walk to the last node
    cur.next = node
    return head
}

// With a tail pointer, the same insert is O(1)
class LinkedListWithTail {
    var head: ListNode? = null
    var tail: ListNode? = null

    fun addLast(value: Int) {
        val node = ListNode(value)
        val last = tail
        if (last == null) { head = node; tail = node } else { last.next = node; tail = node }
    }
}
```

#### 4. Complexity

This whole note is the tables above. The key sentence to remember: **linked lists make insertion fast and access slow; arrays are the opposite.**

#### 5. Common Mistakes

1. **Saying insertion is always `O(1)`.** It is `O(1)` only if you already hold the node.
2. **Forgetting the recursion stack** in the space complexity.
3. **Calling `length` inside a loop** (`O(n²)`). Compute it once, or keep a `size`.
4. **Saying access is `O(1)`** (that is an array).
5. **Ignoring the pointer overhead** when comparing memory.

#### 6. Say This in the Interview

1. "Access is `O(n)` because there is no index. Inserting or deleting after a node I already hold is `O(1)`."
2. "My solution uses two pointers, so the extra space is `O(1)`. A recursive version would use `O(n)` stack space."
3. "I keep a tail pointer so appending is `O(1)`."

#### 7. Quick Check

1. What is the extra space of an iterative reverse?
2. What is the extra space of a recursive reverse of `n` nodes?

<details>
<summary>Answers</summary>

1. `O(1)`.
2. `O(n)`, for the call stack.

</details>

#### 8. Related LeetCode Questions

| # | Question | Complexity point |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | iterative `O(1)` vs recursive `O(n)` space |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | one pass instead of two |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | `O(1)` space instead of a set |
| 707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) (Medium) | cost of each operation |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | `O(1)` operations |
