# Classic Divide & Conquer — Max Subarray, Closest Pair, Fast Exponentiation

#### 1. Definition — Must Know

A short tour of three named problems that use divide and conquer (topic 3), beyond sorting and searching. Know the idea of each — full code is optional.

#### 2. Why It Is Used — Must Know

1. These are the examples interviewers reach for when they want to check you can apply divide and conquer to something other than sorting.
2. Each shows a slightly different "combine" step, which is usually where the real thinking happens.

#### 3. How It Works — Must Know

**Maximum Subarray (divide and conquer version)**

```text
Split the array in half.
The best subarray is either:
  entirely in the left half, or
  entirely in the right half, or
  crosses the middle (must be handled directly by scanning outward from the midpoint)
Take the best of the three.
```

*(In practice, Kadane's algorithm solves this in O(n) with a single pass — see `03-leetcode-patterns` topic 20. The divide and conquer version is O(n log n) and exists mainly to show the technique.)*

**Closest Pair of Points**

```text
Split the points into a left half and a right half (by x-coordinate).
Recursively find the closest pair in each half.
The true answer might be one point from each half, close to the dividing line —
check only the points within that narrow strip (this is the clever part).
```

**Fast Exponentiation (power by repeated squaring)**

```text
pow(x, 8) = pow(x, 4) * pow(x, 4)
pow(x, 4) = pow(x, 2) * pow(x, 2)
pow(x, 2) = pow(x, 1) * pow(x, 1)
```

Instead of multiplying `x` by itself `n` times, square the smaller result and halve `n` each time.

#### 4. Algorithm — Must Know

Fast exponentiation, the one worth knowing by heart:

```text
function power(x, n):
    if n == 0: return 1
    half = power(x, n / 2)
    if n is even: return half * half
    else: return half * half * x
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun power(x: Long, n: Long): Long {
    if (n == 0L) return 1L
    val half = power(x, n / 2)
    return if (n % 2 == 0L) half * half else half * half * x
}
```

#### 6. Complexity — Must Know

| Problem | Naive | Divide and conquer |
|---|---|---|
| Maximum subarray | O(n²) brute force | O(n log n) (Kadane's O(n) is better in practice) |
| Closest pair of points | O(n²) check every pair | O(n log n) |
| Exponentiation (`x^n`) | O(n) — multiply n times | O(log n) — repeated squaring |

#### 7. Common Mistakes — Must Know

1. For maximum subarray: forgetting the "crosses the middle" case, which needs its own direct scan, not a recursive call.
2. For closest pair: checking all points in both halves against each other near the boundary, instead of only the narrow strip — that's what keeps it at O(n log n) rather than O(n²).
3. For fast exponentiation: forgetting the extra `* x` when the exponent is odd.
4. For all three: not recognising that a simpler, non-recursive solution might already be O(n) (as Kadane's is for maximum subarray) — divide and conquer isn't always the best tool, just a valid one to know.

#### 8. Related Topics

1. `3` Divide and Conquer — Split, Solve, Combine — the shared technique
2. `10` Math & Number Theory — fast exponentiation is also a number theory tool (modular exponentiation)
3. `LC 20` More Patterns to Know — Kadane's algorithm as the direct O(n) alternative

#### 9. Interview Must Remember

1. **Fast exponentiation is the one to actually know cold** — O(log n) instead of O(n), by squaring.
2. For maximum subarray and closest pair, know the *shape* of the divide-and-conquer solution, even if Kadane's algorithm beats it in practice for max subarray.
3. The interesting part of most divide-and-conquer problems is the **combine step** — for closest pair, that's the narrow strip check.
