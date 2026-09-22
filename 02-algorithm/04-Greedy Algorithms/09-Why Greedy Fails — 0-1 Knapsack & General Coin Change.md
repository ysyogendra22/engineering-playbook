# Why Greedy Fails — 0/1 Knapsack & General Coin Change

#### 1. Definition — Must Know

1. **0/1 Knapsack**: same setup as Fractional Knapsack (topic 5), but each item must be taken **whole or not at all** — no fractions.
2. **General coin change**: coin change (topic 6) with a coin set that is **not canonical** — greedy no longer guarantees the minimum number of coins.
3. Both are the standard examples used to show that greedy is not a universal tool.

#### 2. Why It Is Used — Must Know

1. Interviewers use these two problems specifically to check whether you blindly apply greedy everywhere, or actually verify the greedy choice property (topic 1) first.
2. Recognising *why* greedy fails here is what points you toward Dynamic Programming instead.

#### 3. How It Works — Must Know

**0/1 Knapsack counter-example:**

```text
Capacity = 50
Items (value, weight): (60, 10)  (100, 20)  (120, 30)

Greedy by value/weight ratio (same idea as topic 5):
Ratios: 6, 5, 4 → take item 1 (value/weight 6) fully: weight 10, value 60
        take item 2 fully: weight 30, value 160
        item 3 doesn't fit whole (needs 30, only 20 capacity left) → skip
Greedy total = 160

But the actual best choice is item 2 + item 3: weight 20 + 30 = 50, value 100 + 120 = 220

Greedy (160) < Optimal (220) — greedy is wrong here.
```

**General coin change counter-example** (already shown in topic 1): coins {1, 3, 4}, target 6 — greedy gives 4+1+1 = 3 coins, but 3+3 = 2 coins is better.

#### 4. Algorithm — Must Know

There's no greedy algorithm to give here — that's the point. The correct approach for both is Dynamic Programming:

```text
0/1 Knapsack (DP):
  dp[i][w] = best value using the first i items with capacity w
  dp[i][w] = max(
      dp[i-1][w],                                  # skip item i
      dp[i-1][w - weight[i]] + value[i]             # take item i, if it fits
  )
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun knapsack01(capacity: Int, weights: IntArray, values: IntArray): Int {
    val n = weights.size
    val dp = Array(n + 1) { IntArray(capacity + 1) }
    for (i in 1..n) {
        for (w in 0..capacity) {
            dp[i][w] = dp[i - 1][w]                                   // skip item i
            if (weights[i - 1] <= w) {
                dp[i][w] = maxOf(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            }
        }
    }
    return dp[n][capacity]
}
```

#### 6. Complexity — Must Know

| Problem | Greedy | Correct approach |
|---|---|---|
| 0/1 Knapsack | Wrong answer, O(n log n) | DP, O(n × capacity) |
| General coin change | Wrong answer, O(k) | DP, O(target × k) |

#### 7. Common Mistakes — Must Know

1. Reusing the Fractional Knapsack greedy idea for 0/1 Knapsack because the problems "look similar" — they need different techniques.
2. Assuming a coin set is canonical without checking — always ask or verify with a small counter-example.
3. Giving up on the problem instead of switching to DP once greedy is shown to fail — the failure is the *signal* to switch, not a dead end.

#### 8. Related Topics

1. `5` Fractional Knapsack — the version where greedy *does* work
2. `6` Coin Change with Canonical Coin Systems — the version where greedy *does* work
3. `10` Greedy vs Dynamic Programming — How to Tell — the general decision process
4. `5` Dynamic Programming (its own folder) — the correct technique for both problems here

#### 9. Interview Must Remember

1. **0/1 Knapsack and non-canonical coin change are the two go-to examples of "greedy looks right but isn't".**
2. The fix for both is Dynamic Programming — build a table of best answers to subproblems, don't just scan once.
3. If you can construct a counter-example (even a tiny one, by hand), that's proof enough to abandon greedy and switch approach.
