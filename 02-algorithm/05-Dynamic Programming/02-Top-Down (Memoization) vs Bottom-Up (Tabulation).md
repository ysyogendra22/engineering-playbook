# Top-Down (Memoization) vs Bottom-Up (Tabulation)

#### 1. Definition — Must Know

1. **Top-down**: write the normal recursive solution, add a cache. You start from the big problem and work down to base cases, caching along the way.
2. **Bottom-up (tabulation)**: start from the base cases and build a table up to the final answer, using a loop instead of recursion.
3. Both compute the exact same answers — they just build them in opposite directions.

#### 2. Why It Is Used — Must Know

1. Top-down is usually the easier one to *write first* — it's your recursive solution plus a cache, so it reads naturally.
2. Bottom-up is usually faster in practice (no function call overhead, no recursion depth limit) and makes space optimisation (topic 7) much easier to see.

#### 3. How It Works — Must Know

Fibonacci, both ways:

```text
Top-down: start at fib(5), and go DOWN as needed
fib(5) needs fib(4) and fib(3)
   fib(4) needs fib(3) [cached!] and fib(2)
     ...
   until base cases are hit, then answers bubble back UP

Bottom-up: start at fib(0) and fib(1), and go UP
fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1
fib(3) = fib(2) + fib(1) = 2
fib(4) = fib(3) + fib(2) = 3
fib(5) = fib(4) + fib(3) = 5
```

#### 4. Algorithm — Must Know

```text
Top-down:
  cache = {}
  function f(n):
      if n in cache: return cache[n]
      if base case: return base answer
      result = combine(f(smaller n))
      cache[n] = result
      return result

Bottom-up:
  table[base cases] = base answers
  for each state, smallest to largest:
      table[state] = combine(table[smaller states])
  return table[final state]
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Top-down
fun fibTopDown(n: Int, cache: MutableMap<Int, Long> = mutableMapOf()): Long {
    if (n <= 1) return n.toLong()
    cache[n]?.let { return it }
    val result = fibTopDown(n - 1, cache) + fibTopDown(n - 2, cache)
    cache[n] = result
    return result
}

// Bottom-up
fun fibBottomUp(n: Int): Long {
    if (n <= 1) return n.toLong()
    val table = LongArray(n + 1)
    table[1] = 1
    for (i in 2..n) table[i] = table[i - 1] + table[i - 2]
    return table[n]
}
```

#### 6. Complexity — Must Know

| | Time | Space | Notes |
|---|---|---|---|
| Top-down | O(n) | O(n) cache + O(n) stack depth | Easier to write from the recursive version |
| Bottom-up | O(n) | O(n) table (can often shrink, topic 7) | No recursion, no stack-depth risk |

Same time complexity either way — the real trade-off is **how you get there**, and how easy the space is to optimise afterward.

#### 7. Common Mistakes — Must Know

1. In top-down: forgetting to check the cache before doing the recursive work (see Memoization, topic 8 in the Recursion folder).
2. In bottom-up: filling the table in the wrong order, so a cell is used before it's actually computed.
3. Assuming one approach is always "better" — top-down is often clearer to reason about first; bottom-up is often easier to optimise for space afterward. Use whichever helps you finish correctly first.

#### 8. Related Topics

1. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — how you decide the bottom-up fill order
2. `7` Space Optimisation — Keeping Only the Last Row or Two — much easier to see in bottom-up form
3. `8` Memoization — the Bridge to Dynamic Programming (in the Recursion folder)

#### 9. Interview Must Remember

1. **Start top-down** if you're unsure — write the recursion first, then add a cache.
2. **Convert to bottom-up** once the recurrence is clear — it's usually a small rewrite, and helps with space optimisation.
3. Both give the same answer and the same Big-O time — the difference is style, stack usage, and how easy further optimisation is.
