# Stack Operations & Complexity

#### 1. Definition — Must Know

1. The core stack operations are **push**, **pop**, **peek / top**, and **isEmpty**.
2. All of them run in **`O(1)`** time.
3. Different classes use different names for the same actions. You must know the Kotlin names and the Java names.

#### 2. Why It Is Used — Must Know

1. Every stack solution is built from these four calls.
2. Choosing the safe or throwing version matters when the stack may be empty.
3. Mixing the names of `Stack`, `Deque` and `ArrayDeque` is a common source of bugs.

#### 3. How It Works — Must Know

```text
Start:          []
push(1):        [1]
push(2):        [1, 2]
push(3):        [1, 2, 3]       ← 3 is the top
peek():         → 3             stack is still [1, 2, 3]
pop():          → 3             stack is [1, 2]
pop():          → 2             stack is [1]
isEmpty():      → false
pop():          → 1             stack is []
pop():          → error / null  (underflow)
```

#### 4. Core Concepts — Must Know

1. **Push** — add to the top.
2. **Pop** — remove and return the top.
3. **Peek / Top** — look at the top without removing.
4. **isEmpty** — true when there are no items.
5. **Names by class:**

| Action | Kotlin `ArrayDeque` | `java.util.Stack` | Java `Deque` (e.g. `java.util.ArrayDeque`) |
|---|---|---|---|
| Push | `addLast(x)` | `push(x)` | `push(x)` (adds to the **front**) |
| Pop | `removeLast()` | `pop()` | `pop()` (removes from the **front**) |
| Pop (safe) | `removeLastOrNull()` | — (throws `EmptyStackException`) | `poll()` / `pollFirst()` → `null` |
| Peek | `last()` | `peek()` | `peek()` (looks at the **front**) |
| Peek (safe) | `lastOrNull()` | — | `peek()` → `null` if empty |
| Empty | `isEmpty()` | `empty()` / `isEmpty()` | `isEmpty()` |

6. **Rule of thumb:** use Kotlin `ArrayDeque` with `addLast` / `removeLast` / `last()`. The names are clear and there is no front/back confusion.
7. **Other useful calls:** `size`, `clear()`, `contains(x)` (`O(n)`), iterating with `for (x in stack)` (bottom to top for `ArrayDeque`).
8. **Underflow handling:** decide the behaviour: throw, return `null`, or return a default.

#### 5. Algorithm — Must Know

Safe pop:

```text
if stack is not empty: value = pop()
else: handle "nothing to pop"
```

Check the top before acting on it:

```text
while stack is not empty and stack.top satisfies a condition: pop()
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val stack = ArrayDeque<String>()

// Push
stack.addLast("a")
stack.addLast("b")
stack.add("c")                     // add = addLast

// Peek
println(stack.last())              // c
println(stack.lastOrNull())        // c

// Pop
println(stack.removeLast())        // c
println(stack.removeLastOrNull())  // b

// isEmpty / size
println(stack.isEmpty())           // false
println(stack.size)                // 1

stack.clear()
println(stack.removeLastOrNull())  // null — no exception
// stack.removeLast()              // would throw NoSuchElementException

// Iterate bottom → top without removing
val s = ArrayDeque(listOf(1, 2, 3))
for (x in s) print("$x ")          // 1 2 3
println()

// Java-style Deque (note: push/pop/peek work at the FRONT)
val d: java.util.Deque<Int> = java.util.ArrayDeque()
d.push(1); d.push(2)
println(d.peek())                  // 2
println(d.pop())                   // 2

// Small helper for "peek or default"
fun <T> ArrayDeque<T>.peekOr(default: T): T = lastOrNull() ?: default
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Notes |
|---|---:|---|
| `push` | `O(1)` amortized | rare resize costs `O(n)` |
| `pop` | `O(1)` | |
| `peek` | `O(1)` | |
| `isEmpty` / `size` | `O(1)` | |
| `contains` | `O(n)` | |
| `clear` | `O(n)` | |
| Iteration | `O(n)` | |
| Space | `O(n)` | |

#### 8. Common Operation Patterns — Must Know

1. **Pop while the top is worse:** `while (stack.isNotEmpty() && stack.last() < x) stack.removeLast()` (monotonic stack).
2. **Pop two, push one:** evaluate an operator (`b = pop(); a = pop(); push(a op b)`).
3. **Push a marker:** `-1` or a sentinel index at the bottom to avoid empty checks.
4. **Peek then decide:** compare with the top before pushing.
5. **Drain at the end:** `while (stack.isNotEmpty()) …` to handle leftovers.
6. **Push pairs:** `IntArray` or `Pair` entries such as `(value, count)`.

#### 9. Edge Cases / Common Mistakes

1. Popping an empty stack.
2. Peeking at the wrong end of a `Deque` (`peek()` is the front).
3. Using `pop` before `peek` and then losing the value.
4. In two-operand evaluation: using the wrong order (`a - b` where `a` was pushed first).
5. Forgetting that `Stack.push` returns the item and `Deque.push` returns nothing.
6. Using `stack.remove(x)` (remove a specific item, `O(n)`) instead of `removeLast()`.
7. Checking `size > 0` repeatedly when `isNotEmpty()` is clearer.
8. Modifying the stack while iterating with `for`.

#### 10. When to Use / When Not to Use

**Use the throwing versions when:**

1. An empty stack means a bug in your logic and you want it to fail loudly.

**Use the safe versions when:**

1. Empty is a normal case (undo with nothing to undo).

#### 11. Related Topics

1. Stack Fundamentals — LIFO
2. Stack Implementation
3. Min Stack
4. Common Stack Edge Cases

#### 12. Interview Must Remember

1. **Push = `addLast`, pop = `removeLast`, peek = `last()`.**
2. Java `Deque.push/pop/peek` act on the **front**.
3. All are `O(1)`; check for empty before pop/peek.
4. Prefer `ArrayDeque` over `java.util.Stack`.
