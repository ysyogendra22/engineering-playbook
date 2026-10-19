# Common Stack Edge Cases

#### 1. Definition — Must Know

1. These are the situations where stack code most often **crashes or gives wrong answers**.
2. Most come from five places: **empty stack**, **wrong end of a Deque**, **leftovers at the end**, **ties in monotonic stacks**, and **order of operands**.
3. Check this list before you say "done".

#### 2. Why It Is Used — Must Know

1. Interviewers watch if you test the empty and one-item cases yourself.
2. A single wrong comparison (`<` vs `<=`) changes the answer on equal values.
3. In real code, an unchecked `pop()` is a common crash.

#### 3. How It Works — Must Know

The most common crash and the most common silent bug:

```text
Crash:   "())"  →  the second ')' arrives and the stack is empty → removeLast() throws.
         Always check isNotEmpty() before pop/peek.

Silent:  [2, 2] next greater element
         pop while top < current  → 2 < 2 is false → the first 2 stays → answer -1  (strictly greater)
         pop while top <= current → the first 2 gets answer 2                       (greater or equal)
         The problem statement decides. A wrong choice gives wrong answers only on ties.
```

#### 4. Core Concepts — Must Know

| # | Edge case | What happens | Fix |
|---|---|---|---|
| 1 | `pop`/`peek` on an empty stack | `NoSuchElementException` | check `isNotEmpty()` or use `...OrNull()` |
| 2 | Closing bracket first (`")("`) | pop on empty | check empty before matching |
| 3 | Leftover items after the loop | missed answers / false "valid" | check `stack.isEmpty()`, or process leftovers |
| 4 | Ties in monotonic stacks | wrong on equal values | choose `<` or `<=` from the problem; be consistent |
| 5 | Left boundary when stack is empty | wrong width / index | use `-1`; right boundary default `n` |
| 6 | Missing sentinel in histogram | last bars not counted | extra step with height `0` |
| 7 | Storing values when you need distances | cannot compute `i - j` | store indexes |
| 8 | Operand order in RPN (`a - b`, `a / b`) | wrong sign / result | `b = pop(); a = pop(); a op b` |
| 9 | Integer division and negatives | rounding differs | Kotlin `/` truncates toward zero |
| 10 | `Deque.push/pop/peek` act on the **front** | order reversed | use `addLast`/`removeLast`/`last()` consistently |
| 11 | `java.util.Stack` vs `ArrayDeque` mixed | confusing, slower | use `ArrayDeque` |
| 12 | Modifying a stack while iterating with `for` | `ConcurrentModificationException` | drain with `while` |
| 13 | Deep recursion instead of a stack | `StackOverflowError` | explicit stack |
| 14 | Min Stack with `<` in the compact version | wrong after popping duplicates | use `<=` |
| 15 | Multi-digit numbers / spaces in parsers | wrong numbers | `num = num * 10 + digit`; skip spaces |
| 16 | Last token not processed | missing last operand | handle the end of input |
| 17 | `Int` overflow (area, sums, products) | wrong values | use `Long` |
| 18 | Decode String: nested counts | wrong repeats | one stack for counts, one for strings |
| 19 | Simplify Path: `..` at root, empty parts | wrong path | ignore `..` on an empty stack; skip `""` and `.` |
| 20 | Asteroid Collision: equal sizes | both should explode | handle the `==` case |

#### 5. Algorithm — Must Know

Checklist before you finish:

```text
1. Can I pop/peek an empty stack anywhere? (first character, empty input)
2. What is left in the stack at the end, and did I handle it?
3. Monotonic stack: strict or non-strict? Indexes or values?
4. Left/right boundaries: -1 and n when missing? Sentinel added?
5. Two-operand pops: right operand first?
6. Am I using the right end of the Deque for every action?
7. Could the input be very deep (use an explicit stack)? Could numbers overflow?
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val stack = ArrayDeque<Int>()

// 1. Empty stack
// stack.removeLast()                     // NoSuchElementException
println(stack.removeLastOrNull())         // null
println(stack.lastOrNull())               // null

// 2. Safe bracket check
fun isValid(s: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val st = ArrayDeque<Char>()
    for (c in s) {
        if (c in pairs) {
            if (st.isEmpty() || st.removeLast() != pairs[c]) return false
        } else st.addLast(c)
    }
    return st.isEmpty()                    // leftovers mean invalid
}

// 3. Ties: strict vs non-strict
fun nextGreaterStrict(nums: IntArray): IntArray {
    val res = IntArray(nums.size) { -1 }
    val st = ArrayDeque<Int>()
    for (i in nums.indices) {
        while (st.isNotEmpty() && nums[st.last()] < nums[i]) res[st.removeLast()] = nums[i]   // '<' strict
        st.addLast(i)
    }
    return res
}
println(nextGreaterStrict(intArrayOf(2, 2)).toList())     // [-1, -1]

// 4. Java Deque ends
val dq = java.util.ArrayDeque<Int>()
dq.push(1); dq.push(2)                    // push adds to the FRONT
println(dq.peek())                        // 2
dq.addLast(0)                             // the back
println(dq)                               // [2, 1, 0]

// 5. Operand order in RPN: "5 3 -" means 5 - 3
fun applyMinus(stack: ArrayDeque<Int>) {
    val b = stack.removeLast()
    val a = stack.removeLast()
    stack.addLast(a - b)                  // not b - a
}

// 6. Division truncates toward zero
println(-7 / 2)                           // -3
println(7 / -2)                           // -3

// 7. Overflow in area
val h = 100_000; val w = 100_000
println(h * w)                            // 1410065408 (overflow)
println(h.toLong() * w)                   // 10000000000
```

#### 7. Time & Space Complexity — Must Know

| Concern | Impact |
|---|---|
| Missing the empty check | crash (not a complexity issue, but a correctness one) |
| `contains` on a stack | `O(n)`; keep a separate set if needed |
| Deep recursion | uses call-stack memory, risk of overflow |
| Storing pairs/objects per item | extra memory per push |

#### 8. Common Bug Families — Must Know

1. **Empty-state bugs:** pop/peek on empty; leftovers at the end.
2. **Tie bugs:** `<` vs `<=` in monotonic stacks.
3. **Boundary bugs:** `-1` / `n` / sentinel in histogram-style problems.
4. **Order bugs:** operand order; Deque ends.
5. **Parsing bugs:** multi-digit, spaces, last token.
6. **Number bugs:** overflow, division rounding.
7. **Structure bugs:** value vs index in the stack; wrong stack type.

#### 9. Edge Cases / Common Mistakes

1. Testing only the example from the problem.
2. Returning from inside the loop and skipping the final emptiness check.
3. Using `stack.size` after a pop and expecting the old value.
4. Treating `peek()` as `pop()`.
5. Mixing a `Stack` class and `Deque` methods.
6. Forgetting to clear or reset a reused stack between test cases (class fields).
7. Not stating assumptions about invalid input (non-bracket characters, empty string).

#### 10. When to Use / When Not to Use

**Use this checklist when:**

1. You finish any stack solution.

**Remember:**

1. Most stack bugs are an unchecked empty pop or a wrong tie rule.

#### 11. Related Topics

1. Stack Operations & Complexity
2. Valid / Balanced Parentheses
3. Monotonic Stack
4. Largest Rectangle in Histogram

#### 12. Interview Must Remember

1. **Check empty before pop/peek. Check leftovers at the end.**
2. **Decide `<` vs `<=` from the problem statement.**
3. Operand order: pop the right operand first.
4. Use indexes, sentinels (`-1`, `n`, height `0`), and `Long` where needed.
