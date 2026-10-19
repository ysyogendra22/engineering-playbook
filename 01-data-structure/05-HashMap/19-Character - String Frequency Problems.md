# Character / String Frequency Problems

#### 1. Definition — Must Know

1. These are string problems solved by **counting characters** (or words).
2. The counter is either a **`HashMap<Char, Int>`** (any characters) or an **`IntArray(26)`** (lowercase letters only).
3. Comparing two counters tells you if two strings use the same letters (anagrams, permutations, ransom notes, palindromes).

#### 2. Why It Is Used — Must Know

1. It avoids sorting the strings (`O(n log n)`) and works in `O(n)`.
2. It is the most common string pattern in interviews.
3. It is the base of the sliding window string problems.

#### 3. How It Works — Must Know

*Longest Palindrome* (LeetCode 409): build the longest palindrome from the given letters.

`s = "abccccdd"`

```text
counts:  a:1  b:1  c:4  d:2

Each pair of equal letters can sit on both sides:  c,c  c,c  d,d  → 4 + 2 = 6 letters in pairs ... (c:4 → 4, d:2 → 2, total 6)
One leftover single letter (a or b) can go in the middle → +1

Answer: 7     e.g. "dccaccd"
```

Rule: add `count / 2 * 2` for every letter. If any letter has an odd count, add `1` for the middle.

*Find All Anagrams in a String* uses the same counts, but in a fixed window that slides one step at a time.

#### 4. Core Concepts — Must Know

1. **Pick the counter:**

| Input | Counter |
|---|---|
| Lowercase `a`–`z` | `IntArray(26)`, index `c - 'a'` |
| ASCII | `IntArray(128)` or `IntArray(256)` |
| Any Unicode | `HashMap<Char, Int>` |
| Words | `HashMap<String, Int>` |

2. **Two strings are anagrams** when all their letter counts are equal.
3. **Compare two arrays** with `contentEquals`. Compare two maps with `==`.
4. **Add for one string, subtract for the other.** If all counts end at 0, they match.
5. **Palindrome rule:** at most one letter may have an odd count.
6. **Normalize first:** `lowercase()`, remove spaces and punctuation if the problem says to ignore them.

#### 5. Algorithm — Must Know

```text
count = counter for string A (add)
for each character of string B: count[c] -= 1
all counts are 0  →  same letters
```

#### 6. Kotlin Implementation — Must Know

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
        length += c / 2 * 2
        if (c % 2 == 1) hasOdd = true
    }
    return if (hasOdd) length + 1 else length
}

// Palindrome Permutation — can some rearrangement be a palindrome?
fun canPermutePalindrome(s: String): Boolean {
    val odd = HashSet<Char>()
    for (c in s) if (!odd.add(c)) odd.remove(c)       // toggle
    return odd.size <= 1
}

// Find All Anagrams in a String — fixed window
fun findAnagrams(s: String, p: String): List<Int> {
    if (p.length > s.length) return emptyList()
    val need = IntArray(26)
    val window = IntArray(26)
    for (c in p) need[c - 'a']++
    val result = mutableListOf<Int>()
    for (i in s.indices) {
        window[s[i] - 'a']++
        if (i >= p.length) window[s[i - p.length] - 'a']--
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

// Any characters (not only a–z)
fun charCounts(s: String): Map<Char, Int> = s.groupingBy { it }.eachCount()
```

Checks: `longestPalindrome("abccccdd")` → `7`. `findAnagrams("cbaebabacd", "abc")` → `[0, 6]`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Anagram check | `O(n)` | `O(1)` for 26 letters |
| Longest Palindrome | `O(n)` | `O(alphabet)` |
| Find All Anagrams | `O(26 · n)` ≈ `O(n)` | `O(1)` |
| Sort by frequency | `O(n + u log u)` | `O(u)` |

`u` = number of distinct characters.

#### 8. Common Frequency-String Patterns — Must Know

1. **Valid Anagram** (LeetCode 242).
2. **Ransom Note** (LeetCode 383).
3. **First Unique Character in a String** (LeetCode 387).
4. **Longest Palindrome** (LeetCode 409), **Palindrome Permutation** (LeetCode 266, premium).
5. **Find All Anagrams in a String** (LeetCode 438), **Permutation in String** (LeetCode 567).
6. **Sort Characters By Frequency** (LeetCode 451).
7. **Group Anagrams** (LeetCode 49) — counts or sorted letters as a key.
8. **Minimum Number of Steps to Make Two Strings Anagram** (LeetCode 1347) — count differences.
9. **Word frequency** in text — `HashMap<String, Int>`.

#### 9. Edge Cases / Common Mistakes

1. `IntArray(26)` with uppercase letters, digits, or spaces. This gives an index error.
2. Different lengths in an anagram check.
3. Forgetting to normalize case or remove spaces.
4. Comparing map counts when one map still has `0` entries.
5. Palindrome: allowing more than one odd count.
6. Unicode: a Kotlin `Char` is a 16-bit unit. Emoji need code points.
7. Using `==` to compare two `IntArray`s. Use `contentEquals`.
8. Empty strings: two empty strings are anagrams.

#### 10. When to Use / When Not to Use

**Use `IntArray(26)` when:**

1. The input is lowercase English letters. It is faster and uses `O(1)` space.

**Use a `HashMap` when:**

1. The alphabet is large or unknown, or the items are words.

**Avoid counting when:**

1. Order matters (substrings, subsequences). Use DP or two pointers.

#### 11. Related Topics

1. Frequency Counting
2. Group Anagrams Pattern
3. HashMap + Two Pointers / Sliding Window
4. String Algorithms (`02-algorithm/08-String Algorithms`)

#### 12. Interview Must Remember

1. **Letters `a`–`z` → `IntArray(26)`. Anything else → `HashMap`.**
2. Anagram = equal counts. Palindrome = at most one odd count.
3. `contentEquals` for arrays; `==` for maps.
4. Normalize case and say your alphabet assumption.
