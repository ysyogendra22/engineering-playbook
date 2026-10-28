# Reverse Nodes in K-Group

> A famous Hard question. It looks scary, but it is "reverse a list" repeated, with careful connecting.

#### 1. What Is It?

Reverse the nodes of the list **`k` at a time**. If fewer than `k` nodes remain at the end, **leave them as they are**.

```text
1 → 2 → 3 → 4 → 5,  k = 2   →   2 → 1 → 4 → 3 → 5
1 → 2 → 3 → 4 → 5,  k = 3   →   3 → 2 → 1 → 4 → 5
```

This is *Reverse Nodes in k-Group* (LeetCode 25). You may only change the pointers, not the values, and extra space should be `O(1)`.

#### 2. How It Works

Handle one group at a time with a **dummy node** and a pointer `groupPrev` (the node just before the group):

1. Find the **k-th node** of the group (`kth`). If it does not exist (fewer than `k` nodes left), stop.
2. Remember `groupNext = kth.next` (the first node after the group).
3. **Reverse** the `k` nodes. While reversing, make the first node point to `groupNext`. (Start `prev` at `groupNext`.)
4. Connect: `groupPrev.next = kth` (the new first node of the group). The old first node is now the **tail** of the group, so it becomes the next `groupPrev`.

```text
1 → 2 → 3 → 4 → 5,  k = 2

group 1: groupPrev = dummy;  kth = 2;  groupNext = 3;  oldFirst = 1
   reverse (1, 2) with prev starting at 3:   2 → 1 → 3
   dummy.next = 2          dummy → 2 → 1 → 3 → 4 → 5
   groupPrev = oldFirst = 1

group 2: kth = 4;  groupNext = 5;  oldFirst = 3
   reverse (3, 4):  4 → 3 → 5
   1.next = 4              dummy → 2 → 1 → 4 → 3 → 5
   groupPrev = 3

group 3: from 3, the next 2 nodes are 5 and null → fewer than k → stop

result: 2 → 1 → 4 → 3 → 5
```

#### 3. Brute Force vs Optimized

| | Brute force | Pointer reversal |
|---|---|---|
| Idea | copy values into a list, reverse each chunk of `k`, write back | reverse each group by re-linking |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun reverseKGroupArray(head: ListNode?, k: Int): ListNode? {
    val nodes = mutableListOf<ListNode>()
    var cur = head
    while (cur != null) { nodes.add(cur); cur = cur.next }
    var start = 0
    while (start + k <= nodes.size) {
        var l = start
        var r = start + k - 1
        while (l < r) {                                           // swap the values inside the chunk
            val t = nodes[l].`val`; nodes[l].`val` = nodes[r].`val`; nodes[r].`val` = t
            l++; r--
        }
        start += k
    }
    return head
}
```

It changes values, which the question forbids. Use it only to explain your thinking.

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Reverse Nodes in k-Group (LeetCode 25)
fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var groupPrev: ListNode = dummy

    while (true) {
        // 1. find the k-th node of this group
        var kth: ListNode? = groupPrev
        repeat(k) { kth = kth?.next }
        val end = kth ?: break                                    // fewer than k nodes left: stop

        val groupNext = end.next                                   // 2. the first node after the group
        val oldFirst = groupPrev.next!!                            //    it will become the tail

        // 3. reverse the group; the first node ends up pointing to groupNext
        var prev: ListNode? = groupNext
        var cur: ListNode? = oldFirst
        while (cur !== groupNext) {
            val next = cur!!.next
            cur.next = prev
            prev = cur
            cur = next
        }

        // 4. connect the previous part to the new head of the group
        groupPrev.next = end
        groupPrev = oldFirst
    }
    return dummy.next
}
```

Checks: `reverseKGroup(1→2→3→4→5, 2)` → `2→1→4→3→5`. `reverseKGroup(1→2→3→4→5, 3)` → `3→2→1→4→5`. `reverseKGroup(1→2, 1)` → `1→2`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Iterative, group by group | `O(n)` | `O(1)` |
| Recursive version | `O(n)` | `O(n / k)` stack |

#### 6. Common Mistakes

1. **Reversing a last group that has fewer than `k` nodes.** Check that the k-th node exists first.
2. **Losing `groupNext`** before reversing.
3. **Not connecting the previous group** to the new head (`groupPrev.next = end`).
4. **Using the wrong node as the next `groupPrev`.** It must be the **old first** node (now the group's tail).
5. **No dummy node,** so the head of the whole list is a special case.
6. **Starting `prev` as `null`** inside a group. Start it as `groupNext`, so the group's tail links to the rest.
7. **`k = 1`:** nothing changes (it works).

#### 7. Say This in the Interview

1. "For each group I check that `k` nodes exist, remember the node after the group, reverse the group with `prev` starting at that node, and connect it to the previous part. The old first node becomes the tail and the next `groupPrev`."
2. "One pass, `O(n)` time and `O(1)` space."

#### 8. Quick Check

1. What if only 2 nodes remain and `k = 3`?
2. Which node is the next `groupPrev`?

<details>
<summary>Answers</summary>

1. The loop stops and those 2 nodes stay in the same order.
2. The old first node of the group you just reversed (it is now the group's tail).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | the base (note 05) |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (Medium) | one section (note 14) |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Medium) | `k = 2` |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard) | this note |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) (Medium) | another pointer re-linking task |
