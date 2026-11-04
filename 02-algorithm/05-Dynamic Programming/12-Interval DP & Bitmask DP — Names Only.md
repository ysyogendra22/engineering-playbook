# Interval DP & Bitmask DP

> Two advanced DP shapes. You rarely have to invent them in a first-round interview, but you should recognise them and know the template of each.

#### 1. What Is It?

| Type | State | When |
|---|---|---|
| **Interval DP** | `dp[i][j]` = best answer for the **range** `i..j` | the answer for a range comes from **splitting it at some point `k`** |
| **Bitmask DP** | `dp[mask]` = best answer when the **set of used items** is `mask` | `n ≤ 20` and you must track **which items** are used (a subset) |

**Interval DP signals:** "burst balloons", "matrix chain multiplication", "merge stones", "minimum cost to cut", "remove boxes", "palindrome partitioning cost".

**Bitmask DP signals:** `n` up to about 20, "visit every node once" (travelling salesman), "assign tasks to people", "partition into `k` equal subsets", "all subsets".

#### 2. How It Works

**Interval DP.** Process ranges by **increasing length**. For each range, try every split point `k`.

```mermaid
flowchart LR
    A["dp[i][j]"] --> B["pick split k, i < k < j"]
    B --> C["dp[i][k] + dp[k][j] + cost of joining at k"]
    C --> D["keep the best over all k"]
```

*Burst Balloons (LeetCode 312).* Burst balloons to maximise coins. Bursting balloon `k` gives `nums[left] × nums[k] × nums[right]`. The trick: think of `k` as the **last** balloon burst in the range, so its neighbours are fixed (`left` and `right`).

```text
nums = [3, 1, 5, 8], pad with 1 on both sides: [1, 3, 1, 5, 8, 1]
dp[left][right] = max over k of dp[left][k] + dp[k][right] + a[left] * a[k] * a[right]
answer dp[0][5] = 167
```

**Bitmask DP.** An integer's bits represent a subset. `mask = 0b0101` means items 0 and 2 are used. To add item `i`: `mask or (1 shl i)`. To test: `(mask shr i) and 1`.

*Partition to K Equal Sum Subsets (LeetCode 698).* `dp[mask]` = the current partial sum (mod target) when the items in `mask` are placed, or `−1` if not reachable.

```text
nums = [4, 3, 2, 3, 5, 2, 1], k = 4, total 20 → target 5
dp[mask] tracks (sum so far) mod 5. Fill the current bucket up to 5, then start a new one.
reachable full mask with value 0  →  true
```

**Cost:** interval DP is `O(n³)` (states `n²` × split `n`). Bitmask DP is `O(2ⁿ · n)`. So bitmask works only for `n ≲ 20`.

**Other examples:** Matrix Chain Multiplication (interval), Minimum Cost to Merge Stones (interval), Travelling Salesman (bitmask, `O(2ⁿ n²)`), Shortest Path Visiting All Nodes (bitmask + BFS).

#### 3. Brute Force vs Optimized

| Problem | Brute force | DP |
|---|---|---|
| Burst Balloons | try every order of bursts: `O(n!)` | `O(n³)` |
| Partition to K subsets | try every assignment of items to subsets: `O(kⁿ)` | `O(2ⁿ · n)` |
| Travelling Salesman | every permutation `O(n!)` | `O(2ⁿ · n²)` |

```kotlin
// Brute force Burst Balloons: try every order. O(n!). Only for tiny inputs.
fun maxCoinsBrute(nums: List<Int>): Int {
    if (nums.isEmpty()) return 0
    var best = 0
    for (i in nums.indices) {
        val left = if (i > 0) nums[i - 1] else 1
        val right = if (i < nums.size - 1) nums[i + 1] else 1
        val rest = nums.toMutableList().also { it.removeAt(i) }
        best = maxOf(best, left * nums[i] * right + maxCoinsBrute(rest))
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Burst Balloons (LeetCode 312): interval DP, k is the LAST balloon to burst in (left, right)
fun maxCoins(nums: IntArray): Int {
    val a = intArrayOf(1) + nums + intArrayOf(1)
    val n = a.size
    val dp = Array(n) { IntArray(n) }
    for (len in 2 until n) {
        for (left in 0 until n - len) {
            val right = left + len
            for (k in left + 1 until right) {
                dp[left][right] = maxOf(dp[left][right], dp[left][k] + dp[k][right] + a[left] * a[k] * a[right])
            }
        }
    }
    return dp[0][n - 1]
}

// Partition to K Equal Sum Subsets (LeetCode 698): bitmask DP
fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
    val total = nums.sum()
    if (total % k != 0) return false
    val target = total / k
    val n = nums.size
    val dp = IntArray(1 shl n) { -1 }                 // partial sum (mod target) for each used-set, -1 = unreachable
    dp[0] = 0
    for (mask in 0 until (1 shl n)) {
        if (dp[mask] == -1) continue
        for (i in 0 until n) {
            if (((mask shr i) and 1) == 1) continue    // item i is already used
            val next = mask or (1 shl i)
            if (dp[next] != -1) continue
            if (dp[mask] + nums[i] <= target) dp[next] = (dp[mask] + nums[i]) % target
        }
    }
    return dp[(1 shl n) - 1] == 0
}
```

Checks: `maxCoins(intArrayOf(3, 1, 5, 8))` → `167`. `maxCoins(intArrayOf(1, 5))` → `10`. `maxCoins(intArrayOf())` → `0`. `maxCoinsBrute(listOf(3, 1, 5, 8))` → `167`. `canPartitionKSubsets(intArrayOf(4, 3, 2, 3, 5, 2, 1), 4)` → `true`. `canPartitionKSubsets(intArrayOf(1, 2, 3, 4), 3)` → `false` (the total `10` is not divisible by 3). `canPartitionKSubsets(intArrayOf(2, 2, 2, 2, 3, 4, 5), 4)` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Interval DP | `O(n³)` | `O(n²)` |
| Bitmask DP | `O(2ⁿ · n)` | `O(2ⁿ)` |

#### 6. Common Mistakes

1. **Interval DP:** treating `k` as the **first** burst instead of the last (neighbours then change).
2. **Interval DP:** wrong loop order (ranges must grow from short to long).
3. **Forgetting to pad** with `1` at both ends (Burst Balloons).
4. **Bitmask:** `mask and (1 shl i) != 0` without parentheses (operator precedence). Use `((mask shr i) and 1) == 1`.
5. **Bitmask with `n > 22`** (too much memory and time).
6. **Using an `Int` mask for `n ≥ 32`.** Use `Long`, or reconsider the approach.

#### 7. Say This in the Interview

1. "The answer for a range depends on a split point, so this is interval DP. I fill ranges by increasing length: `O(n³)`."
2. "With `n` up to about 20 and a need to remember which items are used, I'd use a bitmask: `dp[mask]`, with `O(2ⁿ · n)` time."
3. "I'd name the technique and the template first. I'd only code it if the interviewer asks."

#### 8. Quick Check

1. Which technique for `n = 15` items where you must know which were used?
2. Time complexity of interval DP?
3. How do you add item `i` to a mask?

<details>
<summary>Answers</summary>

1. Bitmask DP (`2¹⁵ = 32,768` states).
2. `O(n³)`.
3. `mask or (1 shl i)`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) (Hard) | interval DP, last burst |
| 1039 | [Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) (Medium) | interval DP |
| 1547 | [Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) (Hard) | interval DP |
| 698 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) (Medium) | bitmask DP |
| 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (Hard) | bitmask + BFS |
| 526 | [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) (Medium) | bitmask DP or backtracking |
