# Jump Game

> A top greedy question at FAANG. Two versions: *can I reach the end?* (55) and *fewest jumps to the end* (45).

#### 1. What Is It?

`nums[i]` is the **maximum** jump length from index `i`. You start at index 0.

- **Jump Game (55):** can you reach the last index?
- **Jump Game II (45):** what is the minimum number of jumps to reach the last index? (It is always reachable.)

```text
[2, 3, 1, 1, 4]  → true, min jumps = 2   (0 → 1 → 4)
[3, 2, 1, 0, 4]  → false                 (you always get stuck at index 3)
```

#### 2. How It Works

**Jump Game (55): track the farthest index you can reach.**

1. `farthest = 0`.
2. For each index `i`: if `i > farthest`, you cannot even stand here, so return `false`.
3. Update `farthest = max(farthest, i + nums[i])`.
4. If you finish the loop, return `true`.

```text
[3, 2, 1, 0, 4]
i=0: farthest = 3
i=1: farthest = 3
i=2: farthest = 3
i=3: farthest = 3     (0 jump)
i=4: 4 > 3 → false
```

**Jump Game II (45): think in "levels", like BFS.**

- `curEnd` = the farthest index reachable with the jumps made so far.
- `farthest` = the farthest index reachable with one more jump.
- When `i` reaches `curEnd`, you must jump: `jumps++`, `curEnd = farthest`.

```text
[2, 3, 1, 1, 4]
i=0: farthest = 2.  i == curEnd (0) → jumps = 1, curEnd = 2
i=1: farthest = 4
i=2: farthest = 4.  i == curEnd (2) → jumps = 2, curEnd = 4
i=3: farthest = 4
done (curEnd covers the last index): jumps = 2
```

Why greedy works: reaching a farther index never hurts, because every index before it is also reachable.

#### 3. Brute Force vs Optimized

| | Brute force | Better | Greedy |
|---|---|---|---|
| Jump Game | DFS, try every jump length: `O(2^n)` | DP `good[i]`: `O(n²)` | farthest reach: `O(n)` |
| Jump Game II | try all paths | DP `min[i]`: `O(n²)` | levels: `O(n)` |

```kotlin
// Brute force: try every jump length from every position
fun canJumpBrute(nums: IntArray, i: Int = 0): Boolean {
    if (i >= nums.size - 1) return true
    for (step in 1..nums[i]) if (canJumpBrute(nums, i + step)) return true
    return false
}
```

The DP version is in note 10.

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
    for (i in 0 until nums.size - 1) {                // we never need to jump from the last index
        farthest = maxOf(farthest, i + nums[i])
        if (i == curEnd) {
            jumps++
            curEnd = farthest
        }
    }
    return jumps
}
```

Checks: `canJump([2,3,1,1,4])` → `true`. `canJump([3,2,1,0,4])` → `false`. `canJump([0])` → `true`. `jump([2,3,1,1,4])` → `2`. `jump([2,3,0,1,4])` → `2`. `jump([0])` → `0`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Jump Game (greedy) | `O(n)` | `O(1)` |
| Jump Game II (greedy) | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Not returning `false`** when `i > farthest`.
2. **Jump Game II:** looping to `nums.size` instead of `nums.size − 1`, which counts one jump too many.
3. **Confusing** "maximum jump" with "exactly that many steps".
4. **Single element** `[0]`: reachable, 0 jumps.
5. **Overflow** is not a concern here, but `i + nums[i]` can be large; `Int` is fine for the usual limits.

#### 7. Say This in the Interview

1. "I keep the farthest index I can reach. If I ever stand beyond it, the end is unreachable. `O(n)` time, `O(1)` space."
2. "For the minimum jumps I treat each jump as a level: when I finish the current level, I make a jump to the farthest reach."

#### 8. Quick Check

1. When does `canJump` return `false`?
2. In Jump Game II, when do you increase `jumps`?

<details>
<summary>Answers</summary>

1. When the current index is greater than the farthest reachable index.
2. When `i` reaches `curEnd` (the end of the current level).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | farthest reach |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Medium) | levels |
| 1306 | [Jump Game III](https://leetcode.com/problems/jump-game-iii/) (Medium) | BFS/DFS (not greedy) |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) (Medium) | running balance (note 12) |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium) | same "reach and cut" idea (note 15) |
