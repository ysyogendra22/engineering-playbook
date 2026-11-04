# Dynamic Programming Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–15.

#### 1. Key Takeaways

1. DP = **overlapping subproblems** + **optimal substructure**. Solve each state once and remember it.
2. Always say the **four steps**: **state**, **recurrence**, **base case**, **fill order** (and the answer cell).
3. Complexity = **number of states × work per state**.
4. Start with the **brute-force recursion** and its complexity, then add a memo (top-down), then convert to a table (bottom-up) if needed.
5. If `dp[i]` uses only the last row or last few values, **reduce the space** (but then you can't rebuild the solution).
6. **0/1** items: capacity loop **down**. **Unbounded** items: capacity loop **up**.
7. **Combinations**: coins outside. **Permutations**: amount outside.
8. Test greedy with a counter-example before trusting it (`{1, 3, 4}`, amount 6).

#### 2. Complexity Table

| Family | State | Time | Space (optimised) |
|---|---|---|---|
| 1D (stairs, robber, Kadane) | `i` | `O(n)` | `O(1)` |
| Grid paths | `(r, c)` | `O(m · n)` | `O(n)` |
| LCS / Edit Distance | `(i, j)` | `O(m · n)` | `O(n)` |
| 0/1 Knapsack, Subset Sum | `(i, w)` | `O(n · W)` | `O(W)` |
| Unbounded / Coin Change | amount | `O(amount · coins)` | `O(amount)` |
| LIS | ending index | `O(n²)`, `O(n log n)` | `O(n)` |
| Palindromic subsequence | `(i, j)` | `O(n²)` | `O(n)` |
| Word Break | prefix | `O(n²)` | `O(n)` |
| State machine (stocks) | day + mode | `O(n)` | `O(1)` |
| Interval DP | `(i, j)` + split | `O(n³)` | `O(n²)` |
| Bitmask DP | `mask` | `O(2ⁿ · n)` | `O(2ⁿ)` |

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "ways to reach step n", Fibonacci-like | 1D, last two states | 04 |
| "can't take two adjacent" | House Robber: `max(dp[i−1], dp[i−2] + x)` | 04 |
| best subarray ending here | Kadane | 04 |
| grid, move right / down | 2D grid DP | 05 |
| two strings: common, convert | LCS / Edit Distance | 05 |
| "choose items under a capacity, each once" | 0/1 knapsack | 06 |
| "split into two equal-sum parts" | subset sum to `total / 2` | 06 |
| "assign + / − to reach target" | count subsets with sum `(total + target)/2` | 06 |
| "unlimited coins, fewest" | unbounded, min | 06, 14 |
| "number of combinations / permutations" | unbounded, loop order | 14 |
| "longest increasing / chain" | LIS | 13 |
| palindrome in a string | expand centres, or range DP | 10 |
| split a string into dictionary words | prefix DP | 10 |
| count decodings | one or two digit steps | 10 |
| buy / sell with a rule | state machine | 11 |
| split a range, last / first choice | interval DP | 12 |
| `n ≤ 20`, which items used | bitmask DP | 12 |
| "list all solutions" | backtracking, not DP | 15 |

#### 4. Templates to Memorise

**Top-down**

```kotlin
val memo = HashMap<Int, Int>()
fun solve(i: Int): Int {
    if (base) return value
    memo[i]?.let { return it }
    val r = combine(solve(i - 1), solve(i - 2))
    memo[i] = r
    return r
}
```

**Bottom-up 1D**

```kotlin
val dp = IntArray(n + 1); dp[0] = base
for (i in 1..n) dp[i] = /* from dp[i - 1], dp[i - 2], ... */
```

**House Robber**

```kotlin
var skip = 0; var take = 0
for (x in nums) { val cur = maxOf(skip, take + x); take = skip; skip = cur }
```

**Kadane**

```kotlin
var cur = nums[0]; var best = nums[0]
for (i in 1 until n) { cur = maxOf(nums[i], cur + nums[i]); best = maxOf(best, cur) }
```

**LCS**

```kotlin
dp[i][j] = if (a[i-1] == b[j-1]) dp[i-1][j-1] + 1 else maxOf(dp[i-1][j], dp[i][j-1])
```

**Edit distance**

```kotlin
dp[i][j] = if (a[i-1] == b[j-1]) dp[i-1][j-1] else 1 + minOf(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
// base: dp[i][0] = i, dp[0][j] = j
```

**0/1 knapsack (one row)**

```kotlin
for (i in items) for (w in capacity downTo weight[i]) dp[w] = maxOf(dp[w], dp[w - weight[i]] + value[i])
```

**Unbounded: min coins / combinations / permutations**

```kotlin
for (a in 1..amount) for (c in coins) if (c <= a) dp[a] = minOf(dp[a], dp[a - c] + 1)   // min coins
for (c in coins) for (a in c..amount) dp[a] += dp[a - c]                                 // combinations
for (a in 1..amount) for (c in coins) if (c <= a) dp[a] += dp[a - c]                     // permutations
```

**LIS in `O(n log n)`**

```kotlin
var lo = 0; var hi = size
while (lo < hi) { val mid = (lo + hi) / 2; if (tails[mid] < x) lo = mid + 1 else hi = mid }
tails[lo] = x; if (lo == size) size++
```

**Stock with cooldown**

```kotlin
sold = hold + p; hold = maxOf(hold, rest - p); rest = maxOf(rest, prevSold)
```

**Bitmask**

```kotlin
val next = mask or (1 shl i)      // add item i
((mask shr i) and 1) == 1          // item i used?
```

#### 5. Brute Force to Optimized

| Problem | Brute force | DP |
|---|---|---|
| Fibonacci / stairs | `O(2ⁿ)` | `O(n)` |
| House Robber | `O(2ⁿ)` subsets | `O(n)` |
| LCS | `O(2ⁿ)` subsequences | `O(m · n)` |
| Edit Distance | `O(3^(m+n))` | `O(m · n)` |
| Coin Change | all coin sequences | `O(amount · coins)` |
| 0/1 Knapsack, Subset Sum | `O(2ⁿ)` | `O(n · W)` |
| LIS | `O(2ⁿ)` | `O(n²)`, `O(n log n)` |
| Word Break | `O(2ⁿ)` splits | `O(n²)` |
| Burst Balloons | `O(n!)` | `O(n³)` |
| Travelling-style | `O(n!)` | `O(2ⁿ · n²)` |

#### 6. Common Mistakes and Edge Cases

1. **No clear definition of `dp[i]`.**
2. **Wrong base case** (`dp[0]`, empty string, amount 0).
3. **Wrong loop direction** (0/1 down, unbounded up).
4. **Wrong fill order** (reading a cell not yet computed).
5. **Loop order for combinations vs permutations.**
6. **`Int.MAX_VALUE` for "impossible"** then `+ 1` (overflow). Use `amount + 1`.
7. **Updating a state with today's value** instead of yesterday's (stock problems).
8. **Index off-by-one** between strings (`i − 1`) and the table.
9. **Space-optimising** before you know you don't need the solution path.
10. **Trusting greedy** without a counter-example.
11. **Edge cases:** empty input, one element, impossible target, all negatives (Kadane).

#### 7. What to Say Out Loud

1. "The brute force tries every choice, which is `O(2ⁿ)`. The same subproblems repeat, so I'll use DP."
2. "State: `dp[i]` means ... Recurrence: ... Base case: ... I fill in increasing order and the answer is `dp[n]`."
3. "That's `n` states with `O(1)` work: `O(n)` time. Each state only needs the last two, so space is `O(1)`."
4. "Greedy doesn't work here: for `{1, 3, 4}` and 6 it gives 3 coins, not 2."
5. "I'll test an empty input, a single element and an impossible case."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 1D |
| Easy | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | 1D min |
| Easy | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | memo |
| Medium | [House Robber](https://leetcode.com/problems/house-robber/) | take or skip |
| Medium | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane |
| Medium | [Coin Change](https://leetcode.com/problems/coin-change/) | unbounded min |
| Medium | [Unique Paths](https://leetcode.com/problems/unique-paths/) | grid |
| Medium | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | grid min |
| Medium | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | LIS |
| Medium | [Word Break](https://leetcode.com/problems/word-break/) | prefix DP |
| Medium | [Decode Ways](https://leetcode.com/problems/decode-ways/) | 1 or 2 digits |
| Medium | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | two strings |
| Medium | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 knapsack |
| Medium | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | combinations |
| Medium | [Target Sum](https://leetcode.com/problems/target-sum/) | subset count |
| Medium | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | expand centres |
| Medium | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | state machine |
| Medium | [Edit Distance](https://leetcode.com/problems/edit-distance/) | insert / delete / replace |
| Hard | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | interval DP |
| Hard | [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) | sort + LIS |
