# Partition Linked List

#### 1. What Is It?

Re-arrange a list **by a rule** while keeping the original order inside each group. Two common questions:

- **Partition List** (LeetCode 86): put all nodes `< x` before nodes `>= x`.
- **Odd Even Linked List** (LeetCode 328): put all nodes at odd positions first, then even positions.

```text
1 → 4 → 3 → 2 → 5 → 2,  x = 3   →   1 → 2 → 2 → 4 → 3 → 5
1 → 2 → 3 → 4 → 5               →   1 → 3 → 5 → 2 → 4
```

The pattern is the same: **build two lists, then join them.**

#### 2. How It Works

1. Make two dummy nodes, one for each group.
2. Walk the list once. Append every node to the group it belongs to.
3. Set the **tail of the second group to `null`** (very important, or you get a cycle).
4. Connect the first group's tail to the second group's head.

```text
1 → 4 → 3 → 2 → 5 → 2,  x = 3

small: 1 → 2 → 2
big:   4 → 3 → 5
join:  1 → 2 → 2 → 4 → 3 → 5
```

No new nodes are created. Existing nodes are re-linked: `O(1)` extra space.

#### 3. Brute Force vs Optimized

| | Brute force | Two dummy lists |
|---|---|---|
| Idea | copy values into two arrays, join them, rebuild a list | re-link the same nodes |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun partitionArray(head: ListNode?, x: Int): ListNode? {
    val small = mutableListOf<Int>()
    val big = mutableListOf<Int>()
    var cur = head
    while (cur != null) {
        if (cur.`val` < x) small.add(cur.`val`) else big.add(cur.`val`)
        cur = cur.next
    }
    val dummy = ListNode(0)
    var tail = dummy
    for (v in small + big) { tail.next = ListNode(v); tail = tail.next!! }
    return dummy.next
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Partition List (LeetCode 86)
fun partition(head: ListNode?, x: Int): ListNode? {
    val smallDummy = ListNode(0)
    val bigDummy = ListNode(0)
    var small = smallDummy
    var big = bigDummy
    var cur = head
    while (cur != null) {
        if (cur.`val` < x) { small.next = cur; small = cur }
        else { big.next = cur; big = cur }
        cur = cur.next
    }
    big.next = null                          // cut, or the list may loop back
    small.next = bigDummy.next               // join
    return smallDummy.next
}

// Odd Even Linked List (LeetCode 328): by position, not by value
fun oddEvenList(head: ListNode?): ListNode? {
    if (head?.next == null) return head
    var odd: ListNode = head
    val evenHead = head.next
    var even = evenHead
    while (even?.next != null) {
        odd.next = even.next
        odd = odd.next!!
        even.next = odd.next
        even = even.next
    }
    odd.next = evenHead
    return head
}
```

Checks: `partition(1→4→3→2→5→2, 3)` → `1→2→2→4→3→5`. `partition(2→1, 2)` → `1→2`. `oddEvenList(1→2→3→4→5)` → `1→3→5→2→4`. `oddEvenList(2→1→3→5→6→4→7)` → `2→3→6→7→1→5→4`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Partition List | `O(n)` | `O(1)` |
| Odd Even Linked List | `O(n)` | `O(1)` |

#### 6. When to Use This Pattern

| You see | Think |
|---|---|
| "put nodes less than x first" | two dummy lists |
| "group by odd/even position" | two pointers building two lists |
| "keep the relative order" | append to the tail of each group (stable) |
| "do it in place" | re-link nodes, do not create new ones |

#### 7. Common Mistakes

1. **Not setting `big.next = null`.** The last big node may still point to a small node: an infinite loop.
2. **Changing `cur.next` while you still need it.** In the code above we only change `small.next` and `big.next` (the tails), so `cur = cur.next` is safe. If you change `cur.next` itself, save it first.
3. **Forgetting the dummy nodes** and writing special cases for the first node.
4. **Mixing up "odd position" and "odd value"** in question 328 (it is position).
5. **Changing the order inside a group.** The question wants it kept.

#### 8. Say This in the Interview

1. "I build two lists with dummy nodes, one for each side, then join them. The order inside each side stays the same."
2. "I set the tail of the second list to `null` to avoid a cycle. `O(n)` time and `O(1)` space."

#### 9. Quick Check

1. Why cut `big.next`?
2. Does Partition List sort the list?

<details>
<summary>Answers</summary>

1. The last big node may still point to a node now in the small list, which creates a cycle.
2. No. It only separates the nodes `< x` from the others and keeps the order inside each group.

</details>

#### 10. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) (Medium) | two dummy lists |
| 328 | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) (Medium) | by position |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) (Easy) | dummy node (note 03) |
| 725 | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/) (Medium) | cut into equal parts |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) | the same idea on an array |
