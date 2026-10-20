# Group Anagrams Pattern

> A top HashMap interview question. The idea "make a canonical key" is used in many problems.

#### 1. What Is It?

**Anagrams** are words with the same letters in a different order: `eat`, `tea`, `ate`.

**Group Anagrams** (LeetCode 49): put the words that are anagrams of each other into one group.

Method: give every word a **key** that is the **same for all its anagrams**, then use `key → list of words`.

Two good keys:

| Key | How | Cost per word of length `k` |
|---|---|---|
| **Sorted letters** | `"eat"` → `"aet"` | `O(k log k)` |
| **Letter counts** | 26 numbers, e.g. `[1,0,0,0,1,...,1,...]` | `O(k)` |

#### 2. How It Works

`words = ["eat", "tea", "tan", "ate", "nat", "bat"]`

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

The result is `map.values`. The order of the groups and of the words inside a group does not matter.

Why a key works: all anagrams have the same letters, so they have the same sorted form (or the same counts). Different words give different keys.

#### 3. Kotlin Code

```kotlin
// Key = sorted letters
fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val groups = HashMap<String, MutableList<String>>()
    for (word in strs) {
        val key = String(word.toCharArray().also { it.sort() })
        groups.getOrPut(key) { mutableListOf() }.add(word)
    }
    return groups.values.toList()
}

// Key = letter counts (faster for long words). Lowercase a-z only.
fun groupAnagramsCount(strs: Array<String>): List<List<String>> {
    val groups = HashMap<List<Int>, MutableList<String>>()
    for (word in strs) {
        val count = IntArray(26)
        for (c in word) count[c - 'a']++
        groups.getOrPut(count.toList()) { mutableListOf() }.add(word)     // a List compares by content
    }
    return groups.values.toList()
}

// One line
fun groupAnagramsShort(strs: Array<String>): List<List<String>> =
    strs.groupBy { it.toCharArray().sorted().joinToString("") }.values.toList()
```

Check: `groupAnagrams(["eat","tea","tan","ate","nat","bat"])` → `[[eat, tea, ate], [tan, nat], [bat]]` (the order may differ).

#### 4. Complexity

For `n` words of length up to `k`:

| Key | Time | Space |
|---|---|---|
| Sorted letters | `O(n · k log k)` | `O(n · k)` |
| Letter counts | `O(n · k)` | `O(n · k)` |

#### 5. Common Mistakes

1. **Using an `IntArray` as the key.** Arrays compare by reference, so nothing groups. Use `count.toList()` or a `String`.
2. **A count key without separators** if you make it a `String` (`"11"` could mean `1,1` or `11`). Use `"1,1"`.
3. **Capital letters or digits** with `IntArray(26)`.
4. **`chars.toString()`** gives an address, not the text. Use `String(chars)` or `joinToString("")`.
5. **The empty string** `""` forms its own group. That is correct.
6. **Adding to a read-only list.** Use `MutableList` in the map.

#### 6. Say This in the Interview

1. "All anagrams have the same sorted letters, so I use the sorted word as the key and group words under it."
2. "That is `O(n · k log k)`. For long words I can use a 26-letter count as the key and get `O(n · k)`."
3. "Never use an `IntArray` as a key. I convert it to a `List` or a `String`."

#### 7. Quick Check

1. What is the sorted-letter key of `"listen"` and `"silent"`?
2. Why can't an `IntArray` be the key?

<details>
<summary>Answers</summary>

1. Both give `"eilnst"`, so they are in the same group.
2. Two arrays with the same numbers are different objects and are not equal as keys.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 49 | Group Anagrams (Medium) | this note |
| 242 | Valid Anagram (Easy) | compare two counts |
| 438 | Find All Anagrams in a String (Medium) | counts in a window |
| 249 | Group Shifted Strings (Medium, premium) | key = pattern of differences |
| 2273 | Find Resultant Array After Removing Anagrams (Easy) | compare neighbour keys |
