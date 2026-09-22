# Prime Checking — Trial Division up to √n

#### 1. Definition — Must Know

A number is **prime** if it's greater than 1 and has no divisors other than 1 and itself. **Trial division** checks primality by testing possible divisors — and the key trick is you only need to check up to `√n`, not all the way to `n`.

#### 2. Why It Is Used — Must Know

Primality checking appears directly in many problems, and understanding *why* checking up to `√n` is enough (rather than just knowing the rule) is what separates a memorised trick from real understanding.

#### 3. How It Works — Must Know

```text
Is 37 prime? Check divisors from 2 up to √37 ≈ 6.08, so check 2..6:
  37 / 2 → not divisible
  37 / 3 → not divisible
  37 / 4 → not divisible
  37 / 5 → not divisible
  37 / 6 → not divisible
No divisors found → 37 is prime.

Why stop at √n? If n = a * b, and a ≤ b, then a ≤ √n. In other words,
if n has ANY divisor pair, at least one of the two divisors must be
√n or smaller — so if nothing up to √n divides n, nothing larger can
either (its "partner" divisor would have already been found).
```

#### 4. Algorithm — Must Know

```text
function isPrime(n):
    if n < 2: return false
    for i in 2 to floor(sqrt(n)):
        if n % i == 0:
            return false
    return true
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    var i = 2
    while (i.toLong() * i <= n) {   // avoids computing sqrt() directly, and avoids overflow
        if (n % i == 0) return false
        i++
    }
    return true
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Trial division up to √n | O(√n) |
| Checking every number up to n | O(n) — much slower, unnecessary |
| Checking every number for MANY queries | Use the Sieve of Eratosthenes instead (topic 3) |

#### 7. Common Mistakes — Must Know

1. Forgetting the `n < 2` check — numbers less than 2 (0, 1, and negatives) are not prime by definition.
2. Checking divisibility all the way up to `n` instead of stopping at `√n` — correct, but unnecessarily slow.
3. Using this approach for **many** primality checks over a range — if you need to check many numbers up to some limit, the Sieve of Eratosthenes (topic 3) is far more efficient overall.

#### 8. Related Topics

1. `3` Sieve of Eratosthenes — All Primes up to n at Once — the better tool for checking many numbers
2. `1` GCD & LCM — the Euclidean Algorithm — another core number theory tool

#### 9. Interview Must Remember

1. Only check divisors **up to √n** — and be ready to explain why that's sufficient.
2. O(√n) per check — fine for a single number, but switch to a sieve (topic 3) if checking many numbers.
3. Don't forget: numbers below 2 are never prime.
