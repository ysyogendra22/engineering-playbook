# Palindrome Linked List

#### 1. What Is It?

Check if a linked list reads the **same forwards and backwards**.

```text
1 → 2 → 2 → 1   palindrome
1 → 2 → 3       not a palindrome
```

This is *Palindrome Linked List* (LeetCode 234). The follow-up is always: **`O(n)` time and `O(1)` space.** A singly linked list cannot be read backwards, so we reverse half of it.

This note combines two earlier tools: **find the middle** (note 07) and **reverse a list** (note 05).

#### 2. How It Works

1. Find the **middle** with slow and fast pointers.
2. **Reverse the second half** of the list.
3. **Compare** the first half with the reversed second half, node by node.
4. (Optional) **Reverse the second half again** to restore the list.

```text
1 → 2 → 3 → 2 → 1

1. middle: slow stops at 3
2. reverse from the node after the middle (2 → 1):  1 → 2 → 3 → 1 → 2   (the second half now reads 1, 2)
3. compare:  first half 1, 2   vs   second half 1, 2   → equal → palindrome
```

For an odd length the middle node is skipped in the comparison. Comparison ends when the second half ends.

#### 3. Brute Force vs Optimized

| | Brute force | Reverse half |
|---|---|---|
| Idea | copy the values into an array and compare from both ends | reverse the second half in place |
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` |

```kotlin
fun isPalindromeArray(head: ListNode?): Boolean {
    val values = mutableListOf<Int>()
    var cur = head
    while (cur != null) { values.add(cur.`val`); cur = cur.next }
    var l = 0
    var r = values.size - 1
    while (l < r) { if (values[l++] != values[r--]) return false }
    return true
}
```

The array version is a fine first answer. The interviewer will then ask for `O(1)` space.

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

private fun reverse(head: ListNode?): ListNode? {
    var prev: ListNode? = null
    var cur = head
    while (cur != null) {
        val next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    }
    return prev
}

// Palindrome Linked List (LeetCode 234): O(n) time, O(1) space
fun isPalindrome(head: ListNode?): Boolean {
    if (head?.next == null) return true
    var slow: ListNode? = head
    var fast: ListNode? = head
    while (fast?.next != null && fast.next!!.next != null) {      // slow stops at the first middle
        slow = slow!!.next
        fast = fast.next!!.next
    }
    var second = reverse(slow!!.next)                              // reverse the second half
    val secondHead = second                                         // remember it to restore later
    var first: ListNode? = head
    var result = true
    while (second != null) {
        if (first!!.`val` != second.`val`) { result = false; break }
        first = first.next
        second = second.next
    }
    slow.next = reverse(secondHead)                                 // restore the list
    return result
}
```

Checks: `isPalindrome(1→2→2→1)` → `true`. `isPalindrome(1→2)` → `false`. `isPalindrome(1→2→3→2→1)` → `true`. `isPalindrome(1)` → `true`.

Here `slow` stops at the **first** middle: for `1→2→2→1` it stops at the first `2`, and the second half is `2→1`. For `1→2→3→2→1` it stops at `3`, and the second half is `2→1`; the middle `3` is not compared.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Reverse the second half | `O(n)` | `O(1)` |
| Copy to an array | `O(n)` | `O(n)` |

#### 6. Common Mistakes

1. **Using the second middle** for an even-length list. The halves then have different sizes. Use the first middle.
2. **Comparing the middle node** in an odd-length list. Stop when the second half ends.
3. **Forgetting to cut or restore** the list. The first half still points into the second half; comparing until the second half ends makes this safe. Restore the list if the interviewer asks.
4. **Empty and one-node lists** are palindromes.
5. **Comparing nodes** instead of values.

#### 7. Say This in the Interview

1. "The easy way is to copy into an array: `O(n)` space. To get `O(1)` space, I find the middle, reverse the second half, and compare it with the first half."
2. "I restore the list afterwards, so the input is not changed."

#### 8. Quick Check

1. After reversing the second half of `1→2→3→2→1`, what do you compare?
2. Is an empty list a palindrome?

<details>
<summary>Answers</summary>

1. `1, 2` (the first half) with `1, 2` (the reversed second half). The middle `3` is skipped.
2. Yes (nothing to mismatch).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | this note |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) | two pointers on a string |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (Easy) | step 1 |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | step 2 |
| 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) (Medium) | the same first two steps (note 20) |
