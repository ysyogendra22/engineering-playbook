# Hashing / Hash Function — Basic Concept

> Keep this at a basic level. Interviews ask the idea, not the maths.

#### 1. What Is It?

**Hashing** turns a key into a **number** called the **hash code**. The map uses that number to pick the **bucket** where the pair is stored.

A **hash function** is the rule that makes the number. In Kotlin and Java it is the `hashCode()` method.

A good hash function is:

- **fast**,
- **consistent**: the same key always gives the same number,
- **spread out**: different keys usually give different numbers.

#### 2. How It Works

```text
key "abc"
   ↓ hashCode()                    96354          (a number)
   ↓ mix the bits, keep the low part
   ↓ with a table of 16 buckets    bucket 3
```

How `String.hashCode()` works: `s[0]·31^(n−1) + s[1]·31^(n−2) + … + s[n−1]`.

```text
"abc" = 97·31² + 98·31 + 99 = 93217 + 3038 + 99 = 96354
```

**The most important rule (asked in interviews):**

> If two keys are **equal** (`equals()`), they **must** have the **same** hash code.

The reverse is not required. Two different keys *may* share a hash code. That is a **collision** (next note).

Hash codes of common types:

| Type | Hash code |
|---|---|
| `Int` | the number itself |
| `Char` | its code |
| `String` | the formula above |
| `List`, `Pair`, `data class` | built from the hash codes of the contents |
| `IntArray`, `Array` | identity based. **Two arrays with the same content have different hash codes.** |

#### 3. Kotlin Code

```kotlin
println("abc".hashCode())                       // 96354
println(42.hashCode())                          // 42
println("Aa".hashCode() == "BB".hashCode())     // true: a collision

println(listOf(1, 2).hashCode() == listOf(1, 2).hashCode())          // true
println(intArrayOf(1, 2).hashCode() == intArrayOf(1, 2).hashCode())  // false (arrays use identity)
println(intArrayOf(1, 2).contentHashCode() == intArrayOf(1, 2).contentHashCode()) // true

// A custom key: equals and hashCode use the SAME fields
class Point(val x: Int, val y: Int) {
    override fun equals(other: Any?) = other is Point && x == other.x && y == other.y
    override fun hashCode(): Int = 31 * x + y
}

// Easier: a data class writes both for you
data class Point2(val x: Int, val y: Int)
```

#### 4. Complexity

| Action | Time |
|---|---|
| Hash of an `Int` | `O(1)` |
| Hash of a `String` of length `L` | `O(L)` (Java remembers it after the first time) |
| Hash of a `List` of size `L` | `O(L)` |

A long key makes every map operation slower, because hashing and comparing read the whole key.

#### 5. Common Mistakes

1. **Writing `equals()` but not `hashCode()`** (or the opposite). The map then loses keys.
2. **Using different fields** in `equals` and `hashCode`.
3. **Using an array as a key.** Use a `List`, a `String`, or a `data class`.
4. **Changing a key** after it is in the map. Its hash code changes, and the map can no longer find it.
5. **Thinking different keys always have different hash codes.** They do not.
6. **Using `hash % size` with a negative hash.** The index can be negative. Use `and 0x7fffffff` first.

#### 6. Say This in the Interview

1. "The hash code picks the bucket. `equals()` then finds the exact key inside the bucket."
2. "Equal keys must have equal hash codes. In Kotlin a `data class` gives me both."
3. "I avoid arrays as keys because they use identity hash codes."

#### 7. Quick Check

1. If `a.equals(b)` is true, what must be true about their hash codes?
2. Why can't an `IntArray` be a good map key?

<details>
<summary>Answers</summary>

1. They must be equal.
2. Two arrays with the same content have different hash codes and are not `equals`, so a lookup with a new array never finds the old one.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 706 | Design HashMap (Easy) | build buckets with a hash function (note 26) |
| 705 | Design HashSet (Easy) | same idea |
| 49 | Group Anagrams (Medium) | a good key (sorted letters) |
| 187 | Repeated DNA Sequences (Medium) | hash of a substring |
