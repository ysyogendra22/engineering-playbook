# HashSet with Strings / Characters

#### 1. Definition — Must Know

1. Many string problems ask "**which characters (or words) have I seen?**". A `HashSet<Char>` or `HashSet<String>` answers that in `O(1)`.
2. Use a set of `Char` for letters and symbols, and a set of `String` for words or substrings.
3. For lowercase English letters only, a `BooleanArray(26)` is even faster.

#### 2. Why It Is Used — Must Know

1. It gives easy solutions to: repeated characters, pangrams, unique characters, vowels, banned words.
2. It builds the base for windowed string problems.
3. Strings are very common in mobile apps (validation, search, text parsing).

#### 3. How It Works — Must Know

Find the **first repeated character** in `"abcdbe"`:

```text
seen = {}
a → new   seen = {a}
b → new   seen = {a, b}
c → new   seen = {a, b, c}
d → new   seen = {a, b, c, d}
b → add returns false → b is the first repeated character
```

Check a **pangram** (every letter `a`–`z` at least once):

```text
"the quick brown fox jumps over the lazy dog"
→ keep only letters → put in a set → set.size == 26 → true
```

#### 4. Core Concepts — Must Know

1. **`HashSet<Char>`** for single characters. **`HashSet<String>`** for words or substrings.
2. **`toSet()` on a `String`** makes a set of its characters: `"hello".toSet()` → `{h, e, l, o}`.
3. **Normalize first:** `lowercase()`, `trim()`, remove punctuation if the problem needs it.
4. **Array alternative:** for `'a'..'z'` use `BooleanArray(26)` and `c - 'a'` as the index.
5. **Substrings in a set are expensive:** each substring costs `O(L)` to build and hash.
6. **Unicode warning:** a Kotlin `Char` is a 16-bit unit. Emoji and some symbols are two `Char`s (a surrogate pair). For interviews, assume the problem says "lowercase English letters" or ASCII.

| Task | Tool |
|---|---|
| Letters seen? | `HashSet<Char>` or `BooleanArray(26)` |
| Word allowed or banned? | `HashSet<String>` |
| All characters unique? | `s.toSet().size == s.length` |
| Count letters | `IntArray(26)` or `HashMap<Char, Int>` |

#### 5. Algorithm — Must Know

```text
seen = empty set
for each character c in s:
    if seen.add(c) is false → c repeats
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// First repeated character
fun firstRepeated(s: String): Char? {
    val seen = HashSet<Char>()
    for (c in s) if (!seen.add(c)) return c
    return null
}

// All characters unique (isogram / unique characters)
fun hasAllUniqueChars(s: String): Boolean = s.toSet().size == s.length

// Pangram
fun isPangram(sentence: String): Boolean =
    sentence.lowercase().filter { it in 'a'..'z' }.toSet().size == 26

// Count vowels using a constant set
private val VOWELS = setOf('a', 'e', 'i', 'o', 'u')
fun countVowels(s: String): Int = s.lowercase().count { it in VOWELS }

// Array version, faster for lowercase letters
fun hasAllUniqueLowercase(s: String): Boolean {
    val seen = BooleanArray(26)
    for (c in s) {
        val i = c - 'a'
        if (seen[i]) return false
        seen[i] = true
    }
    return true
}

// Distinct words, ignoring case
fun distinctWords(text: String): Set<String> =
    text.lowercase().split(" ", ",", ".").filter { it.isNotBlank() }.toSet()

// Number of distinct substrings of a given length
fun distinctSubstrings(s: String, len: Int): Int {
    val set = HashSet<String>()
    for (i in 0..s.length - len) set.add(s.substring(i, i + len))
    return set.size
}
```

Checks: `firstRepeated("abcdbe")` → `'b'`. `hasAllUniqueChars("abc")` → `true`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| Set of characters, length `n` | `O(n)` | `O(min(n, alphabet))` |
| `BooleanArray(26)` version | `O(n)` | `O(1)` |
| Distinct words, `w` words of length `L` | `O(w × L)` | `O(w × L)` |
| Distinct substrings of length `k` | `O(n × k)` | `O(n × k)` |

#### 8. Common String-Set Patterns — Must Know

1. **First repeated character** and **unique characters** checks.
2. **Pangram** (LeetCode 1832 *Check if the Sentence Is Pangram*).
3. **Jewels and Stones** (LeetCode 771) — set lookup.
4. **Longest substring without repeating characters** (LeetCode 3) — set plus sliding window.
5. **Word Break** (LeetCode 139) — the dictionary as a `HashSet<String>`.
6. **Repeated DNA sequences** (LeetCode 187) — substrings of length 10 in two sets.
7. **Check if two strings share a character** — set intersection.

#### 9. Edge Cases / Common Mistakes

1. Case: `'A'` and `'a'` are different. Normalize if needed.
2. Spaces and punctuation counted as characters.
3. Empty string. `toSet()` is empty, and `firstRepeated` returns `null`.
4. Using a `BooleanArray(26)` with uppercase letters or digits. This gives an index error.
5. Building many substrings and running out of memory.
6. Surrogate pairs (emoji) split into two `Char`s.
7. Accent marks and Unicode normalization (not an interview topic, but real in apps).

#### 10. When to Use / When Not to Use

**Use a `HashSet<Char>` when:**

1. The character set is unknown or large.

**Use a `BooleanArray`/`IntArray(26)` when:**

1. The input is lowercase English letters. It is faster and lighter.

**Use a `HashMap` when:**

1. You need counts per character.

#### 11. Related Topics

1. Fast Membership / Lookup Pattern
2. HashSet + Sliding Window
3. Duplicate Detection
4. String (`02-algorithm/08-String Algorithms`)

#### 12. Interview Must Remember

1. **`s.toSet()` gives distinct characters.**
2. Unique characters: `s.toSet().size == s.length`.
3. For `a`–`z`, a `BooleanArray(26)` beats a set.
4. Normalize case first and state your alphabet assumption.
