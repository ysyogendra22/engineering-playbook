# Matrix Exponentiation & Extended Euclidean — Name Only

#### 1. Definition — Must Know

1. **Matrix exponentiation** uses the same "repeated squaring" idea as fast exponentiation (topic 4), but applied to **matrices** instead of plain numbers — useful for computing terms of a linear recurrence (like Fibonacci) in O(log n) instead of O(n).
2. The **extended Euclidean algorithm** is a variant of the Euclidean algorithm (topic 1) that, alongside the GCD, also finds integers `x` and `y` such that `a*x + b*y = gcd(a, b)` — used to compute **modular inverses**, needed for modular division.

#### 2. Why It Is Used — Must Know

Both are genuinely advanced tools — worth recognising by name and knowing roughly what problem they solve, but not something most interviews expect implemented from memory.

#### 3. How It Works — Must Know

**Matrix exponentiation** (idea only):

```text
Fibonacci can be written as a matrix multiplication:

| F(n+1) |   | 1  1 |   | F(n)   |
| F(n)   | = | 1  0 | × | F(n-1) |

So computing F(n) becomes: raise the matrix [[1,1],[1,0]] to the power n,
using the same repeated-squaring trick as fast exponentiation (topic 4).

This computes the n-th Fibonacci number in O(log n) matrix multiplications,
instead of O(n) additions — useful when n is astronomically large.
```

**Extended Euclidean algorithm** (idea only):

```text
Alongside computing gcd(a, b), it also tracks coefficients x, y such that:
   a*x + b*y = gcd(a, b)

This is the standard way to find the MODULAR INVERSE of a number
(needed to "divide" under a modulus, since normal division isn't
directly defined in modular arithmetic — see topic 5).
```

#### 4. Algorithm — Must Know

*(Name and purpose only — not expected to be derived or implemented from memory at this level.)*

#### 5. Kotlin Implementation — Must Know

*(Not expected — these are awareness-level topics.)*

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Matrix exponentiation (for a fixed-size recurrence matrix) | O(k³ log n), k = matrix size (small, fixed), n = the term you want |
| Extended Euclidean algorithm | O(log(min(a, b))) — same order as plain GCD |

#### 7. Common Mistakes — Must Know

1. Reaching for matrix exponentiation on a small `n` where a simple loop (or even plain DP) already runs fast enough — it's only worth the complexity when `n` is extremely large.
2. Confusing the "extended" Euclidean algorithm (finds `x, y` coefficients too) with the plain Euclidean algorithm (topic 1, finds only the GCD) — different tools, related name.
3. Spending interview time trying to derive either technique from scratch — for an awareness-only topic, describing the idea and its use case is the right depth.

#### 8. Related Topics

1. `4` Fast (Modular) Exponentiation — Repeated Squaring — the same core idea, applied to plain numbers instead of matrices
2. `1` GCD & LCM — the Euclidean Algorithm — the simpler version the extended algorithm builds on
3. `5` Modular Arithmetic Basics — Avoiding Overflow — where modular inverses (found via extended Euclidean) would be used

#### 9. Interview Must Remember

1. **Matrix exponentiation** = repeated squaring, applied to matrices, for computing huge terms of a linear recurrence fast.
2. **Extended Euclidean** = GCD, plus the coefficients needed to find a modular inverse.
3. Both are name-and-idea topics here — know what they're for, and mention them when relevant, without expecting to derive them live.
