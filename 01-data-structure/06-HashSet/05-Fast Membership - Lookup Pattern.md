# Fast Membership / Lookup Pattern

#### 1. Definition — Must Know

1. The **fast membership pattern** means: put the values you will check **into a set first**, then check each query in `O(1)`.
2. It replaces repeated scans of a list or array (`O(n)` each) with a set lookup.
3. It is a **preprocess once, query many times** idea.

#### 2. Why It Is Used — Must Know

1. Checking `list.contains(x)` inside a loop gives `O(n × m)`.
2. Building a set first gives `O(n + m)`.
3. It appears in real code: blocked words, allowed permissions, feature flags, supported file types.

#### 3. How It Works — Must Know

Problem: *Jewels and Stones* (LeetCode 771). Count how many stones are also jewels.

```text
jewels = "aA"           stones = "aAAbbbb"

Slow: for each stone, scan "aA" to see if it matches       → O(stones × jewels)

Fast: jewelSet = { 'a', 'A' }                              → build once, O(jewels)
      for each stone: if stone in jewelSet → count++       → O(stones)

a → yes, A → yes, A → yes, b → no, b → no, b → no, b → no   → 3
```

#### 4. Core Concepts — Must Know

1. **Choose which side becomes the set.** Put the group you look **in** into the set. Usually the smaller or fixed group.
2. **Build once.** Do not rebuild the set inside the loop.
3. **Read-only after building** is fine. Use `setOf(...)` for constants.
4. **Cost model:** `O(m)` to build, `O(1)` per lookup, so `O(m + n)` total.
5. **Small fixed alphabets** can use a plain `BooleanArray` instead of a set.

| Group size | Best structure |
|---|---|
| Tiny (under about 10 items), checked a few times | A list is fine |
| Large or checked many times | `HashSet` |
| Small integer range (e.g. letters) | `BooleanArray` / `BitSet` |
| Needs ordering or ranges | `TreeSet` |

#### 5. Algorithm — Must Know

```text
lookup = set of the values to check against
for each query item:
    if item in lookup → use it
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Jewels and Stones
fun numJewelsInStones(jewels: String, stones: String): Int {
    val jewelSet = jewels.toHashSet()
    return stones.count { it in jewelSet }
}

// Constant set, built once
private val VOWELS = setOf('a', 'e', 'i', 'o', 'u')
fun countVowels(s: String): Int = s.lowercase().count { it in VOWELS }

// Filter text with a banned list (Most Common Word style)
fun removeBanned(words: List<String>, banned: List<String>): List<String> {
    val bannedSet = banned.map { it.lowercase() }.toHashSet()
    return words.filter { it.lowercase() !in bannedSet }
}

// Fast lookup of many ids
fun findKnown(ids: List<Int>, knownIds: List<Int>): List<Int> {
    val known = knownIds.toHashSet()           // build once
    return ids.filter { it in known }          // O(1) each
}
```

A simple array version for lowercase letters:

```kotlin
fun containsAllLetters(word: String, allowed: String): Boolean {
    val ok = BooleanArray(26)
    for (c in allowed) ok[c - 'a'] = true
    return word.all { ok[it - 'a'] }
}
```

#### 7. Time & Space Complexity — Must Know

| Step | Time |
|---|---:|
| Build the set from `m` items | `O(m)` |
| Each lookup | `O(1)` average |
| `n` lookups | `O(n)` |
| **Total** | **`O(m + n)`** |
| Space | `O(m)` |

Without the set: `O(m × n)`.

#### 8. Common Lookup Patterns — Must Know

1. **Allowed / banned list** — spam words, blocked users.
2. **Characters check** — vowels, digits, brackets.
3. **Known ids** — filter a list against a list of existing ids.
4. **Dictionary words** — `Word Break` style problems start by putting the dictionary in a set.
5. **Android example:** a `Set<String>` of granted permissions or enabled feature flags checked on every screen.

#### 9. Edge Cases / Common Mistakes

1. Building the set inside the loop, which makes it `O(n × m)` again.
2. Putting the larger group in the set when the smaller one would save memory.
3. Case problems: `"Apple"` and `"apple"` are different. Normalize first.
4. Using a `List<String>` for a banned list that is checked thousands of times.
5. Forgetting that the set holds copies of references only. Changing a mutable object inside breaks lookups.
6. Using a set for a 3-item check. A list is fine and simpler.

#### 10. When to Use / When Not to Use

**Use when:**

1. You check the same group many times.
2. The group is more than a handful of items.

**Avoid when:**

1. You check only once or twice with a tiny group.
2. You need the **position** of the match. Use a `HashMap<Value, Index>`.

#### 11. Related Topics

1. HashSet Fundamentals
2. HashSet vs HashMap
3. HashSet with Strings / Characters
4. Intersection / Common Elements

#### 12. Interview Must Remember

1. **Build the set once, query in `O(1)`.**
2. `O(m + n)` instead of `O(m × n)`.
3. Normalize case and whitespace before building the set.
4. Need the index → use a `HashMap`.
