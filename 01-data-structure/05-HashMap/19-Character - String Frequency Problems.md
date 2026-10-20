# Character / String Frequency Problems

> Very common in FAANG interviews. Most string questions start by counting letters.

#### 1. What Is It?

These are string questions solved by **counting characters**.

The counter is:

- `IntArray(26)` when the input is lowercase `a`–`z` (fast, `O(1)` space),
- `HashMap<Char, Int>` for any other characters,
- `HashMap<String, Int>` for words.

Comparing two counters tells you if two strings use the same letters: anagrams, permutations, ransom notes, palindromes.

#### 2. How It Works

Three rules to remember:

1. **Two strings are anagrams** when all their letter counts are equal.
2. **A string can be rearranged into a palindrome** when **at most one** letter has an odd count.
3. **To compare windows**, keep a count array for the window and compare it with the target counts.

*Longest Palindrome* (LeetCode 409): build the longest palindrome from the letters.

`s = "abccccdd"`

```text
counts:  a:1  b:1  c:4  d:2

Pairs of equal letters go on both sides:
    c has 4 → 2 pairs → 4 letters
    d has 2 → 1 pair  → 2 letters
    letters in pairs: 4 + 2 = 6

One leftover single letter (a or b) can go in the middle → +1

answer: 7     e.g. "dccaccd"
```

#### 3. Kotlin Code

```kotlin
// Valid Anagram
fun isAnagram(s: String, t: String): Boolean {
    if (s.length != t.length) return false
    val count = IntArray(26)
    for (i in s.indices) {
        count[s[i] - 'a']++
        count[t[i] - 'a']--
    }
    return count.all { it == 0 }
}

// Longest Palindrome that can be built from the letters
fun longestPalindrome(s: String): Int {
    val count = HashMap<Char, Int>()
    for (c in s) count[c] = (count[c] ?: 0) + 1
    var length = 0
    var hasOdd = false
    for (c in count.values) {
        length += c / 2 * 2                    // use the pairs
        if (c % 2 == 1) hasOdd = true
    }
    return if (hasOdd) length + 1 else length
}

// Palindrome Permutation: can some rearrangement be a palindrome?
fun canPermutePalindrome(s: String): Boolean {
    val odd = HashSet<Char>()
    for (c in s) if (!odd.add(c)) odd.remove(c)    // toggle the letter in and out
    return odd.size <= 1
}

// Find All Anagrams in a String: a fixed window of letter counts
fun findAnagrams(s: String, p: String): List<Int> {
    if (p.length > s.length) return emptyList()
    val need = IntArray(26)
    val window = IntArray(26)
    for (c in p) need[c - 'a']++
    val result = mutableListOf<Int>()
    for (i in s.indices) {
        window[s[i] - 'a']++
        if (i >= p.length) window[s[i - p.length] - 'a']--      // the letter that left the window
        if (i >= p.length - 1 && window.contentEquals(need)) result.add(i - p.length + 1)
    }
    return result
}

// Sort Characters By Frequency
fun frequencySort(s: String): String {
    val count = s.groupingBy { it }.eachCount()
    return count.entries
        .sortedByDescending { it.value }
        .joinToString("") { it.key.toString().repeat(it.value) }
}
```

Checks: `longestPalindrome("abccccdd")` → `7`. `findAnagrams("cbaebabacd", "abc")` → `[0, 6]`.

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| Anagram check | `O(n)` | `O(1)` for 26 letters |
| Longest Palindrome | `O(n)` | `O(alphabet)` |
| Find All Anagrams | `O(26 · n)` ≈ `O(n)` | `O(1)` |
| Sort by frequency | `O(n + u log u)` | `O(u)` |

#### 5. Common Mistakes

1. **`IntArray(26)` with capital letters, digits or spaces.** It crashes with an index error.
2. **Different lengths** in an anagram check.
3. **Not normalising case** (`'A'` vs `'a'`).
4. **Palindrome rule:** allowing more than one odd count.
5. **Comparing two `IntArray`s with `==`.** Use `contentEquals`.
6. **Maps with zero counts** make `==` fail. Remove zero-count keys first.
7. **Emoji and other Unicode.** A Kotlin `Char` is only a part of them. State your assumption.

#### 6. Say This in the Interview

1. "I assume lowercase English letters, so I use an `IntArray(26)`: `O(1)` space."
2. "Two strings are anagrams if every letter count is equal."
3. "For a palindrome, at most one letter may have an odd count."

#### 7. Quick Check

1. Can `"carrace"` be rearranged into a palindrome?
2. Why does `findAnagrams` subtract a letter when `i >= p.length`?

<details>
<summary>Answers</summary>

1. Yes. Counts: c:2, a:2, r:2, e:1 — only one odd count.
2. That letter just left the window, so its count must go down.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 242 | Valid Anagram (Easy) | equal counts |
| 383 | Ransom Note (Easy) | enough letters |
| 387 | First Unique Character in a String (Easy) | count, then scan |
| 409 | Longest Palindrome (Easy) | pairs plus one |
| 438 | Find All Anagrams in a String (Medium) | fixed window |
| 567 | Permutation in String (Medium) | fixed window |
| 451 | Sort Characters By Frequency (Medium) | counts, then sort |
| 49 | Group Anagrams (Medium) | counts as a key (note 20) |
