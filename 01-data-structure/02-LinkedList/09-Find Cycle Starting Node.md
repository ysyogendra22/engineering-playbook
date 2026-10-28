# Find Cycle Starting Node

> The follow-up to cycle detection. The trick looks like magic, so learn the two steps and the short reason.

#### 1. What Is It?

Given a list with a cycle, return the **node where the cycle begins** (the first node you enter the cycle at). If there is no cycle, return `null`.

```text
1 → 2 → 3 → 4
        ↑   ↓
        6 ← 5        the cycle starts at node 3
```

This is *Linked List Cycle II* (LeetCode 142).

#### 2. How It Works

**Two phases.**

1. **Detect:** run slow and fast until they meet inside the cycle (note 08). If `fast` reaches `null`, return `null`.
2. **Find the start:** put one pointer at the **head** and keep the other at the **meeting point**. Move **both one step at a time**. The place where they meet is the cycle start.

```text
list: 3 → 2 → 0 → -4 → (back to 2)

phase 1: slow and fast meet at -4 (inside the cycle)
phase 2: p1 = head (3), p2 = meeting point (-4)
         step: p1 = 2, p2 = 2      they meet at node 2 → the cycle starts at 2
```

**Why it works (short version).** Let `a` be the distance from the head to the cycle start, and `c` the cycle length. When they meet, `fast` has walked exactly **one extra full round** of the cycle more than `slow`. A little algebra shows that the meeting point is `a` steps *before* the cycle start (going around). So walking `a` steps from the head and `a` steps from the meeting point lands both on the cycle start.

You do not need to prove it in an interview. Say the two phases and the key fact: "the distance from the head to the start equals the distance from the meeting point to the start".

#### 3. Brute Force vs Optimized

| | Brute force | Floyd, phase 2 |
|---|---|---|
| Idea | store visited nodes in a set; the first repeat is the start | slow/fast, then two single steps |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun detectCycleSet(head: ListNode?): ListNode? {
    val seen = HashSet<ListNode>()
    var cur = head
    while (cur != null) {
        if (!seen.add(cur)) return cur                // the first node seen twice is the start
        cur = cur.next
    }
    return null
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Linked List Cycle II (LeetCode 142)
fun detectCycle(head: ListNode?): ListNode? {
    var slow = head
    var fast = head
    while (fast != null && fast.next != null) {          // phase 1: find a meeting point
        slow = slow!!.next
        fast = fast.next!!.next
        if (slow === fast) {
            var p1 = head                                // phase 2: one pointer from the head
            var p2 = slow                                // one pointer from the meeting point
            while (p1 !== p2) {
                p1 = p1!!.next
                p2 = p2!!.next
            }
            return p1                                    // the cycle start
        }
    }
    return null
}

// Find the Duplicate Number (LeetCode 287): treat nums[i] as "next index". The duplicate is the cycle start.
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
```

Checks: `detectCycle` on `3→2→0→-4` (tail to node `2`) → node `2`. A list with no cycle → `null`. `findDuplicate([1,3,4,2,2])` → `2`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Floyd, two phases | `O(n)` | `O(1)` |
| HashSet | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Starting phase 2 before the pointers meet.** Check that a cycle exists first.
2. **Moving the phase 2 pointers at different speeds.** Both move **one** step.
3. **Putting both phase 2 pointers at the head.** One starts at the head, the other at the meeting point.
4. **Returning the meeting point** instead of the start.
5. **Comparing values** instead of nodes.

#### 7. Say This in the Interview

1. "Phase 1: slow and fast meet inside the cycle if there is one. Phase 2: I reset one pointer to the head, and move both one step at a time. They meet at the start of the cycle."
2. "`O(n)` time and `O(1)` space. The reason is that the head-to-start distance equals the meeting-point-to-start distance around the loop."

#### 8. Quick Check

1. In phase 2, how fast do the two pointers move?
2. What do you return if `fast` reaches `null` in phase 1?

<details>
<summary>Answers</summary>

1. Both one step at a time.
2. `null` (there is no cycle).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | phase 1 only |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | this note |
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium) | cycle start in an array |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) (Easy) | detect a loop |
