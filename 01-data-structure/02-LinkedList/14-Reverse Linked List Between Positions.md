# Reverse Linked List Between Positions

#### 1. What Is It?

Reverse only the part of the list from position `left` to position `right` (1-based). The rest stays.

```text
1 → 2 → 3 → 4 → 5,  left = 2, right = 4   →   1 → 4 → 3 → 2 → 5
```

This is *Reverse Linked List II* (LeetCode 92). It is a very common Medium question because it mixes finding a position with reversing, and the head may change (when `left = 1`).

#### 2. How It Works

Use a **dummy node** and the **head insertion** method:

1. Walk `prev` to the node **just before** position `left`.
2. `cur` is the node at position `left`. It will end up as the **tail** of the reversed part.
3. Repeat `right − left` times: take the node **after `cur`** and **move it to the front** of the reversed part (right after `prev`).

```text
1 → 2 → 3 → 4 → 5     left=2, right=4
prev = 1,  cur = 2

round 1: move = 3 (cur.next)
   cur.next = move.next      (2 → 4)
   move.next = prev.next     (3 → 2)
   prev.next = move          (1 → 3)
   list: 1 → 3 → 2 → 4 → 5

round 2: move = 4
   cur.next = move.next      (2 → 5)
   move.next = prev.next     (4 → 3)
   prev.next = move          (1 → 4)
   list: 1 → 4 → 3 → 2 → 5   ✓
```

`cur` never moves. It stays as the tail of the reversed section, and every other node is pulled to the front.

#### 3. Brute Force vs Optimized

| | Brute force | Head insertion |
|---|---|---|
| Idea | copy the values to an array, reverse that part, rebuild or rewrite | re-link nodes in one pass |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun reverseBetweenArray(head: ListNode?, left: Int, right: Int): ListNode? {
    val nodes = mutableListOf<ListNode>()
    var cur = head
    while (cur != null) { nodes.add(cur); cur = cur.next }
    var l = left - 1
    var r = right - 1
    while (l < r) {                                      // swap the VALUES in the range
        val t = nodes[l].`val`; nodes[l].`val` = nodes[r].`val`; nodes[r].`val` = t
        l++; r--
    }
    return head
}
```

Changing values is quick but some interviewers do not allow it. Re-linking nodes is the safer answer.

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Reverse Linked List II (LeetCode 92)
fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
    if (head == null || left == right) return head
    val dummy = ListNode(0)
    dummy.next = head
    var prev: ListNode = dummy
    repeat(left - 1) { prev = prev.next!! }              // the node before position left
    val cur = prev.next!!                                // the node at position left (becomes the tail)
    repeat(right - left) {
        val move = cur.next!!                            // the node to pull to the front
        cur.next = move.next
        move.next = prev.next
        prev.next = move
    }
    return dummy.next
}

// Swap Nodes in Pairs (LeetCode 24): reverse every group of 2
fun swapPairs(head: ListNode?): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var prev: ListNode = dummy
    while (prev.next?.next != null) {
        val first = prev.next!!
        val second = first.next!!
        first.next = second.next                         // first → third
        second.next = first                              // second → first
        prev.next = second                               // prev → second
        prev = first                                     // first is now the tail of the swapped pair
    }
    return dummy.next
}
```

Checks: `reverseBetween(1→2→3→4→5, 2, 4)` → `1→4→3→2→5`. `reverseBetween(5, 1, 1)` → `5`. `reverseBetween(3→5, 1, 2)` → `5→3`. `swapPairs(1→2→3→4)` → `2→1→4→3`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Reverse between positions | `O(n)` (one pass) | `O(1)` |

#### 6. Common Mistakes

1. **No dummy node.** If `left = 1`, the head changes.
2. **Moving `cur`.** In the head-insertion method `cur` stays; only `prev.next` changes.
3. **Wrong order of the three pointer changes.** Save with `cur.next = move.next` **first**.
4. **Off-by-one in positions** (1-based). `prev` moves `left − 1` times.
5. **`left == right`:** nothing to do.
6. **Positions beyond the length.** Usually guaranteed valid. Ask.

#### 7. Say This in the Interview

1. "I use a dummy node. I find the node before position `left`, then pull the next node to the front of the section `right − left` times. One pass, `O(1)` space."
2. "`cur` stays as the tail of the reversed part."

#### 8. Quick Check

1. How many pull-to-front rounds for `left = 2`, `right = 5`?
2. What does `prev` point to when the reversal is finished?

<details>
<summary>Answers</summary>

1. `5 − 2 = 3`.
2. The new first node of the reversed section (the old node at `right`).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | reverse everything (note 05) |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (Medium) | this note |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Medium) | groups of 2 |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard) | groups of `k` (note 15) |
| 1721 | [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) (Medium) | swap the k-th from each end |
