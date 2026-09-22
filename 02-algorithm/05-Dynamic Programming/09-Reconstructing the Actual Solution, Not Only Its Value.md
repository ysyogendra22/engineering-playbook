# Reconstructing the Actual Solution, Not Only Its Value

#### 1. Definition — Must Know

Most DP explanations compute a single **number** (the best value, the count, the length). Reconstruction means also recovering the **actual sequence of choices** that produced that number — which items were taken, which path was walked, what the actual longest common subsequence string is.

#### 2. Why It Is Used — Must Know

1. Interviewers often ask "now print the actual subsequence / path / items", as a follow-up once the value-only DP works — it checks you understand the table, not just the recurrence formula.
2. It forces you to remember not just *what* the best value at each state is, but *how* you got there.

#### 3. How It Works — Must Know

Reconstructing the Longest Common Subsequence string (table from `05-2D DP`, comparing `"abcde"` and `"ace"`):

```text
Start at dp[5][3] (bottom-right corner) and walk backward:

If a[i-1] == b[j-1]:       # this character is part of the LCS
    include it, move diagonally to dp[i-1][j-1]
Else if dp[i-1][j] > dp[i][j-1]:
    move up to dp[i-1][j]                     # this row's character wasn't used
Else:
    move left to dp[i][j-1]                   # this column's character wasn't used

Walking backward from dp[5][3] for "abcde" vs "ace" traces out: e, c, a
Reverse it: "ace" — the actual LCS string, not just its length (3)
```

#### 4. Algorithm — Must Know

```text
1. Solve the DP normally, building the full table (don't space-optimise
   away the table you need to trace back through — see topic 7).
2. Start at the final state (the answer's position in the table).
3. Use the recurrence "in reverse": at each state, figure out which
   earlier choice led here (a match? took the item? skipped it?).
4. Follow that trail back to a base case, collecting the choices.
5. Reverse the collected choices to get them in the right order.
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun lcsString(a: String, b: String): String {
    val dp = Array(a.length + 1) { IntArray(b.length + 1) }
    for (i in 1..a.length) for (j in 1..b.length) {
        dp[i][j] = if (a[i - 1] == b[j - 1]) dp[i - 1][j - 1] + 1
                    else maxOf(dp[i - 1][j], dp[i][j - 1])
    }
    val sb = StringBuilder()
    var i = a.length; var j = b.length
    while (i > 0 && j > 0) {
        when {
            a[i - 1] == b[j - 1] -> { sb.append(a[i - 1]); i--; j-- }
            dp[i - 1][j] > dp[i][j - 1] -> i--
            else -> j--
        }
    }
    return sb.reverse().toString()
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Building the table | Same as the value-only version |
| Reconstruction walk | O(n + m) extra — one pass back through the table |

Reconstruction rarely changes the Big-O — it's a small extra pass, not a new algorithm.

#### 7. Common Mistakes — Must Know

1. Space-optimising the table (topic 7) and then being unable to reconstruct the path — you need the full table if reconstruction is required.
2. Forgetting to **reverse** the collected sequence at the end, since you build it backward.
3. Getting the tie-breaking rule wrong when two directions give the same value (any consistent rule works, but it must be applied consistently).

#### 8. Related Topics

1. `5` 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence — the example used here
2. `7` Space Optimisation — Keeping Only the Last Row or Two — the trade-off against reconstruction
3. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — reconstruction reads this recurrence backward

#### 9. Interview Must Remember

1. Reconstruction = **walk the table backward**, undoing the recurrence step by step from the final state.
2. You need the **full table** to do this — don't space-optimise it away if reconstruction is required.
3. Collect choices as you walk back, then **reverse** them at the end.
