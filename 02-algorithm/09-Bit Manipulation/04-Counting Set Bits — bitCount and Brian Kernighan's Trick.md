# Counting Set Bits — bitCount and Brian Kernighan's Trick

#### 1. Definition — Must Know

Counting **set bits** means counting how many `1`s are in a number's binary representation (also called the "population count" or "Hamming weight"). **Brian Kernighan's trick** does this efficiently: `n and (n - 1)` always clears the **lowest** set bit, so repeating it counts the set bits directly, without checking every single bit position.

#### 2. Why It Is Used — Must Know

1. Counting set bits shows up directly in problems (Hamming Weight, Hamming Distance) and indirectly wherever a bitmask represents a subset — the number of set bits is the size of that subset.
2. Brian Kernighan's trick is a small, memorable optimisation: instead of always checking all 32 bit positions, it only loops once **per set bit**, which is faster when the number has few 1s.

#### 3. How It Works — Must Know

```text
n = 0b10110   (22, has 3 set bits)

n and (n - 1):
  n     = 0b10110
  n - 1 = 0b10101
  AND   = 0b10100    ← the lowest set bit (the rightmost 1) is now cleared

Repeat:
  n     = 0b10100
  n - 1 = 0b10011
  AND   = 0b10000    ← next lowest set bit cleared

Repeat:
  n     = 0b10000
  n - 1 = 0b01111
  AND   = 0b00000    ← last set bit cleared, n is now 0 → stop

3 iterations → 3 set bits, matching what we expect.
```

Why `n and (n - 1)` works: subtracting 1 flips the lowest set bit to 0 and every bit after it (to the right) to 1. ANDing with the original number keeps everything above the lowest set bit unchanged, but zeroes out that lowest set bit and everything after it.

#### 4. Algorithm — Must Know

```text
function countSetBits(n):
    count = 0
    while n != 0:
        n = n and (n - 1)   # clears the lowest set bit
        count++
    return count
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun countSetBitsKernighan(n: Int): Int {
    var num = n
    var count = 0
    while (num != 0) {
        num = num and (num - 1)
        count++
    }
    return count
}

// Kotlin/Java also has a built-in for this:
fun countSetBitsBuiltIn(n: Int): Int = Integer.bitCount(n)
```

#### 6. Complexity — Must Know

| Approach | Time |
|---|---|
| Check every bit position (32 iterations) | O(32) = O(1), but always the full 32 |
| Brian Kernighan's trick | O(number of set bits), which is ≤ 32 |
| `Integer.bitCount()` (built-in) | O(1) — often a single hardware instruction |

#### 7. Common Mistakes — Must Know

1. Reimplementing Brian Kernighan's trick by hand in real code when `Integer.bitCount()` (or Kotlin's `countOneBits()` on `Int`) already does this, correctly and fast — know the trick for interviews, but use the built-in in production code.
2. Confusing `n and (n - 1)` (clears the lowest set bit) with `n and (n + 1)` or other variations — the exact formula matters.
3. Not handling `n = 0` — the loop correctly does zero iterations, but it's worth double-checking as an edge case.

#### 8. Related Topics

1. `2` Check, Set, Clear, and Toggle a Bit — the more basic single-bit operations
2. `5` Power-of-Two Check — uses the same `n and (n - 1)` formula for a different purpose
3. `6` Bitmask — Representing a Set of Up to ~20 Items — where "number of set bits" means "size of the subset"

#### 9. Interview Must Remember

1. `n and (n - 1)` **clears the lowest set bit** — memorise this one formula, it powers several tricks.
2. Brian Kernighan's trick loops once per set bit, not once per bit position — faster for numbers with few 1s.
3. In real code, prefer the built-in (`Integer.bitCount()` / `Int.countOneBits()`) — know the manual trick for interviews and for understanding *why* it works.
