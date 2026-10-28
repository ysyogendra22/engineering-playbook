# Find Middle of Linked List

#### 1. What Is It?

Return the **middle node** of a linked list. If the length is even, there are two middle nodes, and the question usually asks for the **second** one.

```text
1 → 2 → 3 → 4 → 5        middle: 3
1 → 2 → 3 → 4            two middles: 2 and 3 → return the second (3)
```

This is *Middle of the Linked List* (LeetCode 876). It is also a **building block**: Palindrome Linked List, Reorder List, Sort List (merge sort) and Delete the Middle Node all start by finding the middle.

#### 2. How It Works

Use **slow and fast pointers** (note 06). `slow` moves 1 step, `fast` moves 2. When `fast` cannot move two more steps, `slow` is in the middle.

```text
1 → 2 → 3 → 4 → 5 → null
slow=1 fast=1
slow=2 fast=3
slow=3 fast=5      fast.next is null → stop. Middle = 3

1 → 2 → 3 → 4 → null
slow=1 fast=1
slow=2 fast=3
slow=3 fast=null   fast is null → stop. Middle = 3 (the second middle)
```

Loop condition: `while (fast != null && fast.next != null)`.

To get the **first** middle for an even length (useful when you want to split the list in two halves): stop one step earlier with `while (fast.next != null && fast.next.next != null)`.

#### 3. Brute Force vs Optimized

| | Brute force | Slow and fast |
|---|---|---|
| Idea | pass 1: count `n`; pass 2: walk `n / 2` steps | one pass |
| Time | `O(n)` (two passes) | `O(n)` (one pass) |
| Space | `O(1)` | `O(1)` |

```kotlin
fun middleNodeTwoPass(head: ListNode?): ListNode? {
    var n = 0
    var cur = head
    while (cur != null) { n++; cur = cur.next }
    cur = head
    repeat(n / 2) { cur = cur!!.next }
    return cur
}
```

Both are `O(n)`. The one-pass version is what interviewers expect, and the idea (two speeds) is reused in cycle detection.

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Middle of the Linked List (LeetCode 876): second middle for an even length
fun middleNode(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
    }
    return slow
}

// First middle (to split a list into two halves)
fun firstMiddle(head: ListNode?): ListNode? {
    if (head == null) return null
    var slow: ListNode = head
    var fast: ListNode = head
    while (fast.next != null && fast.next!!.next != null) {
        slow = slow.next!!
        fast = fast.next!!.next!!
    }
    return slow
}

// Delete the Middle Node of a Linked List (LeetCode 2095)
fun deleteMiddle(head: ListNode?): ListNode? {
    if (head?.next == null) return null              // 0 or 1 node: nothing is left
    var slow: ListNode = head
    var fast = head.next!!.next                      // start fast one step ahead so slow stops BEFORE the middle
    while (fast != null && fast.next != null) {
        slow = slow.next!!
        fast = fast.next!!.next
    }
    slow.next = slow.next!!.next
    return head
}
```

Checks: `middleNode(1→2→3→4→5)` → `3→4→5`. `middleNode(1→2→3→4→5→6)` → `4→5→6`. `deleteMiddle(1→3→4→7→1→2→6)` → `1→3→4→1→2→6`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Slow and fast | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Condition `while (fast.next != null)`** without checking `fast != null`. It crashes on an even-length list.
2. **Returning the wrong middle** for an even length. Read the question.
3. **Not handling an empty list or a single node.**
4. **Deleting the middle:** you need the node **before** the middle. Start `fast` one step ahead.
5. **Forgetting `!!`/null checks** in Kotlin when moving `fast.next.next`.

#### 7. Say This in the Interview

1. "I use slow and fast pointers. When `fast` reaches the end, `slow` is at the middle. One pass, `O(1)` space."
2. "For an even length this returns the second middle. For the first middle I stop one step earlier."

#### 8. Quick Check

1. Which middle does the standard loop return for `1 → 2 → 3 → 4`?
2. How many steps does `fast` take compared with `slow`?

<details>
<summary>Answers</summary>

1. The second middle, `3`.
2. Twice as many.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | this note |
| 2095 | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) (Medium) | stop before the middle |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | middle + reverse (note 13) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) (Medium) | middle + reverse + merge (note 20) |
| 148 | [Sort List](https://leetcode.com/problems/sort-list/) (Medium) | split at the middle, merge sort |
