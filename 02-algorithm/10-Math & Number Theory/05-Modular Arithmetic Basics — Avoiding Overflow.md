# Modular Arithmetic Basics — Avoiding Overflow

#### 1. Definition — Must Know

**Modular arithmetic** means doing arithmetic "wrapping around" after reaching a fixed value, the **modulus** (often written `mod m`). It's used constantly in problems that ask for an answer "modulo `10^9 + 7`" (or similar), because the true answer would otherwise be an enormous number that doesn't fit in a normal integer type.

#### 2. Why It Is Used — Must Know

1. Many counting or combinatorics problems have answers that grow astronomically large (way beyond what a 64-bit `Long` can hold) — taking everything mod a large prime keeps the numbers small and safe throughout.
2. Getting the modular rules right (especially for subtraction) is a common, easy-to-get-wrong detail — worth knowing precisely.

#### 3. How It Works — Must Know

```text
Addition:       (a + b) mod m = ((a mod m) + (b mod m)) mod m
Multiplication: (a * b) mod m = ((a mod m) * (b mod m)) mod m
Subtraction:    (a - b) mod m = ((a mod m) - (b mod m) + m) mod m
                                                          ↑ add m before the final mod,
                                                            to avoid a negative result
```

```text
Example: (3 - 7) mod 5
  Naively: 3 - 7 = -4, and -4 mod 5 in some languages gives -4 (NOT 1, which is
  the mathematically correct answer)

  Correct way: ((3 mod 5) - (7 mod 5) + 5) mod 5
             = (3 - 2 + 5) mod 5
             = 6 mod 5
             = 1    ← correct
```

Kotlin's `%` operator can return a **negative** result when the left operand is negative — this is why the `+ m` step before the final mod is essential for subtraction.

#### 4. Algorithm — Must Know

```text
addMod(a, b, m)      = ((a % m) + (b % m)) % m
multiplyMod(a, b, m)  = ((a % m) * (b % m)) % m
subtractMod(a, b, m) = (((a % m) - (b % m)) % m + m) % m
```

#### 5. Kotlin Implementation — Must Know

```kotlin
const val MOD = 1_000_000_007L

fun addMod(a: Long, b: Long): Long = (a % MOD + b % MOD) % MOD
fun multiplyMod(a: Long, b: Long): Long = (a % MOD * (b % MOD)) % MOD
fun subtractMod(a: Long, b: Long): Long = ((a % MOD - b % MOD) % MOD + MOD) % MOD
```

#### 6. Complexity — Must Know

Each modular operation is O(1) — the cost concern here isn't speed, it's **correctness and overflow safety**.

#### 7. Common Mistakes — Must Know

1. Forgetting the `+ m` before the final mod when subtracting — this is the single most common modular arithmetic bug.
2. Multiplying two large numbers **before** taking the mod, causing overflow — always reduce operands with `% MOD` first, or use a wider type (`Long` instead of `Int`).
3. Applying `% MOD` only at the very end of a long calculation, instead of after every operation — intermediate values can overflow before you ever reach that final mod.

#### 8. Related Topics

1. `4` Fast (Modular) Exponentiation — Repeated Squaring — uses these exact rules at every step
2. `7` Overflow Awareness in Kotlin — Long vs Int Limits — the broader overflow topic this connects to
3. `1` GCD & LCM — the Euclidean Algorithm — modular division (using an inverse) builds on GCD, a more advanced topic beyond this one

#### 9. Interview Must Remember

1. **Addition and multiplication**: reduce each operand mod `m` first, then combine, then mod again.
2. **Subtraction**: add `m` before the final mod, to avoid a negative result.
3. Apply the mod at **every step** of a calculation, not just at the end — this is what actually prevents overflow.
