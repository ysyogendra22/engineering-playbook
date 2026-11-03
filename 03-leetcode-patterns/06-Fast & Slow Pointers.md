# Fast & Slow Pointers

> Two pointers at different speeds. They meet if there is a cycle, and the slow one sits in the middle when the fast one finishes.

#### 1. What Is It?

Also called **Floyd's tortoise and hare**. `slow` moves 1 step and `fast` moves 2 steps. It uses `O(1)` space where a hash set would use `O(n)`.

**Signals**

- "Is there a **cycle** in the linked list?"
- "Find the **middle** of a list"
- "Find where the cycle **starts**"
- A sequence that repeats: happy number, "find the duplicate" with values used as pointers
- "Nth node from the end" (a gap version of the same idea)

#### 2. How It Works

**Cycle detection**

```text
1 → 2 → 3 → 4
        ↑   ↓
        6 ← 5
slow: 1, 2, 3, 4, 5 ...      fast: 1, 3, 5, 3, 5 ...
They land on the same node → cycle.
```

If `fast` reaches `null`, there is no cycle. Inside a cycle, `fast` gains one step on `slow` every move, so it must catch up.

**Middle of the list.** When `fast` reaches the end, `slow` is at the middle. For an even count, this version returns the **second** middle.

**Find the cycle start (two phases)**

1. Move until `slow == fast` (they meet inside the cycle).
2. Put one pointer back at the head. Move both **one step at a time**. They meet at the cycle start.

Why: if the head is `a` steps from the cycle start and the meeting point is `b` steps inside the cycle, then `a` equals the remaining distance to the start (mod the cycle length).

**Numbers as pointers.** For a number `x`, define `next(x)`. Happy number: `next` is the sum of squares of the digits. Find the duplicate: `next(i) = nums[i]`. Both form a "linked list" with a cycle.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Fast / slow |
|---|---|---|
| Cycle in a list | `HashSet` of visited nodes, `O(n)` space | two pointers, `O(1)` space |
| Middle of a list | count nodes, then walk `n/2` (two passes) | one pass |
| Find the duplicate | sort `O(n log n)` or set `O(n)` space | Floyd `O(n)`, `O(1)` space |

```kotlin
fun hasCycleSet(head: ListNode?): Boolean {
    val seen = HashSet<ListNode>()
    var cur = head
    while (cur != null) {
        if (!seen.add(cur)) return true
        cur = cur.next
    }
    return false
}
```

#### 4. Kotlin Code

```kotlin
class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

// Linked List Cycle (LeetCode 141)
fun hasCycle(head: ListNode?): Boolean {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) return true
    }
    return false
}

// Middle of the Linked List (LeetCode 876): second middle for even length
fun middleNode(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
    }
    return slow
}

// Linked List Cycle II (LeetCode 142): node where the cycle begins
fun detectCycle(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) {
            var start = head
            while (start !== slow) {
                start = start!!.next
                slow = slow!!.next
            }
            return start
        }
    }
    return null
}

// Happy Number (LeetCode 202)
fun isHappy(n: Int): Boolean {
    fun next(x: Int): Int {
        var sum = 0
        var v = x
        while (v > 0) { val d = v % 10; sum += d * d; v /= 10 }
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

// Find the Duplicate Number (LeetCode 287): values 1..n in an array of n+1, treat nums[i] as "next"
fun findDuplicate(nums: IntArray): Int {
    var slow = nums[0]
    var fast = nums[0]
    do {
        slow = nums[slow]
        fast = nums[nums[fast]]
    } while (slow != fast)
    slow = nums[0]
    while (slow != fast) {
        slow = nums[slow]
        fast = nums[fast]
    }
    return slow
}

// Remove Nth Node From End of List (LeetCode 19): fast starts n steps ahead
fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var fast: ListNode? = dummy
    var slow: ListNode? = dummy
    for (i in 0 until n) fast = fast?.next
    while (fast?.next != null) {
        fast = fast.next
        slow = slow!!.next
    }
    slow!!.next = slow.next?.next
    return dummy.next
}
```

Helper for checks: `fun build(vararg v: Int): ListNode?` creates a list `v[0] → v[1] → ...`.

Checks: `hasCycle(build(3,2,0,-4))` with the tail linked to the second node → `true`; a plain `build(1,2)` → `false`. `middleNode(build(1,2,3,4,5)).val` → `3`; `middleNode(build(1,2,3,4,5,6)).val` → `4`. `detectCycle` on `3→2→0→-4→(back to 2)` → the node with value `2`. `isHappy(19)` → `true` (19 → 82 → 68 → 100 → 1); `isHappy(2)` → `false`. `findDuplicate([1,3,4,2,2])` → `2`; `findDuplicate([3,1,3,4,2])` → `3`. `removeNthFromEnd(build(1,2,3,4,5), 2)` → `1→2→3→5`.

(Palindrome Linked List uses slow/fast to find the middle, then reverses the second half. See `DS LinkedList` note 13.)

#### 5. Complexity

| Problem | Time | Space |
|---|---|---|
| Cycle / middle / cycle start | `O(n)` | `O(1)` |
| Find the duplicate | `O(n)` | `O(1)` |
| Happy number | `O(log n)` per step; the sequence is bounded | `O(1)` |

#### 6. Common Mistakes

1. **Checking only `fast != null`.** You also need `fast.next != null` before `fast.next.next`.
2. **Comparing values** (`slow.val == fast.val`) instead of node identity (`===`).
3. **Cycle start:** moving the second pointer by 2 in phase 2. Both move by 1.
4. **Wrong middle for even length.** Decide first or second middle and test with 2 and 4 nodes.
5. **Empty list or one node:** `head == null` must return safely.
6. **Remove Nth:** forgetting a dummy node when the head itself is removed.

#### 7. Say This in the Interview

1. "A hash set works in `O(n)` space. Floyd's algorithm uses two pointers at different speeds, so space is `O(1)`."
2. "If there is a cycle, the fast pointer gains one node per step on the slow one, so they must meet."
3. "To find the start, I reset one pointer to the head and move both one step at a time. They meet at the cycle start."

#### 8. Quick Check

1. What is returned for the middle of `1→2→3→4` with the template above?
2. Why does `fast` need two null checks?

<details>
<summary>Answers</summary>

1. Node `3` (the second middle).
2. `fast` can be `null` (even length) or `fast.next` can be `null` (odd length). Otherwise `fast.next.next` crashes.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | meet inside the cycle |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | slow at the middle |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) (Easy) | cycle in a number sequence |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | two phases |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) | gap between pointers |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | middle + reverse |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) | array as a linked list |
