# Memoization — the Bridge to Dynamic Programming

#### 1. Definition — Must Know

1. **Memoization** means saving the result of a function call the first time you compute it, so that if the same call happens again, you return the saved answer instead of recomputing it.
2. It is the simplest way to turn a slow recursive function into a fast one, once you notice the same subproblem is being solved more than once (see the repeated `fib(2)` and `fib(1)` calls in topic 4's recursion tree).

#### 2. Why It Is Used — Must Know

1. Plain recursive Fibonacci is O(2ⁿ) because it recomputes the same values again and again. Memoization brings it down to O(n).
2. It is the first step toward Dynamic Programming (topic 5 in `02-algorithm`) — DP is really "recursion plus memoization", organised more carefully.

#### 3. How It Works — Must Know

```text
fib(4) without memoization:      fib(4) with memoization:

        fib(4)                          fib(4)
       /      \                        /      \
   fib(3)    fib(2)                fib(3)    fib(2) ← already cached, return instantly
   /   \      /   \                /   \
fib(2) fib(1) fib(1) fib(0)    fib(2) fib(1)
 ...repeats fib(2), fib(1)...    (fib(2) computed once, cached, reused)
```

1. The first time `fib(2)` is computed, save its answer in a cache (a `HashMap` or an array).
2. The next time `fib(2)` is requested, look it up in the cache and return it immediately — no recursion needed.

#### 4. Algorithm — Must Know

```text
cache = empty map

function f(n):
    if n is in cache:
        return cache[n]
    if n meets the base case:
        result = base answer
    else:
        result = combine(n, f(smaller n))
    cache[n] = result
    return result
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun fib(n: Int, cache: MutableMap<Int, Long> = mutableMapOf()): Long {
    if (n <= 1) return n.toLong()
    cache[n]?.let { return it }                 // cache hit — return immediately
    val result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result                            // cache the result before returning
    return result
}
```

#### 6. Complexity — Must Know

| Version | Time | Space |
|---|---|---|
| Naive recursive `fib(n)` | O(2ⁿ) | O(n) stack depth |
| Memoized `fib(n)` | O(n) | O(n) cache + O(n) stack depth |

Each distinct subproblem (`fib(0)` through `fib(n)`) is now computed exactly once, instead of exponentially many times.

#### 7. Common Mistakes — Must Know

1. Forgetting to check the cache **before** doing the recursive work — you must look it up first.
2. Forgetting to **save** the result into the cache before returning it.
3. Using a cache key that doesn't fully describe the subproblem (for example, only `n` when the function actually depends on `n` and some other changing parameter too).
4. Not resetting or scoping the cache correctly between separate top-level calls, when that matters.

#### 8. Related Topics

1. `4` Recursion Tree & Tracing Complexity by Hand — how you spot that memoization is needed
2. `5` Dynamic Programming (its own folder) — the fuller, more structured version of this idea
3. `9` Classic Divide & Conquer — problems where the pieces don't repeat, so memoization has nothing to save

#### 9. Interview Must Remember

1. Memoization = **cache the result of each distinct input**, so you never solve the same subproblem twice.
2. It only helps when subproblems genuinely **repeat** — check the recursion tree first (topic 4).
3. Saying "I'll memoize this" and pointing at the repeated calls in the tree is a strong, concrete interview answer.
