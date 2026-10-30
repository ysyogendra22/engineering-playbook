# Greedy vs Dynamic Programming — How to Tell

> The decision you make in the first two minutes of an interview. This note gives you a checklist.

#### 1. What Is It?

Both greedy and DP solve **optimization** problems (min, max, count). The difference:

| | Greedy | Dynamic Programming |
|---|---|---|
| Choice | one choice per step, never reconsidered | tries all choices, keeps the best |
| Needs | greedy choice property | overlapping subproblems + optimal substructure |
| Speed | usually `O(n)` or `O(n log n)` | usually `O(n²)` or `O(n · k)` |
| Risk | wrong answer if the rule is wrong | slower, more memory |

If a greedy rule is correct, it is almost always simpler and faster than DP.

#### 2. How It Works

Ask this one question:

> "If I take the locally best choice now, can it **lock me out** of something better later?"

```text
NO  (nothing is lost by choosing the best now)   → try greedy
YES (an early choice can trap me)                → use DP
```

| Signal | Points to |
|---|---|
| sorting the input makes the answer obvious | greedy |
| you can explain an exchange argument (note 03) | greedy |
| intervals, meetings, "earliest end" | greedy |
| single scan with a running max / min | greedy |
| a small example breaks the obvious rule | DP |
| "count the number of ways" | DP |
| "each item used once, cannot be split" | usually DP (0/1 knapsack shape) |
| choices depend on earlier choices (`dp[i-1]`, `dp[i-2]`) | DP |

**Same problem, both views — Jump Game (LeetCode 55):** "can you reach the last index?" Greedy keeps the farthest reach: `O(n)`. DP asks "can I reach `i` from any earlier `j`?": `O(n²)`. Greedy works because reaching *farther* never hurts.

**Not the same — House Robber (LeetCode 198):** "rob the biggest house" fails (`[3, 5, 3]`: greedy 5, best 6). The early choice blocks the neighbours. Use DP.

#### 3. Brute Force vs Optimized

Three levels for most of these problems:

| Level | Idea | Time |
|---|---|---|
| Brute force | try every choice (recursion) | exponential |
| DP | remember subproblem answers | polynomial |
| Greedy | prove one choice is always safe | linear or `n log n` |

```kotlin
// Jump Game, DP version: O(n²)
fun canJumpDP(nums: IntArray): Boolean {
    val n = nums.size
    val good = BooleanArray(n)
    good[n - 1] = true
    for (i in n - 2 downTo 0) {
        for (j in 1..minOf(nums[i], n - 1 - i)) {
            if (good[i + j]) { good[i] = true; break }
        }
    }
    return good[0]
}

// Jump Game, greedy version: O(n)
fun canJumpGreedy(nums: IntArray): Boolean {
    var farthest = 0
    for (i in nums.indices) {
        if (i > farthest) return false
        farthest = maxOf(farthest, i + nums[i])
    }
    return true
}
```

#### 4. Kotlin Code

A greedy that fails, next to its DP, on House Robber:

```kotlin
// Greedy: always rob the biggest house that is still allowed. WRONG.
fun robGreedy(nums: IntArray): Int {
    val blocked = BooleanArray(nums.size)
    var total = 0
    while (true) {
        var best = -1
        for (i in nums.indices) {
            if (!blocked[i] && (best == -1 || nums[i] > nums[best])) best = i
        }
        if (best == -1) return total
        total += nums[best]
        for (j in maxOf(0, best - 1)..minOf(nums.size - 1, best + 1)) blocked[j] = true
    }
}

// DP: correct
fun robDP(nums: IntArray): Int {
    var prev2 = 0                                         // best up to i − 2
    var prev1 = 0                                         // best up to i − 1
    for (x in nums) {
        val cur = maxOf(prev1, prev2 + x)                 // skip this house, or rob it
        prev2 = prev1
        prev1 = cur
    }
    return prev1
}
```

Checks: `canJumpDP([2,3,1,1,4])` and `canJumpGreedy([2,3,1,1,4])` → `true`. `canJumpGreedy([3,2,1,0,4])` → `false`. `robGreedy([3,5,3])` → `5`, but `robDP([3,5,3])` → `6`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Greedy (typical) | `O(n)` / `O(n log n)` | `O(1)` |
| DP (typical) | `O(n²)` / `O(n · k)` | `O(n)`, often reducible |

#### 6. Common Mistakes

1. **Greedy by default** without a counter-example check.
2. **DP by default** when a simple scan works (slower, harder to explain).
3. **Mixing up the problems**: "minimum number of coins" is DP for general coins, greedy only for canonical ones.
4. **Not stating the choice** to the interviewer. Say "I think this is greedy because ...".
5. **Skipping the proof.** Even one sentence helps.

#### 7. Say This in the Interview

1. "My first idea is greedy: pick ... each time. Let me try to break it with a small example."
2. "It breaks on ..., so a locally best choice can hurt later. I will use DP with state ..."
3. "If it survives, I have an exchange argument: ..."

#### 8. Quick Check

1. Which is faster for Jump Game: greedy or DP?
2. Why does greedy fail for House Robber?

<details>
<summary>Answers</summary>

1. Greedy, `O(n)` against `O(n²)`.
2. Robbing the biggest house blocks its two neighbours, and two smaller houses can add up to more.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | greedy (DP also works) |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Medium) | greedy |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) (Medium) | DP |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | DP |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) | greedy (DP also works) |
