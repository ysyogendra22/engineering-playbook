# Group Anagrams Pattern

#### 1. Definition — Must Know

1. **Anagrams** are words with the same letters in a different order (`eat`, `tea`, `ate`).
2. **Group Anagrams** (LeetCode 49): put all anagrams of each other into one group.
3. The method: compute a **signature key** that is the same for all anagrams, and use `key → list of words`.

#### 2. Why It Is Used — Must Know

1. It is the classic example of the **grouping pattern** with a clever key.
2. The same idea (canonical key) solves many "group things that are equal after a change" problems.
3. It is one of the top HashMap interview questions.

#### 3. How It Works — Must Know

`words = ["eat", "tea", "tan", "ate", "nat", "bat"]`

**Key option 1: sorted letters**

```text
eat → aet
tea → aet
tan → ant
ate → aet
nat → ant
bat → abt

groups:  aet → [eat, tea, ate]
         ant → [tan, nat]
         abt → [bat]
```

**Key option 2: letter counts** (no sorting)

```text
eat → a1 e1 t1  → "1,0,0,0,1,0,...,1,..."    (26 numbers)
tea → the same key
```

#### 4. Core Concepts — Must Know

1. **Signature = canonical form.** Every anagram gives the same signature; different words give different ones.
2. **Sorted-letters key:** `O(k log k)` per word of length `k`. Simple and short.
3. **Count key:** `O(k)` per word. Better for long words, a little longer to write.
4. **Key type:** a `String` (sorted letters), or a `List<Int>` of 26 counts. **Not an `IntArray`.**
5. **Separator in count keys.** `"1,0,..."` — without a separator, `11` and `1,1` blur together.
6. **Result:** `map.values.toList()`. The order of groups and of words in a group is usually free.

| Key | Time per word | Notes |
|---|---:|---|
| Sorted letters | `O(k log k)` | shortest code |
| 26-count list | `O(k)` | faster for long words |
| Product of primes | `O(k)` | tricky (overflow); not recommended |

#### 5. Algorithm — Must Know

```text
groups = empty map
for each word:
    key = signature(word)
    groups.getOrPut(key) { new list }.add(word)
return groups.values
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Sorted letters as the key
fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val groups = HashMap<String, MutableList<String>>()
    for (word in strs) {
        val key = String(word.toCharArray().also { it.sort() })
        groups.getOrPut(key) { mutableListOf() }.add(word)
    }
    return groups.values.toList()
}

// Letter counts as the key — O(k) per word (lowercase a–z)
fun groupAnagramsCount(strs: Array<String>): List<List<String>> {
    val groups = HashMap<List<Int>, MutableList<String>>()
    for (word in strs) {
        val count = IntArray(26)
        for (c in word) count[c - 'a']++
        groups.getOrPut(count.toList()) { mutableListOf() }.add(word)     // List compares by content
    }
    return groups.values.toList()
}

// One-liner with groupBy
fun groupAnagramsShort(strs: Array<String>): List<List<String>> =
    strs.groupBy { it.toCharArray().sorted().joinToString("") }.values.toList()
```

Check: `groupAnagrams(["eat","tea","tan","ate","nat","bat"])` → `[[eat, tea, ate], [tan, nat], [bat]]` (group order may differ).

A related canonical-key idea: *Group Shifted Strings* uses the differences between neighbouring letters as the key.

#### 7. Time & Space Complexity — Must Know

For `n` words of maximum length `k`:

| Key | Time | Space |
|---|---:|---:|
| Sorted letters | `O(n · k log k)` | `O(n · k)` |
| 26-count list | `O(n · k)` | `O(n · k)` |

#### 8. Common Anagram Patterns — Must Know

1. **Group Anagrams** (LeetCode 49).
2. **Valid Anagram** (LeetCode 242) — compare two counts.
3. **Find All Anagrams in a String** (LeetCode 438) — window counts.
4. **Group Shifted Strings** (LeetCode 249, premium) — difference-pattern key.
5. **Find Resultant Array After Removing Anagrams** (LeetCode 2273) — neighbouring signatures.
6. **Canonical key for other equality:** reverse, rotate, case-insensitive, shape.

#### 9. Edge Cases / Common Mistakes

1. Using `IntArray` as the map key. It compares by reference, so nothing groups.
2. Count key as a joined string without a separator (`"11"` ambiguity).
3. Uppercase or non-letter characters in a `IntArray(26)` solution.
4. Empty string `""` — it forms its own group (key `""`).
5. Forgetting that the result order is not defined.
6. Sorting `chars` but forgetting to convert back to a `String` (`toString()` on a `CharArray` gives an address).
7. Using a `HashMap<String, List<String>>` and trying to `add` to a read-only list.
8. Words with different letter cases being treated as different.

#### 10. When to Use / When Not to Use

**Use sorted letters when:**

1. Words are short and you want simple code.

**Use counts when:**

1. Words are long (the sort cost `k log k` matters), or you must reach `O(n · k)`.

**Avoid when:**

1. You only compare two words. A single count array check is enough.

#### 11. Related Topics

1. Grouping Pattern
2. Character / String Frequency Problems
3. HashMap with Custom Objects / Keys
4. Deduplication of Complex States (`01-data-structure/06-HashSet/18-Deduplication of Complex States.md`)

#### 12. Interview Must Remember

1. **Key = sorted letters (or 26 counts). Value = list of words.**
2. **Never use an `IntArray` as a key.** Use a `String` or `List<Int>`.
3. `O(n · k log k)` with sorting, `O(n · k)` with counts.
4. `String(chars)` or `joinToString("")`, not `chars.toString()`.
