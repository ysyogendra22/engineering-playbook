# GCD & LCM — the Euclidean Algorithm

#### 1. Definition — Must Know

1. The **GCD (greatest common divisor)** of two numbers is the largest number that divides both exactly.
2. The **LCM (least common multiple)** is the smallest number that both numbers divide into exactly.
3. The **Euclidean algorithm** computes GCD efficiently, in O(log(min(a, b))) time — far faster than checking every possible divisor.

#### 2. Why It Is Used — Must Know

1. GCD and LCM come up constantly in problems about fractions, ratios, repeating patterns, and simplifying numbers.
2. The Euclidean algorithm is short, elegant, and a genuinely common "write this from memory" interview question.

#### 3. How It Works — Must Know

```text
gcd(48, 18):

48 = 18 * 2 + 12    →  gcd(48, 18) = gcd(18, 12)
18 = 12 * 1 + 6     →  gcd(18, 12) = gcd(12, 6)
12 = 6  * 2 + 0     →  gcd(12, 6)  = gcd(6, 0) = 6

gcd(48, 18) = 6
```

The key insight: `gcd(a, b) = gcd(b, a mod b)` — replacing the larger number with the remainder of dividing by the smaller one, repeatedly, until the remainder is 0. Whatever's left is the GCD.

```text
lcm(a, b) = (a * b) / gcd(a, b)
```

#### 4. Algorithm — Must Know

```text
function gcd(a, b):
    while b != 0:
        (a, b) = (b, a mod b)
    return a

function lcm(a, b):
    return (a * b) / gcd(a, b)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun gcd(a: Int, b: Int): Int {
    var x = a; var y = b
    while (y != 0) {
        val temp = y
        y = x % y
        x = temp
    }
    return x
}

fun lcm(a: Int, b: Int): Long = (a.toLong() * b) / gcd(a, b)
```

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Euclidean algorithm (GCD) | O(log(min(a, b))) |
| LCM (built from GCD) | O(log(min(a, b))) |
| Naive "check every divisor" GCD | O(min(a, b)) — much slower |

#### 7. Common Mistakes — Must Know

1. Computing LCM as `a * b / gcd(a, b)` without watching for overflow — multiplying two large `Int`s first can overflow; cast to `Long` before multiplying (as shown above).
2. Writing a naive GCD (checking every number down from `min(a, b)`) instead of the much faster Euclidean version.
3. Forgetting the base case: `gcd(a, 0) = a` — the loop's stopping condition depends on this.

#### 8. Related Topics

1. `5` Modular Arithmetic Basics — Avoiding Overflow — related number-safety concerns
2. `6` Combinatorics — Factorials, nCr — another place GCD is used, to simplify fractions
3. `8` Matrix Exponentiation & Extended Euclidean — Name Only — a related, more advanced variant

#### 9. Interview Must Remember

1. **`gcd(a, b) = gcd(b, a mod b)`**, repeated until `b == 0` — memorise this, it's short and comes up often.
2. **`lcm(a, b) = a * b / gcd(a, b)`** — watch for overflow when multiplying.
3. O(log(min(a, b))) — much faster than it might first appear, thanks to how quickly the remainder shrinks.
