# Two's Complement — Why Negative Numbers Shift the Way They Do

#### 1. Definition — Must Know

**Two's complement** is how almost every modern computer represents negative integers in binary. To negate a number, you flip every bit and add 1. The very first bit (the most significant bit) acts as the sign: 0 for non-negative, 1 for negative.

#### 2. Why It Is Used — Must Know

1. It explains a handful of things that otherwise look like "magic": why `-1` is all 1-bits, why right-shifting a negative number in Kotlin (`shr`) keeps it negative, and why `n and (n - 1)` (topics 4 and 5) works correctly even conceptually.
2. It's a good, precise thing to be able to explain if an interviewer asks "how are negative numbers stored?"

#### 3. How It Works — Must Know

```text
For a 4-bit example (real Kotlin Ints are 32-bit, same idea, more bits):

  5  = 0101
 -5:  step 1, flip every bit of 5:   0101 → 1010
      step 2, add 1:                1010 + 1 = 1011
 -5  = 1011

Check: 5 + (-5) should equal 0
  0101
+ 1011
------
 10000   ← the leading 1 overflows out of 4 bits and is discarded → 0000 = 0 ✓
```

```text
-1 in two's complement is ALL 1-bits (for any width):
   1  = 0001
  -1:  flip → 1110, add 1 → 1111    (all 1s)
```

#### 4. Algorithm — Must Know

```text
To negate n (get -n):
    invert every bit of n, then add 1
    (in Kotlin: -n, or equivalently n.inv() + 1)
```

#### 5. Kotlin Implementation — Must Know

```kotlin
val n = 5
val negated = n.inv() + 1     // -5, same as just writing -n
println(negated == -n)         // true

// Arithmetic (signed) right shift keeps the sign bit — shifting a negative
// number right with `shr` keeps it negative:
println(-8 shr 1)   // -4  (sign-preserving)

// Unsigned right shift ignores the sign, always filling with 0s from the left:
println(-8 ushr 1)  // a large positive number, NOT -4
```

#### 6. Complexity — Must Know

Not applicable — this is a representation concept, not an algorithm with a runtime cost.

#### 7. Common Mistakes — Must Know

1. Using `shr` (arithmetic shift, sign-preserving) when `ushr` (logical/unsigned shift) is actually needed, or the reverse — pick based on whether the sign should be preserved.
2. Assuming `NOT n` (`n.inv()`) equals `-n` — it's actually `-n - 1` (`NOT n = -(n) - 1`, which is why two's complement negation adds 1 afterward, not before).
3. Forgetting that bit tricks relying on `n and (n - 1)` implicitly depend on how subtraction "borrows" through bits — which is exactly the two's-complement behaviour described here.

#### 8. Related Topics

1. `1` AND, OR, XOR, NOT, Left Shift, Right Shift — the operations affected by signed representation
2. `4` Counting Set Bits — bitCount and Brian Kernighan's Trick — relies on subtraction's borrow behaviour
3. `07` Overflow Awareness in Kotlin — Long vs Int Limits (in `10-Math & Number Theory`) — a related practical concern

#### 9. Interview Must Remember

1. **Two's complement: flip every bit, then add 1, to negate a number.**
2. `-1` is represented as **all 1-bits**, for any integer width.
3. `shr` (arithmetic) preserves the sign when shifting negatives; `ushr` (logical) does not — know which one a problem actually needs.
