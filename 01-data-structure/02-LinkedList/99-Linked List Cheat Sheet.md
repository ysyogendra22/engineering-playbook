# Linked List Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–25.

#### 1. Key Takeaways

1. A linked list gives `O(1)` insert/delete **when you hold the node**, but `O(n)` access by index and search.
2. Most linked list questions fit about **10 patterns**. Name the pattern first.
3. Use a **dummy node** whenever the head can change. Return `dummy.next`.
4. Use **slow and fast pointers** for the middle, cycles, and "n-th from the end".
5. Always **save `next` before you overwrite it**. Most bugs are lost nodes.
6. Say the **brute force** (array, `HashSet`, `HashMap`: `O(n)` space), then show the `O(1)` space pointer trick.
7. Always check: empty list, one node, two nodes, head changing, even and odd length, cycle.

#### 2. Operations and Complexity

| Action | Singly | Doubly | Array |
|---|---|---|---|
| Access by index | `O(n)` | `O(n)` | `O(1)` |
| Search | `O(n)` | `O(n)` | `O(n)` |
| Insert / delete at the head | `O(1)` | `O(1)` | `O(n)` |
| Insert at the tail | `O(n)` (`O(1)` with a tail pointer) | `O(1)` | `O(1)` average |
| Delete a node you hold | `O(n)` | `O(1)` | `O(n)` |
| Walk backwards | no | `O(n)` | `O(n)` |
| Memory per item | 1 pointer | 2 pointers | none |

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Complexity | Note |
|---|---|---|---|
| reverse, reverse in place | **prev / cur / next** | `O(n)`, `O(1)` | 05 |
| reverse part of a list, or groups of `k` | **head insertion**, group-by-group | `O(n)`, `O(1)` | 14, 15 |
| middle node | **slow / fast** | `O(n)`, `O(1)` | 06, 07 |
| has a cycle? | **Floyd's** (slow / fast) | `O(n)`, `O(1)` | 08 |
| where does the cycle start? | **Floyd's, two phases** | `O(n)`, `O(1)` | 09 |
| find a duplicate in `1..n` (array) | **Floyd's on indexes** | `O(n)`, `O(1)` | 09 |
| n-th node from the end | **gap pointers** (+ dummy) | `O(n)`, one pass | 11 |
| two lists meet (intersection) | **pointer switching** | `O(m + n)`, `O(1)` | 12 |
| merge sorted lists | **dummy + tail** | `O(m + n)` | 10 |
| merge `k` sorted lists | **min-heap** or **divide and conquer** | `O(N log k)` | 23 |
| sort a list | **merge sort** (middle + merge) | `O(n log n)` | 10 |
| palindrome | **middle + reverse half + compare** | `O(n)`, `O(1)` | 13 |
| reorder `L0, Ln, L1, Ln−1…` | **middle + reverse + interleave** | `O(n)`, `O(1)` | 20 |
| split by a rule (less than `x`, odd / even) | **two dummy lists + join** | `O(n)`, `O(1)` | 19 |
| add numbers | **carry** (loop while a digit or carry) | `O(n)` | 21 |
| rotate a list | **make a circle, cut at the new tail** | `O(n)`, `O(1)` | 18 |
| copy a list with random pointers | **HashMap** or **weave copies** | `O(n)` | 22 |
| nested `child` lists | **stack** or recursion | `O(n)` | 24 |
| cache with `O(1)` get and put | **HashMap + doubly linked list** | `O(1)` per call | 25 |
| remove nodes by value / duplicates | **dummy + prev** | `O(n)` | 03 |

#### 4. Templates to Memorise

**Node and helpers**

```kotlin
class ListNode(var `val`: Int) { var next: ListNode? = null }
```

**Reverse**

```kotlin
var prev: ListNode? = null
var cur = head
while (cur != null) {
    val next = cur.next
    cur.next = prev
    prev = cur
    cur = next
}
return prev
```

**Middle (second middle for an even length)**

```kotlin
var slow = head
var fast = head
while (fast?.next != null) { slow = slow!!.next; fast = fast.next!!.next }
return slow
```

**Cycle detection and cycle start**

```kotlin
var slow = head; var fast = head
while (fast?.next != null) {
    slow = slow!!.next; fast = fast.next!!.next
    if (slow === fast) {                      // cycle found
        var p = head
        while (p !== slow) { p = p!!.next; slow = slow!!.next }
        return p                              // the cycle start
    }
}
return null
```

**Dummy node + tail (merge)**

