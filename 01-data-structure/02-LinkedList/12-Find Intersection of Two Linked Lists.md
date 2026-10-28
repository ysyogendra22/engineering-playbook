# Find Intersection of Two Linked Lists

#### 1. What Is It?

Two singly linked lists may **merge into one shared tail**. Find the **first shared node** (the intersection). If they never meet, return `null`.

```text
A:      a1 → a2 ↘
                  c1 → c2 → c3
B: b1 → b2 → b3 ↗

intersection: c1   (the same node object, not just the same value)
```

This is *Intersection of Two Linked Lists* (LeetCode 160). "Intersection" means the **same node in memory**, not equal values.

#### 2. How It Works

**The pointer-switching trick.** Start pointer `a` at the head of list A and pointer `b` at the head of list B. Move both one step at a time. When a pointer reaches the **end**, it jumps to the **head of the other list**.

```text
A has length 5 (2 before the shared part + 3 shared),  B has length 6 (3 before + 3 shared)

a walks A (5 nodes), then B (6 nodes)  → 11 steps to reach the end of the combined walk
b walks B (6 nodes), then A (5 nodes)  → 11 steps too

After walking the same total distance, both pointers arrive at the intersection at the same time.
If there is no intersection, both reach null together (both walked lenA + lenB).
```

Why it works: both pointers walk `lenA + lenB` steps in total, so the different lengths of the non-shared parts cancel out.

Another option: find both lengths, advance the longer list by the difference, then walk both together.

#### 3. Brute Force vs Optimized

| | Brute force | Pointer switching |
|---|---|---|
| Idea | nested loops, or a `HashSet` of A's nodes | two pointers that swap lists |
| Time | `O(m · n)` nested, `O(m + n)` with a set | `O(m + n)` |
| Space | `O(1)` nested, `O(m)` with a set | `O(1)` |

```kotlin
fun getIntersectionNodeSet(headA: ListNode?, headB: ListNode?): ListNode? {
    val seen = HashSet<ListNode>()
    var cur = headA
    while (cur != null) { seen.add(cur); cur = cur.next }
    cur = headB
    while (cur != null) {
        if (cur in seen) return cur                    // the first node of B that is also in A
        cur = cur.next
    }
    return null
}
```

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Intersection of Two Linked Lists (LeetCode 160)
fun getIntersectionNode(headA: ListNode?, headB: ListNode?): ListNode? {
    if (headA == null || headB == null) return null
    var a = headA
    var b = headB
    while (a !== b) {
        a = if (a == null) headB else a.next           // at the end, switch to the other list
        b = if (b == null) headA else b.next
    }
    return a                                           // the intersection, or null if they never met
}

// The length-difference version
fun getIntersectionNodeLengths(headA: ListNode?, headB: ListNode?): ListNode? {
    fun length(h: ListNode?): Int { var n = 0; var c = h; while (c != null) { n++; c = c.next }; return n }
    var a = headA
    var b = headB
    var lenA = length(a)
    var lenB = length(b)
    while (lenA > lenB) { a = a!!.next; lenA-- }       // advance the longer list
    while (lenB > lenA) { b = b!!.next; lenB-- }
    while (a !== b) { a = a!!.next; b = b!!.next }
    return a
}
```

Check: lists `4→1→8→4→5` and `5→6→1→8→4→5` where `8→4→5` is shared → node `8`. Two separate lists `2→6→4` and `1→5` → `null`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Pointer switching | `O(m + n)` | `O(1)` |
| Length difference | `O(m + n)` | `O(1)` |
| HashSet | `O(m + n)` | `O(m)` |

#### 6. Common Mistakes

1. **Comparing values** (`a.val == b.val`) instead of nodes (`a === b`).
2. **Switching when `a.next` is `null`** instead of when `a` is `null`. You must walk the `null` step so that both lengths match when there is no intersection.
3. **Infinite loop** when you never switch or switch twice.
4. **Empty list** (return `null`).
5. **Assuming the lists have equal length.**

#### 7. Say This in the Interview

1. "Intersection means the same node, so I compare references. Each pointer walks its list, then the other list. Both walk `m + n` steps, so they meet at the intersection or both become `null` together. `O(m + n)` time, `O(1)` space."
2. "A HashSet of nodes also works but uses `O(m)` extra space."

#### 8. Quick Check

1. Why do both pointers walk the same number of steps?
2. What happens when there is no intersection?

<details>
<summary>Answers</summary>

1. Each walks its own list plus the other list: `m + n` in total.
2. Both reach `null` at the same time, and the loop ends returning `null`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 160 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy) | this note |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) | related two-pointer meeting |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | cycle start |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (Easy) | a different problem with the same name |
