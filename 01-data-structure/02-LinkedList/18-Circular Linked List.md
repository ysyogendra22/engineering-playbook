# Circular Linked List

#### 1. What Is It?

In a **circular linked list** the **last node points back to the first node**, so there is no `null` at the end.

```text
head → [1] → [2] → [3] ─┐
        ↑               │
        └───────────────┘
```

Why it appears in interviews:

- **Round-robin** tasks and "go around the circle" games (the Josephus problem).
- **Rotate List**: connect the tail to the head, then cut at the right place.
- It shows that you handle the stop condition properly: you stop when you come **back to the start**, not at `null`.

#### 2. How It Works

**Traversal.** Start at the head and stop when you return to it:

```text
cur = head
do:
    use cur.value
    cur = cur.next
while cur != head
```

(Use a `do ... while`, because the first node must be visited before the check.)

**Make a list circular:** walk to the tail and set `tail.next = head`.

**Rotate List** (LeetCode 61) using this idea: connect the tail to the head, walk to the new tail (`length − k % length` steps from the head), then cut the circle after it.

```text
1 → 2 → 3 → 4 → 5,  k = 2
tail.next = head   (a circle)
new tail is at (5 − 2) = 3 steps from the head: node 3
new head = node 3's next = 4;  cut: 3.next = null
result: 4 → 5 → 1 → 2 → 3
```

**Josephus problem** (*Find the Winner of the Circular Game*, LeetCode 1823): `n` friends in a circle; count `k`, remove that friend, and continue from the next one. Simulate it with a queue (rotate `k − 1` times, remove the next) or a circular list.

#### 3. Brute Force vs Optimized

| | Brute force | Better |
|---|---|---|
| Rotate by `k` | rotate one step at a time, `k` times: `O(n · k)` | circle + one cut: `O(n)` |
| Josephus | simulate with a queue: `O(n · k)` | a math formula: `O(n)` (advanced) |

```kotlin
fun rotateRightBrute(head: ListNode?, k: Int): ListNode? {
    if (head?.next == null) return head
    var result: ListNode = head
    repeat(k) {                                          // move the last node to the front, k times
        var prev: ListNode = result
        while (prev.next!!.next != null) prev = prev.next!!
        val last = prev.next!!
        prev.next = null
        last.next = result
        result = last
    }
    return result
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Traverse a circular list once
fun circularToList(head: ListNode?): List<Int> {
    if (head == null) return emptyList()
    val result = mutableListOf<Int>()
    var cur: ListNode = head
    do {
        result.add(cur.`val`)
        cur = cur.next!!
    } while (cur !== head)
    return result
}

// Rotate List (LeetCode 61)
fun rotateRight(head: ListNode?, k: Int): ListNode? {
    if (head?.next == null || k == 0) return head
    var length = 1
    var tail: ListNode = head
    while (tail.next != null) { tail = tail.next!!; length++ }
    val steps = length - k % length
    if (steps == length) return head                      // k is a multiple of the length
    tail.next = head                                      // make it circular
    var newTail: ListNode = head
    repeat(steps - 1) { newTail = newTail.next!! }
    val newHead = newTail.next
    newTail.next = null                                   // cut the circle
    return newHead
}

// Find the Winner of the Circular Game (LeetCode 1823): simulate with a queue
fun findTheWinner(n: Int, k: Int): Int {
    val queue = ArrayDeque<Int>()
    for (i in 1..n) queue.addLast(i)
    while (queue.size > 1) {
        repeat(k - 1) { queue.addLast(queue.removeFirst()) }   // count k - 1 friends past
        queue.removeFirst()                                      // the k-th friend leaves
    }
    return queue.first()
}
```

Checks: `rotateRight(1→2→3→4→5, 2)` → `4→5→1→2→3`. `rotateRight(0→1→2, 4)` → `2→0→1`. `findTheWinner(5, 2)` → `3`. `findTheWinner(6, 5)` → `1`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Traverse a circular list | `O(n)` | `O(1)` |
| Rotate List | `O(n)` | `O(1)` |
| Josephus with a queue | `O(n · k)` | `O(n)` |

#### 6. Common Mistakes

1. **Looping forever** because you stop at `null`, which never comes in a circle.
2. **Using `while (cur != head)` from the start.** It never runs. Use `do ... while`.
3. **Forgetting to cut the circle** when you turn it back into a normal list (`newTail.next = null`).
4. **`k` bigger than the length.** Use `k % length`.
5. **An empty list or a one-node list** (a single node points to itself).

#### 7. Say This in the Interview

1. "A circular list has no `null` end, so I stop when I return to the head. I use a `do ... while`."
2. "For Rotate List I connect the tail to the head, walk to the new tail, and cut. That is `O(n)` time and `O(1)` space."

#### 8. Quick Check

1. How do you know a traversal of a circular list is finished?
2. After `tail.next = head`, what must you do before returning the answer?

<details>
<summary>Answers</summary>

1. You have come back to the starting node.
2. Cut the circle at the new tail (`newTail.next = null`).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) (Medium) | circle + cut |
| 1823 | [Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) (Medium) | Josephus |
| 708 | [Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) (Medium, premium) | find the insert place |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | detect a loop (note 08) |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) (Medium) | circular array with `% n` |
