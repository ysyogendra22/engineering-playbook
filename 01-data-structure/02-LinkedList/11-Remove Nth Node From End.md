# Remove Nth Node From End

#### 1. What Is It?

Delete the **n-th node from the end** of a list in **one pass**.

```text
1 → 2 → 3 → 4 → 5,  n = 2   →   1 → 2 → 3 → 5      (the 2nd from the end is 4)
```

This is *Remove Nth Node From End of List* (LeetCode 19). The trick is a **gap** between two pointers (note 06).

#### 2. How It Works

1. Add a **dummy node** before the head (the node to delete may be the head).
2. Move `fast` **`n` steps** ahead.
3. Move `slow` and `fast` **together** until `fast` is the **last node**.
4. Now `slow` is the node **before** the one to delete. Set `slow.next = slow.next.next`.

```text
dummy → 1 → 2 → 3 → 4 → 5,   n = 2
fast moves 2 steps from the dummy: fast = 2,  slow = dummy
move both until fast.next is null:
   fast=3 slow=1;  fast=4 slow=2;  fast=5 slow=3     fast.next is null → stop
slow = 3 is the node before 4.   3.next = 5   → 1 → 2 → 3 → 5
```

The gap between `slow` and `fast` stays `n`. When `fast` is at the end, `slow` is `n` nodes behind it, right before the target.

If `n` equals the length, the target is the **head**. The dummy node handles this: `slow` stays at the dummy and `dummy.next = head.next`.

#### 3. Brute Force vs Optimized

| | Brute force | Gap pointers |
|---|---|---|
| Idea | pass 1: count the length `L`; pass 2: stop at position `L - n - 1` and delete | one pass |
| Time | `O(L)` (two passes) | `O(L)` (one pass) |
| Space | `O(1)` | `O(1)` |

```kotlin
fun removeNthFromEndTwoPass(head: ListNode?, n: Int): ListNode? {
    var length = 0
    var cur = head
    while (cur != null) { length++; cur = cur.next }
    val dummy = ListNode(0)
    dummy.next = head
    var prev: ListNode = dummy
    repeat(length - n) { prev = prev.next!! }              // walk to the node before the target
    prev.next = prev.next!!.next
    return dummy.next
}
```

Both are `O(L)`. The interviewer's follow-up is "can you do it in one pass?".

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Remove Nth Node From End of List (LeetCode 19)
fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var fast: ListNode? = dummy
    var slow: ListNode = dummy
    repeat(n) { fast = fast!!.next }                   // create a gap of n
    while (fast!!.next != null) {                      // move until fast is the last node
        fast = fast!!.next
        slow = slow.next!!
    }
    slow.next = slow.next!!.next                       // delete the target
    return dummy.next
}

// Rotate List (LeetCode 61): the new tail is (length - k % length) nodes from the start
fun rotateRight(head: ListNode?, k: Int): ListNode? {
    if (head?.next == null || k == 0) return head
    var length = 1
    var tail: ListNode = head
    while (tail.next != null) { tail = tail.next!!; length++ }
    val steps = length - k % length
    if (steps == length) return head                   // k is a multiple of the length: nothing changes
    tail.next = head                                   // make it a circle
    var newTail: ListNode = head
    repeat(steps - 1) { newTail = newTail.next!! }
    val newHead = newTail.next
    newTail.next = null                                // cut the circle
    return newHead
}
```

Checks: `removeNthFromEnd(1→2→3→4→5, 2)` → `1→2→3→5`. `removeNthFromEnd(1, 1)` → `null`. `removeNthFromEnd(1→2, 1)` → `1`. `rotateRight(1→2→3→4→5, 2)` → `4→5→1→2→3`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Two pointers with a gap | `O(L)` | `O(1)` |

#### 6. Common Mistakes

1. **No dummy node.** Deleting the head becomes a special case and often crashes.
2. **Stopping with the wrong condition:** `fast.next != null` leaves `slow` before the target. `fast != null` leaves `slow` on the target (too late).
3. **Gap of `n + 1` vs `n`.** Test with `n = 1` and `n = length`.
4. **`n` larger than the length.** Usually guaranteed not to happen. Ask.
5. **Deleting `slow` itself** instead of `slow.next`.

#### 7. Say This in the Interview

1. "I add a dummy node, move `fast` `n` steps ahead, then move both until `fast` is the last node. Then `slow` is right before the node to delete. One pass, `O(1)` space."
2. "The dummy node covers the case where the head is removed."

#### 8. Quick Check

1. For `1 → 2 → 3` and `n = 3`, which node is removed and where does `slow` stop?
2. Why add a dummy node?

<details>
<summary>Answers</summary>

1. The head (`1`). `slow` stays at the dummy node.
2. So deleting the head works like any other node.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) | this note |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) (Medium) | find the new tail with `k % length` |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | slow and fast |
| 2095 | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) (Medium) | stop before the middle |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy) | pointer trick (note 12) |
