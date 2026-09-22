# Overflow Awareness in Kotlin — Long vs Int Limits

#### 1. Definition — Must Know

**Overflow** happens when a calculation's true result is larger than the number type can hold, causing it to "wrap around" silently to an incorrect (often negative) value, instead of throwing an error. Kotlin's `Int` holds up to about 2.1 billion; `Long` holds up to about 9.2 × 10¹⁸.

#### 2. Why It Is Used — Must Know

This isn't an algorithm — it's a **habit**. Overflow bugs are silent (no crash, no error, just a wrong answer), which makes them one of the sneakiest sources of failed test cases in coding interviews, especially in problems involving sums, products, or large constraints.

#### 3. How It Works — Must Know

```text
Int range: roughly -2,147,483,648 to 2,147,483,647

val a: Int = 2_000_000_000
val b: Int = 2_000_000_000
val sum = a + b     // TRUE value is 4,000,000,000 — overflows Int!
                     // actual result: a negative, wrong number

val sumSafe = a.toLong() + b.toLong()   // 4,000,000,000 — correct, fits in Long
```

```text
Common overflow triggers to watch for:
- Summing a large array of Ints            (use Long for the running total)
- Multiplying two large numbers             (n * n for n around 100,000+ overflows Int)
- Computing n! or nCr for moderately large n
- Modular exponentiation, if you forget to reduce intermediate values (see topic 4, 5)
```

#### 4. Algorithm — Must Know

```text
Before writing a sum/product, ask:
1. What's the maximum possible value this could reach,
   given the problem's stated constraints?
2. Does that maximum fit inside Int (about 2.1 billion)?
3. If not, or if unsure, use Long from the start.
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Danger: two Int values multiplied — result type is still Int, can overflow
val n = 100_000
val product = n * n   // WRONG: overflows Int (100,000 * 100,000 = 10,000,000,000)

// Fix: cast at least one operand to Long before multiplying
val safeProduct = n.toLong() * n   // correct: 10,000,000,000

// A helper worth having on hand:
fun Int.toLongSafe(): Long = this.toLong()
```

#### 6. Complexity — Must Know

Not applicable — this is a correctness practice, not a runtime-cost topic. Using `Long` instead of `Int` has no meaningful performance difference for typical interview-sized problems.

#### 7. Common Mistakes — Must Know

1. Multiplying two `Int` values and assuming the result is automatically promoted to `Long` — it is **not**; the multiplication happens in `Int` first, and *then* the (already-overflowed) result is assigned or cast.
2. Reading the problem's constraints but not actually calculating the worst-case sum or product to check if it fits in `Int`.
3. Using `Long` "just in case" everywhere without checking — usually harmless, but occasionally a specific data structure or API expects `Int` and needs an explicit conversion.

#### 8. Related Topics

1. `4` Fast (Modular) Exponentiation — Repeated Squaring — where overflow bugs are especially easy to introduce
2. `5` Modular Arithmetic Basics — Avoiding Overflow — the companion technique for keeping numbers bounded
3. `6` Combinatorics — Factorials, nCr — factorials overflow `Long` surprisingly quickly too

#### 9. Interview Must Remember

1. **Check the constraints, calculate the worst-case value, and decide `Int` vs `Long` deliberately** — don't guess.
2. Casting happens **before** the operation matters — `a.toLong() * b`, not `(a * b).toLong()`, if `a * b` alone could already overflow.
3. Overflow is silent — no crash, no exception, just a wrong answer. Treat it as seriously as an off-by-one error.
