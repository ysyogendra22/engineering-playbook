# 1D DP — Fibonacci, Climbing Stairs, House Robber

#### 1. Definition — Must Know

**1D DP** means the state needs only **one number** to describe it — usually a position or index. `dp[i]` is a single array, not a grid.

#### 2. Why It Is Used — Must Know

1. It's the simplest shape of DP, and the right place to build the four-step habit (topic 3) before moving to 2D problems.
2. House Robber in particular introduces a very common DP shape: "take it, or skip it" — the same shape reappears in Knapsack-style DP (topic 6).

#### 3. How It Works — Must Know

**House Robber**: rob houses in a row for maximum money, but you can't rob two adjacent houses.

```text
Houses: [2, 7, 9, 3, 1]

dp[i] = max money robbing houses 0..i

dp[0] = 2                                    (only house 0)
dp[1] = max(2, 7) = 7                        (rob 0, or rob 1)
dp[2] = max(dp[1], dp[0] + 9) = max(7, 11) = 11    (skip house 2, or rob it + best up to i-2)
dp[3] = max(dp[2], dp[1] + 3) = max(11, 10) = 11
dp[4] = max(dp[3], dp[2] + 1) = max(11, 12) = 12

Answer: 12  (rob houses 0, 2, 4 → 2 + 9 + 1 = 12)
```

#### 4. Algorithm — Must Know

```text
State:      dp[i] = best answer considering houses 0..i
Recurrence: dp[i] = max(
                dp[i - 1],              # skip house i
                dp[i - 2] + house[i]    # rob house i, add best from two houses back
            )
Base case:  dp[0] = house[0]
            dp[1] = max(house[0], house[1])
Fill order: i = 2 up to n - 1
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun rob(houses: IntArray): Int {
    if (houses.isEmpty()) return 0
    if (houses.size == 1) return houses[0]
    val dp = IntArray(houses.size)
    dp[0] = houses[0]
    dp[1] = maxOf(houses[0], houses[1])
    for (i in 2 until houses.size) {
        dp[i] = maxOf(dp[i - 1], dp[i - 2] + houses[i])
    }
    return dp[houses.size - 1]
}
```

#### 6. Complexity — Must Know

| Problem | Time | Space |
|---|---|---|
| Fibonacci | O(n) | O(n), or O(1) optimised |
| Climbing Stairs | O(n) | O(n), or O(1) optimised |
| House Robber | O(n) | O(n), or O(1) optimised (only `dp[i-1]` and `dp[i-2]` are ever needed) |

#### 7. Common Mistakes — Must Know

1. In House Robber: forgetting that "skip house i" means carrying forward `dp[i-1]` unchanged, not just ignoring house i's value.
2. Off-by-one errors in the base cases — House Robber needs **two** base cases (`dp[0]` and `dp[1]`), not just one.
3. Not noticing that all three of these only ever need the last one or two values — a strong hint for space optimisation (topic 7).

#### 8. Related Topics

1. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — the method used here
2. `7` Space Optimisation — Keeping Only the Last Row or Two — applies directly to all three examples
3. `6` Knapsack-Style DP — House Robber's "take it or skip it" recurrence reappears there

#### 9. Interview Must Remember

1. **House Robber's recurrence is the template for many DP problems:** `dp[i] = max(skip, take + dp[i-2])`.
2. 1D DP problems almost always end up needing only the last one or two states — flag this for space optimisation.
3. Get the base cases right first — with two-state recurrences, you need two of them.
