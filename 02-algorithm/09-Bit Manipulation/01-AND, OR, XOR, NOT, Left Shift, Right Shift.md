# AND, OR, XOR, NOT, Left Shift, Right Shift

#### 1. Definition — Must Know

The six basic bitwise operations, each working on the individual bits of a number:

1. **AND** (`and`) — 1 only if both bits are 1.
2. **OR** (`or`) — 1 if at least one bit is 1.
3. **XOR** (`xor`) — 1 if the bits are different (exactly one is 1).
4. **NOT** (`.inv()`) — flips every bit.
5. **Left shift** (`shl`) — moves all bits left, filling with 0s (multiplies by 2 per shift).
6. **Right shift** (`shr`) — moves all bits right (divides by 2 per shift, for positive numbers).

#### 2. Why It Is Used — Must Know

1. These are the building blocks every other bit-manipulation technique (topics 2–8) is made from — worth being completely comfortable with before moving on.
2. They're also genuinely fast: each is a single CPU instruction, so bit tricks often replace an O(n) loop or extra data structure with O(1) work.

#### 3. How It Works — Must Know

```text
a = 0b1100   (12)
b = 0b1010   (10)

a AND b = 0b1000   (8)    ← 1 only where BOTH have a 1
a OR  b = 0b1110   (14)   ← 1 where EITHER has a 1
a XOR b = 0b0110   (6)    ← 1 where they DIFFER
NOT a   = ...11110011      (flips every bit — result depends on the number of bits)

a shl 1 = 0b11000  (24)   ← shift left by 1 = multiply by 2
a shr 1 = 0b0110   (6)    ← shift right by 1 = divide by 2 (for positive numbers)
```

#### 4. Algorithm — Must Know

There's no algorithm here — these are primitive operations, the vocabulary the rest of this folder is written in.

#### 5. Kotlin Implementation — Must Know

```kotlin
val a = 12   // 0b1100
val b = 10   // 0b1010

val and = a and b   // 8
val or  = a or b    // 14
val xor = a xor b   // 6
val not = a.inv()   // flips every bit
val left  = a shl 1 // 24
val right = a shr 1 // 6
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Every bitwise operation | O(1) — a single CPU instruction |

#### 7. Common Mistakes — Must Know

1. Confusing `and`/`or` (bitwise, work on individual bits) with `&&`/`\|\|` (logical, work on whole booleans) — Kotlin uses infix function names (`and`, `or`, `xor`, `shl`, `shr`), not symbols like some other languages.
2. Forgetting that right shift on a **negative** number in most languages is "arithmetic" (keeps the sign bit) — use `ushr` (unsigned shift) in Kotlin if you specifically need zeros shifted in regardless of sign.
3. Assuming shifting left forever keeps multiplying correctly — shifting past the size of the integer type (32 or 64 bits) causes overflow/wraparound, same as any other overflow.

#### 8. Related Topics

1. `2` Check, Set, Clear, and Toggle a Bit — the next layer built on these operations
2. `3` XOR Tricks — Single Number, Cancelling Pairs — a deeper look at XOR specifically
3. `8` Two's Complement — Why Negative Numbers Shift the Way They Do — the reasoning behind signed shifts

#### 9. Interview Must Remember

1. **AND** = both. **OR** = either. **XOR** = different. All O(1).
2. Left shift by `k` = multiply by `2^k`. Right shift by `k` ≈ divide by `2^k` (careful with negatives).
3. In Kotlin, these are infix functions: `and`, `or`, `xor`, `shl`, `shr`, `ushr`, `.inv()` — not symbols like `&`, `\|`, `^`, `<<`, `>>` (those exist in Java, not Kotlin).
