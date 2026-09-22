# Optimal Substructure & Overlapping Subproblems

#### 1. Definition — Must Know

1. **Optimal substructure**: the best answer to a problem can be built from the best answers to its smaller pieces.
2. **Overlapping subproblems**: solving the problem the normal recursive way ends up solving the exact same smaller problem again and again.
3. A problem needs **both** properties for Dynamic Programming (DP) to help. Miss either one and DP either doesn't apply, or doesn't speed anything up.

#### 2. Why It Is Used — Must Know

1. This is the two-question test to run *before* reaching for DP: "does the best answer come from best sub-answers?" and "do I keep solving the same sub-answer more than once?"
2. It's also the cleanest way to explain, out loud, *why* a problem is a DP problem — not just "it feels like DP".

#### 3. How It Works — Must Know

Fibonacci has both properties:

```text
fib(5) = fib(4) + fib(3)              ← optimal substructure: built from smaller answers
fib(4) = fib(3) + fib(2)
                 ↑
        fib(3) appears in both fib(5)'s and fib(4)'s expansion — overlapping subproblem
```

Contrast with **Merge Sort** (topic 3 in `02-algorithm`'s Recursion folder): it has optimal substructure (the sorted whole is built from sorted halves), but **no** overlapping subproblems — the left half and right half are completely different data, never recomputed. That's why Merge Sort doesn't benefit from memoization, even though it's recursive.

#### 4. Algorithm — Must Know

```text
Ask two questions:
1. Can I express the answer to the whole problem using answers to smaller
   versions of the same problem?             → optimal substructure?
2. If I solve it with plain recursion, do the same smaller inputs
   come up more than once?                    → overlapping subproblems?

Both YES  →  Dynamic Programming will help (memoize or tabulate)
Only Q1   →  plain divide and conquer is enough (no caching needed)
Neither   →  DP is not the right tool here
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// A quick way to SEE overlapping subproblems: count how many times each n is requested.
val callCounts = mutableMapOf<Int, Int>()

fun fibCountCalls(n: Int): Int {
    callCounts[n] = (callCounts[n] ?: 0) + 1
    if (n <= 1) return n
    return fibCountCalls(n - 1) + fibCountCalls(n - 2)
}
// fibCountCalls(10) will show callCounts[2] and callCounts[3] called many times over —
// that repetition is the overlapping-subproblems signal.
```

#### 6. Complexity — Must Know

| Property present | What it means for complexity |
|---|---|
| Optimal substructure only | Recursion works, no speed-up from caching needed |
| Both properties | Naive recursion is often exponential; caching brings it down to polynomial |

#### 7. Common Mistakes — Must Know

1. Reaching for DP on a problem that has optimal substructure but **no** overlapping subproblems — the caching adds memory cost for no benefit.
2. Assuming any recursive problem automatically has overlapping subproblems — check by actually tracing a few calls (topic 4 in the Recursion folder).
3. Missing optimal substructure — some problems' best answer does *not* come cleanly from best sub-answers (this is often where greedy also fails, and DP is the fallback specifically because it tries all sub-choices instead of committing to one).

#### 8. Related Topics

1. `4` Recursion Tree & Tracing Complexity by Hand (in the Recursion folder) — how you spot the repeated calls
2. `2` Top-Down (Memoization) vs Bottom-Up (Tabulation) — what to do once both properties are confirmed
3. `8` Memoization — the Bridge to Dynamic Programming (in the Recursion folder)

#### 9. Interview Must Remember

1. **Two checks, always:** optimal substructure, and overlapping subproblems.
2. If a problem only has the first, plain recursion or divide and conquer is enough — DP would be wasted effort.
3. "The same subproblem keeps appearing" is the concrete, provable reason to say "this needs DP" in an interview.
