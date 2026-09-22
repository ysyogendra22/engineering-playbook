# 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence

#### 1. Definition — Must Know

**2D DP** means the state needs **two numbers** to describe it — often two positions (a row and a column in a grid), or a position in each of two strings. `dp[i][j]` is a table, not a single array.

#### 2. Why It Is Used — Must Know

1. Comparing two sequences (two strings, or moving through a 2D grid) naturally needs two indices to describe where you are — one number isn't enough.
2. Edit Distance and Longest Common Subsequence (LCS) are two of the most commonly asked DP problems in interviews.

#### 3. How It Works — Must Know

**Longest Common Subsequence** of `"abcde"` and `"ace"`:

```text
        ""  a  c  e
    ""   0  0  0  0
    a    0  1  1  1
    b    0  1  1  1
    c    0  1  2  2
    d    0  1  2  2
    e    0  1  2  3   ← answer = 3  ("ace")

dp[i][j] = LCS length of the first i characters of "abcde"
           and the first j characters of "ace"

If the characters match: dp[i][j] = dp[i-1][j-1] + 1
If they don't match:     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Unique Paths** (grid, top-left to bottom-right, only right/down moves) works the same way: `dp[i][j] = dp[i-1][j] + dp[i][j-1]` — the number of ways to reach a cell is the sum of the ways to reach the cell above and the cell to the left.

#### 4. Algorithm — Must Know

```text
State:      dp[i][j] = answer using the first i elements of sequence A
                        and the first j elements of sequence B
                        (or: the answer at grid position (i, j))
Recurrence: depends on the problem — usually compares element i of A
            with element j of B, or combines dp[i-1][j] and dp[i][j-1]
Base case:  dp[0][*] and dp[*][0]  (empty prefix of one sequence)
Fill order: row by row (or column by column) — each cell only needs
            cells above, to the left, or diagonally above-left
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun longestCommonSubsequence(a: String, b: String): Int {
    val dp = Array(a.length + 1) { IntArray(b.length + 1) }
    for (i in 1..a.length) {
        for (j in 1..b.length) {
            dp[i][j] = if (a[i - 1] == b[j - 1]) {
                dp[i - 1][j - 1] + 1
            } else {
                maxOf(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }
    return dp[a.length][b.length]
}
```

#### 6. Complexity — Must Know

| Problem | Time | Space |
|---|---|---|
| Grid paths | O(rows × cols) | O(rows × cols), or O(cols) optimised |
| LCS | O(n × m) | O(n × m), or O(min(n, m)) optimised |
| Edit Distance | O(n × m) | O(n × m), or O(min(n, m)) optimised |

#### 7. Common Mistakes — Must Know

1. Using 0-indexed strings but 1-indexed DP tables without being careful — `dp[i][j]` usually represents "the first `i` characters", so `a[i - 1]` is the actual `i`-th character.
2. Forgetting the base row and base column (`dp[0][j]` and `dp[i][0]`) — these represent "one sequence is empty", and they're not always all zero (Edit Distance's base row/column count insertions or deletions).
3. Filling the table in the wrong order and reading a cell that hasn't been computed yet.

#### 8. Related Topics

1. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — the same method, with two state variables
2. `7` Space Optimisation — Keeping Only the Last Row or Two — 2D DP often only needs the previous row
3. `10` String DP — Palindromes, Word Break, Decode Ways — more string-based DP problems

#### 9. Interview Must Remember

1. Two sequences (or a grid) usually means **two indices in the state** — `dp[i][j]`.
2. Draw the small table by hand first (as in the LCS example) — it makes the recurrence obvious before you write code.
3. Get the **base row and base column** right — they're easy to get wrong and they seed the whole table.
