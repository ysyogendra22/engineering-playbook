# Interval DP & Bitmask DP — Names Only

#### 1. Definition — Must Know

1. **Interval DP**: the state is a range `[i, j]` inside a sequence, and the recurrence tries every way to split that range into two smaller ranges. Used for problems like "matrix chain multiplication" or "burst balloons".
2. **Bitmask DP**: the state includes a bitmask representing which items (out of a small set, usually ≤ 20) have been used so far. Used for problems like "visit all cities in the cheapest order" (a small Travelling Salesman Problem).

#### 2. Why It Is Used — Must Know

Both are advanced DP shapes. You are not expected to derive these from scratch under interview pressure — knowing the name, the shape of the state, and one example each is enough to recognise them if they come up.

#### 3. How It Works — Must Know

**Interval DP** (idea only):

```text
dp[i][j] = best answer for the range from i to j

To compute dp[i][j], try every split point k between i and j:
    dp[i][j] = best over all k of ( dp[i][k] + dp[k+1][j] + cost of combining them )

Fill order: by increasing interval LENGTH (small ranges first, then bigger ones
that are built from smaller ones) — same idea as the palindrome DP fill order
in `10-String DP`.
```

**Bitmask DP** (idea only):

```text
dp[mask][i] = best answer having visited exactly the cities in `mask`,
              currently standing at city i

mask is an integer whose bits represent which cities have been visited
(bit j = 1 means city j has been visited) — see `09-Bit Manipulation`
in this folder for how bitmasks work.
```

#### 4. Algorithm — Must Know

*(Shape only — not expected to be written from memory.)*

```text
Interval DP:
  for length in 2..n:
      for i in 0..(n - length):
          j = i + length - 1
          dp[i][j] = best over all split points k in (i, j) of combine(dp[i][k], dp[k+1][j])

Bitmask DP:
  for mask in all possible bitmasks:
      for i in 0..n-1:
          if bit i is set in mask:
              dp[mask][i] = best over all j where bit j is also set in mask
                            of ( dp[mask without bit i][j] + cost(j, i) )
```

#### 5. Kotlin Implementation — Must Know

*(Not expected — these problems are usually solved with a description of the state and recurrence, not full code, at this level.)*

#### 6. Complexity — Must Know

| | Complexity |
|---|---|
| Interval DP | O(n³) typically — O(n²) states, O(n) work to try each split |
| Bitmask DP | O(2ⁿ × n) or O(2ⁿ × n²) — exponential in the number of items, only usable for small n (roughly ≤ 20) |

#### 7. Common Mistakes — Must Know

1. Trying to apply bitmask DP to a large number of items — it only works because `2ⁿ` stays manageable for small n (around 20 or fewer).
2. Getting the interval DP fill order wrong — like palindrome DP, it must go by increasing interval length, not simple index order.
3. Spending too long trying to derive these from first principles in an interview — for an awareness-only topic, naming the shape and moving on is the right call.

#### 8. Related Topics

1. `10` String DP — Palindromes, Word Break, Decode Ways — palindrome DP is a simple interval DP
2. `09` Bit Manipulation (its own folder) — how bitmasks work, needed to understand bitmask DP
3. `11` Complexity Classes (P, NP, NP-Complete) (its own folder) — why TSP-style problems need this exponential approach at all

#### 9. Interview Must Remember

1. **Interval DP** = state is a range `[i, j]`, fill order goes by increasing length.
2. **Bitmask DP** = state includes "which items have I used", only practical for small n (≤ ~20).
3. Both are fine to know by name and shape only — say what they are and when you'd reach for them, without necessarily coding them live.
