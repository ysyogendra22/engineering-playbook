# Hashing / Hash Function — Basic Concept

#### 1. Definition — Must Know

1. **Hashing** turns a key into a **number** (the **hash code**). That number picks the bucket where the entry is stored.
2. A **hash function** is the rule that makes this number. In Kotlin/Java it is `hashCode()`.
3. A good hash function is **fast**, **consistent** (same key → same number), and **spreads keys evenly**.

#### 2. Why It Is Used — Must Know

1. It lets a map jump straight to the right bucket instead of scanning every entry.
2. This is the reason `get` and `put` are `O(1)` on average.
3. Interviewers ask about it to check you know why `equals()` and `hashCode()` must match.

#### 3. How It Works — Must Know

```text
key "abc"
   ↓ hashCode()              96354       (a number)
   ↓ spread the bits         96354 XOR (96354 >>> 16) = 96355
   ↓ keep the low bits       96355 AND (tableSize - 1)      tableSize = 16 → 3
bucket 3
```

`String.hashCode()` rule: `s[0]·31^(n−1) + s[1]·31^(n−2) + … + s[n−1]`.

```text
"abc" = 97·31² + 98·31 + 99 = 93217 + 3038 + 99 = 96354
```

Why `AND (size − 1)`? Java keeps the table size as a **power of 2**, so this is a fast replacement for `% size`.

#### 4. Core Concepts — Must Know

1. **Same key → same hash**, every time in one run. If the key changes, the hash may change.
2. **Equal keys → equal hashes** (the contract). The opposite is not required: different keys *may* share a hash.
3. **Different keys with the same hash = collision** (see "Collision Handling").
4. **Built-in hashes:**

| Type | Hash code |
|---|---|
| `Int` | the number itself |
| `Long` | `(v xor (v ushr 32)).toInt()` |
| `Char` | its code |
| `Boolean` | `1231` / `1237` |
| `String` | polynomial with 31 (above) |
| `List` | combines the hashes of items |
| `Pair`, `data class` | combines the hashes of fields |

5. **Arrays use identity hashes.** Two arrays with the same content have different hashes. Use `contentHashCode()` if you need content hashing, or use a `List`.
6. **Hashes can be negative.** Never use `hash % n` as an index without fixing the sign (`and 0x7fffffff` or `Math.floorMod`).
7. **Good hash:** spreads values evenly. **Bad hash:** `return 1` — every key in one bucket, so `O(n)` operations.

#### 5. Algorithm — Must Know

```text
indexFor(key):
    h = key.hashCode()
    h = h XOR (h >>> 16)              // mix the high bits into the low bits
    return h AND (tableSize - 1)      // table size is a power of two
```

#### 6. Kotlin Implementation — Must Know

```kotlin
println("abc".hashCode())              // 96354
println(42.hashCode())                 // 42
println("Aa".hashCode())               // 2112
println("BB".hashCode())               // 2112  — a collision: different strings, same hash

println(listOf(1, 2).hashCode() == listOf(1, 2).hashCode())     // true
println(intArrayOf(1, 2).hashCode() == intArrayOf(1, 2).hashCode()) // false (identity)
println(intArrayOf(1, 2).contentHashCode() == intArrayOf(1, 2).contentHashCode()) // true

// A correct custom hashCode
class Point(val x: Int, val y: Int) {
    override fun equals(other: Any?) = other is Point && x == other.x && y == other.y
    override fun hashCode(): Int = 31 * x + y          // uses the same fields as equals
}

// A safe bucket index for your own table
fun bucketIndex(key: Any?, size: Int): Int = (key.hashCode() and 0x7fffffff) % size
```

`data class Point(val x: Int, val y: Int)` writes `equals` and `hashCode` for you.

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---|
| Computing an `Int` hash | `O(1)` |
| Computing a `String` hash | `O(length)` (Java caches it after the first call) |
| Computing a `List` hash | `O(size)` |
| Finding the bucket | `O(1)` |

A long key makes every map operation slower, because hashing and comparing read the whole key.

#### 8. Common Hashing Ideas — Must Know

1. **Hash a key to find a bucket** — the core of HashMap and HashSet.
2. **Build a good composite key** (a `Pair`, a `data class`, or a joined `String`).
3. **Rolling hash** (Rabin–Karp) — update a substring hash in `O(1)` as the window slides (`02-algorithm/08-String Algorithms`).
4. **Hash for equality checks** — equal hashes are a quick reason to compare; different hashes mean "not equal" for sure.
5. **Not for security.** `hashCode()` is not a cryptographic hash.

#### 9. Edge Cases / Common Mistakes

1. Overriding `equals()` but not `hashCode()` (or the reverse).
2. Using fields in `hashCode` that are not in `equals`, or fields that change.
3. `hash % n` with a negative hash gives a negative index.
4. Expecting the same `hashCode()` across different runs or JVMs. Only equality inside one run is promised.
5. Using an array as a key.
6. Hashing a very long string again and again. Cache the result if it is needed repeatedly.
7. Thinking different keys always have different hashes. They do not.

#### 10. When to Use / When Not to Use

**Think about the hash when:**

1. You write a custom class that will be a map key or set item.
2. You explain why map lookup is fast.

**Do not:**

1. Write your own hash function in interviews unless asked. Use the built-in ones.
2. Use `hashCode()` for security (passwords, tokens).

#### 11. Related Topics

1. Collision Handling — Basic Concept
2. HashMap with Custom Objects / Keys
3. Designing a Simple HashMap — Concept
4. String Algorithms — rolling hash (`02-algorithm/08-String Algorithms`)

#### 12. Interview Must Remember

1. **Hash code → bucket index → compare with `equals()`.**
2. **Equal keys must have equal hash codes.**
3. Different keys can share a hash (a collision). That is allowed.
4. Arrays hash by identity. Use `List` or `contentHashCode()`.
