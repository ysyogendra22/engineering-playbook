# Stack Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–25.

#### 1. Key Takeaways

1. A stack is **LIFO**: add and remove at the same end. All main operations are `O(1)`.
2. In Kotlin use `ArrayDeque`: `addLast` (push), `removeLast` (pop), `last()` (peek). Never pop an empty stack.
3. Think "stack" when you see **matching pairs**, **undo / go back**, **nested structure**, or **"next greater / smaller"**.
4. The `while` loop inside a `for` loop is still `O(n)`: every item is pushed once and popped once.
5. Store **indexes** (not values) in monotonic stacks. You need them for distances and widths.
6. Say the brute force first, then the stack: "`O(n²)` becomes `O(n)`".

#### 2. Kotlin Operations and Complexity

| Action | Kotlin | If empty | Time |
|---|---|---|---|
| push | `addLast(x)` | — | `O(1)` |
| pop | `removeLast()` / `removeLastOrNull()` | crash / `null` | `O(1)` |
| peek | `last()` / `lastOrNull()` | crash / `null` | `O(1)` |
| empty? | `isEmpty()` / `isNotEmpty()` | — | `O(1)` |
| search | `contains(x)` | — | `O(n)` |

Memory for `n` items: `O(n)`. Avoid `java.util.Stack`. On a Java `Deque`, `push`/`pop` work at the **front**.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Pop when... | Note | Example |
|---|---|---|---|---|
| brackets, tags, nested pairs | **matching** | a closer arrives and the top matches | 04 | Valid Parentheses |
| "next greater / smaller element", "days until warmer" | **monotonic stack** | the new item beats the top | 05–07, 10 | Daily Temperatures |
| "nearest bigger/smaller on the left", spans | **previous greater/smaller** | the top is useless | 08, 09 | Online Stock Span |
| areas, widths, "largest rectangle" | **monotonic stack with boundaries** | a shorter bar arrives | 11, 23 | Largest Rectangle in Histogram |
| "sum over all subarrays of min/max" | **contribution technique** | same as boundaries | 24, 25 | Sum of Subarray Minimums |
| undo, backspace, remove adjacent equal | **push and pop to undo** | the new item cancels the top | 12, 20 | Remove All Adjacent Duplicates |
| calculator, postfix, expressions | **numbers stack** | an operator arrives | 12, 16 | Evaluate Reverse Polish Notation |
| nested `k[...]`, brackets with counts | **save and restore state** | `]` or `)` arrives | 19 | Decode String |
| `.` / `..` / back navigation | **path stack** | `..` arrives | 18 | Simplify Path |
| collisions, chain reactions | **simulation stack** | the new item destroys the top | 21 | Asteroid Collision |
| "get min in `O(1)`" | **stack with extra data** | — | 13 | Min Stack |
| "do it without recursion" | **explicit stack DFS** | node is finished | 14 | Binary Tree Inorder Traversal |

#### 4. Templates to Memorise

**Matching brackets**

```kotlin
val stack = ArrayDeque<Char>()
for (c in s) {
    if (c in match) {                                    // match = closing → opening
        if (stack.isEmpty() || stack.removeLast() != match[c]) return false
    } else stack.addLast(c)
}
return stack.isEmpty()
```

**Monotonic stack (next greater element)**

```kotlin
val result = IntArray(n) { -1 }
val stack = ArrayDeque<Int>()                            // indexes
for (i in nums.indices) {
    while (stack.isNotEmpty() && nums[stack.last()] < nums[i]) result[stack.removeLast()] = nums[i]
    stack.addLast(i)
}
```

**Two operands (calculator, postfix)**

```kotlin
val b = stack.removeLast()                               // RIGHT operand first
val a = stack.removeLast()
stack.addLast(a - b)
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Optimized |
|---|---|---|
| Valid Parentheses | delete `()` `[]` `{}` again and again: `O(n²)` | stack: `O(n)` |
| Next Greater / Daily Temperatures | scan right for each item: `O(n²)` | monotonic stack: `O(n)` |
| Online Stock Span | walk back on every call: `O(n)` per call | stack of `(price, span)`: `O(1)` average |
| Largest Rectangle in Histogram | expand from every bar: `O(n²)` | increasing stack: `O(n)` |
| Min Stack | scan for the minimum: `O(n)` | store the minimum with each item: `O(1)` |
| Remove Adjacent Duplicates | repeated `replace`: `O(n²)` | one stack pass: `O(n)` |
| Sum of Subarray Minimums | all subarrays: `O(n²)` | contribution technique: `O(n)` |

#### 6. Common Mistakes and Edge Cases

1. Pop or peek on an **empty** stack. Check `isNotEmpty()` inside the `while` condition.
2. Forgetting the **items left** in the stack at the end (brackets: `"(("`; monotonic: they have no answer).
3. **`<` versus `<=`** on equal values. Read the question: strictly greater or not?
4. Storing **values** when you need **distances** or **widths**.
5. **Operand order**: pop the right number first (`5 3 -` is `5 - 3`).
6. Histogram: forgetting the extra bar of height `0`, or the left limit `-1`.
7. Multi-digit numbers, spaces and the last token in parsers.
8. Overflow in areas and sums: use `Long`.
9. Deep recursion: use an explicit stack.
10. Test: empty input, one item, all equal, all increasing, all decreasing.

#### 7. What to Say Out Loud

1. "The most recent unresolved item decides what happens next, so I will use a stack."
2. "Brute force is `O(n²)`. With a stack each item is pushed and popped once, so it is `O(n)` time and `O(n)` space."
3. "Edge cases: empty input, a single item, equal values, and items left in the stack."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Idea |
|---|---|---|
| Easy | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | matching |
| Easy | [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | push and pop to undo |
| Easy | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | `#` pops |
| Easy | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | monotonic stack + map |
| Easy | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | two stacks |
| Medium | [Min Stack](https://leetcode.com/problems/min-stack/) | stack with extra data |
| Medium | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | monotonic stack |
| Medium | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | numbers stack |
| Medium | [Decode String](https://leetcode.com/problems/decode-string/) | save and restore |
| Medium | [Simplify Path](https://leetcode.com/problems/simplify-path/) | path stack |
| Medium | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | simulation |
| Medium | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | previous greater |
| Medium | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | increasing stack |
| Medium | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | numbers stack |
| Hard | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | boundaries |
| Hard | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | decreasing stack |
