# Greedy + Sorting — the Usual Pairing

#### 1. What Is It?

Most greedy solutions start with a **sort**. After sorting, the "best choice" is simply the next item in the list, so one loop finishes the job.

```text
1. Sort by a key (the key is the whole idea).
2. Walk through the items once, making the obvious choice.
```

The hard part is picking the **right sort key**. Examples:

| Question | Sort by |
|---|---|
| match children with cookies | greed and size (both ascending) |
| pick the most non-overlapping meetings | end time |
| fill a bag with the best value per weight | value / weight (descending) |
| split people between two cities | cost A − cost B |

#### 2. How It Works

**Assign Cookies** (LeetCode 455). Child `i` needs a cookie of size `>= g[i]`. Each child gets at most one cookie. Maximize the happy children.

Sort both lists. Give the **smallest cookie that satisfies** the least greedy child, so big cookies stay for big appetites.

```text
g = [1, 2, 3]   cookies = [1, 1]

child 1 (needs 1): cookie 1 works  → happy = 1
child 2 (needs 2): cookie 1 too small → no more cookies
answer: 1
```

**Two City Scheduling** (LeetCode 1029). `2n` people, each has a cost for city A and city B. Send exactly `n` to each city with minimum total cost.

Idea: start by sending everyone to A. Moving person `i` to B changes the cost by `costB − costA`. Sort by `costA − costB` and send the first `n` people (the ones who gain most from A) to A.

```text
[[10,20],[30,200],[400,50],[30,20]]
diff = A − B:  -10, -170, 350, 10
sorted:  [30,200] (-170), [10,20] (-10), [30,20] (10), [400,50] (350)
first 2 → A: 30 + 10 = 40
last 2  → B: 20 + 50 = 70      total = 110
```

#### 3. Brute Force vs Optimized

| | Brute force | Sort + greedy |
|---|---|---|
| Two City Scheduling | try all ways to choose `n` people for A | sort by `costA − costB` |
| Time | `O(2^(2n))` | `O(n log n)` |
| Space | recursion depth | `O(1)` extra |

```kotlin
fun twoCityBrute(costs: Array<IntArray>): Int {
    val n = costs.size / 2
    fun go(i: Int, a: Int): Int {                        // a = people sent to A so far
        if (i == costs.size) return 0
        var best = Int.MAX_VALUE
        if (a < n) best = minOf(best, costs[i][0] + go(i + 1, a + 1))
        if (i - a < n) best = minOf(best, costs[i][1] + go(i + 1, a))
        return best
    }
    return go(0, 0)
}
```

#### 4. Kotlin Code

```kotlin
// Assign Cookies (LeetCode 455)
fun findContentChildren(g: IntArray, s: IntArray): Int {
    g.sort()
    s.sort()
    var child = 0
    for (cookie in s) {
        if (child < g.size && g[child] <= cookie) child++      // this cookie makes a child happy
    }
    return child
}

// Array Partition (LeetCode 561): pair up numbers to maximize the sum of the smaller ones
fun arrayPairSum(nums: IntArray): Int {
    nums.sort()
    var sum = 0
    for (i in nums.indices step 2) sum += nums[i]               // neighbours waste the least
    return sum
}

// Two City Scheduling (LeetCode 1029)
fun twoCitySchedCost(costs: Array<IntArray>): Int {
    val sorted = costs.sortedBy { it[0] - it[1] }
    val n = costs.size / 2
    var total = 0
    for (i in sorted.indices) total += if (i < n) sorted[i][0] else sorted[i][1]
    return total
}
```

Checks: `findContentChildren([1,2,3], [1,1])` → `1`. `findContentChildren([1,2], [1,2,3])` → `2`. `arrayPairSum([1,4,3,2])` → `4`. `twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])` → `110`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort | `O(n log n)` | `O(1)` to `O(n)` depending on the sort |
| One pass after sorting | `O(n)` | `O(1)` |
| Total | `O(n log n)` | `O(1)` to `O(n)` |

#### 6. Common Mistakes

1. **Wrong sort key.** Test your key on a small example.
2. **Sorting only one list** in matching problems (both must be sorted).
3. **Overflow when comparing by subtraction** (`a[0] - b[0]` with big numbers). Use `compareBy` or `sortedBy`.
4. **Forgetting that sorting changes the input** (`g.sort()` is in place). Say so, or copy first.
5. **Skipping the reason** the sort key is right.

#### 7. Say This in the Interview

1. "Sorting makes the best choice obvious, so I sort by ... and scan once. `O(n log n)` time."
2. "The sort key is ... because swapping any other order does not improve the answer."

#### 8. Quick Check

1. Why give each child the smallest cookie that works?
2. What is the sort key for Two City Scheduling?

<details>
<summary>Answers</summary>

1. Bigger cookies are kept for children with bigger needs.
2. `costA − costB`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | sort both, two pointers |
| 561 | [Array Partition](https://leetcode.com/problems/array-partition/) (Easy) | sort, take every second |
| 976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) (Easy) | sort descending, check 3 neighbours |
| 1029 | [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) (Medium) | sort by `costA − costB` |
| 406 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) (Medium) | sort by height, insert by count |
