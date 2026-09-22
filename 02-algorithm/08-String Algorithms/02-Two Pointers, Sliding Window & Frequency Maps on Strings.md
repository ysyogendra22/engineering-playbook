# Two Pointers, Sliding Window & Frequency Maps on Strings

#### 1. Definition — Must Know

Most string interview problems aren't solved with a named string algorithm at all — they're solved with the same general techniques used on arrays: **two pointers**, a **sliding window**, and **frequency maps** (counting characters), just applied to characters instead of numbers.

#### 2. Why It Is Used — Must Know

1. This is, in practice, how the large majority of string problems in interviews actually get solved — recognising this early saves you from hunting for a "special string algorithm" that usually isn't needed.
2. It connects this folder directly back to `04` Two Pointers and `05` Sliding Window in `03-leetcode-patterns`, so the same templates apply.

#### 3. How It Works — Must Know

**Two pointers** — checking if a string is a palindrome:

```text
"racecar"
 ↑     ↑
left  right

s[left] == s[right]? 'r' == 'r' → move both pointers inward
's' == 'a'? no wait — continue: 'a'=='a', 'c'=='c', pointers meet at 'e' → palindrome
```

**Sliding window** — longest substring without repeating characters:

```text
"abcabcbb"

Expand right, shrink left when a repeat is found, track the max window size seen.
See `05-Sliding Window` in `03-leetcode-patterns` for the full walkthrough.
```

**Frequency map** — checking if two strings are anagrams:

```text
"listen" and "silent"

count each character in "listen": {l:1, i:1, s:1, t:1, e:1, n:1}
count each character in "silent": {s:1, i:1, l:1, e:1, n:1, t:1}

Same counts → anagrams
```

#### 4. Algorithm — Must Know

```text
Two pointers on a string:      left = 0, right = length - 1, move inward
Sliding window on a string:    expand right, shrink left based on a condition
Frequency map:                 count characters in a HashMap<Char, Int>,
                                or an IntArray of size 26 for lowercase letters
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun isAnagram(a: String, b: String): Boolean {
    if (a.length != b.length) return false
    val counts = IntArray(26)
    for (c in a) counts[c - 'a']++
    for (c in b) counts[c - 'a']--
    return counts.all { it == 0 }
}

fun isPalindrome(s: String): Boolean {
    var left = 0
    var right = s.length - 1
    while (left < right) {
        if (s[left] != s[right]) return false
        left++; right--
    }
    return true
}
```

#### 6. Complexity — Must Know

| Technique | Time | Space |
|---|---|---|
| Two pointers on a string | O(n) | O(1) |
| Sliding window on a string | O(n) | O(k), k = distinct characters tracked |
| Frequency map | O(n) | O(1) for a fixed alphabet (26 letters), O(n) for a general one |

#### 7. Common Mistakes — Must Know

1. Building a new frequency map from scratch inside a sliding window loop, instead of incrementally updating one map as the window moves — this turns an O(n) solution into O(n × k).
2. Using a `HashMap<Char, Int>` when a fixed-size `IntArray(26)` would be faster and simpler, for lowercase-letters-only problems.
3. Treating every string problem as needing KMP or another named algorithm, when a simple two-pointer or frequency-map approach already solves it in O(n).

#### 8. Related Topics

1. `4` Two Pointers, `5` Sliding Window, `20` More Patterns to Know (all in `03-leetcode-patterns`) — the full pattern write-ups
2. `3` Palindrome Checks & Palindrome-Related DP — the DP version, for finding the longest palindromic substring

#### 9. Interview Must Remember

1. **Most string problems are array problems in disguise** — reach for two pointers, sliding window, or a frequency map first.
2. A fixed-size array (`IntArray(26)`) beats a `HashMap` for counting lowercase letters — faster and simpler.
3. Update frequency counts incrementally inside a sliding window, never rebuild from scratch each step.
