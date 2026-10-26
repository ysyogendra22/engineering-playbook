# Stack Fundamentals — LIFO

#### 1. What Is a Stack?

A **stack** is a list where you add and remove items at **one end only**. That end is the **top**.

The last item you add is the first item that comes out. This is **LIFO**: **L**ast **I**n, **F**irst **O**ut.

Picture a pile of plates. You put a plate on top, and you take a plate from the top.

**Why use a stack?** It always gives you the **most recent unfinished item first**. That is exactly what you need for matching brackets, undoing actions, going back, and finding the "next bigger" item.

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Push** | add an item on top |
| **Pop** | remove the top item and return it |
| **Peek** | look at the top item, do not remove it |
| **`O(1)`** | the work stays the same however big the stack is (fast) |

#### 3. How It Works

```text
push(10)   →  [10]
push(20)   →  [10, 20]
push(30)   →  [10, 20, 30]     ← 30 is the top
peek()     →  30               stack stays [10, 20, 30]
pop()      →  30               stack is now [10, 20]
pop()      →  20               stack is now [10]
```

The opposite of a stack is a **queue** (a line at a shop): the first one in is the first one out.

#### 4. The Call Stack (Asked in Interviews)

Your program uses a stack every time a function calls another function.

```kotlin
fun factorial(n: Int): Int = if (n <= 1) 1 else n * factorial(n - 1)
```

```text
factorial(3) calls factorial(2) calls factorial(1)

stack while running:   [f(3), f(2), f(1)]
f(1) returns 1         → f(1) leaves the stack
f(2) returns 2 * 1     → f(2) leaves
f(3) returns 3 * 2 = 6 → f(3) leaves
```

If the recursion goes too deep, this stack runs out of space and the program crashes with `StackOverflowError`. This is why some problems ask you to use **your own stack** instead of recursion.

#### 5. Kotlin Code

Use `ArrayDeque`. Always add and remove at the **end**.

```kotlin
val stack = ArrayDeque<Int>()

stack.addLast(10)                  // push
stack.addLast(20)
println(stack.last())              // peek → 20
println(stack.removeLast())        // pop  → 20
println(stack.isEmpty())           // false

// Popping an empty stack crashes. This version returns null instead:
println(stack.removeLastOrNull())  // 10
println(stack.removeLastOrNull())  // null
```

Example: reverse a string (push every character, then pop them all).

```kotlin
fun reverse(s: String): String {
    val stack = ArrayDeque<Char>()
    for (c in s) stack.addLast(c)
    val result = StringBuilder()
    while (stack.isNotEmpty()) result.append(stack.removeLast())
    return result.toString()
}
// reverse("stack") → "kcats"
```

Avoid `java.util.Stack` (old and slow). On a Java `Deque`, `push` and `pop` work at the **front**, so do not mix them with `addLast`.

#### 6. How to Spot a Stack Problem

| If the question has... | Think... |
|---|---|
| brackets, tags, nested pairs | match each closing one with the latest opening one |
| "next greater / smaller element" | monotonic stack |
| undo, go back, remove the last thing | pop |
| evaluate an expression | stack of numbers |
| "without recursion" | your own stack |

The full practice list is in section 11.

#### 7. Complexity

| Action | Time |
|---|---|
| `push`, `pop`, `peek`, `isEmpty` | `O(1)` |
| Memory for `n` items | `O(n)` |

#### 8. Common Mistakes

1. **Popping an empty stack.** It crashes. Check `isNotEmpty()` first or use `removeLastOrNull()`.
2. **Mixing the two ends** of a `Deque`.
3. **Forgetting the items left in the stack** after the loop. They are often part of the answer.
4. **Using a stack when you need the oldest item first.** That is a queue.

#### 9. Say This in the Interview

1. "The most recent item decides what happens next, so I will use a stack."
2. "Each item is pushed once and popped once, so time is `O(n)` and space is `O(n)`."
3. "Edge cases: empty input, one item, and leftovers in the stack."

#### 10. Quick Check

1. You push `1`, `2`, `3`, then pop once. What is on top?
2. Why does `")("` fail a bracket check?

<details>
<summary>Answers</summary>

1. `2`.
2. The first `)` arrives when the stack is empty, so there is no `(` to match it.

</details>

#### 11. Related LeetCode Questions (Often Asked)

Solve them in this order. The first column is the LeetCode number (search by title if a number looks wrong).

**Start here — Easy**

| # | Question | Main idea | Note in this folder |
|---|---|---|---|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | push opening, match closing with the top | 04 |
| 1047 | [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | pop when the new character equals the top | 20 |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | `#` means pop | 12 |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | two stacks, move only when the output stack is empty | Queue folder, note 14 |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | rotate the queue after each push | 22 |
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | monotonic stack + map | 06 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | keep the minimum so far next to each item | 13 |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | monotonic stack of indexes | 10 |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | pop two numbers, apply the operator, push | 16 |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/) | one stack for counts, one for text | 19 |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | `..` pops, names push | 18 |
| 735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | new left-mover pops smaller right-movers | 21 |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | delay `+`/`-`, do `*`/`/` at once | 12 |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | circular array: loop `2n` times | 06 |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | previous greater element | 09 |
| 402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | pop bigger digits before a smaller one | 12 |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | stack of indexes to remove | 04 |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | sort by position, stack of arrival times | 21 |

**Hard — these separate strong candidates**

| # | Question | Main idea | Note |
|---|---|---|---|
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | increasing stack, width from the new top | 11 |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | histogram for every row | 23 |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | decreasing stack (or two pointers) | 11 |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | stack of indexes, base `-1` | 04 |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | stack of results and signs for brackets | 12 |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | contribution technique | 25 |

**If you have little time, do these 8 first:** 20, 155, 739, 150, 394, 735, 84, 42.

Stack is also used inside tree questions: *Binary Tree Inorder Traversal* (94) and *Validate Binary Search Tree* (98) with an explicit stack. See note 14.

For a one-page revision of everything in this folder, read the **Stack Cheat Sheet** (note 26).
