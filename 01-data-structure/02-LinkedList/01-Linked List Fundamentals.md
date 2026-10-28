# Linked List Fundamentals

> Start here. Linked list questions are short to state but easy to get wrong because of pointers. Almost every question uses one of about 8 patterns, and this folder teaches them in order.

#### 1. What Is a Linked List?

A **linked list** is a chain of **nodes**. Each node stores a **value** and a **pointer** (a reference) to the **next** node. The last node points to `null`.

```text
head → [ 1 | • ] → [ 2 | • ] → [ 3 | • ] → null
```

- You only keep the **head** (the first node). To reach other nodes, you follow the `next` pointers.
- Nodes are **not** stored next to each other in memory, so there is **no index**.

Why it is used: **inserting and deleting** is cheap when you already hold the node (just change pointers, nothing shifts). It is the base of stacks, queues, LRU caches and hash table chains.

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Node** | one item: a value and a `next` pointer |
| **Head** | the first node |
| **Tail** | the last node (its `next` is `null`) |
| **Pointer / reference** | a link to another node |
| **Singly linked** | each node has `next` only |
| **Doubly linked** | each node has `prev` and `next` |
| **Circular** | the last node points back to the head |
| **Dummy node** | a fake node placed before the head, to avoid special cases |

#### 3. How It Works

Array versus linked list:

| | Array | Linked list |
|---|---|---|
| Access item `i` | `O(1)` | `O(n)` (walk from the head) |
| Insert / delete at the front | `O(n)` (shift) | `O(1)` |
| Insert / delete after a known node | `O(n)` | `O(1)` |
| Search | `O(n)` | `O(n)` |
| Memory | compact | extra pointer per node |

To visit every node you walk with a pointer:

```text
cur = head
while cur != null:
    use cur.value
    cur = cur.next
```

The two golden rules of linked list code:

1. **Never lose a node.** Save `cur.next` **before** you change `cur.next`.
2. **Always think about `null`:** an empty list, a one-node list, the end of the list.

#### 4. Kotlin Code

```kotlin
// The node used in all notes of this folder
class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

// Helpers to build and print lists (use them to test your solutions)
fun makeList(vararg values: Int): ListNode? {
    val dummy = ListNode(0)
    var tail = dummy
    for (v in values) {
        tail.next = ListNode(v)
        tail = tail.next!!
    }
    return dummy.next
}

fun ListNode?.toValues(): List<Int> {
    val result = mutableListOf<Int>()
    var cur = this
    while (cur != null) {
        result.add(cur.`val`)
        cur = cur.next
    }
    return result
}

// Usage
val head = makeList(1, 2, 3)
println(head.toValues())              // [1, 2, 3]

// Traversal and length
fun length(head: ListNode?): Int {
    var count = 0
    var cur = head
    while (cur != null) { count++; cur = cur.next }
    return count
}
```

A **dummy node** removes the "what if the head changes?" problem. You build or edit the list after the dummy, and return `dummy.next`.

#### 5. How to Spot a Linked List Pattern

| If the question says... | Think... | Note |
|---|---|---|
| reverse (all, part, groups of `k`) | three pointers `prev` / `cur` / `next` | 05, 14, 15 |
| middle, "n-th from the end", cycle, intersection | slow and fast pointers | 06–09, 11, 12 |
| merge sorted lists | dummy node + two pointers | 10, 23 |
| palindrome | middle + reverse the second half | 13 |
| rearrange (partition, reorder, odd-even) | split into pieces and join | 19, 20 |
| add numbers stored as lists | dummy node + carry | 21 |
| copy / clone with random pointers | HashMap or weaving | 22 |
| cache with fast get / put | doubly linked list + HashMap | 17, 25 |
| remove a node / the head may change | dummy node | 03, 11 |

#### 6. Complexity

| Action | Time |
|---|---|
| Access by position | `O(n)` |
| Insert / delete at the head | `O(1)` |
| Insert / delete after a known node | `O(1)` |
| Search, length | `O(n)` |
| Memory | `O(n)` |

#### 7. Common Mistakes

1. **Losing the rest of the list** by overwriting `next` before saving it.
2. **`NullPointerException`** from `cur.next.next` when `cur.next` is `null`. Check first.
3. **Not handling an empty list or a one-node list.**
4. **Forgetting that the head can change** (deleting the head, reversing). Use a dummy node.
5. **Creating a cycle by accident** (the old tail still points to something).
6. **Comparing nodes with `==` instead of `===`** when you mean "the same node" (`===` is identity).

#### 8. Say This in the Interview

1. "Let me confirm: is it singly or doubly linked? Can it have a cycle? Can it be empty?"
2. "I will use a dummy node so the head needs no special case."
3. "I will use two pointers, so the time is `O(n)` and the extra space is `O(1)`."

#### 9. Quick Check

1. What is the time to get the 5th node in a linked list?
2. Why save `cur.next` before changing `cur.next`?

<details>
<summary>Answers</summary>

1. `O(n)`. You walk from the head.
2. Once you overwrite `cur.next`, the rest of the list is lost.

</details>

#### 10. Related LeetCode Questions (Easy → Medium)

Solve them in this order. Search by title if a link looks wrong.

**Start here — Easy**

| # | Question | Main idea | Note |
|---|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | `prev` / `cur` / `next` | 05 |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | dummy + two pointers | 10 |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | slow and fast | 08 |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | slow and fast | 07 |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | switch heads | 12 |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | middle + reverse | 13 |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | dummy node | 03 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | gap of `n` | 11 |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Floyd phase 2 | 09 |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | carry | 21 |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | reverse a part | 14 |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | middle + reverse + merge | 20 |
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | map or weave | 22 |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | two lists | 19 |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | doubly list + map | 25 |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) | merge sort | 10 |

**Hard — these separate strong candidates**

| # | Question | Main idea | Note |
|---|---|---|---|
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | reverse `k` at a time | 15 |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | heap or divide and conquer | 23 |

**If you have little time, do these 8 first:** 206, 21, 141, 142, 19, 2, 143, 146.

For one-page revision, read the **Linked List Cheat Sheet** (note 99).
