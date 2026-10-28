# Reorder Linked List

> This question uses **three tools in a row**: find the middle, reverse a list, merge two lists. Interviewers love it because it checks all three.

#### 1. What Is It?

Re-arrange `L0 → L1 → L2 → … → Ln` into `L0 → Ln → L1 → Ln−1 → L2 → …` (first, last, second, second-last, …). Change the **nodes**, not the values.

```text
1 → 2 → 3 → 4 → 5   →   1 → 5 → 2 → 4 → 3
1 → 2 → 3 → 4       →   1 → 4 → 2 → 3
```

This is *Reorder List* (LeetCode 143).

#### 2. How It Works

1. **Find the middle** with slow and fast pointers (note 07).
2. **Reverse the second half** (note 05) and cut the first half there.
3. **Interleave** the two halves: one node from the first half, one from the reversed second half.

```text
1 → 2 → 3 → 4 → 5

1. middle = 3
2. first half:  1 → 2 → 3      second half reversed:  5 → 4
3. take 1, then 5, then 2, then 4, then 3
   1 → 5 → 2 → 4 → 3   ✓
```

The first half is the same size or one node longer than the second half, so the loop can run until the second half ends.

#### 3. Brute Force vs Optimized

| | Brute force | Middle + reverse + merge |
|---|---|---|
| Idea | put all nodes in an array and link with two pointers (front and back) | three steps, in place |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun reorderListArray(head: ListNode?) {
    val nodes = mutableListOf<ListNode>()
    var cur = head
    while (cur != null) { nodes.add(cur); cur = cur.next }
    var l = 0
    var r = nodes.size - 1
    while (l < r) {
        nodes[l].next = nodes[r]
        l++
        if (l == r) break
        nodes[r].next = nodes[l]
        r--
    }
    if (nodes.isNotEmpty()) nodes[l].next = null
}
```

This is a good first answer. Then say "I can do it in `O(1)` space with three steps".

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

private fun reverse(head: ListNode?): ListNode? {
    var prev: ListNode? = null
    var cur = head
    while (cur != null) {
        val next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    }
    return prev
}

// Reorder List (LeetCode 143): changes the list in place
fun reorderList(head: ListNode?) {
    if (head?.next == null) return

    // 1. find the middle (the first middle for an even length)
    var slow: ListNode = head
    var fast: ListNode? = head
    while (fast?.next != null && fast.next!!.next != null) {
        slow = slow.next!!
        fast = fast.next!!.next
    }

    // 2. reverse the second half and cut the first half
    var second = reverse(slow.next)
    slow.next = null

    // 3. interleave
    var first: ListNode? = head
    while (second != null) {
        val firstNext = first!!.next
        val secondNext = second.next
        first.next = second
        second.next = firstNext
        first = firstNext
        second = secondNext
    }
}
```

Checks: `1→2→3→4→5` becomes `1→5→2→4→3`. `1→2→3→4` becomes `1→4→2→3`. `1→2` stays `1→2`.

Trace for `1→2→3→4`: middle is `2`; second half `3→4` reversed is `4→3`; first half `1→2`. Interleave: `1→4`, then `4→2`, then `2→3`. Result `1→4→2→3`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Three steps | `O(n)` | `O(1)` |
| Array version | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Not cutting the first half** (`slow.next = null`). The last node still points into the second half and creates a cycle.
2. **Using the wrong middle.** For an even length use the first middle, so the first half has the extra node or the halves are equal.
3. **Losing `next` pointers** in the interleave. Save both `next` values before re-linking.
4. **Returning something.** The function changes the list in place and returns nothing.
5. **Edge cases:** one node, two nodes.

#### 7. Say This in the Interview

1. "Reorder List is three known steps: find the middle, reverse the second half, merge the two halves alternately. All in place, `O(n)` time, `O(1)` space."
2. "I cut the list at the middle first, so there is no cycle."

#### 8. Quick Check

1. What does the second half look like before the interleave for `1→2→3→4→5`?
2. Why cut the first half?

<details>
<summary>Answers</summary>

1. `5→4` (the nodes `4→5` reversed). The first half is `1→2→3`.
2. Otherwise node `3` still points to `4`, and the final list may loop.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | step 1 (note 07) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | step 2 (note 05) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) | step 3 is a similar merge (note 10) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) (Medium) | this note |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | middle + reverse (note 13) |
