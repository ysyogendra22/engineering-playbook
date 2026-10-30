# Candy — Two-Pass Greedy

> A Hard question that becomes easy once you know the **two-pass trick**: handle the left neighbour in one pass and the right neighbour in another.

#### 1. What Is It?

Children stand in a line, each with a rating. Give every child at least 1 candy. A child with a **higher rating than a neighbour** must get **more candy than that neighbour**. Return the **minimum total candy**.

```text
ratings = [1, 0, 2]   → candies [2, 1, 2]   total 5
ratings = [1, 2, 2]   → candies [1, 2, 1]   total 4   (equal ratings need no extra)
```

This is *Candy* (LeetCode 135).

#### 2. How It Works

Each child has **two rules**: one about the left neighbour, one about the right. Satisfying both at once is hard, so do them **one at a time**:

1. Start everyone with 1 candy.
2. **Left to right:** if `rating[i] > rating[i−1]`, then `candy[i] = candy[i−1] + 1`.
3. **Right to left:** if `rating[i] > rating[i+1]`, then `candy[i] = max(candy[i], candy[i+1] + 1)`.
4. Sum the candies.

```text
ratings:           1  0  2
start:             1  1  1
left → right:      1  1  2      (2 > 0, so 1 + 1)
right → left:      2  1  2      (1 > 0, so max(1, 1 + 1) = 2)
total = 5
```

The `max` in the second pass keeps what the first pass already guaranteed.

**Pattern: two-pass greedy.** Use it when each item depends on **both** neighbours (or on everything to its left and right). It also appears in *Product of Array Except Self* and *Trapping Rain Water*.

#### 3. Brute Force vs Optimized

| | Brute force | Two passes |
|---|---|---|
| Idea | keep fixing violations until nothing changes | one pass each way |
| Time | `O(n²)` worst case | `O(n)` |
| Space | `O(n)` | `O(n)` |

```kotlin
fun candyBrute(ratings: IntArray): Int {
    val n = ratings.size
    val candy = IntArray(n) { 1 }
    var changed = true
    while (changed) {                                       // repeat until all rules hold
        changed = false
        for (i in 0 until n) {
            if (i > 0 && ratings[i] > ratings[i - 1] && candy[i] <= candy[i - 1]) {
                candy[i] = candy[i - 1] + 1; changed = true
            }
            if (i < n - 1 && ratings[i] > ratings[i + 1] && candy[i] <= candy[i + 1]) {
                candy[i] = candy[i + 1] + 1; changed = true
            }
        }
    }
    return candy.sum()
}
```

#### 4. Kotlin Code

```kotlin
// Candy (LeetCode 135)
fun candy(ratings: IntArray): Int {
    val n = ratings.size
    val candies = IntArray(n) { 1 }
    for (i in 1 until n) {
        if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1
    }
    for (i in n - 2 downTo 0) {
        if (ratings[i] > ratings[i + 1]) candies[i] = maxOf(candies[i], candies[i + 1] + 1)
    }
    return candies.sum()
}
```

Checks: `candy([1,0,2])` → `5`. `candy([1,2,2])` → `4`. `candy([1,3,2,2,1])` → `7` (candies `[1,2,1,2,1]`). `candy([5])` → `1`.

A related question, *Queue Reconstruction by Height* (LeetCode 406), uses a different greedy: sort by height descending (and by count ascending), then insert each person at index `count`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Two passes | `O(n)` | `O(n)` |
| One-pass slope counting (advanced) | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Only one pass.** `[1, 0, 2]` is wrong with only the left-to-right pass.
2. **Not using `max`** in the second pass. You can then break the first pass's work.
3. **Equal ratings:** no extra candy is required. Use `>`, not `>=`.
4. **Starting candies at 0.** Everyone gets at least 1.
5. **Overflow:** sums fit in `Int` for the usual limits (`n` up to 20,000).

#### 7. Say This in the Interview

1. "Each child has a left rule and a right rule. I satisfy the left rule in a left-to-right pass, then the right rule in a right-to-left pass using `max`, so the first pass stays valid. `O(n)` time."
2. "Equal ratings do not force extra candy."

#### 8. Quick Check

1. Candies for `[3, 2, 1]`?
2. Why `max` in the second pass?

<details>
<summary>Answers</summary>

1. `[3, 2, 1]` (total 6). The left pass leaves `[1,1,1]`, the right pass builds `3, 2, 1`.
2. A child may already have more candy from the left pass. We must satisfy both rules.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) | left pass and right pass |
| 135 | [Candy](https://leetcode.com/problems/candy/) (Hard) | this note |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) | left max and right max |
| 406 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) (Medium) | sort, then insert |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) (Medium) | running balance (note 12) |
