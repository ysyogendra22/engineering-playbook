# Greedy Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–15.

#### 1. Key Takeaways

1. Greedy = make the best **local** choice and never go back. It is correct only when the problem has the **greedy choice property**.
2. Most greedy answers are **sort + one pass**: `O(n log n)`. Or **one scan** with a running value: `O(n)`.
3. Before coding: **try to break your rule** with a 3 to 5 item example. Then give a one-line exchange argument.
4. If a small example breaks the rule, use **DP** (0/1 knapsack, general coin change, house robber).
5. **Intervals:** "most intervals / fewest removals / arrows" → sort by **end**. "Merge" → sort by **start**.
6. Say the brute force first, then the greedy, then **why** it is correct.

#### 2. Complexity Table

| Pattern | Time | Space |
|---|---|---|
| sort + scan | `O(n log n)` | `O(1)` to `O(n)` |
| running value (jump, gas, stock) | `O(n)` | `O(1)` |
| heap greedy (Huffman, task scheduler, sticks) | `O(n log n)` | `O(n)` |
| Dijkstra (heap) | `O((V + E) log V)` | `O(V + E)` |
| Kruskal | `O(E log E)` | `O(V)` |
| two-pass (candy) | `O(n)` | `O(n)` |

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern / rule | Complexity | Note |
|---|---|---|---|
| match two groups (children and cookies) | sort both, two pointers | `O(n log n)` | 02 |
| split into two groups with min cost | sort by `costA − costB` | `O(n log n)` | 02 |
| most non-overlapping intervals, fewest removed | sort by **end**, keep if `start >= lastEnd` | `O(n log n)` | 04 |
| fewest arrows for ranges | sort by end, shoot at the end | `O(n log n)` | 04 |
| fewest meeting rooms | sort starts and ends, sweep | `O(n log n)` | 04 |
| items can be split, maximize value | sort by value / weight | `O(n log n)` | 05 |
| change with real coins / bills | biggest first | `O(coins)` | 06 |
| shortest path, no negative edges | Dijkstra (min-heap) | `O((V+E) log V)` | 07 |
| connect all nodes, min cost | Kruskal (sort + Union-Find) or Prim | `O(E log E)` | 07 |
| merge the two smallest repeatedly | min-heap (Huffman, sticks) | `O(n log n)` | 08 |
| "can I reach the end?" | farthest reach | `O(n)` | 11 |
| "fewest jumps" | levels: `curEnd`, `farthest` | `O(n)` | 11 |
| circular route, find the start | running tank + total check | `O(n)` | 12 |
| same item can't repeat within `n` | most frequent first (formula or max-heap) | `O(n)` | 13 |
| each item depends on both neighbours | two passes (left, right) | `O(n)` | 14 |
| cut a string into parts by last occurrence | last index + `end` | `O(n)` | 15 |
| buy and sell, unlimited trades | add every rise | `O(n)` | 15 |

#### 4. Templates to Memorise

**Sort by end (intervals)**

```kotlin
var kept = 0
var lastEnd = Int.MIN_VALUE
for (iv in intervals.sortedBy { it[1] }) {
    if (iv[0] >= lastEnd) { kept++; lastEnd = iv[1] }
}
val removed = intervals.size - kept
```

**Farthest reach (Jump Game)**

```kotlin
var farthest = 0
for (i in nums.indices) {
    if (i > farthest) return false
    farthest = maxOf(farthest, i + nums[i])
}
return true
```

**Jump Game II levels**

```kotlin
var jumps = 0; var curEnd = 0; var farthest = 0
for (i in 0 until nums.size - 1) {
    farthest = maxOf(farthest, i + nums[i])
    if (i == curEnd) { jumps++; curEnd = farthest }
}
```

**Gas Station**

```kotlin
var total = 0; var tank = 0; var start = 0
for (i in gas.indices) {
    val d = gas[i] - cost[i]
    total += d; tank += d
    if (tank < 0) { start = i + 1; tank = 0 }
}
return if (total >= 0) start else -1
```

