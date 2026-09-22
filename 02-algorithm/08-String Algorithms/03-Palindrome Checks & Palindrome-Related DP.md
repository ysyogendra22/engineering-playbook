# Palindrome Checks & Palindrome-Related DP

#### 1. Definition — Must Know

1. A **palindrome** reads the same forwards and backwards ("racecar", "abba").
2. **Checking** if a given string is a palindrome is a simple two-pointer problem (topic 2). **Finding** the longest palindromic substring inside a larger string needs Dynamic Programming (or a different, faster trick — see below).

#### 2. Why It Is Used — Must Know

Palindrome problems are extremely common in interviews, and they come in two very different difficulty levels: a simple O(n) check, and a genuinely trickier O(n²) "find the longest one" search — knowing which is which matters.

#### 3. How It Works — Must Know

**Checking one substring** (two pointers, O(length)):

```text
"level"
 ↑   ↑
compare outer characters, move inward: 'l'=='l', 'e'=='e', meet at 'v' → palindrome
```

**Longest Palindromic Substring** (DP, considering every substring):

```text
dp[i][j] = true if s[i..j] is a palindrome

dp[i][i] = true                              (single character, base case)
dp[i][i+1] = (s[i] == s[i+1])                (two characters, base case)
dp[i][j] = (s[i] == s[j]) AND dp[i+1][j-1]   (general case — must fill
                                               SHORTER substrings first)

Example, s = "babad":
dp["a"]     = true (length 1)
dp["bab"]   = (s[0]==s[2]) AND dp["a"] (the middle) = true AND true = true
dp["aba"]   = true, also length 3

Longest found: "bab" or "aba" (both length 3, either is a valid answer)
```

#### 4. Algorithm — Must Know

```text
Simple check:
  left = 0, right = length - 1
  while left < right:
      if s[left] != s[right]: return false
      left++; right--
  return true

Longest palindromic substring (DP):
  for length in 1..n:                    # fill by increasing substring length
      for i in 0..(n - length):
          j = i + length - 1
          if length == 1: dp[i][j] = true
          elif length == 2: dp[i][j] = (s[i] == s[j])
          else: dp[i][j] = (s[i] == s[j]) AND dp[i+1][j-1]
          if dp[i][j] and length > bestLength:
              bestLength = length; bestStart = i
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun longestPalindrome(s: String): String {
    val n = s.length
    if (n == 0) return ""
    val dp = Array(n) { BooleanArray(n) }
    var start = 0
    var maxLength = 1
    for (i in 0 until n) dp[i][i] = true
    for (length in 2..n) {
        for (i in 0..n - length) {
            val j = i + length - 1
            dp[i][j] = s[i] == s[j] && (length == 2 || dp[i + 1][j - 1])
            if (dp[i][j] && length > maxLength) {
                start = i
                maxLength = length
            }
        }
    }
    return s.substring(start, start + maxLength)
}
```

#### 6. Complexity — Must Know

| Problem | Time | Space |
|---|---|---|
| Check one substring | O(length) | O(1) |
| Longest palindromic substring (DP) | O(n²) | O(n²) |
| Longest palindromic substring (expand-around-centre trick) | O(n²) | O(1) |

🟡 **The expand-around-centre trick**: for each possible centre (there are `2n - 1` of them, including "between two characters" for even-length palindromes), expand outward with two pointers while the characters still match. Same O(n²) time as the DP version, but O(1) space — often preferred in practice for this specific problem.

#### 7. Common Mistakes — Must Know

1. Filling the DP table in the wrong order — `dp[i][j]` needs `dp[i+1][j-1]` (a shorter, inner substring), so you must fill **by increasing length**, not simple row-by-row order.
2. Forgetting the separate base case for length-2 substrings (`dp[i][i+1]` has no inner substring to check).
3. Not considering **even-length** palindromes separately when using the expand-around-centre trick — you need to try both "centred on one character" and "centred between two characters".

#### 8. Related Topics

1. `2` Two Pointers, Sliding Window & Frequency Maps on Strings — the simple check
2. `10` String DP — Palindromes, Word Break, Decode Ways (in `05-Dynamic Programming`) — more on this DP shape
3. `12` Interval DP & Bitmask DP — Names Only (in `05-Dynamic Programming`) — palindrome DP is a simple interval DP

#### 9. Interview Must Remember

1. **Checking** a palindrome is O(n) with two pointers. **Finding the longest one** is O(n²), either with DP or the expand-around-centre trick.
2. Palindrome DP fills by **increasing substring length** — say this explicitly, it's the detail that trips people up.
3. Mention the expand-around-centre alternative — it solves the same problem with the same time but less space.
