# Proving Correctness with an Exchange Argument

> You do not need a math proof in an interview. You need a short, clear reason. This note gives you the reason in plain words.

#### 1. What Is It?

An **exchange argument** shows that a greedy choice is safe:

> Take **any** optimal answer. If it does not use the greedy choice, **swap** the greedy choice in. The answer does not get worse. So some optimal answer uses the greedy choice.

Repeat this for every step and the greedy answer is optimal.

#### 2. How It Works

**Example: pick the most non-overlapping meetings.** Greedy rule: always pick the meeting that **ends first**.

```text
Take any optimal schedule. Look at its first meeting X.
Let G be the meeting that ends earliest of all.

If X = G: nothing to do.
If X ≠ G: G ends no later than X, so replace X with G.
          Everything after X still fits, because G ends even earlier.
          The schedule has the same size, so it is still optimal.

So an optimal schedule that starts with G exists.
Remove G and the meetings that overlap it, and repeat on the rest.
```

Why other rules fail (try to break them with small cases):

| Rule | Counter-example | Result |
|---|---|---|
| earliest **start** | `[0,10]`, `[1,2]`, `[3,4]` | picks 1 meeting, best is 2 |
| **shortest** meeting | `[0,5]`, `[4,6]`, `[5,10]` (the short `[4,6]` overlaps both others) | picks 1 meeting, best is 2 |
| earliest **end** | none (proved above) | optimal |

The three-line template to say out loud:

1. "Suppose an optimal answer does not use my greedy choice."
2. "I swap my choice in."
3. "The result is still valid and no worse, so my choice is safe."

#### 3. Brute Force vs Optimized (Test Your Greedy)

You can also **test** a greedy idea by comparing it to a brute force on small random inputs. This is a good habit when you practise.

```kotlin
fun greedyCount(intervals: Array<IntArray>): Int {
    var count = 0
    var lastEnd = Int.MIN_VALUE
    for (iv in intervals.sortedBy { it[1] }) {
        if (iv[0] >= lastEnd) { count++; lastEnd = iv[1] }
    }
    return count
}

// Brute force: try every subset (n must be small)
fun bruteCount(intervals: Array<IntArray>): Int {
    val n = intervals.size
    var best = 0
    for (mask in 0 until (1 shl n)) {
        val chosen = (0 until n).filter { mask and (1 shl it) != 0 }
            .map { intervals[it] }
            .sortedBy { it[0] }
        var ok = true
        for (i in 1 until chosen.size) {
            if (chosen[i][0] < chosen[i - 1][1]) { ok = false; break }
        }
        if (ok) best = maxOf(best, chosen.size)
    }
    return best
}
```

Check: for `[[1,3],[2,4],[3,5]]` both return `2`. If the two ever disagree on a random small input, your greedy rule is wrong.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Greedy | `O(n log n)` | `O(1)` extra |
| Brute force subsets | `O(2^n · n log n)` | `O(n)` |

#### 5. Common Mistakes

1. **"It works on the examples, so it is correct."** Examples are not proof.
2. **A proof that never uses an optimal answer.** The argument must start from *any* optimal answer.
3. **Forgetting to show the swap keeps the answer valid** (no new overlap, same size).
4. **Over-explaining.** In an interview, 3 to 4 sentences are enough.

#### 6. Say This in the Interview

1. "Here is why it is safe: if an optimal answer picked something else first, I can swap in the earliest-ending meeting and nothing breaks."
2. "I also tried a few small counter-examples and none broke it."

#### 7. Quick Check

1. What do you start from in an exchange argument?
2. Why does "earliest start" fail for meetings?

<details>
<summary>Answers</summary>

1. Any optimal answer.
2. A long meeting that starts early can block many short ones. `[0,10]` blocks `[1,2]` and `[3,4]`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) | earliest end first |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium) | shoot at the earliest end |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | smallest fitting cookie |
| 1029 | [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) (Medium) | sort by difference |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium) | cut as early as possible |
