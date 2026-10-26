# Common Stack Edge Cases

> Read this list before every stack interview, and run through it at the end of every solution.

#### 1. What Is It?

These are the situations where stack solutions most often **crash** or **give a wrong answer**. Interviewers watch if you check them yourself. Most bugs come from five places:

1. an **empty** stack,
2. **items left over** at the end,
3. **equal values** in a monotonic stack,
4. the **order of two numbers** in a calculator,
5. the **wrong end** of a `Deque`.

#### 2. The Checklist

| # | Edge case | What goes wrong | Fix |
|---|---|---|---|
| 1 | `pop` / `peek` on an empty stack | `NoSuchElementException` | check `isNotEmpty()` or use `removeLastOrNull()` |
| 2 | Closing bracket comes first (`")("`) | pop on empty | check empty before matching |
| 3 | Items left after the loop | wrong "valid" answer, missed answers | check `stack.isEmpty()` / handle leftovers |
| 4 | Equal values (`[2, 2]`) | wrong answer on ties | choose `<` or `<=` from the question |
| 5 | No left limit (stack empty) | wrong width / index | use `-1`; right limit default is `n` |
| 6 | Histogram without the extra `0` bar | last bars never counted | loop one step past the end |
| 7 | Storing values when you need distance | cannot compute `i - j` | store **indexes** |
| 8 | Operand order (`5 3 -`) | `3 - 5` instead of `5 - 3` | pop right first, then left |
| 9 | Integer division with negatives | rounding differs | Kotlin `/` truncates toward zero (usually what is asked) |
| 10 | Java `Deque.push` / `pop` | they work at the **front** | use `addLast` / `removeLast` / `last()` |
| 11 | Changing the stack inside `for (x in stack)` | `ConcurrentModificationException` | use a `while` loop |
| 12 | Very deep recursion | `StackOverflowError` | use your own stack |
| 13 | Min Stack with `<` (compact version) | wrong after popping duplicate minimums | use `<=` |
| 14 | Multi-digit numbers, spaces, last token | wrong numbers | `num = num * 10 + digit`, skip spaces, handle the end |
| 15 | Big products (area, sums) | `Int` overflow | use `Long` |

#### 3. Kotlin Code

```kotlin
val stack = ArrayDeque<Int>()

// 1. Empty stack
println(stack.removeLastOrNull())        // null  (stack.removeLast() would crash)
println(stack.lastOrNull())              // null

// 3. Leftovers: a bracket check must end with isEmpty()
fun isValid(s: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val st = ArrayDeque<Char>()
    for (c in s) {
        if (c in pairs) {
            if (st.isEmpty() || st.removeLast() != pairs[c]) return false
        } else st.addLast(c)
    }
    return st.isEmpty()                  // "((" must fail
}

// 4. Equal values: '<' means strictly greater
fun nextGreater(nums: IntArray): IntArray {
    val res = IntArray(nums.size) { -1 }
    val st = ArrayDeque<Int>()
    for (i in nums.indices) {
        while (st.isNotEmpty() && nums[st.last()] < nums[i]) res[st.removeLast()] = nums[i]
        st.addLast(i)
    }
    return res
}
// nextGreater([2, 2]) → [-1, -1]. With '<=' it would be [2, -1].

// 8. Operand order: "5 3 -" means 5 - 3
fun minus(st: ArrayDeque<Int>) {
    val b = st.removeLast()              // right
    val a = st.removeLast()              // left
    st.addLast(a - b)
}

// 10. Java Deque: push adds to the FRONT
val dq = java.util.ArrayDeque<Int>()
dq.push(1); dq.push(2)
println(dq.peek())                       // 2 (front)

// 15. Overflow
println(100_000 * 100_000)               // 1410065408 (wrong)
println(100_000L * 100_000)              // 10000000000
```

#### 4. Complexity

Edge cases do not change the time or space. They change **correctness**. An unchecked `pop` is a crash, not a slow program.

#### 5. Common Mistakes

1. **Testing only the example from the question.** Also test: empty input, one item, all items equal, all increasing, all decreasing.
2. **Returning early and skipping the final `isEmpty()` check.**
3. **Mixing `java.util.Stack` and `ArrayDeque`.**
4. **Not saying your assumption out loud** (for example, "I assume the input has only brackets").

#### 6. Say This in the Interview

1. "Edge cases I will check: empty input, a single item, and items left in the stack."
2. "For equal values I use strict `<`, because the question says *strictly* greater."
3. "I will use `Long` here to avoid overflow."

#### 7. Quick Check

1. What does `isValid("((")` return, and which line makes sure of it?
2. What happens if you `pop` the right number second in `8 2 /`?

<details>
<summary>Answers</summary>

1. `false`. The final `return st.isEmpty()` fails because two `(` are left.
2. You compute `2 / 8 = 0` instead of `8 / 2 = 4`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Edge case to watch |
|---|---|---|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) | empty stack, leftovers |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) (Medium) | duplicate minimums |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium) | operand order, division |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium) | equal temperatures |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard) | sentinel, `-1` limit |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) (Medium) | `..` at the root |