```kotlin
val dummy = ListNode(0)
var tail = dummy
while (a != null && b != null) {
    if (a.`val` <= b.`val`) { tail.next = a; a = a.next } else { tail.next = b; b = b.next }
    tail = tail.next!!
}
tail.next = a ?: b
return dummy.next
```

**N-th from the end (remove)**

```kotlin
val dummy = ListNode(0); dummy.next = head
var fast: ListNode? = dummy; var slow: ListNode = dummy
for (i in 0..n) fast = fast?.next
while (fast != null) { fast = fast.next; slow = slow.next!! }
slow.next = slow.next?.next
return dummy.next
```

**Intersection**

```kotlin
var a = headA; var b = headB
while (a !== b) { a = if (a == null) headB else a.next; b = if (b == null) headA else b.next }
return a
```

**Carry (add two numbers)**

```kotlin
while (a != null || b != null || carry > 0) {
    val sum = (a?.`val` ?: 0) + (b?.`val` ?: 0) + carry
    carry = sum / 10
    tail.next = ListNode(sum % 10); tail = tail.next!!
    a = a?.next; b = b?.next
}
```

**Doubly list: remove a node you hold**

```kotlin
node.prev!!.next = node.next
node.next!!.prev = node.prev
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Reverse list | copy into an array, rebuild `O(n)` space | in-place pointers `O(1)` |
| Cycle detection | `HashSet` of nodes `O(n)` space | Floyd's `O(1)` |
| Middle | count the length, then walk `2 passes` | slow / fast, 1 pass |
| N-th from the end | count the length, then walk | gap pointers, 1 pass |
| Intersection | `HashSet` of nodes, or compare every pair `O(m·n)` | pointer switching `O(1)` |
| Palindrome | copy to an array `O(n)` space | reverse the second half `O(1)` |
| Merge `k` lists | collect + sort `O(N log N)` / one by one `O(kN)` | heap / divide and conquer `O(N log k)` |
| Copy with random | `O(n²)` search, or HashMap `O(n)` space | weave copies `O(1)` extra |
| LRU cache | list scan `O(n)` | HashMap + doubly list `O(1)` |
| Reorder / rotate | array of nodes `O(n)` space | pointer steps `O(1)` |
| Add numbers | convert to a number (overflow) | carry digit by digit |

#### 6. Common Mistakes and Edge Cases

1. `NullPointerException` on `cur.next.next`. Check `cur?.next != null` first.
2. Overwriting `cur.next` **before saving it** (lost nodes).
3. No dummy node, so removing the head becomes a special case.
4. Not cutting the list (`x.next = null`) after a split, which creates a cycle.
5. Using `==` instead of `===` for "same node", or comparing nodes when you need values.
6. Wrong middle for even length (first or second). Decide and test both.
7. Floyd's: forgetting to **reset one pointer to `head`** in phase 2.
8. K-group reverse: reversing a last group smaller than `k`.
9. Add numbers: losing the **last carry**.
10. Deep recursion on a long list can overflow the stack: say it and offer the iterative version.
11. LRU: the node must store its **key**, or you cannot remove it from the map.
12. Test: empty, one node, two nodes, head removed, tail removed, even / odd length, with and without a cycle.

#### 7. What to Say Out Loud

1. "Can the list be empty? Is it sorted? Can it have a cycle? Can I change the nodes, or only the values?"
2. "Brute force uses `O(n)` extra space (array / set). I can use two pointers to get `O(1)` space."
3. "I will use a dummy node so the head is not a special case."
4. "Time `O(n)`, space `O(1)`. Edge cases: empty list, one node, the head changing."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | reverse |
| Easy | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | dummy + tail |
| Easy | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | slow / fast |
| Easy | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | slow / fast |
| Easy | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | dummy node |
| Easy | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | one pointer |
| Easy | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | pointer switching |
| Easy | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | middle + reverse |
| Medium | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | gap pointers |
| Medium | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Floyd's, two phases |
| Medium | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | carry |
| Medium | [Reorder List](https://leetcode.com/problems/reorder-list/) | middle + reverse + merge |
| Medium | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | head insertion |
| Medium | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | pointer re-linking |
| Medium | [Rotate List](https://leetcode.com/problems/rotate-list/) | circle + cut |
| Medium | [Partition List](https://leetcode.com/problems/partition-list/) | two lists |
| Medium | [Sort List](https://leetcode.com/problems/sort-list/) | merge sort |
| Medium | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | map / weave |
| Medium | [LRU Cache](https://leetcode.com/problems/lru-cache/) | map + doubly list |
| Hard | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | group reversal |
| Hard | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | heap / divide and conquer |
