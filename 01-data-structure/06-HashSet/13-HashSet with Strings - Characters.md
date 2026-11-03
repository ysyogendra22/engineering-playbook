# HashSet with Strings / Characters

> A set of **characters** answers "is every letter different?", "which letters appear?" and "is the alphabet covered?". For lowercase letters, a `BooleanArray(26)` is even faster.

#### 1. What Is It?

Strings are made of characters, and many string questions are about **which characters exist** or **whether a character repeats**.

| Question | Tool |
|---|---|
| Are all characters unique? | `HashSet<Char>` (or `BooleanArray`) |
| Which characters appear in both strings? | set intersection |
| Does the text contain every letter `a..z`? | set size `== 26` |
| Longest substring without repeats | set + sliding window (note 14) |
| Distinct substrings / words | `HashSet<String>` |
| Is a string made only of allowed letters? | `allowed.toSet().containsAll(...)` |

**Signals:** "unique characters", "no repeating character", "distinct letters", "common letters", "pangram", "duplicate letters".

#### 2. How It Works

**All unique?** Add characters one by one. If `add` returns `false`, a repeat exists.

```text
"abca" → add a, add b, add c, add a → false → NOT unique
```

**Array instead of a set (lowercase only).** `val seen = BooleanArray(26)`; index `c - 'a'`. No hashing, no boxing, so it is faster and uses `O(1)` space (26 slots). For all ASCII use `BooleanArray(128)`.

**Characters vs strings.** `'a'` (a `Char`) and `"a"` (a `String`) are different keys. Keep the types consistent.

**Distinct strings.** Use `HashSet<String>`. Normalise first (`lowercase()`, `trim()`) if the question treats `"Cat"` and `"cat"` as the same.

**Valid Sudoku (LeetCode 36)** is the classic "many sets" problem: each row, each column and each 3×3 box must contain no repeated digit. Keep a set per row, per column and per box, or one set of strings such as `"5 in row 0"`, `"5 in col 3"`, `"5 in box 1"`.

```text
board digit '5' at (0, 0):  add "5r0", "5c0", "5b0".  If any add returns false → invalid.
```

**Longest Substring Without Repeating Characters (LeetCode 3)** with a set: grow the right end; while the new character is already in the window, remove from the left (note 14).

#### 3. Brute Force vs Optimized

| Task | Brute force | Set |
|---|---|---|
| All characters unique? | compare every pair `O(n²)` | set `O(n)` |
| Pangram | check each letter with `contains` `O(26 · n)` | set size `O(n)` |
| Common letters | nested loops `O(m · n)` | set intersection `O(m + n)` |
| Unique characters (lowercase) | | `BooleanArray(26)`, `O(n)` and `O(1)` space |

```kotlin
// Brute force: unique characters by comparing every pair
fun isUniqueBrute(s: String): Boolean {
    for (i in s.indices) for (j in i + 1 until s.length) if (s[i] == s[j]) return false
    return true
}
```

#### 4. Kotlin Code

```kotlin
// All characters unique (set)
fun isUnique(s: String): Boolean {
    val seen = HashSet<Char>()
    for (c in s) if (!seen.add(c)) return false
    return true
}

// All characters unique (array, lowercase only)
fun isUniqueArray(s: String): Boolean {
    val seen = BooleanArray(26)
    for (c in s) {
        val i = c - 'a'
        if (seen[i]) return false
        seen[i] = true
    }
    return true
}

// Check if the Sentence Is Pangram (LeetCode 1832)
fun checkIfPangram(sentence: String): Boolean = sentence.toSet().size == 26

// Letters that appear in both words
fun commonLetters(a: String, b: String): Set<Char> = a.toSet() intersect b.toSet()

// Valid Sudoku (LeetCode 36)
fun isValidSudoku(board: Array<CharArray>): Boolean {
    val seen = HashSet<String>()
    for (r in 0 until 9) {
        for (c in 0 until 9) {
            val d = board[r][c]
            if (d == '.') continue
            val box = (r / 3) * 3 + c / 3
            if (!seen.add("$d in row $r") || !seen.add("$d in col $c") || !seen.add("$d in box $box")) return false
        }
    }
    return true
}

// Longest Substring Without Repeating Characters (LeetCode 3), set version
fun lengthOfLongestSubstring(s: String): Int {
    val window = HashSet<Char>()
    var left = 0
    var best = 0
    for (right in s.indices) {
        while (!window.add(s[right])) {                  // a repeat: shrink from the left
            window.remove(s[left])
            left++
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}
```

Checks: `isUnique("abc")` → `true`. `isUnique("abca")` → `false`. `isUnique("")` → `true`. `isUniqueArray("abc")` → `true`; `isUniqueArray("abca")` → `false`. `isUniqueBrute("abca")` → `false`. `checkIfPangram("thequickbrownfoxjumpsoverthelazydog")` → `true`. `checkIfPangram("leetcode")` → `false`. `commonLetters("hello", "world")` → `[l, o]`. `lengthOfLongestSubstring("abcabcbb")` → `3`. `lengthOfLongestSubstring("bbbbb")` → `1`. `lengthOfLongestSubstring("pwwkew")` → `3`. `lengthOfLongestSubstring("")` → `0`. A Sudoku board with two `5`s in the first row → `isValidSudoku` is `false`; the standard valid LeetCode example board → `true`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| `isUnique` | `O(n)` | `O(alphabet)` |
| Pangram | `O(n)` | `O(26)` |
| `isValidSudoku` | `O(81)` = `O(1)` | `O(81)` |
| Longest substring (set) | `O(n)` | `O(alphabet)` |

An early exit makes `isUnique` finish within the alphabet size + 1 steps for a long string, since a string longer than the alphabet must repeat.

#### 6. Common Mistakes

1. **Using a `String` set when you need a `Char` set** (or the reverse).
2. **Index out of range** for `BooleanArray(26)` with upper-case or non-letters.
3. **Case sensitivity:** `'A'` and `'a'` are different.
4. **Sudoku:** computing the box index wrongly. It is `(r / 3) * 3 + c / 3`.
5. **Longest substring:** using `if` instead of `while` when shrinking.
6. **Forgetting that a string longer than the alphabet** (for example 27 lowercase letters) must contain a repeat.

#### 7. Say This in the Interview

1. "I'll add each character to a set. If `add` returns false, there's a repeat. `O(n)` time, and the set has at most as many entries as the alphabet size."
2. "For lowercase letters I can use a `BooleanArray(26)` instead: no hashing, `O(1)` space."
3. "For Sudoku I keep one set of strings, encoding the digit with its row, column and box."

#### 8. Quick Check

1. How many distinct characters does `"hello"` have?
2. Box index of cell `(4, 7)` in Sudoku?
3. Can a lowercase string of length 30 have all unique characters?

<details>
<summary>Answers</summary>

1. `4` (`h, e, l, o`).
2. `(4 / 3) * 3 + 7 / 3 = 3 + 2 = 5`.
3. No. There are only 26 lowercase letters, so a repeat must exist.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1832 | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) (Easy) | set size 26 |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Easy) | counts |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) | set + window |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (Medium) | sets per row, column, box |
| 2351 | [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) (Easy) | seen set |
| 1941 | [Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) (Easy) | counts, then a set |
