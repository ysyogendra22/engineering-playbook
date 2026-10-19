# Min Stack

#### 1. Definition — Must Know

1. A **Min Stack** is a stack that supports `push`, `pop`, `top` **and `getMin()` — the smallest item currently in the stack — all in `O(1)`**.
2. It is *Min Stack* (LeetCode 155). If a number and a title ever disagree, trust the title.
3. The trick: each stack entry also remembers **the minimum at the time it was pushed**.

#### 2. Why It Is Used — Must Know

1. It is a common design question.
2. A normal stack finds the minimum only by scanning all items (`O(n)`).
3. The idea (store extra info with each item) is reused in Max Stack, Max Frequency Stack and queues with min/max.

#### 3. How It Works — Must Know

Keep a second stack (`minStack`) that stores the minimum **so far** at each level.

```text
push(5):    stack [5]            minStack [5]
push(3):    stack [5, 3]         minStack [5, 3]       (3 < 5 → new min)
push(7):    stack [5, 3, 7]      minStack [5, 3, 3]    (7 is not smaller → repeat the old min)
getMin():   → 3
pop():      stack [5, 3]         minStack [5, 3]
pop():      stack [5]            minStack [5]
getMin():   → 5
```

Because both stacks always have the same size, `pop` removes from both, and the minimum "goes back" to the correct earlier value automatically.

#### 4. Core Concepts — Must Know

1. **Two parallel stacks:** `stack` (values) and `minStack` (the minimum at each level).
2. **Push:** `minStack.push(min(x, minStack.top))` (or `x` if empty).
3. **Pop:** pop from both.
4. **`getMin`:** `minStack.top`. `O(1)`.
5. **One-stack variant:** store pairs `(value, minSoFar)` in a single stack.
6. **Space-saving variant:** push to `minStack` only when `x <= currentMin`, and pop from it only when the popped value equals the min. Use `<=` so duplicates of the minimum are handled.
7. **The same idea gives Max Stack** (flip the comparison).
8. **Time/space trade-off:** `O(1)` operations cost `O(n)` extra space.

| Design | Space | Notes |
|---|---|---|
| Parallel `minStack` (push every time) | `O(n)` | simplest |
| Pairs `(value, min)` in one stack | `O(n)` | one structure |
| `minStack` only on new minimum (`<=`) | `O(k)` | `k` = number of new minimums |

#### 5. Algorithm — Must Know

```text
push(x):   stack.push(x);  minStack.push(minStack empty ? x : min(x, minStack.top))
pop():     minStack.pop();  return stack.pop()
top():     return stack.top
getMin():  return minStack.top
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Two stacks
class MinStack {
    private val stack = ArrayDeque<Int>()
    private val minStack = ArrayDeque<Int>()

    fun push(x: Int) {
        stack.addLast(x)
        val currentMin = minStack.lastOrNull()
        minStack.addLast(if (currentMin == null) x else minOf(x, currentMin))
    }

    fun pop() {
        stack.removeLast()
        minStack.removeLast()
    }

    fun top(): Int = stack.last()

    fun getMin(): Int = minStack.last()
}

// One stack of pairs
class MinStackPairs {
    private val stack = ArrayDeque<IntArray>()            // [value, minSoFar]

    fun push(x: Int) {
        val min = if (stack.isEmpty()) x else minOf(x, stack.last()[1])
        stack.addLast(intArrayOf(x, min))
    }

    fun pop() { stack.removeLast() }
    fun top(): Int = stack.last()[0]
    fun getMin(): Int = stack.last()[1]
}

// Space-saving: push to minStack only on a new minimum (<=)
class MinStackCompact {
    private val stack = ArrayDeque<Int>()
    private val minStack = ArrayDeque<Int>()

    fun push(x: Int) {
        stack.addLast(x)
        if (minStack.isEmpty() || x <= minStack.last()) minStack.addLast(x)
    }

    fun pop() {
        val removed = stack.removeLast()
        if (removed == minStack.last()) minStack.removeLast()
    }

    fun top(): Int = stack.last()
    fun getMin(): Int = minStack.last()
}

// Usage
val m = MinStack()
m.push(-2); m.push(0); m.push(-3)
println(m.getMin())   // -3
m.pop()
println(m.top())      // 0
println(m.getMin())   // -2
```

A Max Stack is the same code with `maxOf`.

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `push` | `O(1)` |
| `pop` | `O(1)` |
| `top` | `O(1)` |
| `getMin` | `O(1)` |
| Space | `O(n)` extra (compact version: only for new minimums) |

#### 8. Common Min/Max Stack Patterns — Must Know

1. **Min Stack** (LeetCode 155).
2. **Max Stack** (LeetCode 716, premium) — needs `popMax`, which is harder (a stack plus a sorted structure).
3. **Maximum Frequency Stack** (LeetCode 895) — a map of frequency → stack.
4. **Queue with `getMin` in `O(1)`** — two min-stacks (queue from two stacks).
5. **Running minimum/maximum** in streams.
6. **Android example:** the lowest battery level or frame time seen since the last reset, with undo.

#### 9. Edge Cases / Common Mistakes

1. Pushing to `minStack` only when `x < min` (strict) with the compact version. Duplicate minimums then break after a `pop`. Use `<=`.
2. Forgetting to pop `minStack` together with `stack`.
3. Calling `getMin` / `top` on an empty stack. State what you do.
4. Using a single `min` variable. After popping the minimum you cannot recover the previous one.
5. Comparing `Int` objects with `===`. Use `==`.
6. First push: `minStack` is empty, so the min is `x` itself.
7. Negative numbers and `Int.MIN_VALUE` are fine here (no arithmetic tricks), unlike the "encode the difference" one-stack trick, which can overflow.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need `O(1)` min (or max) with push/pop.

**Avoid when:**

1. You need the min of arbitrary ranges or of a sliding window (monotonic queue or a segment tree).
2. Memory is very tight and the compact variant is acceptable.

#### 11. Related Topics

1. Stack Implementation
2. Stack Using Queues
3. Queue Using Two Stacks (`01-data-structure/04-Queue/14-Queue Using Two Stacks.md`)
4. Monotonic Queue (`01-data-structure/04-Queue/13-Monotonic Queue.md`)

#### 12. Interview Must Remember

1. **Each push also records the minimum so far (second stack or pairs).**
2. Pop both stacks together; `getMin` is the top of `minStack`.
3. Compact version: push on `x <= min` (not `<`).
4. All operations `O(1)`; extra space `O(n)`.
