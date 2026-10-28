# Merge Two Sorted Linked Lists

#### 1. What Is It?

Given two **sorted** linked lists, join them into **one sorted list** by **re-linking the existing nodes** (no new nodes needed).

```text
1 → 2 → 4
1 → 3 → 4
merged: 1 → 1 → 2 → 3 → 4 → 4
```

This is *Merge Two Sorted Lists* (LeetCode 21). It is the "merge" step of **merge sort** (*Sort List*, LeetCode 148) and the base of *Merge k Sorted Lists*.

#### 2. How It Works

Use a **dummy node** and a `tail` pointer. Compare the two current nodes. Attach the **smaller** one to `tail`, and move that list forward. When one list ends, attach the rest of the other.

```text
a: 1 → 2 → 4      b: 1 → 3 → 4      dummy → (tail)

compare 1 and 1 → take a's 1     dummy → 1(a)        a at 2
compare 2 and 1 → take b's 1     dummy → 1 → 1(b)    b at 3
compare 2 and 3 → take a's 2     ... → 2             a at 4
compare 4 and 3 → take b's 3     ... → 3             b at 4
compare 4 and 4 → take a's 4     ... → 4             a ends
attach the rest of b (4)         ... → 4

result: 1 → 1 → 2 → 3 → 4 → 4
```

The dummy node means you never need a special case for "which list gives the first node?".

**Recursive** version: the smaller head becomes the head of the answer, and its `next` is the merge of the rest.

#### 3. Brute Force vs Optimized

| | Brute force | Merge with pointers |
|---|---|---|
| Idea | collect all values, sort, build a new list | compare the heads and re-link |
| Time | `O((m + n) log(m + n))` | `O(m + n)` |
| Space | `O(m + n)` | `O(1)` (iterative) |

```kotlin
fun mergeTwoListsBrute(a: ListNode?, b: ListNode?): ListNode? {
    val values = mutableListOf<Int>()
    var cur = a
    while (cur != null) { values.add(cur.`val`); cur = cur.next }
    cur = b
    while (cur != null) { values.add(cur.`val`); cur = cur.next }
    values.sort()
    val dummy = ListNode(0)
    var tail = dummy
    for (v in values) { tail.next = ListNode(v); tail = tail.next!! }
    return dummy.next
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Merge Two Sorted Lists (LeetCode 21): iterative, O(1) space
fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
    val dummy = ListNode(0)
    var tail = dummy
    var a = list1
    var b = list2
    while (a != null && b != null) {
        if (a.`val` <= b.`val`) { tail.next = a; a = a.next }
        else { tail.next = b; b = b.next }
        tail = tail.next!!
    }
    tail.next = a ?: b                              // attach whatever is left
    return dummy.next
}

// Recursive version
fun mergeTwoListsRecursive(a: ListNode?, b: ListNode?): ListNode? {
    if (a == null) return b
    if (b == null) return a
    return if (a.`val` <= b.`val`) {
        a.next = mergeTwoListsRecursive(a.next, b)
        a
    } else {
        b.next = mergeTwoListsRecursive(a, b.next)
        b
    }
}

// Sort List (LeetCode 148): merge sort on a linked list, O(n log n) time
fun sortList(head: ListNode?): ListNode? {
    if (head?.next == null) return head
    var slow: ListNode = head
    var fast = head.next                             // start fast one ahead so slow stops at the first middle
    while (fast != null && fast.next != null) {
        slow = slow.next!!
        fast = fast.next!!.next
    }
    val second = slow.next
    slow.next = null                                 // cut the list in two
    return mergeTwoLists(sortList(head), sortList(second))
}
```

Checks: `mergeTwoLists(1→2→4, 1→3→4)` → `1→1→2→3→4→4`. `mergeTwoLists(null, 0)` → `0`. `sortList(4→2→1→3)` → `1→2→3→4`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Iterative merge | `O(m + n)` | `O(1)` |
| Recursive merge | `O(m + n)` | `O(m + n)` stack |
| Sort List (merge sort) | `O(n log n)` | `O(log n)` stack |

#### 6. Common Mistakes

1. **Forgetting to attach the rest** of the longer list.
2. **Not moving `tail`** after attaching a node.
3. **No dummy node,** which makes the first node a special case.
4. **Creating new nodes** when re-linking is enough (more memory).
5. **Using `<` vs `<=`** inconsistently (matters only for stability).
6. **Sort List: not cutting the list** (`slow.next = null`) before the recursive calls, which loops forever.

#### 7. Say This in the Interview

1. "I use a dummy node and a tail pointer. At each step I attach the smaller head and move that list forward. When one list ends, I attach the rest of the other. `O(m + n)` time and `O(1)` space."
2. "This is the merge step of merge sort, so a linked list can be sorted in `O(n log n)`."

#### 8. Quick Check

1. What does `tail.next = a ?: b` do?
2. Why is merge sort a good sort for linked lists?

<details>
<summary>Answers</summary>

1. It attaches the remaining nodes of whichever list is not finished.
2. Merging needs only pointer changes, no random access and no extra array.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) | this note |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy) | the same idea on arrays |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) (Medium) | split + merge |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) | heap or divide and conquer (note 23) |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) (Medium) | two lists joined (note 19) |
