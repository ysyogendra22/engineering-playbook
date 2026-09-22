# String DP — Palindromes, Word Break, Decode Ways

#### 1. Definition — Must Know

**String DP** applies the same four-step method (topic 3) to problems about a single string: is a substring a palindrome, can the string be split into valid words, how many ways can it be decoded.

#### 2. Why It Is Used — Must Know

1. These three problems (palindromes, word break, decode ways) are among the most frequently asked string interview questions, and they all share the same underlying shape: "can/how many ways can this prefix (or substring) be built validly?"
2. Once you've seen the shape once, the others become much faster to recognise and solve.

#### 3. How It Works — Must Know

**Word Break**: can `"leetcode"` be split into words from a dictionary `{"leet", "code"}`?

```text
dp[i] = true if s[0..i) can be fully split into dictionary words

dp[0] = true   (empty prefix)
dp[4] = true   ("leet" is in the dictionary, and dp[0] is true)
dp[8] = true   ("code" is in the dictionary, and dp[4] is true)

→ dp[8] (the whole string) is true
```

**Decode Ways**: how many ways can `"226"` be decoded, where 'A'=1 ... 'Z'=26?

```text
dp[i] = number of ways to decode the first i characters

"2" → could be "2" alone           → dp[1] = 1
"22" → "2"+"2" or "22"             → dp[2] = 2
"226" → "2"+"26", "22"+"6", "2"+"2"+"6" → dp[3] = 3
(check: does s[i-1] form a valid 1-digit code? does s[i-2..i) form a valid 2-digit code?)
```

**Longest Palindromic Substring** uses a 2D table: `dp[i][j] = true` if `s[i..j]` is a palindrome, built from the inside out: `dp[i][j] = (s[i] == s[j]) AND dp[i+1][j-1]`.

#### 4. Algorithm — Must Know

```text
Word Break:
  dp[0] = true
  for i in 1..n:
      for j in 0 until i:
          if dp[j] is true AND s[j until i] is in the dictionary:
              dp[i] = true
              break

Decode Ways:
  dp[0] = 1
  for i in 1..n:
      if s[i-1] is a valid single digit ('1'-'9'): dp[i] += dp[i-1]
      if s[i-2..i) is a valid two-digit code ("10"-"26"): dp[i] += dp[i-2]
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun wordBreak(s: String, dictionary: Set<String>): Boolean {
    val dp = BooleanArray(s.length + 1)
    dp[0] = true
    for (i in 1..s.length) {
        for (j in 0 until i) {
            if (dp[j] && s.substring(j, i) in dictionary) {
                dp[i] = true
                break
            }
        }
    }
    return dp[s.length]
}
```

#### 6. Complexity — Must Know

| Problem | Time | Space |
|---|---|---|
| Word Break | O(n² × average word length) for the substring checks | O(n) |
| Decode Ways | O(n) | O(n), or O(1) optimised |
| Longest Palindromic Substring (DP) | O(n²) | O(n²) |

#### 7. Common Mistakes — Must Know

1. In Word Break: re-checking substrings inefficiently — using a `HashSet` for the dictionary lookup (O(1)) instead of scanning a list (O(k)).
2. In Decode Ways: forgetting that `"0"` is never a valid single digit, and that two-digit codes must be between `"10"` and `"26"` — a leading zero like `"06"` is invalid.
3. In palindrome DP: filling the table in the wrong order — you need `dp[i+1][j-1]` (a shorter, inner substring) before `dp[i][j]`, so the fill order goes by increasing substring length, not simple row order.

#### 8. Related Topics

1. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — the method behind all three
2. `5` 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence — the 2D version this palindrome DP uses
3. `08` String Algorithms (its own folder) — general string techniques (two pointers work for palindrome *checking*, but not for finding the longest one)

#### 9. Interview Must Remember

1. **Word Break and Decode Ways share the same recurrence shape:** "can/how many ways to reach position `i`, by trying every valid last piece."
2. Decode Ways is really 1D DP with two possible "last steps" (one digit, or two digits) — the same shape as House Robber's two options.
3. Palindrome DP fills **by substring length**, from short substrings to long ones — not the usual left-to-right row order.
