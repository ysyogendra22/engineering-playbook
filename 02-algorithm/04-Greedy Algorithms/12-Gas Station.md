# Gas Station

#### 1. What Is It?

There are `n` gas stations in a circle. At station `i` you get `gas[i]` fuel. Driving to the next station costs `cost[i]`. Your tank is empty at the start and unlimited in size.

Return the **starting station** that lets you drive around the circle once, or `-1` if it is impossible. The answer is unique if it exists.

```text
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]    → answer 3
```

This is *Gas Station* (LeetCode 134), a favourite greedy question.

#### 2. How It Works

Let `diff[i] = gas[i] − cost[i]` (fuel gained minus fuel used at station `i`).

Two facts make a one-pass answer possible:

1. **If the total of all `diff` is negative**, there is not enough gas. Answer `-1`.
2. **If the tank goes negative** while driving from `start` to station `i`, then **no station between `start` and `i` can be a valid start** either (each of them reaches `i` with even less fuel). So the next candidate is `i + 1`.

Algorithm: keep `tank` and `start`. At each station add `diff`. If `tank < 0`, set `start = i + 1` and `tank = 0`. At the end, if `total >= 0`, `start` is the answer.

```text
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2, -2, -2, 3, 3]       total = 0

i=0: tank = -2 → start = 1, tank = 0
i=1: tank = -2 → start = 2, tank = 0
i=2: tank = -2 → start = 3, tank = 0
i=3: tank = 3
i=4: tank = 6
total = 0 >= 0 → answer 3
```

#### 3. Brute Force vs Optimized

| | Brute force | Greedy |
|---|---|---|
| Idea | try each station as the start, simulate the full circle | one pass with `tank` and `total` |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` | `O(1)` |

```kotlin
fun canCompleteCircuitBrute(gas: IntArray, cost: IntArray): Int {
    val n = gas.size
    for (start in 0 until n) {
        var tank = 0
        var steps = 0
        while (steps < n) {
            val i = (start + steps) % n
            tank += gas[i] - cost[i]
            if (tank < 0) break
            steps++
        }
        if (steps == n) return start
    }
    return -1
}
```

#### 4. Kotlin Code

```kotlin
// Gas Station (LeetCode 134)
fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
    var total = 0
    var tank = 0
    var start = 0
    for (i in gas.indices) {
        val diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if (tank < 0) {                    // cannot reach i + 1 from this start
            start = i + 1
            tank = 0
        }
    }
    return if (total >= 0) start else -1
}
```

Checks: `canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])` → `3`. `canCompleteCircuit([2,3,4], [3,4,3])` → `-1`. `canCompleteCircuit([5], [4])` → `0`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Greedy | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Forgetting the `total >= 0` check.** `start` can look valid while the total gas is not enough.
2. **Not resetting `tank`** when you move `start`.
3. **Simulating the wrap-around** with extra loops. The `total` check makes it unnecessary.
4. **Off-by-one:** the new start is `i + 1`, not `i`.
5. **Returning `start == n`.** If `total >= 0`, `start` is always `< n`.

#### 7. Say This in the Interview

1. "If total gas is less than total cost, no start works. Otherwise a start exists."
2. "If I run out between `start` and `i`, none of the stations in between can work, so I try `i + 1`. One pass, `O(n)`."

#### 8. Quick Check

1. If `tank` becomes negative at station 4, what is the next start candidate?
2. When is the answer `-1`?

<details>
<summary>Answers</summary>

1. Station 5.
2. When the sum of `gas[i] − cost[i]` over all stations is negative.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) (Medium) | running balance + reset |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | running reach (note 11) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium) | reset a running sum when negative |
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) (Easy) | running counts |
| 135 | [Candy](https://leetcode.com/problems/candy/) (Hard) | two-pass greedy (note 14) |
