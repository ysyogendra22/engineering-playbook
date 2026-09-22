# Fast (Modular) Exponentiation — Repeated Squaring

#### 1. Definition — Must Know

**Fast exponentiation** computes `x^n` in O(log n) time instead of O(n), by repeatedly **squaring** and halving the exponent, instead of multiplying `x` by itself `n` times one at a time. **Modular exponentiation** does the same thing while also taking a modulo at each step, to compute `x^n mod m` without the numbers ever growing unreasonably large.

#### 2. Why It Is Used — Must Know

1. It's the single most important number-theory technique to know cold — it shows up directly, and also as a building block inside other algorithms.
2. Modular exponentiation specifically is essential whenever a problem asks for an answer "mod 10^9 + 7" (a very common constraint) and involves exponentiation.

#### 3. How It Works — Must Know

```text
Compute 3^13 using repeated squaring:

13 in binary is 1101, which means 13 = 8 + 4 + 1

3^13 = 3^8 * 3^4 * 3^1

3^1 = 3
3^2 = 3^1 * 3^1 = 9
3^4 = 3^2 * 3^2 = 81
3^8 = 3^4 * 3^4 = 6561

3^13 = 6561 * 81 * 3 = 1,594,323

Only needed 4 squarings (3^1 → 3^2 → 3^4 → 3^8) and a few multiplications
to combine the right ones — not 13 separate multiplications.
```

The recursive version makes the halving explicit:

```text
power(x, n) = power(x, n/2) * power(x, n/2)              if n is even
power(x, n) = power(x, n/2) * power(x, n/2) * x           if n is odd
power(x, 0) = 1
```

#### 4. Algorithm — Must Know

```text
function power(x, n, mod):
    result = 1
    x = x mod mod
    while n > 0:
        if n is odd:
            result = (result * x) mod mod
        x = (x * x) mod mod     # square x
        n = n / 2                # halve n (integer division)
    return result
```

This is the **iterative** version — it avoids the extra function-call overhead of computing `power(x, n/2)` twice recursively.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun modPow(base: Long, exponent: Long, mod: Long): Long {
    var result = 1L
    var b = base % mod
    var e = exponent
    while (e > 0) {
        if (e % 2 == 1L) {
            result = (result * b) % mod
        }
        b = (b * b) % mod
        e /= 2
    }
    return result
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Fast exponentiation | O(log n) |
| Naive (`x` multiplied `n` times) | O(n) |

#### 7. Common Mistakes — Must Know

1. Forgetting to take the modulo at **every** multiplication step, not just at the end — the intermediate numbers can overflow `Long` if you wait too long.
2. Using recursion with two separate calls (`power(x, n/2) * power(x, n/2)`) instead of computing it once and squaring — doubles the work for no reason.
3. Forgetting the extra `* x` when the exponent is odd.

#### 8. Related Topics

1. `3` Divide and Conquer — Split, Solve, Combine (in `03-Recursion & Divide and Conquer`) — fast exponentiation is a divide-and-conquer algorithm
2. `9` Classic Divide & Conquer — Max Subarray, Closest Pair, Fast Exponentiation (in `03-Recursion & Divide and Conquer`) — the same algorithm covered there
3. `5` Modular Arithmetic Basics — Avoiding Overflow

#### 9. Interview Must Remember

1. Fast exponentiation = **repeated squaring**, O(log n) instead of O(n).
2. For modular exponentiation, take the **mod at every multiplication**, not just at the end.
3. This is the one number-theory algorithm worth being able to write correctly, from memory, without hesitation.
