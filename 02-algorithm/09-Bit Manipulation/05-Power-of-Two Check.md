# Power-of-Two Check

#### 1. Definition — Must Know

A number is a **power of two** if it's `1, 2, 4, 8, 16, ...` — in binary, that means it has **exactly one set bit**. Checking for this reuses the same `n and (n - 1)` formula from Brian Kernighan's trick (topic 4).

#### 2. Why It Is Used — Must Know

1. It's a very short, elegant check (one line) that's a favourite small interview question, precisely because it tests whether you understand *why* `n and (n - 1)` works, not just that it does.
2. Powers of two come up naturally in bitmask problems (topic 6), capacity doubling, and memory alignment.

#### 3. How It Works — Must Know

```text
n = 8   = 0b1000   (exactly one set bit)
n - 1 = 7 = 0b0111

n and (n - 1) = 0b1000 and 0b0111 = 0b0000 = 0
                                            ↑ zero means it WAS a power of two

n = 10  = 0b1010   (two set bits)
n - 1 = 9 = 0b1001

n and (n - 1) = 0b1010 and 0b1001 = 0b1000 = 8   (not zero) → NOT a power of two
```

If a number has exactly one set bit, then `n - 1` flips that single bit to 0 and everything below it to 1 — leaving **no** overlapping 1s with the original number, so the AND is exactly 0. If a number has more than one set bit, at least one of those bits survives the AND, giving a non-zero result.

#### 4. Algorithm — Must Know

```text
function isPowerOfTwo(n):
    if n <= 0: return false          # powers of two are always positive
    return (n and (n - 1)) == 0
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun isPowerOfTwo(n: Int): Boolean {
    return n > 0 && (n and (n - 1)) == 0
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Time | O(1) — one subtraction, one AND, one comparison |
| Space | O(1) |

#### 7. Common Mistakes — Must Know

1. **Forgetting the `n > 0` check** — the formula `n and (n - 1) == 0` is also true for `n = 0` itself, but 0 is not a power of two.
2. Reaching for a loop (`while n > 1: divide by 2`) when the O(1) bit trick is available and just as easy to write, once known.
3. Not explaining *why* the trick works when asked — just stating the formula without the reasoning is a weaker interview answer than walking through the binary example above.

#### 8. Related Topics

1. `4` Counting Set Bits — bitCount and Brian Kernighan's Trick — this check is really "count of set bits == 1"
2. `1` AND, OR, XOR, NOT, Left Shift, Right Shift — the base operations used here

#### 9. Interview Must Remember

1. A power of two has **exactly one set bit**, so `n and (n - 1) == 0`.
2. Don't forget the **`n > 0`** guard — `0` passes the bit check but isn't a power of two.
3. Be ready to explain *why* it works (subtracting 1 clears the single set bit and flips everything below it), not just recite the formula.
