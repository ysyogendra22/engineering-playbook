# Merge K Sorted Linked Lists

#### 1. What Is It?

You get `k` sorted linked lists. Merge them into **one sorted list**.

```text
1 → 4 → 5
1 → 3 → 4          →   1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
2 → 6
```

This is *Merge k Sorted Lists* (LeetCode 23), a Hard question asked very often. It is the "Merge Two Sorted Lists" idea (note 10) made bigger. Let `N` be the total number of nodes.

#### 2. How It Works

**Method 1 — Min-heap.** Keep the **current head of every list** in a min-heap.

1. Put the head of each non-empty list in the heap.
2. Take the smallest node out, append it to the result.
3. If that node has a `next`, put `next` in the heap.
4. Repeat until the heap is empty.

The heap never holds more than `k` nodes, so each push or pop costs `O(log k)`.

**Method 2 — Divide and conquer.** Merge the lists in pairs (like merge sort): `k` lists → `k/2` → `k/4` → … → 1. Each "level" touches every node once, and there are `log k` levels.

```text
[L1, L2, L3, L4]  →  [L1+L2, L3+L4]  →  [all]
```

#### 3. Brute Force vs Optimized

| Approach | Time | Space | Note |
|---|---|---|---|
| Put all values in an array, sort, rebuild | `O(N log N)` | `O(N)` | simple, ignores that the lists are sorted |
| Merge one by one (`result = merge(result, list)`) | `O(k · N)` | `O(1)` | the result grows each time |
| **Min-heap** | `O(N log k)` | `O(k)` | the usual answer |
| **Divide and conquer** | `O(N log k)` | `O(log k)` stack | no heap, uses only `merge two` |

```kotlin
fun mergeKListsSort(lists: Array<ListNode?>): ListNode? {
    val values = mutableListOf<Int>()
    for (head in lists) {
        var cur = head
        while (cur != null) { values.add(cur.`val`); cur = cur.next }
    }
    values.sort()
    val dummy = ListNode(0)
    var tail = dummy
    for (v in values) { tail.next = ListNode(v); tail = tail.next!! }
    return dummy.next
}
```

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Method 1: min-heap
fun mergeKLists(lists: Array<ListNode?>): ListNode? {
    val heap = PriorityQueue<ListNode>(compareBy<ListNode> { it.`val` })
    for (head in lists) if (head != null) heap.add(head)

    val dummy = ListNode(0)
    var tail = dummy
    while (heap.isNotEmpty()) {
        val smallest = heap.poll()
        tail.next = smallest                       // reuse the node, no new node
        tail = smallest
        smallest.next?.let { heap.add(it) }        // the next node of that list joins the heap
    }
    return dummy.next
}

// Method 2: divide and conquer
fun mergeKListsDC(lists: Array<ListNode?>): ListNode? {
    fun solve(left: Int, right: Int): ListNode? {
        if (left > right) return null
        if (left == right) return lists[left]
        val mid = (left + right) / 2
        return mergeTwo(solve(left, mid), solve(mid + 1, right))
    }
    return solve(0, lists.size - 1)
}

// Merge Two Sorted Lists (note 10)
fun mergeTwo(a: ListNode?, b: ListNode?): ListNode? {
    val dummy = ListNode(0)
    var tail = dummy
    var x = a
    var y = b
    while (x != null && y != null) {
        if (x.`val` <= y.`val`) { tail.next = x; x = x.next }
        else { tail.next = y; y = y.next }
        tail = tail.next!!
    }
    tail.next = x ?: y
    return dummy.next
}
```

Checks (both methods): `[1→4→5, 1→3→4, 2→6]` → `1→1→2→3→4→4→5→6`. `[]` → `null`. `[null]` → `null`. `[null, 1]` → `1`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Min-heap | `O(N log k)` | `O(k)` |
| Divide and conquer | `O(N log k)` | `O(log k)` (recursion) |
| Merge one by one | `O(k · N)` | `O(1)` |

#### 6. Common Mistakes

1. **Pushing `null` heads** into the heap. Skip empty lists.
2. **Pushing all nodes** into the heap. That is `O(N)` heap space and slower. Push only the current heads.
3. **Using the same `ListNode` comparator wrong** (comparing nodes, not values). Compare `val`.
4. **Merge one by one** and stating `O(N log k)`. It is `O(k · N)`.
5. **Empty array or all-empty lists:** return `null`.
6. **Not moving `tail`.**

#### 7. Say This in the Interview

1. "Brute force: collect and sort, `O(N log N)`. Better: a min-heap of the `k` current heads. Each node is pushed and popped once, so `O(N log k)` time and `O(k)` space."
2. "Alternatively, I merge pairs of lists like merge sort. Same time, and no heap."

#### 8. Quick Check

1. What is the heap size at most?
2. Why is merging one by one slow?

<details>
<summary>Answers</summary>

1. `k` (one node per list).
2. The merged list grows. The first lists are copied over and over: about `k · N` steps in total.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) | the base (note 10) |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) | this note |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) (Medium) | merge sort on a list |
| 378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium) | heap of row heads |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) (Medium) | heap of the next candidates |
