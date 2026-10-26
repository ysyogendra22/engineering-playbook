# Min Stack

#### 1. What Is It?

A **Min Stack** is a stack that also tells you the **smallest item currently inside it**, in `O(1)` time.

| Operation | Must be |
|---|---|
| `push(x)` | `O(1)` |
| `pop()` | `O(1)` |
| `top()` | `O(1)` |
| `getMin()` | `O(1)` |

This is *Min Stack* (LeetCode 155). It is a very common design question.

The problem: a normal stack can only find the minimum by looking at every item (`O(n)`). And one variable `min` is not enough: if you pop the minimum, you do not know what the old minimum was.

**Idea:** every time you push, also remember **the minimum so far**.

#### 2. How It Works

Keep a second stack, `minStack`. It has the same size as the main stack. At each level it stores the smallest value from the bottom up to that level.

```text
push(5):   stack [5]          minStack [5]
push(3):   stack [5, 3]       minStack [5, 3]       3 is smaller → new minimum
push(7):   stack [5, 3, 7]    minStack [5, 3, 3]    7 is not smaller → repeat the old minimum
getMin():  → 3                (top of minStack)

pop():     stack [5, 3]       minStack [5, 3]       7 leaves
pop():     stack [5]          minStack [5]          3 leaves, and the minimum goes back to 5
getMin():  → 5
```

Because both stacks always have the same size, popping both keeps them in step. The old minimum comes back by itself.

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | scan all items in `getMin()` | store the minimum next to each item |
| `getMin()` | `O(n)` | `O(1)` |
| Extra space | `O(1)` | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
class MinStackBrute {
    private val items = ArrayList<Int>()

    fun push(x: Int) { items.add(x) }
    fun pop() { items.removeAt(items.size - 1) }
    fun top(): Int = items.last()
    fun getMin(): Int = items.min()          // scans every item: O(n)   (Kotlin 1.7+)
}
```

The question asks for `O(1)` `getMin()`, so we trade `O(n)` extra memory for speed.

#### 4. Kotlin Code

```kotlin
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

// Usage
val m = MinStack()
m.push(-2); m.push(0); m.push(-3)
println(m.getMin())   // -3
m.pop()
println(m.top())      // 0
println(m.getMin())   // -2
```

**Same idea, one stack.** Store pairs `[value, minSoFar]`:

```kotlin
class MinStackPairs {
    private val stack = ArrayDeque<IntArray>()               // [value, minSoFar]

    fun push(x: Int) {
        val min = if (stack.isEmpty()) x else minOf(x, stack.last()[1])
        stack.addLast(intArrayOf(x, min))
    }

    fun pop() { stack.removeLast() }
    fun top(): Int = stack.last()[0]
    fun getMin(): Int = stack.last()[1]
}
```

A **Max Stack** is the same code with `maxOf`.

#### 5. Complexity

| Operation | Time |
|---|---|
| `push`, `pop`, `top`, `getMin` | `O(1)` |
| Extra memory | `O(n)` (the second stack) |

#### 6. Common Mistakes

1. **Using one `min` variable.** After you pop the minimum you cannot get the previous one.
2. **Popping only one stack.** Always pop both.
3. **Calling `getMin()` or `top()` on an empty stack.** Say how you handle it (throw, or the problem guarantees it does not happen).
4. **Space-saving trick done wrong.** Some solutions push onto `minStack` only when `x` is a new minimum. Then use `x <= min` (not `<`), or duplicate minimums break after a pop.

#### 7. Say This in the Interview

1. "A single `min` variable fails when the minimum is popped, so I store the minimum with every item."
2. "I keep a second stack with the minimum so far. Push and pop both stacks together."
3. "All four operations are `O(1)`. The cost is `O(n)` extra space."
4. "For a Max Stack I only flip the comparison."

#### 8. Quick Check

1. Push `4`, `2`, `6`. What is `getMin()`? Pop twice. What is `getMin()` now?
2. Why must `minStack` repeat the old minimum when you push `7` on top of `3`?

<details>
<summary>Answers</summary>

1. `2`. After two pops only `4` remains, so `getMin()` is `4`.
2. So both stacks have the same size. Then one `pop` on each keeps them in step.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) (Medium) | this note |
| 716 | [Max Stack](https://leetcode.com/problems/max-stack/) (Hard, premium) | needs `popMax` too |
| 895 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) (Hard) | map from frequency to stack |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) (Easy) | design with stacks |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) (Medium) | stack design |
