# Reverse Linked List

> The most asked linked list question. Be able to write it from memory, both ways.

#### 1. What Is It?

**Reversing** a linked list means turning every `next` pointer around, so the list runs the other way.

```text
before:  1 → 2 → 3 → null
after:   3 → 2 → 1 → null
```

It is *Reverse Linked List* (LeetCode 206). The idea is also the base of Reverse Between Positions, Reverse in K-Group, Palindrome Linked List and Reorder List.

#### 2. How It Works

**Iterative: three pointers** `prev`, `cur`, `next`. For each node: save `next`, point `cur` backwards to `prev`, then move both forward.

```text
list: 1 → 2 → 3 → null        prev = null, cur = 1

step 1: next = 2;  1.next = null;   prev = 1;  cur = 2     null ← 1    2 → 3
step 2: next = 3;  2.next = 1;      prev = 2;  cur = 3     null ← 1 ← 2    3
step 3: next = null; 3.next = 2;    prev = 3;  cur = null  null ← 1 ← 2 ← 3

cur is null → stop. The new head is prev (3).
```

**Recursive:** reverse the rest of the list first, then fix the pointer of the current node.

```text
reverse(1 → 2 → 3):
   reverse(2 → 3) returns the head of 3 → 2 → null
   now 2.next is null; we want 2 → 1, so set head.next.next = head  (2.next = 1)
   and head.next = null (1 no longer points to 2)
   → 3 → 2 → 1 → null
```

Base case: an empty list or a single node is already reversed.

#### 3. Brute Force vs Optimized

| | Brute force | Iterative (in place) | Recursive |
|---|---|---|---|
| Idea | copy values into an array, write them back reversed | change the pointers | change the pointers on the way back |
| Time | `O(n)` | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` | `O(n)` (call stack) |

```kotlin
fun reverseListBrute(head: ListNode?): ListNode? {
    val values = mutableListOf<Int>()
    var cur = head
    while (cur != null) { values.add(cur.`val`); cur = cur.next }
    cur = head
    for (i in values.indices.reversed()) { cur!!.`val` = values[i]; cur = cur.next }
    return head
}
```

The follow-up question is always "can you do it without extra space?".

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Iterative: O(n) time, O(1) space
fun reverseList(head: ListNode?): ListNode? {
    var prev: ListNode? = null
    var cur = head
    while (cur != null) {
        val next = cur.next          // 1. save the rest of the list
        cur.next = prev              // 2. turn the pointer around
        prev = cur                   // 3. move prev forward
        cur = next                   // 4. move cur forward
    }
    return prev                      // the new head
}

// Recursive: O(n) time, O(n) stack space
fun reverseListRecursive(head: ListNode?): ListNode? {
    if (head == null || head.next == null) return head       // base case
    val newHead = reverseListRecursive(head.next)             // reverse the rest
    head.next!!.next = head                                    // the next node points back to me
    head.next = null                                           // I become the tail
    return newHead
}
```

Checks: `reverseList(1→2→3→4→5)` → `5→4→3→2→1`. `reverseList(null)` → `null`. `reverseList(1)` → `1`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Iterative | `O(n)` | `O(1)` |
| Recursive | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Overwriting `cur.next` before saving it.** The rest of the list is lost.
2. **Returning `cur` instead of `prev`.** At the end `cur` is `null`.
3. **Forgetting `head.next = null`** in the recursive version. It creates a cycle.
4. **Empty or one-node list.** Both should work (the loop does nothing / the base case).
5. **Recursion depth** on a very long list.

#### 7. Say This in the Interview

1. "I walk through the list with `prev`, `cur` and `next`. For each node I save the next node, point `cur` back to `prev`, and move forward. Time `O(n)`, space `O(1)`."
2. "The recursive version is shorter but uses `O(n)` stack space."
3. "The new head is `prev` when the loop ends."

#### 8. Quick Check

1. What is `prev` at the start?
2. After the loop, which pointer is the new head?

<details>
<summary>Answers</summary>

1. `null` (the old head becomes the tail, pointing to `null`).
2. `prev`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | this note |
| 92 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (Medium) | reverse part (note 14) |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (Medium) | reverse groups of 2 |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | reverse the second half (note 13) |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) (Medium) | reverse + merge (note 20) |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard) | reverse `k` at a time (note 15) |
