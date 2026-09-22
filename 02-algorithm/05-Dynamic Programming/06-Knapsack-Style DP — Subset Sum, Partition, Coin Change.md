# Knapsack-Style DP — Subset Sum, Partition, Coin Change

#### 1. Definition — Must Know

**Knapsack-style DP** covers problems where you choose a subset of items, under a capacity or target limit, to hit or optimise some goal. The state is usually `dp[index][remaining capacity]`, and the recurrence is always some version of "take this item, or don't".

#### 2. Why It Is Used — Must Know

1. This is the DP shape behind 0/1 Knapsack (see `04-Greedy Algorithms/09`, where greedy fails and this is the fix), Subset Sum, Partition Equal Subset Sum, and general Coin Change.
2. Recognising "this is a knapsack shape" lets you reuse the same recurrence pattern across several differently-worded problems.

#### 3. How It Works — Must Know

**Subset Sum**: given numbers, can some subset add up exactly to a target?

```text
Numbers: [3, 34, 4, 12, 5, 2]   Target: 9

dp[i][t] = true if some subset of the first i numbers sums to exactly t

dp[i][t] = dp[i-1][t]                          # don't use number i
           OR dp[i-1][t - number[i]]           # use number i (if it fits)

{4, 5} sums to 9 → dp[...][9] = true
```

**Coin Change (general, minimum coins)** — same shape as canonical coin change (`04-Greedy Algorithms/06`), but works for **any** coin set, not just canonical ones:

```text
dp[amount] = minimum coins to make exactly `amount`
dp[amount] = min over every coin c of ( dp[amount - c] + 1 ), if amount - c >= 0
dp[0] = 0   (zero coins needed for amount 0)
```

#### 4. Algorithm — Must Know

```text
0/1 Knapsack shape (take it once, or skip it):
  dp[i][w] = max(
      dp[i-1][w],                           # skip item i
      dp[i-1][w - weight[i]] + value[i]     # take item i (if it fits)
  )

Unbounded shape (take an item as many times as you want, like coin change):
  dp[amount] = min/max over each coin c of ( dp[amount - c] + 1 )
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun coinChangeMinCoins(coins: IntArray, amount: Int): Int {
    val dp = IntArray(amount + 1) { Int.MAX_VALUE / 2 }  // "infinity" placeholder
    dp[0] = 0
    for (a in 1..amount) {
        for (coin in coins) {
            if (coin <= a) {
                dp[a] = minOf(dp[a], dp[a - coin] + 1)
            }
        }
    }
    return if (dp[amount] >= Int.MAX_VALUE / 2) -1 else dp[amount]
}
```

#### 6. Complexity — Must Know

| Problem | Time | Space |
|---|---|---|
| 0/1 Knapsack | O(n × capacity) | O(n × capacity), or O(capacity) optimised |
| Subset Sum | O(n × target) | O(n × target), or O(target) optimised |
| General Coin Change | O(amount × number of coin types) | O(amount) |

#### 7. Common Mistakes — Must Know

1. Confusing the **0/1** shape (each item used at most once, so loop items on the outside) with the **unbounded** shape (an item can be reused, like coins) — the loop order matters and swapping it gives a wrong answer.
2. Initialising the "impossible" placeholder incorrectly (using `0` instead of a large "infinity" value for minimisation problems).
3. Not handling the "not possible" case (target unreachable) explicitly.

#### 8. Related Topics

1. `1` The Greedy Choice Property, `09` Why Greedy Fails (in `04-Greedy Algorithms`) — why these problems need DP, not greedy
2. `3` The Four Steps — State, Recurrence, Base Case, Fill Order
3. `7` Space Optimisation — Keeping Only the Last Row or Two — the 2D knapsack table often reduces to 1D

#### 9. Interview Must Remember

1. Knapsack-shape recurrence: **"take it, or don't"** — `dp[i][w] = max/combine(skip, take)`.
2. **0/1 vs unbounded** changes your loop order — know which one the problem is asking for.
3. This is the DP fix whenever a greedy approach on a knapsack-like problem is shown to be wrong (`04-Greedy Algorithms/09`).
