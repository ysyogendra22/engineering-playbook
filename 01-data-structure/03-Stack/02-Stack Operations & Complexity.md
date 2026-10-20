# Stack Operations & Complexity

#### 1. What Is It?

A stack has four basic operations. You must know them by heart, and you must know **which Kotlin call does each one**.

| Operation | What it does | Kotlin `ArrayDeque` | When the stack is empty |
|---|---|---|---|
| **Push** | add on top | `addLast(x)` | — |
| **Pop** | remove the top and return it | `removeLast()` | crashes (`NoSuchElementException`) |
| **Pop (safe)** | same, but safe | `removeLastOrNull()` | returns `null` |
| **Peek** | look at the top | `last()` | crashes |
| **Peek (safe)** | same, but safe | `lastOrNull()` | returns `null` |
| **isEmpty** | any items? | `isEmpty()` / `isNotEmpty()` | — |

Use **`ArrayDeque`** and always work at the **end**. That is the whole rule.

Other classes you may see (do not use them in new code):

| Class | Push / pop / peek | Why avoid |
|---|---|---|
| `java.util.Stack` | `push` / `pop` / `peek` | old and slow |
| `java.util.Deque` (Java) | `push` / `pop` / `peek` | work at the **front**, easy to mix up with `addLast` |

#### 2. How It Works

Most stack solutions use one of three small patterns. Learn to recognise them.

**Pattern A — pop while the top is worse (monotonic stack)**

```text
nums = [2, 1, 5]    find the next bigger number for each

see 2 → push                 [2]
see 1 → 1 < 2, push          [2, 1]
see 5 → 5 > 1, pop 1 (its answer is 5)
        5 > 2, pop 2 (its answer is 5)
        push 5               [5]
```

**Pattern B — pop two, push one (calculators)**

```text
tokens: 3 4 +      → push 3, push 4, then "+": pop 4, pop 3, push 3 + 4 = 7
```

**Pattern C — push, and pop to undo (matching, backspace)**

```text
text: a b # c      → push a, push b, "#" pops b, push c → result "ac"
```

#### 3. Kotlin Code

```kotlin
val stack = ArrayDeque<Int>()

stack.addLast(1)                   // push
stack.addLast(2)
stack.addLast(3)

println(stack.last())              // peek → 3
println(stack.removeLast())        // pop  → 3
println(stack.size)                // 2
println(stack.isNotEmpty())        // true

// Pattern A: pop while the top is smaller than the new number
fun popWhileSmaller(stack: ArrayDeque<Int>, x: Int) {
    while (stack.isNotEmpty() && stack.last() < x) stack.removeLast()
    stack.addLast(x)
}

// Pattern B: pop two numbers, push the result. Pop the RIGHT number first.
fun applyMinus(stack: ArrayDeque<Int>) {
    val b = stack.removeLast()     // right number
    val a = stack.removeLast()     // left number
    stack.addLast(a - b)           // "5 3 -" means 5 - 3 = 2, not 3 - 5
}

// Safe pop on a stack that might be empty
val top: Int? = stack.removeLastOrNull()
```

Read the items without removing them: `for (x in stack)` goes from **bottom to top**.

#### 4. Complexity

| Operation | Time |
|---|---|
| `push`, `pop`, `peek`, `isEmpty`, `size` | `O(1)` |
| `contains(x)` / search | `O(n)` |
| Memory for `n` items | `O(n)` |

Many stack solutions have a `while` loop inside a `for` loop. That is still `O(n)`, because **each item is pushed once and popped once**.

#### 5. Common Mistakes

1. **Pop or peek on an empty stack.** Check `isNotEmpty()` inside the `while` condition, before `last()`.
2. **Wrong operand order.** For `-` and `/`, pop the right number first, then the left.
3. **Using `remove(x)`.** It removes a specific value (`O(n)`), not the top. Use `removeLast()`.
4. **Changing the stack inside `for (x in stack)`.** It crashes. Use a `while` loop.

#### 6. Say This in the Interview

1. "I push as I scan, and pop when the top no longer helps."
2. "The `while` loop does not make it `O(n²)`, because every item is popped at most once."
3. "I check for an empty stack before reading the top."

#### 7. Quick Check

1. Why is `while (stack.last() < x)` risky?
2. For tokens `8 2 /`, which number do you pop first?

<details>
<summary>Answers</summary>

1. If the stack is empty, `last()` crashes. Write `stack.isNotEmpty() && stack.last() < x`.
2. `2` (the right number). Then pop `8`. The result is `8 / 2 = 4`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Pattern |
|---|---|---|
| 20 | Valid Parentheses (Easy) | C — match and pop |
| 1047 | Remove All Adjacent Duplicates In String (Easy) | C — pop to undo |
| 844 | Backspace String Compare (Easy) | C — `#` pops |
| 150 | Evaluate Reverse Polish Notation (Medium) | B — pop two, push one |
| 739 | Daily Temperatures (Medium) | A — pop while smaller |