**Heap: merge the two smallest**

```kotlin
val heap = PriorityQueue<Int>()
for (x in sticks) heap.add(x)
var cost = 0
while (heap.size > 1) { val m = heap.poll() + heap.poll(); cost += m; heap.add(m) }
```

**Two-pass (Candy)**

```kotlin
val c = IntArray(n) { 1 }
for (i in 1 until n) if (r[i] > r[i - 1]) c[i] = c[i - 1] + 1
for (i in n - 2 downTo 0) if (r[i] > r[i + 1]) c[i] = maxOf(c[i], c[i + 1] + 1)
```

**Partition by last occurrence**

```kotlin
var start = 0; var end = 0
for (i in s.indices) {
    end = maxOf(end, last[s[i] - 'a'])
    if (i == end) { sizes.add(end - start + 1); start = i + 1 }
}
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Greedy |
|---|---|---|
| Max non-overlapping intervals | all subsets `O(2^n)` | sort by end `O(n log n)` |
| Meeting Rooms II | count overlap at each start `O(n²)` | sorted starts and ends |
| Jump Game | DFS `O(2^n)` / DP `O(n²)` | farthest reach `O(n)` |
| Gas Station | try each start `O(n²)` | one pass `O(n)` |
| Candy | repeat fixing `O(n²)` | two passes `O(n)` |
| Stock I | all pairs `O(n²)` | running minimum `O(n)` |
| Stock II | try every buy / sell `O(2^n)` | sum of rises `O(n)` |
| Task Scheduler | all orders `O(n!)` | formula `O(n)` |
| Connect sticks | any merge order, exponential | min-heap `O(n log n)` |
| Two City Scheduling | `O(2^n)` | sort by difference |

#### 6. Common Mistakes and Edge Cases

1. Trusting a rule because it works on the sample. **Try to break it.**
2. Sorting intervals by **start** when you need **end** (or the other way round for merge).
3. Touching intervals: `[1,2]` and `[2,3]` do not overlap in 435 and 253. Balloons that touch share an arrow in 452.
4. Greedy on 0/1 knapsack or on coins `{1,3,4}`: **wrong**. Use DP.
5. Dijkstra with negative edges: **wrong**. Use Bellman-Ford.
6. Subtracting to compare (`a - b`) can overflow. Use `compareBy` / `sortedBy`.
7. Gas Station: forgetting the `total >= 0` check. Task Scheduler: forgetting `max(tasks.size, formula)`.
8. Candy: a single pass only, or `>=` instead of `>`.
9. Edge cases: empty input, one element, all equal, already sorted, ties.

#### 7. What to Say Out Loud

1. "Brute force tries every choice, which is exponential. I think a greedy rule works: ..."
2. "Let me test it on a small tricky example before I commit."
3. "It is safe because if an optimal answer did not use my choice, I could swap it in without making it worse."
4. "Time `O(n log n)` for the sort, `O(1)` extra space. If the rule broke, I would use DP."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | sort + two pointers |
| Easy | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | biggest first |
| Easy | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | running minimum |
| Easy | [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) | best ratio first |
| Easy | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | two pointers |
| Easy | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | max-heap |
| Medium | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | sum of rises |
| Medium | [Jump Game](https://leetcode.com/problems/jump-game/) | farthest reach |
| Medium | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | levels |
| Medium | [Gas Station](https://leetcode.com/problems/gas-station/) | running tank |
| Medium | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | sort by end |
| Medium | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | sort by end |
| Medium | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | sweep |
| Medium | [Partition Labels](https://leetcode.com/problems/partition-labels/) | last occurrence |
| Medium | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | most frequent first |
| Medium | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | max-heap |
| Medium | [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) | sort by difference |
| Medium | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | sort, then insert |
| Medium | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra |
| Medium | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Kruskal / Prim |
| Hard | [Candy](https://leetcode.com/problems/candy/) | two passes |
