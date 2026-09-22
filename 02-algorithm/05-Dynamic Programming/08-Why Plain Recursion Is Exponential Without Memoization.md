# Why Plain Recursion Is Exponential Without Memoization

#### 1. Definition — Must Know

When a recursive function has overlapping subproblems (topic 1) but **no cache**, the same subproblems get recomputed again and again — and the total number of calls grows exponentially with the input size.

#### 2. Why It Is Used — Must Know

1. This is the concrete "before" picture that motivates every DP solution — it's worth being able to explain *why* naive recursion is slow, not just that it is.
2. Being able to say the actual number (O(2ⁿ)) and *why* it's that shape is a strong, precise interview answer.

#### 3. How It Works — Must Know

Naive Fibonacci calls itself twice per call, and the recursion tree roughly doubles in size at every level (see the recursion tree in `03-Recursion & Divide and Conquer/04`):

```text
fib(n) makes 2 calls: fib(n-1) and fib(n-2)
Each of those makes 2 more calls, and so on...

Level 0:  1 call    (fib(n))
Level 1:  2 calls    (fib(n-1), fib(n-2))
Level 2:  4 calls
Level 3:  8 calls
...
Level k: ~2^k calls

Total calls ≈ 2^0 + 2^1 + ... + 2^n ≈ 2^(n+1) - 1  →  O(2ⁿ)
```

`fib(30)` alone makes over 2.7 million calls, almost all of them repeats of a call already made.

#### 4. Algorithm — Must Know

```text
To see this for any recursive function, ask:
1. How many recursive calls does one call make?           (the "branching factor")
2. How much does the input shrink per call?                (usually by 1)
3. If branching factor > 1 and shrink is small (by 1),
   the tree grows exponentially — O(branching_factor ^ depth)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Naive — exponential
fun fibSlow(n: Int): Long {
    if (n <= 1) return n.toLong()
    return fibSlow(n - 1) + fibSlow(n - 2)   // 2 calls per call → exponential
}

// Memoized — linear (see `02-Top-Down (Memoization) vs Bottom-Up (Tabulation)`)
fun fibFast(n: Int, cache: MutableMap<Int, Long> = mutableMapOf()): Long {
    if (n <= 1) return n.toLong()
    cache[n]?.let { return it }
    return (fibFast(n - 1, cache) + fibFast(n - 2, cache)).also { cache[n] = it }
}
```

#### 6. Complexity — Must Know

| Version | Time | Why |
|---|---|---|
| `fibSlow` | O(2ⁿ) | Every call branches into 2 more, with almost no shrinkage in depth |
| `fibFast` (memoized) | O(n) | Each of the n distinct subproblems is computed exactly once |

#### 7. Common Mistakes — Must Know

1. Writing a correct recursive solution, running it on a small test case where it's fast, and not noticing it will time out on a larger input.
2. Assuming any recursive function is "automatically" exponential — this only happens when subproblems overlap **and** aren't cached (Merge Sort, for instance, is recursive but not exponential, since its subproblems don't overlap).
3. Adding memoization without first checking that the subproblems actually repeat — caching a function whose calls never repeat adds overhead for no benefit.

#### 8. Related Topics

1. `1` Optimal Substructure & Overlapping Subproblems — the property that causes this
2. `2` Top-Down (Memoization) vs Bottom-Up (Tabulation) — the fix
3. `4` Recursion Tree & Tracing Complexity by Hand (in the Recursion folder) — the way to see this happening

#### 9. Interview Must Remember

1. **Exponential blow-up = overlapping subproblems + no cache.** State both halves of that sentence.
2. Naive Fibonacci is the standard example: O(2ⁿ) without memoization, O(n) with it.
3. This is your justification for adding a cache — not just "it feels faster", but a specific, provable reason.
