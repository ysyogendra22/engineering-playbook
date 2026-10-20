# Deque

#### 1. What Is It?

A **deque** (say "deck", short for double-ended queue) lets you **add and remove at both ends**.

It can act as:

- a **queue**: add at the back, remove at the front,
- a **stack**: add and remove at the same end,
- or both at once.

In Kotlin, `ArrayDeque` is a deque. So the `ArrayDeque` you already use for stacks and queues is the deque.

Why interviewers care: a deque is the tool for **sliding window maximum** (note 13), **0-1 BFS** (note 17), palindrome checks from both ends, and undo/redo.

#### 2. How It Works

```text
         addFirst ↓                    ↓ addLast
front →  [ A ][ B ][ C ][ D ]  ← back
         removeFirst ↑                 ↑ removeLast

addFirst(X):    [ X ][ A ][ B ][ C ][ D ]
addLast(Y):     [ X ][ A ][ B ][ C ][ D ][ Y ]
removeFirst():  [ A ][ B ][ C ][ D ][ Y ]         X leaves
removeLast():   [ A ][ B ][ C ][ D ]              Y leaves
```

| Role | Calls you use |
|---|---|
| Queue | `addLast` + `removeFirst` |
| Stack | `addLast` + `removeLast` |
| Deque | any of the four |

Names in Kotlin and in Java:

| Action | Kotlin `ArrayDeque` | Java `Deque` (returns `null`/`false` on failure) |
|---|---|---|
| Add front | `addFirst(x)` | `offerFirst(x)` |
| Add back | `addLast(x)` | `offerLast(x)` |
| Remove front | `removeFirst()` / `removeFirstOrNull()` | `pollFirst()` |
| Remove back | `removeLast()` / `removeLastOrNull()` | `pollLast()` |
| Peek front | `first()` / `firstOrNull()` | `peekFirst()` |
| Peek back | `last()` / `lastOrNull()` | `peekLast()` |

Warning: on a Java `Deque`, `push(x)` adds to the **front** and `pop()` removes from the **front**. Do not mix them with `addLast`.

#### 3. Kotlin Code

```kotlin
val dq = ArrayDeque<Int>()

dq.addLast(2)
dq.addLast(3)
dq.addFirst(1)                    // [1, 2, 3]
println(dq.first())               // 1
println(dq.last())                // 3
println(dq.removeFirst())         // 1   → [2, 3]
println(dq.removeLast())          // 3   → [2]
println(dq[0])                    // 2   (index access works, O(1))

// Palindrome check: compare from both ends
fun isPalindrome(s: String): Boolean {
    val d = ArrayDeque<Char>()
    for (c in s) if (c.isLetterOrDigit()) d.addLast(c.lowercaseChar())
    while (d.size > 1) {
        if (d.removeFirst() != d.removeLast()) return false
    }
    return true
}
// isPalindrome("A man, a plan, a canal: Panama") → true

// Undo / redo with two deques
class History {
    private val undoStack = ArrayDeque<String>()
    private val redoStack = ArrayDeque<String>()

    fun perform(action: String) { undoStack.addLast(action); redoStack.clear() }
    fun undo(): String? = undoStack.removeLastOrNull()?.also { redoStack.addLast(it) }
    fun redo(): String? = redoStack.removeLastOrNull()?.also { undoStack.addLast(it) }
}
```

#### 4. Complexity

| Action | Time |
|---|---|
| `addFirst`, `addLast`, `removeFirst`, `removeLast`, `first`, `last` | `O(1)` |
| `deque[i]` (Kotlin `ArrayDeque`) | `O(1)` |
| `contains`, remove from the middle | `O(n)` |

#### 5. Common Mistakes

1. **Mixing `push`/`pop` (front) with `addLast`/`removeLast` (back)** on a Java `Deque`.
2. **`removeFirst()` or `first()` on an empty deque** crashes. Use the `...OrNull()` versions.
3. **Adding `null`** to `java.util.ArrayDeque`. It throws.
4. **Using the wrong end** and getting reversed order.
5. **Removing from the middle** and expecting `O(1)`.

#### 6. Say This in the Interview

1. "A deque gives `O(1)` add and remove at both ends, so I can use it as a stack, a queue, or both."
2. "For a sliding window maximum I keep a monotonic deque of indexes."
3. "For 0-1 BFS I push 0-cost neighbours to the front and 1-cost neighbours to the back."

#### 7. Quick Check

1. Which two calls make a deque behave like a stack?
2. Where does `push(x)` add on a Java `Deque`?

<details>
<summary>Answers</summary>

1. `addLast` and `removeLast` (or `addFirst` and `removeFirst`).
2. At the **front**.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 641 | Design Circular Deque (Medium) | ring buffer with two ends |
| 239 | Sliding Window Maximum (Hard) | monotonic deque (note 13) |
| 2290 | Minimum Obstacle Removal to Reach Corner (Hard) | 0-1 BFS (note 17) |
| 862 | Shortest Subarray with Sum at Least K (Hard) | monotonic deque (note 19) |
| 125 | Valid Palindrome (Easy) | compare from both ends |
