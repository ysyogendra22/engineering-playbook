# Deque

#### 1. Definition — Must Know

1. A **deque** ("deck", double-ended queue) lets you **add and remove at both ends**.
2. It can act as a **queue** (add back, remove front), as a **stack** (add and remove at the same end), or as both at once.
3. In Kotlin, `ArrayDeque` is a deque.

#### 2. Why It Is Used — Must Know

1. One structure replaces both a stack and a queue.
2. It supports **sliding window maximum/minimum** (monotonic queue) in `O(n)`.
3. It supports **0-1 BFS** and **palindrome checks** from both ends.
4. Real uses: undo/redo, browser history, work stealing between threads.

#### 3. How It Works — Must Know

```text
        addFirst ↓                    ↓ addLast
front → [ A ][ B ][ C ][ D ] ← back
        removeFirst ↑                 ↑ removeLast

addFirst(X):   [ X ][ A ][ B ][ C ][ D ]
addLast(Y):    [ X ][ A ][ B ][ C ][ D ][ Y ]
removeFirst(): [ A ][ B ][ C ][ D ][ Y ]       (X leaves)
removeLast():  [ A ][ B ][ C ][ D ]            (Y leaves)
```

Different roles:

```text
Queue:  addLast + removeFirst
Stack:  addLast + removeLast     (or addFirst + removeFirst)
Deque:  any of the four
```

#### 4. Core Concepts — Must Know

1. **Four main operations:** `addFirst`, `addLast`, `removeFirst`, `removeLast`. Also `first()` and `last()` to look.
2. **All are `O(1)` amortized** on `ArrayDeque`.
3. **Kotlin `ArrayDeque`** also behaves like a list: `deque[i]` is `O(1)`, `size`, `contains` (`O(n)`).
4. **Java `Deque` names:**

| Action | Kotlin `ArrayDeque` | Java `Deque` (throws) | Java `Deque` (null/false) |
|---|---|---|---|
| Add front | `addFirst(x)` | `addFirst(x)` | `offerFirst(x)` |
| Add back | `addLast(x)` | `addLast(x)` | `offerLast(x)` |
| Remove front | `removeFirst()` / `removeFirstOrNull()` | `removeFirst()` | `pollFirst()` |
| Remove back | `removeLast()` / `removeLastOrNull()` | `removeLast()` | `pollLast()` |
| Peek front | `first()` / `firstOrNull()` | `getFirst()` | `peekFirst()` |
| Peek back | `last()` / `lastOrNull()` | `getLast()` | `peekLast()` |

5. **Warning:** on a Java `Deque`, `push(x)` adds to the **front** and `pop()` removes from the front. Mixing `push` with `addLast` is confusing.
6. **`java.util.ArrayDeque` does not allow `null`.** Kotlin's does.
7. **Bounded deque / circular deque:** fixed size, wrap-around indices (LeetCode 641).

#### 5. Algorithm — Must Know

Palindrome check with a deque:

```text
put all characters in a deque
while size > 1:
    if removeFirst() != removeLast(): not a palindrome
palindrome
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val dq = ArrayDeque<Int>()

dq.addLast(2)
dq.addLast(3)
dq.addFirst(1)                    // [1, 2, 3]
println(dq.first())               // 1
println(dq.last())                // 3
println(dq.removeFirst())         // 1   → [2, 3]
println(dq.removeLast())          // 3   → [2]
println(dq[0])                    // 2   (index access works)

// As a stack
val stack = ArrayDeque<Int>()
stack.addLast(1); stack.addLast(2)
println(stack.removeLast())       // 2

// As a queue
val queue = ArrayDeque<Int>()
queue.addLast(1); queue.addLast(2)
println(queue.removeFirst())      // 1

// Palindrome check from both ends
fun isPalindrome(s: String): Boolean {
    val d = ArrayDeque<Char>()
    for (c in s) if (c.isLetterOrDigit()) d.addLast(c.lowercaseChar())
    while (d.size > 1) {
        if (d.removeFirst() != d.removeLast()) return false
    }
    return true
}

// Undo / redo with two deques (idea)
class History {
    private val undo = ArrayDeque<String>()
    private val redo = ArrayDeque<String>()

    fun perform(action: String) { undo.addLast(action); redo.clear() }
    fun undo(): String? = undo.removeLastOrNull()?.also { redo.addLast(it) }
    fun redo(): String? = redo.removeLastOrNull()?.also { undo.addLast(it) }
}
```

Java style:

```kotlin
import java.util.Deque
import java.util.ArrayDeque as JavaArrayDeque

val d: Deque<Int> = JavaArrayDeque()
d.offerFirst(1)
d.offerLast(2)
println(d.pollFirst())    // 1
println(d.pollLast())     // 2
println(d.pollFirst())    // null
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `addFirst` / `addLast` | `O(1)` amortized |
| `removeFirst` / `removeLast` | `O(1)` |
| `first` / `last` | `O(1)` |
| `get(i)` (Kotlin `ArrayDeque`) | `O(1)` |
| `contains` | `O(n)` |
| Insert / remove in the middle | `O(n)` |
| Space | `O(n)` |

#### 8. Common Deque Patterns — Must Know

1. **Sliding Window Maximum** (LeetCode 239) — monotonic deque.
2. **0-1 BFS** — front for weight 0, back for weight 1.
3. **Palindrome check** from both ends.
4. **Design Circular Deque** (LeetCode 641).
5. **Undo / redo history** and browser back/forward.
6. **Work-stealing queues** (one thread takes from the front, others steal from the back).
7. **Shortest Subarray with Sum at Least K** (LeetCode 862) — monotonic deque.
8. **Android example:** the back stack as a deque; a list of recent searches (add front, trim the back).

#### 9. Edge Cases / Common Mistakes

1. Mixing `push`/`pop` (front) with `addLast`/`removeLast` on a Java `Deque`.
2. `removeFirst()`, `first()` on an empty deque throw. Use the `...OrNull()` versions.
3. Adding `null` to `java.util.ArrayDeque`.
4. Using `removeAt(i)` in the middle and expecting `O(1)`.
5. Forgetting that `ArrayDeque.remove(x)` (by value) is `O(n)`.
6. Assuming the deque is sorted. It only keeps insertion positions.
7. Using the wrong end for a stack/queue role and getting reverse order.
8. Calling `removeFirst()` on a `MutableList` in JDK 21 builds and expecting it to exist on older Android versions. Use `ArrayDeque`.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need both ends, or one structure for stack and queue.
2. You solve window max/min or 0-1 BFS.

**Avoid when:**

1. You need only one end. A stack or queue name states your intent better.
2. You need fast removal from the middle. Use a linked list with a map.

#### 11. Related Topics

1. Queue Operations
2. Monotonic Queue
3. 0-1 BFS
4. Circular Queue
5. Stack (`01-data-structure/03-Stack`)

#### 12. Interview Must Remember

1. **Deque = add and remove at both ends, all `O(1)`.**
2. Kotlin: `ArrayDeque` with `addFirst/addLast/removeFirst/removeLast`.
3. Java `Deque.push` adds to the **front**.
4. Used for sliding window max, 0-1 BFS, palindromes.
