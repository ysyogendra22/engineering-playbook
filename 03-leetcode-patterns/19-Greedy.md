# Greedy

> Take the best choice right now and never look back. It is only correct when you can justify it.

#### 1. What Is It?

A **greedy** algorithm builds the answer by making the locally best choice at each step. It is fast (usually `O(n log n)` for a sort, or `O(n)`), but only correct when the problem has the **greedy choice property**: a local best choice never blocks the global best.

The full theory and 15 notes are in `ALG Greedy Algorithms`. This note is the interview shortcut.

**Signals**

- "Minimum number of ..." or "maximum number of ..." where each step has an obvious best option
- Intervals, scheduling, matching two lists
- "Can you reach the end?", "fewest jumps", "start from which station?"
- Sorting makes the choice obvious
- A sample-driven rule *seems* right (this is also the warning sign)

**Common greedy rules**

| Problem family | Rule |
|---|---|
| Max non-overlapping intervals, min arrows | sort by **end**, take what fits |
| Merge intervals | sort by **start** |
| Match two lists | sort both, two pointers |
| Reach / jumps | track the **farthest reachable** index |
| Circular route | running tank; restart after a negative |
| Schedule with cool-down | most frequent first (heap) |
| Buy and sell, unlimited | add every rise |
| Cut a string into parts | last occurrence of each letter |

#### 2. How It Works

**Test before you trust.**

1. State the rule in one sentence.
2. Try to **break it** with 3 to 5 items (include a tie and an extreme).
3. Give a one-line **exchange argument**: if an optimal answer did not use my choice, I can swap my choice in without making it worse.

**Greedy vs DP**

| Question | Greedy | DP |
|---|---|---|
| Does one choice never need to be reconsidered? | yes | no |
| Is there a counter-example for the local rule? | no | yes |
| Typical cost | `O(n log n)` | `O(n × states)` |
| Example | Jump Game (reach) | Coin Change with `{1,3,4}` |

If the greedy rule fails on any small input, switch to DP.

**Jump Game.** Keep `farthest`. At index `i`, if `i > farthest` you're stuck. Else `farthest = max(farthest, i + nums[i])`.

**Jump Game II.** Think in levels like BFS: `curEnd` is the end of the current jump range. When you reach it, take one more jump and move `curEnd` to `farthest`.

**Gas Station.** If total gas ≥ total cost, a solution exists. Keep a running tank. When it goes negative at `i`, no start in `[start, i]` works, so set `start = i + 1`.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Greedy |
|---|---|---|
| Jump Game | try every jump, `O(2ⁿ)`, or DP `O(n²)` | `O(n)` |
| Jump Game II | DP `O(n²)` | levels, `O(n)` |
| Gas Station | try each start, `O(n²)` | one pass, `O(n)` |
| Assign Cookies | try all matchings | sort both, `O(n log n)` |
| Stock II | recursion on buy/sell, `O(2ⁿ)` | add every rise, `O(n)` |

```kotlin
// O(n^2) DP for Jump Game: reach[i] = can we land on i?
fun canJumpBrute(nums: IntArray): Boolean {
    val reach = BooleanArray(nums.size)
    reach[0] = true
    for (i in nums.indices) {
        if (!reach[i]) continue
        for (j in i + 1..minOf(nums.size - 1, i + nums[i])) reach[j] = true
    }
    return reach[nums.size - 1]
}
```

#### 4. Kotlin Code

```kotlin
// Jump Game (LeetCode 55)
fun canJump(nums: IntArray): Boolean {
    var farthest = 0
    for (i in nums.indices) {
        if (i > farthest) return false
        farthest = maxOf(farthest, i + nums[i])
    }
    return true
}

// Jump Game II (LeetCode 45)
fun jump(nums: IntArray): Int {
    var jumps = 0
    var curEnd = 0
    var farthest = 0
    for (i in 0 until nums.size - 1) {
        farthest = maxOf(farthest, i + nums[i])
        if (i == curEnd) { jumps++; curEnd = farthest }
    }
    return jumps
}

// Assign Cookies (LeetCode 455)
fun findContentChildren(g: IntArray, s: IntArray): Int {
    g.sort()
    s.sort()
    var child = 0
    for (cookie in s) {
        if (child < g.size && cookie >= g[child]) child++        // smallest cookie that satisfies the least greedy child
    }
    return child
}

// Gas Station (LeetCode 134)
fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
    var total = 0
    var tank = 0
    var start = 0
    for (i in gas.indices) {
        val diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if (tank < 0) { start = i + 1; tank = 0 }
    }
    return if (total >= 0) start else -1
}

// Best Time to Buy and Sell Stock II (LeetCode 122)
fun maxProfitUnlimited(prices: IntArray): Int {
    var profit = 0
    for (i in 1 until prices.size) {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1]
    }
    return profit
}

// Partition Labels (LeetCode 763)
fun partitionLabels(s: String): List<Int> {
    val last = IntArray(26)
    for (i in s.indices) last[s[i] - 'a'] = i
    val sizes = mutableListOf<Int>()
    var start = 0
    var end = 0
    for (i in s.indices) {
        end = maxOf(end, last[s[i] - 'a'])
        if (i == end) { sizes.add(end - start + 1); start = i + 1 }
    }
    return sizes
}
```

Intervals (Non-overlapping Intervals, Minimum Arrows) are in note 09. Task Scheduler is in `ALG Greedy Algorithms` note 13.

Checks: `canJump([2,3,1,1,4])` → `true`; `([3,2,1,0,4])` → `false`. `jump([2,3,1,1,4])` → `2`; `([2,3,0,1,4])` → `2`. `findContentChildren([1,2,3], [1,1])` → `1`; `([1,2], [1,2,3])` → `2`. `canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])` → `3`; `([2,3,4], [3,4,3])` → `-1`. `maxProfitUnlimited([7,1,5,3,6,4])` → `7`. `partitionLabels("ababcbacadefegdehijhklij")` → `[9,7,8]`.

#### 5. Complexity

| Pattern | Time | Space |
|---|---|---|
| Sort + scan | `O(n log n)` | `O(1)` to `O(n)` |
| Running value (jump, gas, stock) | `O(n)` | `O(1)` |
| Heap greedy | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Trusting a rule that only works on the sample.** Break it first.
2. **Sorting by the wrong key** (start vs end for intervals).
3. **Greedy on 0/1 knapsack or general coin change.** Use DP.
4. **Gas Station:** skipping the `total >= 0` check.
5. **Jump Game II:** looping to `size` instead of `size − 1` (an extra jump).
6. **Assign Cookies:** matching the largest cookie to the smallest child (wastes cookies).
7. **No proof.** In an interview, always give a one-line reason it is safe.

#### 7. Say This in the Interview

1. "A brute force tries every choice. I think taking the ... each time is safe. Let me test it on a small tricky example."
2. "If an optimal solution did not take this choice, I could swap it in without making the answer worse. So greedy is correct."
3. "It's `O(n log n)` for the sort and `O(1)` extra space. If the rule broke, I'd use DP."

#### 8. Quick Check

1. Which rule solves "fewest arrows to burst balloons"?
2. Does greedy work for coins `{1,3,4}` and amount 6?

<details>
<summary>Answers</summary>

1. Sort by end, shoot at the end of the first balloon, skip everything that starts at or before that point, repeat.
2. No. Greedy gives 4+1+1 (3 coins) but the best is 3+3 (2 coins). Use DP.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | sort both |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Medium) | add every rise |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | farthest reach |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Medium) | levels |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) (Medium) | running tank |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium) | last occurrence |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) | sort by end |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) | most frequent first |
