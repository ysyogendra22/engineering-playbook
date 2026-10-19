# Lookup / Existence Pattern

#### 1. Definition — Must Know

1. The **lookup pattern** stores data in a map **first**, then answers many questions about it in `O(1)` each.
2. The **existence** part: "is this key in the map?" (`key in map`).
3. The map version of the lookup also returns **what goes with the key** (an index, a mapped letter, an object).

#### 2. Why It Is Used — Must Know

1. It replaces repeated scans of a list (`O(n)` each) with a direct lookup (`O(1)`).
2. It is used for fixed conversions (Roman numerals, brackets) and for "matching" checks (Isomorphic Strings, Word Pattern).
3. In apps: id → object caches, route → screen, type → handler.

#### 3. How It Works — Must Know

Fixed lookup: convert a Roman numeral.

```text
map: I→1, V→5, X→10, L→50, C→100, D→500, M→1000

"MCMXCIV":  M=1000, C=100, M=1000, X=10, C=100, I=1, V=5
Rule: if a symbol is smaller than the next one, subtract it; else add it.
   1000 + (1000-100) + (100-10) + (5-1) = 1994
```

Matching lookup: *Isomorphic Strings* (LeetCode 205). Each letter in `s` must map to exactly one letter in `t`, and no two letters may map to the same one.

```text
s = "egg"   t = "add"
e → a   (store)
g → d   (store)
g → d   (already stored, matches ✓)      → true

s = "foo"   t = "bar"
f → b,  o → a,  o → r   (o is already mapped to a, not r ✗)  → false
```

#### 4. Core Concepts — Must Know

1. **Build the map once**, then look up as often as needed.
2. **`in` checks the key.** `map[key]` gets the value (nullable). Use whichever you need, not both.
3. **Fixed tables** (like Roman numerals) can be a `mapOf(...)` constant.
4. **Two maps for a two-way rule.** A one-to-one match needs one map each way (or one map plus a set of used targets).
5. **Store objects, not copies.** `id → object` lets you read or update later.
6. **Lookup beats search:** `list.find { it.id == x }` is `O(n)`; `map[x]` is `O(1)`.

#### 5. Algorithm — Must Know

```text
map = build from the data (once)
for each query:
    value = map[query]
    if value is null → not found
    else use value
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Roman to Integer
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

// Isomorphic Strings — one map each way
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

// Valid Parentheses — a lookup of closing → opening
fun isValid(s: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = ArrayDeque<Char>()
    for (c in s) {
        if (c in pairs) {                          // a closing bracket
            if (stack.isEmpty() || stack.removeLast() != pairs[c]) return false
        } else {
            stack.addLast(c)
        }
    }
    return stack.isEmpty()
}

// Cache lookup: id → object
data class User(val id: Int, val name: String)
val users = listOf(User(1, "Asha"), User(2, "Ben"))
val byId = users.associateBy { it.id }
println(byId[2]?.name)                              // Ben
println(3 in byId)                                  // false
```

Checks: `romanToInt("MCMXCIV")` → `1994`. `isIsomorphic("egg", "add")` → `true`. `isIsomorphic("foo", "bar")` → `false`.

#### 7. Time & Space Complexity — Must Know

| Step | Time |
|---|---:|
| Build the map from `m` items | `O(m)` |
| Each lookup | `O(1)` average |
| `n` lookups | `O(n)` |
| **Total** | **`O(m + n)`** |
| Space | `O(m)` |

Without the map, a list search per query makes it `O(m × n)`.

#### 8. Common Lookup Patterns — Must Know

1. **Roman to Integer** (LeetCode 13), **Integer to Roman** — fixed tables.
2. **Valid Parentheses** (LeetCode 20) — bracket pairs.
3. **Isomorphic Strings** (LeetCode 205), **Word Pattern** (LeetCode 290) — one-to-one mapping.
4. **Letter Combinations of a Phone Number** (LeetCode 17) — digit → letters.
5. **Two Sum** — value → index (next topic group).
6. **Cache** — `key → loaded object`, checked before loading again.
7. **Android example:** `viewType → ViewHolder factory`, `permission → rationale text`.

#### 9. Edge Cases / Common Mistakes

1. Using `map[key]!!` without checking for a missing key.
2. Looking up with `in` and then again with `[]`. One `[]` is enough.
3. Using only one map in a one-to-one problem. `"ab"` → `"aa"` passes a one-way check but is wrong.
4. Building the map inside the loop, which makes it `O(n²)` again.
5. Different key type than expected (`String` vs `Char`, `Int` vs `Long`). The lookup silently fails.
6. Case and whitespace in string keys.
7. Using `Map<Char, Int>` for 26 letters when an array is faster.

#### 10. When to Use / When Not to Use

**Use when:**

1. You look up the same data many times.
2. You need the value that goes with a key, not only whether it exists.

**Use a `HashSet` when:**

1. You only need existence (`01-data-structure/06-HashSet`).

**Use an array when:**

1. Keys are small integers or letters.

#### 11. Related Topics

1. Key-Value Pair Concept
2. HashSet vs HashMap (`01-data-structure/06-HashSet/03-HashSet vs HashMap.md`)
3. Mapping / Index Tracking
4. Two Sum Pattern

#### 12. Interview Must Remember

1. **Build the map once, look up in `O(1)`.**
2. One-to-one matching needs a map each way.
3. `map[key]` is `null` when missing — handle it.
4. Existence only → a `HashSet` is enough.
