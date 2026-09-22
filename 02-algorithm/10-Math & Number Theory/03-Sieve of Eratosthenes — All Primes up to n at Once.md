# Sieve of Eratosthenes — All Primes up to n at Once

#### 1. Definition — Must Know

The **Sieve of Eratosthenes** finds every prime number up to some limit `n` all at once, by starting with every number marked "possibly prime" and progressively **crossing out (marking as not prime)** every multiple of each prime found, starting from 2.

#### 2. Why It Is Used — Must Know

1. When a problem needs primality info for **many numbers** (not just one), running trial division (topic 2) on each one separately is much slower than building one sieve up front.
2. It's a clean, visual algorithm that's easy to both explain and implement correctly under interview conditions.

#### 3. How It Works — Must Know

```text
Find all primes up to 30:

Start: mark 0 and 1 as not prime. Everything else starts "possibly prime".

Start with 2 (the first prime): cross out every multiple of 2 (4, 6, 8, 10, ...)
Next unmarked number is 3 (prime): cross out every multiple of 3 (6, 9, 12, ...)
Next unmarked number is 5 (prime): cross out every multiple of 5 (10, 15, 20, ...)
Next unmarked number is 7 (prime): cross out every multiple of 7 (14, 21, 28)
Next unmarked number is 11 — but 11² = 121 > 30, so we can STOP here.
                                    (see the "why stop early" note below)

Remaining unmarked numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

**Why you can stop once `i * i > n`**: any composite number ≤ n must have at least one prime factor ≤ √n (same reasoning as trial division, topic 2) — so once you've crossed out multiples of every prime up to √n, everything still unmarked above that point is guaranteed prime.

#### 4. Algorithm — Must Know

```text
function sieve(n):
    isPrime = array of true, size n+1
    isPrime[0] = isPrime[1] = false
    for i in 2 to sqrt(n):
        if isPrime[i]:
            for multiple in i*i, i*i+i, i*i+2i, ... up to n:
                isPrime[multiple] = false
    return isPrime
```

Starting the inner loop at `i * i` (not `2 * i`) is a small but real optimisation — smaller multiples of `i` were already crossed out by smaller primes.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun sieveOfEratosthenes(n: Int): BooleanArray {
    val isPrime = BooleanArray(n + 1) { it >= 2 }
    var i = 2
    while (i.toLong() * i <= n) {
        if (isPrime[i]) {
            var multiple = i * i
            while (multiple <= n) {
                isPrime[multiple] = false
                multiple += i
            }
        }
        i++
    }
    return isPrime
}
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Time | O(n log log n) — close to O(n) in practice |
| Space | O(n) — the boolean array |

Compare with trial division on every number up to n: O(n√n) total — the sieve is dramatically faster when you need primality for a whole range.

#### 7. Common Mistakes — Must Know

1. Starting the inner "cross out multiples" loop at `2 * i` instead of `i * i` — correct either way, but slower.
2. Rebuilding the sieve from scratch for every query, instead of building it **once** and reusing the result — the whole benefit is amortising the cost across many lookups.
3. Using the sieve for a single, one-off primality check on a huge number — trial division (topic 2) is the better fit there; the sieve is for **ranges**.

#### 8. Related Topics

1. `2` Prime Checking — Trial Division up to √n — the single-number version this replaces for bulk queries
2. `1` GCD & LCM — the Euclidean Algorithm

#### 9. Interview Must Remember

1. Sieve = **cross out multiples of each prime, starting from 2**, until `i * i > n`.
2. O(n log log n) — use it whenever you need primality info for a **range** of numbers, not just one.
3. Start the inner loop at `i * i`, not `2i` — a standard, expected optimisation.
