# Cycle Detection — Floyd's Algorithm

> Asked very often. The "tortoise and hare" idea is also used for Find the Duplicate Number and Happy Number.

#### 1. What Is It?

A **cycle** in a linked list means some node's `next` points back to an earlier node, so walking forward never reaches `null`.

```text
1 → 2 → 3 → 4
        ↑   ↓
        6 ← 5          (6 points back to 3)
```

**Floyd's algorithm** (the tortoise and the hare) detects it with two pointers:

- `slow` moves 1 step at a time.
- `fast` moves 2 steps at a time.
- If there is **no cycle**, `fast` reaches `null`.
- If there **is** a cycle, `fast` enters it and eventually **meets** `slow` inside it.

#### 2. How It Works

Why they must meet: inside the cycle, each round `fast` gets **one step closer** to `slow` (it moves 2, `slow` moves 1). The gap shrinks by 1 each round, so it reaches 0. They cannot jump over each other.

```text
list: 1 → 2 → 3 → 4 → 2 (4 points back to 2)

start:  slow=1, fast=1
step 1: slow=2, fast=3
step 2: slow=3, fast=2       (3 → 4 → 2)
step 3: slow=4, fast=4       slow === fast → cycle!
```

If `fast` or `fast.next` becomes `null`, the list ends, so there is no cycle.

Compare the options:

| Way | Time | Space |
|---|---|---|
| `HashSet` of visited nodes | `O(n)` | `O(n)` |
| **Floyd (slow / fast)** | `O(n)` | `O(1)` |

#### 3. Brute Force vs Optimized

| | Brute force | Floyd |
|---|---|---|
| Idea | remember every visited node in a set | two pointers at different speeds |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun hasCycleSet(head: ListNode?): Boolean {
    val seen = HashSet<ListNode>()                    // ListNode has no equals(), so this compares identity
    var cur = head
    while (cur != null) {
        if (!seen.add(cur)) return true               // seen before: a cycle
        cur = cur.next
    }
    return false
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Linked List Cycle (LeetCode 141)
fun hasCycle(head: ListNode?): Boolean {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) return true                // the same node: they met
    }
    return false                                      // fast reached the end
}

// Length of the cycle (0 if there is none): after they meet, walk once around
fun cycleLength(head: ListNode?): Int {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) {
            var length = 1
            var cur = slow!!.next
            while (cur !== slow) { length++; cur = cur!!.next }
            return length
        }
    }
    return 0
}

// The same idea on numbers: Happy Number (LeetCode 202). Squaring digits forms a chain that may loop.
fun isHappy(n: Int): Boolean {
    fun next(x: Int): Int {
        var sum = 0
        var y = x
        while (y > 0) { val d = y % 10; sum += d * d; y /= 10 }
        return sum
    }
    var slow = n
    var fast = next(n)
    while (fast != 1 && slow != fast) {
        slow = next(slow)
        fast = next(next(fast))
    }
    return fast == 1
}
```

Checks: the list `3→2→0→-4` with the tail pointing to `2`: `hasCycle` → `true`. `1→2` with no cycle → `false`. `isHappy(19)` → `true`, `isHappy(2)` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Floyd | `O(n)` | `O(1)` |
| HashSet | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **`slow == fast` at the start.** Both begin at `head`, so check **after** moving.
2. **Not checking `fast.next`** before `fast.next.next` (a crash at the end of the list).
3. **Comparing values** (`slow.val == fast.val`) instead of nodes (`===`). Different nodes can have equal values.
4. **Using a set of values** instead of a set of nodes.
5. **Empty list or a single node.**

#### 7. Say This in the Interview

1. "I use two pointers. `slow` moves one step and `fast` moves two. If there is a cycle they will meet. If `fast` reaches `null`, there is none."
2. "Time `O(n)`, space `O(1)`. A HashSet works too but needs `O(n)` space."

#### 8. Quick Check

1. Why do slow and fast not skip over each other inside a cycle?
2. What do you compare: values or nodes?

<details>
<summary>Answers</summary>

1. The gap between them shrinks by exactly one each round, so it must hit zero.
2. Nodes (`===`).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | this note |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) (Easy) | cycle in a number chain |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | find where the cycle starts (note 09) |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) | cycle in an index chain |
| 457 | [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) (Medium) | cycle detection in an array |
