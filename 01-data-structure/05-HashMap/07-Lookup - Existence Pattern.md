# Lookup / Existence Pattern

#### 1. What Is It?

The **lookup pattern**: store data in a map **first**, then answer many questions about it in `O(1)` each.

- **Existence:** "is this key in the map?" → `key in map`.
- **Lookup:** "what goes with this key?" → `map[key]`.

It replaces a repeated scan of a list (`O(n)` per question) with a direct lookup (`O(1)`).

Typical uses:

- a **fixed table** (Roman numerals, bracket pairs),
- a **matching rule** (Isomorphic Strings, Word Pattern),
- an **id → object** cache.

#### 2. How It Works

**Fixed table: Roman numerals.** Build the map once. If a symbol is smaller than the next one, subtract it. Otherwise add it.

```text
map: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

"MCMXCIV" → M(1000) C(100) M(1000) X(10) C(100) I(1) V(5)
C < M → subtract 100.   X < C → subtract 10.   I < V → subtract 1.
1000 + (1000 - 100) + (100 - 10) + (5 - 1) = 1994
```

**Matching rule: Isomorphic Strings** (LeetCode 205). Each letter of `s` must map to **exactly one** letter of `t`, and no two letters may map to the same one. That needs a map **in both directions**.

```text
s = "egg"   t = "add"
e → a  (store)      g → d  (store)      g → d  (already stored, matches ✓)    → true

s = "foo"   t = "bar"
f → b      o → a      o → r   (o is already mapped to a, not r ✗)            → false
```

#### 3. Kotlin Code

```kotlin
// Roman to Integer (LeetCode 13)
fun romanToInt(s: String): Int {
    val value = mapOf('I' to 1, 'V' to 5, 'X' to 10, 'L' to 50, 'C' to 100, 'D' to 500, 'M' to 1000)
    var total = 0
    for (i in s.indices) {
        val cur = value.getValue(s[i])
        val next = if (i + 1 < s.length) value.getValue(s[i + 1]) else 0
        total += if (cur < next) -cur else cur
    }
    return total
}

// Isomorphic Strings (LeetCode 205): one map each way
fun isIsomorphic(s: String, t: String): Boolean {
    if (s.length != t.length) return false
    val sToT = HashMap<Char, Char>()
    val tToS = HashMap<Char, Char>()
    for (i in s.indices) {
        val a = s[i]
        val b = t[i]
        val mappedB = sToT[a]
        val mappedA = tToS[b]
        if (mappedB != null && mappedB != b) return false
        if (mappedA != null && mappedA != a) return false
        sToT[a] = b
        tToS[b] = a
    }
    return true
}

// id → object lookup
data class User(val id: Int, val name: String)
val users = listOf(User(1, "Asha"), User(2, "Ben"))
val byId = users.associateBy { it.id }
println(byId[2]?.name)         // Ben
println(3 in byId)             // false
```

Checks: `romanToInt("MCMXCIV")` → `1994`. `isIsomorphic("egg", "add")` → `true`. `isIsomorphic("foo", "bar")` → `false`.

**Word Pattern (LeetCode 290)** is the same code: map each pattern letter to a word, and each word back to the letter.

#### 4. Complexity

| | Time |
|---|---|
| Build the map from `m` items | `O(m)` |
| Each lookup | `O(1)` |
| Total for `n` lookups | `O(m + n)` |

Without the map, searching a list for every question costs `O(m × n)`.

#### 5. Common Mistakes

1. **Using only one map** for a one-to-one match. `"ab"` → `"aa"` would wrongly pass a one-way check.
2. **`map[key]!!`** when the key might be missing. It crashes.
3. **Building the map inside the loop.** That is `O(n²)` again.
4. **Wrong key type** (`Char` vs `String`, `Int` vs `Long`). The lookup silently returns `null`.
5. **Case and spaces** in string keys.
6. **Using a map for 26 letters** when an `IntArray(26)` is faster.

#### 6. Say This in the Interview

1. "I build the lookup map once and then each query is `O(1)`."
2. "A one-to-one rule needs a map in both directions."
3. "Total time is `O(m + n)`."

#### 7. Quick Check

1. Is `"ab"` isomorphic to `"aa"`? Why?
2. What does `"IV"` equal as a Roman numeral, and why?

<details>
<summary>Answers</summary>

1. No. Both `a` and `b` would map to `a`, and two letters cannot map to the same one.
2. `4`. `I` (1) is smaller than `V` (5), so subtract: `5 - 1`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 13 | Roman to Integer (Easy) | fixed table |
| 205 | Isomorphic Strings (Easy) | maps in both directions |
| 290 | Word Pattern (Easy) | same idea with words |
| 12 | Integer to Roman (Medium) | table of values and symbols |
| 20 | Valid Parentheses (Easy) | closing → opening lookup |
| 1 | Two Sum (Easy) | value → index lookup |
