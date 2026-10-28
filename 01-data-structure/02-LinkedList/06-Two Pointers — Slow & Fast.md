# Two Pointers — Slow & Fast

> The key pattern of this folder. Notes 07, 08, 09, 11 and 12 are all applications of it.

#### 1. What Is It?

You walk the list with **two pointers** at once. There are two shapes:

| Shape | How | Used for |
|---|---|---|
| **Slow and fast** | slow moves 1 step, fast moves 2 steps | middle, cycle detection, cycle start |
| **Gap (fixed distance)** | move one pointer `n` steps ahead, then move both together | n-th node from the end |
| **Switch heads** | two pointers walk two lists, each switches to the other list's head at the end | intersection of two lists |

Why it works: a linked list has no length and no index. Two pointers moving at different speeds (or with a gap) let you find positions in **one pass** with **`O(1)` extra space**.

How to spot it: "middle of the list", "does it have a cycle", "n-th from the end", "intersection", "palindrome".

#### 2. How It Works

**Slow and fast.** When `fast` reaches the end, `slow` is at the middle (because it moved half as far).

```text
1 → 2 → 3 → 4 → 5 → null
start:    slow=1, fast=1
step 1:   slow=2, fast=3
step 2:   slow=3, fast=5      fast.next is null → stop. slow is the middle: 3
```

With a **cycle**, `fast` laps `slow` and they meet inside the cycle. Without a cycle, `fast` reaches `null`.

**Gap.** To find the 2nd node from the end of `1 → 2 → 3 → 4 → 5`:

```text
move fast 2 steps ahead:   fast=3, slow=1
move both until fast is the last node:   fast=5, slow=4
slow is the 2nd from the end: 4
```

The stop condition decides the exact position. Always test it on a list with 1, 2, 3 and 4 nodes.

#### 3. Brute Force vs Optimized

| | Brute force | Two pointers |
|---|---|---|
| Idea | pass 1: count the length; pass 2: walk to the position (or store nodes in a list) | one pass with two pointers |
| Time | `O(n)` (two passes) | `O(n)` (one pass) |
| Space | `O(1)` or `O(n)` | `O(1)` |

```kotlin
fun middleBrute(head: ListNode?): ListNode? {
    val nodes = mutableListOf<ListNode>()
    var cur = head
    while (cur != null) { nodes.add(cur); cur = cur.next }          // O(n) extra space
    return if (nodes.isEmpty()) null else nodes[nodes.size / 2]
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Middle (second middle when the length is even)
fun middleNode(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast?.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
    }
    return slow
}

// Does the list have a cycle?
fun hasCycle(head: ListNode?): Boolean {
    var slow = head
    var fast = head
    while (fast?.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) return true                  // they met inside the cycle
    }
    return false
}

// The n-th node from the end (gap pointer)
fun nthFromEnd(head: ListNode?, n: Int): ListNode? {
    var fast = head
    repeat(n) { fast = fast?.next }                      // move fast n steps ahead
    var slow = head
    while (fast != null) {
        slow = slow!!.next
        fast = fast.next
    }
    return slow
}
```

Checks: `middleNode(1→2→3→4→5)` → node `3`. `middleNode(1→2→3→4)` → node `3`. `nthFromEnd(1→2→3→4→5, 2)` → node `4`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Slow / fast, gap | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Checking only `fast != null`** and then reading `fast.next.next`. Check `fast?.next != null` too.
2. **Starting the pointers at different nodes** by mistake.
3. **Off-by-one in the gap** (move `n` or `n + 1` steps). Test small lists.
4. **Comparing with `==` instead of `===`** when checking if two pointers are the same node.
5. **Even-length lists:** which middle? Read the question.

#### 7. Say This in the Interview

1. "I use two pointers. `fast` moves twice as fast, so when it reaches the end, `slow` is at the middle. One pass, `O(1)` space."
2. "For the n-th from the end I move one pointer `n` steps ahead, then move both together."
3. "I will test with 1, 2, 3 and 4 nodes."

#### 8. Quick Check

1. In a list of 6 nodes, where is `slow` when `fast` finishes?
2. Why does a cycle make `fast` catch `slow`?

<details>
<summary>Answers</summary>

1. At the 4th node (the second middle).
2. Inside the cycle `fast` gains one step on `slow` each round, so it must catch up.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | slow and fast (note 07) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | slow and fast (note 08) |
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy) | switch heads (note 12) |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) | gap pointer (note 11) |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | find the cycle start (note 09) |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | middle + reverse (note 13) |
