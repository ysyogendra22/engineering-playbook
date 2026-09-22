# Combinatorics — Factorials, nCr

#### 1. Definition — Must Know

1. **Factorial** (`n!`) is the product of all positive integers up to `n` (`5! = 5×4×3×2×1 = 120`) — the number of ways to arrange `n` distinct items in order.
2. **`nCr`** ("n choose r") is the number of ways to choose `r` items from `n`, where **order doesn't matter**: `nCr = n! / (r! × (n - r)!)`.

#### 2. Why It Is Used — Must Know

Counting problems ("how many ways can you...") are common in interviews, and factorials/`nCr` are the basic vocabulary for answering them — plus they connect directly to the branching-factor complexity discussion in `06-Backtracking & Branch and Bound/04`.

#### 3. How It Works — Must Know

```text
5! = 5 * 4 * 3 * 2 * 1 = 120

5C2 (choose 2 items from 5, order doesn't matter):
= 5! / (2! * 3!)
= 120 / (2 * 6)
= 120 / 12
= 10

Check by listing (items a,b,c,d,e; all pairs):
ab, ac, ad, ae, bc, bd, be, cd, ce, de  →  10 pairs ✓
```

For **large** `n` (say, computing `nCr mod a large prime`), computing full factorials directly can overflow — the standard fix is to precompute factorials **mod the prime**, and use a **modular inverse** (an advanced, related technique) instead of true division, since you can't divide normally under a modulus.

#### 4. Algorithm — Must Know

```text
function factorial(n):
    result = 1
    for i in 2 to n:
        result *= i
    return result

function nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun factorial(n: Int): Long {
    var result = 1L
    for (i in 2..n) result *= i
    return result
}

fun nCr(n: Int, r: Int): Long {
    if (r < 0 || r > n) return 0L
    return factorial(n) / (factorial(r) * factorial(n - r))
}

// A faster, overflow-safer way to compute nCr directly, without full factorials:
fun nCrDirect(n: Int, r: Int): Long {
    var result = 1L
    for (i in 0 until minOf(r, n - r)) {
        result = result * (n - i) / (i + 1)
    }
    return result
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Factorial | O(n) |
| `nCr` via factorials | O(n) |
| `nCr` with precomputed factorials (many queries) | O(n) to precompute once, then O(1) per query |

#### 7. Common Mistakes — Must Know

1. Computing large factorials directly and overflowing even a `Long` — `20!` already exceeds `Long`'s range in some contexts; for large `n`, work modulo a prime instead (see topic 5).
2. In `nCrDirect`, dividing before the running product is guaranteed to be exactly divisible — the specific order shown (multiply by `n - i`, then divide by `i + 1`) is chosen precisely so this always works out evenly.
3. Forgetting the `r < 0 || r > n` edge case, which should return 0 (there's no way to choose more items than exist, or a negative number of items).

#### 8. Related Topics

1. `4` Why It's Exponential: O(2ⁿ) and O(n!) (in `06-Backtracking & Branch and Bound`) — where `n!` growth is discussed from the algorithmic side
2. `5` Modular Arithmetic Basics — Avoiding Overflow — needed for `nCr` at large scale
3. `1` GCD & LCM — the Euclidean Algorithm

#### 9. Interview Must Remember

1. **`n!`** = arrangements (order matters). **`nCr`** = selections (order doesn't matter).
2. `nCr = n! / (r! × (n-r)!)` — know this formula, and the direct computation trick that avoids computing huge factorials first.
3. For large `n` modulo a prime, factorial-based division needs a modular inverse — know that this exists as the next step, even if the full technique is more advanced.
