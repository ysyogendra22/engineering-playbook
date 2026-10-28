# Common Linked List Edge Cases

> Read this list before a linked list interview. Run through it at the end of every solution.

#### 1. What Is It?

Edge cases are the inputs where a solution that looks right **crashes** or **loses nodes**. Interviewers watch if you test them yourself. Most linked list bugs come from five places:

1. **empty or tiny** lists,
2. **`null` pointers** (`cur.next.next`),
3. the **head changing**,
4. **losing the rest** of the list,
5. **accidental cycles**.

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | Empty list (`head == null`) | `head.next` crashes | check first and return |
| 2 | One node | `head.next.next` crashes; loops that need two nodes | test it |
| 3 | Two nodes | slow/fast, swap, reverse boundaries break | test it |
| 4 | The head must be deleted or changed | the answer's head is wrong | dummy node |
| 5 | The tail must be deleted | `prev.next` handling | stop at the node before it |
| 6 | `cur.next.next` when `cur.next` is `null` | `NullPointerException` | check `cur?.next != null` |
| 7 | Overwriting `next` before saving it | the rest of the list is lost | `val next = cur.next` first |
| 8 | Forgetting to cut the old tail (`tail.next = null`) | an accidental cycle, infinite loop | set it to `null` |
| 9 | Even vs odd length | the wrong middle | decide which middle, test both |
| 10 | Comparing nodes with `==` | `ListNode` has no `equals`, `==` is identity anyway, but comparing values is a different thing | use `===` for "same node", compare `.val` for values |
| 11 | Cycle in the input | an endless traversal | detect it first if the question allows cycles |
| 12 | Two lists of different lengths | one ends early (merge, add, intersection) | handle leftovers with `a ?: b` |
| 13 | Duplicates | wrong removal logic | decide: keep one copy, or remove all copies |
| 14 | Recursion on a long list | `StackOverflowError` | use the iterative version |
| 15 | Changing the input when it must stay unchanged | the caller's data is damaged | restore it, or copy |
| 16 | `k` larger than the length (rotate, k-group, nth from end) | wrong result or crash | `k % length`; check the length |
| 17 | Carry at the end (add numbers) | the last carry is lost | loop `while (a != null \|\| b != null \|\| carry > 0)` |
| 18 | Returning the wrong head | lost nodes | return `dummy.next` |

#### 3. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// 1 and 2. Guard clauses
fun secondValue(head: ListNode?): Int? {
    if (head?.next == null) return null            // empty or one node
    return head.next!!.`val`
}

// 6. Safe two-step move
fun twoAhead(node: ListNode?): ListNode? = node?.next?.next

// 7. Save before you overwrite
fun reverseSafe(head: ListNode?): ListNode? {
    var prev: ListNode? = null
    var cur = head
    while (cur != null) {
        val next = cur.next                         // save first
        cur.next = prev
        prev = cur
        cur = next
    }
    return prev
}

// 4. Dummy node: removing the head works like removing any node
fun removeValue(head: ListNode?, value: Int): ListNode? {
    val dummy = ListNode(0)
    dummy.next = head
    var prev = dummy
    var cur = head
    while (cur != null) {
        if (cur.`val` == value) prev.next = cur.next else prev = cur
        cur = cur.next
    }
    return dummy.next
}

// 8. Cut the tail when you split a list, or you create a cycle
fun splitInHalf(head: ListNode?): Pair<ListNode?, ListNode?> {
    if (head?.next == null) return head to null
    var slow: ListNode = head
    var fast = head.next
    while (fast != null && fast.next != null) { slow = slow.next!!; fast = fast.next!!.next }
    val second = slow.next
    slow.next = null                                 // cut here
    return head to second
}

// 10. Same node vs same value
val a = ListNode(5); val b = ListNode(5)
println(a === b)                                     // false: different nodes
println(a.`val` == b.`val`)                          // true: same value
```

#### 4. Complexity

Edge cases do not change the complexity. They change **correctness**. One exception: a recursive solution on a long list uses `O(n)` stack and can crash.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Always add: empty, one node, two nodes, the head being changed, the tail being changed, even and odd length.
2. **Not asking** whether the list can have a cycle, be empty, or contain duplicates.
3. **Drawing nothing.** Sketch the list and the pointers on paper or the whiteboard. Most pointer bugs show up in the drawing.
4. **Returning the old `head`** after you changed the first node.

#### 6. Say This in the Interview

1. "Before coding: can the list be empty? Does it have a cycle? Can it have duplicates? Is it sorted?"
2. "I will use a dummy node, and I will test an empty list, one node, two nodes, and an even and odd length."
3. "I save `next` before changing any pointer."

#### 7. Quick Check

1. Which condition protects `cur.next.next`?
2. Why use a dummy node?

<details>
<summary>Answers</summary>

1. `cur?.next != null` (and `cur != null`).
2. So that the head is handled like every other node, and you can return `dummy.next`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) (Easy) | head removed, all nodes removed |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) | remove the head, one node |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy) | one or both lists empty |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium) | final carry, different lengths |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard) | fewer than `k` nodes left |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) | no cycle, cycle at the head |
