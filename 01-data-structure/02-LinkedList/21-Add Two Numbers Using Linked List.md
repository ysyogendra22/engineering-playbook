# Add Two Numbers Using Linked List

#### 1. What Is It?

Two numbers are stored as linked lists, one **digit per node**. Add them and return the sum as a list.

**LeetCode 2 — digits in reverse order** (the head is the ones digit):

```text
2 → 4 → 3   (342)
5 → 6 → 4   (465)
7 → 0 → 8   (807)
```

**LeetCode 445 — digits in normal order** (the head is the most significant digit):

```text
7 → 2 → 4 → 3   (7243)
    5 → 6 → 4   ( 564)
7 → 8 → 0 → 7   (7807)
```

The numbers can be very long, so you cannot convert them to `Int` or `Long`. You add digit by digit, exactly like on paper, with a **carry**.

#### 2. How It Works

**LeetCode 2 (reverse order)** — the head is already the ones digit, so add from the head:

1. Keep `carry = 0`.
2. While there is a digit in `a`, a digit in `b`, **or** a carry: `sum = a + b + carry`, new digit `= sum % 10`, `carry = sum / 10`.
3. Append the digit to the result list (use a dummy node and a tail).

```text
2 → 4 → 3  +  5 → 6 → 4
2+5       = 7   carry 0   → 7
4+6       = 10  carry 1   → 0
3+4+1     = 8   carry 0   → 8
result: 7 → 0 → 8
```

**LeetCode 445 (normal order)** — you need the **last digit first**. Use two **stacks**: push all digits, then pop to add from the end. Build the result by **inserting at the front**, so the most significant digit ends up first.

(Another way: reverse both lists, use the LeetCode 2 method, and reverse the answer. The stack method does not change the input.)

#### 3. Brute Force vs Optimized

| | Brute force | Digit by digit |
|---|---|---|
| Idea | convert each list to a number (`BigInteger`), add, convert back | add with a carry |
| Time | `O(n + m)` | `O(max(n, m))` |
| Space | `O(n + m)` | `O(1)` extra (besides the answer) |

```kotlin
import java.math.BigInteger

fun addTwoNumbersBrute(l1: ListNode?, l2: ListNode?): ListNode? {
    fun toBig(node: ListNode?): BigInteger {
        val sb = StringBuilder()
        var cur = node
        while (cur != null) { sb.append(cur.`val`); cur = cur.next }
        return BigInteger(sb.reverse().toString())       // reverse order list: the head is the last digit
    }
    val digits = (toBig(l1) + toBig(l2)).toString().reversed()
    val dummy = ListNode(0)
    var tail = dummy
    for (ch in digits) { tail.next = ListNode(ch - '0'); tail = tail.next!! }
    return dummy.next
}
```

A plain `Int` or `Long` would overflow on long lists. Interviewers expect the carry method.

#### 4. Kotlin Code

```kotlin
// class ListNode(var `val`: Int) { var next: ListNode? = null }   (note 01)

// Add Two Numbers (LeetCode 2): digits in reverse order
fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
    val dummy = ListNode(0)
    var tail = dummy
    var a = l1
    var b = l2
    var carry = 0
    while (a != null || b != null || carry > 0) {            // the last carry needs a node too
        val sum = (a?.`val` ?: 0) + (b?.`val` ?: 0) + carry
        carry = sum / 10
        tail.next = ListNode(sum % 10)
        tail = tail.next!!
        a = a?.next
        b = b?.next
    }
    return dummy.next
}

// Add Two Numbers II (LeetCode 445): digits in normal order, two stacks
fun addTwoNumbersII(l1: ListNode?, l2: ListNode?): ListNode? {
    val s1 = ArrayDeque<Int>()
    val s2 = ArrayDeque<Int>()
    var a = l1
    while (a != null) { s1.addLast(a.`val`); a = a.next }
    var b = l2
    while (b != null) { s2.addLast(b.`val`); b = b.next }

    var result: ListNode? = null
    var carry = 0
    while (s1.isNotEmpty() || s2.isNotEmpty() || carry > 0) {
        val sum = (s1.removeLastOrNull() ?: 0) + (s2.removeLastOrNull() ?: 0) + carry
        carry = sum / 10
        val node = ListNode(sum % 10)
        node.next = result                                    // insert at the front
        result = node
    }
    return result
}
```

Checks: `addTwoNumbers(2→4→3, 5→6→4)` → `7→0→8`. `addTwoNumbers(0, 0)` → `0`. `addTwoNumbers(9→9→9→9, 1)` → `0→0→0→0→1`. `addTwoNumbersII(7→2→4→3, 5→6→4)` → `7→8→0→7`. `addTwoNumbersII(2→4→3, 5→6→4)` → `8→0→7`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| LeetCode 2 | `O(max(n, m))` | `O(1)` extra |
| LeetCode 445 with stacks | `O(n + m)` | `O(n + m)` |
| LeetCode 445 with reverse | `O(n + m)` | `O(1)` extra |

#### 6. Common Mistakes

1. **Forgetting the final carry** (`999 + 1 = 1000` needs one extra node). Put `carry > 0` in the loop condition.
2. **Different lengths.** Treat a missing digit as `0` (`a?.val ?: 0`).
3. **Converting to `Int` / `Long`.** It overflows.
4. **Using `carry` as a `Boolean`** and then missing sums like `9 + 9 + 1`. The carry is at most 1 here, but write `sum / 10` anyway.
5. **Appending at the head** in LeetCode 2 (the order is reversed). Use a tail pointer.
6. **No dummy node,** which makes the first digit a special case.

#### 7. Say This in the Interview

1. "I add digit by digit with a carry, like on paper. A missing digit counts as zero, and I keep looping while there is a carry."
2. "For the normal-order version I use two stacks (or reverse the lists), so I can add from the least significant digit."

#### 8. Quick Check

1. How many nodes does `5 + 5` (lists `5` and `5`) need in the result?
2. Why does LeetCode 445 need stacks?

<details>
<summary>Answers</summary>

1. Two: `0 → 1`. The carry makes an extra node.
2. The head is the most significant digit, but addition starts from the least significant digit, which is at the end of the list.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium) | carry, reverse order |
| 445 | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) (Medium) | stacks |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) (Easy) | carry on an array |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) (Easy) | carry on strings |
| 369 | [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/) (Medium, premium) | reverse or find the last non-9 |
