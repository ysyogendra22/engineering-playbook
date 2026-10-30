# Why Greedy Fails — 0/1 Knapsack & General Coin Change

> Interviewers often give a problem that *looks* greedy but is not. This note shows the traps.

#### 1. What Is It?

Greedy fails when a locally best choice **blocks a better choice later**. Two classic examples:

1. **0/1 Knapsack.** Each item is taken whole or not at all.
2. **Coin Change** with a coin set like `{1, 3, 4}`.

The cure is **Dynamic Programming**: remember the best answer for smaller subproblems and build up.

#### 2. How It Works

**0/1 Knapsack.** Items (value, weight): `(60, 10)`, `(100, 20)`, `(120, 30)`. Capacity 50. Items cannot be split.

```text
Greedy by value/weight (6, 5, 4):
  take item 1 (w10) → value 60,  left 40
  take item 2 (w20) → value 160, left 20
  item 3 (w30) does not fit      → total 160

Best answer: items 2 + 3 (w50) → 100 + 120 = 220
```

Greedy filled the bag with items that leave 20 unused. A fraction would fix this, but fractions are not allowed.

**Coin Change.** Coins `{1, 3, 4}`, amount 6.

```text
Greedy: 4 + 1 + 1 = 3 coins
Best:   3 + 3     = 2 coins
```

**More traps to remember:**

| Problem | Tempting greedy | Why it fails |
|---|---|---|
| House Robber | rob the biggest house | `[3, 5, 3]`: greedy 5, best 3 + 3 = 6 |
| Dijkstra with negative edges | closest node is final | a negative edge can shorten it later |
| Longest path / TSP | go to the nearest next | local choice blocks the global tour |

**How DP fixes it.** For 0/1 knapsack, `dp[w]` = best value with capacity `w`. For each item, decide "take it" or "skip it" using results of smaller capacities.

#### 3. Brute Force vs Optimized

| | Brute force | Greedy | DP |
|---|---|---|---|
| 0/1 Knapsack | try all subsets `O(2^n)` | `O(n log n)`, **wrong** | `O(n · W)`, correct |
| Coin Change | try all coin sequences, exponential | `O(c)`, **wrong** for `{1,3,4}` | `O(amount · c)` |

```kotlin
// Greedy by value/weight, whole items only: WRONG for 0/1 knapsack
fun knapsackGreedy(values: IntArray, weights: IntArray, capacity: Int): Int {
    var left = capacity
    var total = 0
    for (i in values.indices.sortedByDescending { values[it].toDouble() / weights[it] }) {
        if (weights[i] <= left) { total += values[i]; left -= weights[i] }
    }
    return total
}

// DP: correct
fun knapsackDP(values: IntArray, weights: IntArray, capacity: Int): Int {
    val dp = IntArray(capacity + 1)
    for (i in values.indices) {
        for (w in capacity downTo weights[i]) {            // go downward so each item is used once
            dp[w] = maxOf(dp[w], dp[w - weights[i]] + values[i])
        }
    }
    return dp[capacity]
}
```

Checks: with values `[60, 100, 120]`, weights `[10, 20, 30]`, capacity `50`: `knapsackGreedy` → `160`, `knapsackDP` → `220`.

#### 4. Kotlin Code

The code is above. A tiny way to **find a counter-example** during practice:

```kotlin
fun coinGreedyFails(coins: IntArray, limit: Int): Int? {
    for (amount in 1..limit) {
        var remaining = amount
        var count = 0
        for (c in coins.sortedDescending()) { count += remaining / c; remaining %= c }
        val dp = IntArray(amount + 1) { Int.MAX_VALUE }
        dp[0] = 0
        for (a in 1..amount) for (c in coins) {
            if (c <= a && dp[a - c] != Int.MAX_VALUE) dp[a] = minOf(dp[a], dp[a - c] + 1)
        }
        if (remaining == 0 && count != dp[amount]) return amount
    }
    return null
}
```

Checks: `coinGreedyFails([1, 3, 4], 10)` → `6`. `coinGreedyFails([1, 5, 10, 25], 100)` → `null`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| 0/1 Knapsack DP | `O(n · W)` | `O(W)` |
| Coin Change DP | `O(amount · c)` | `O(amount)` |

(`W` is the capacity. This is "pseudo-polynomial": it depends on the size of the number, not only the count of items.)

#### 6. Common Mistakes

1. **Using the fractional knapsack greedy** on 0/1 knapsack.
2. **Looping capacity upward** in 0/1 DP (it then uses an item many times, which is the *unbounded* version).
3. **Trusting greedy** because the sample passes.
4. **Switching to DP without a state definition.** Say what `dp[i]` means first.
5. **Not saying why greedy fails.** Show the small counter-example.

#### 7. Say This in the Interview

1. "Greedy looks natural here, but with coins 1, 3, 4 and amount 6 it returns 3 coins instead of 2, so I will use DP."
2. "dp[a] is the fewest coins to make amount a. I build it from smaller amounts."

#### 8. Quick Check

1. Why does ratio-greedy fail for 0/1 knapsack?
2. In the 0/1 DP, which direction do you loop over capacity, and why?

<details>
<summary>Answers</summary>

1. It leaves unused space that a different mix of whole items could fill.
2. Downward, so an item is not used twice.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) (Medium) | greedy fails, DP |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | DP |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium) | 0/1 knapsack |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) (Medium) | 0/1 knapsack style |
| 1049 | [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) (Medium) | knapsack, not the greedy heap |
