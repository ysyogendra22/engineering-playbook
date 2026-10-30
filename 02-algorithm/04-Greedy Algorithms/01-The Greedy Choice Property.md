# The Greedy Choice Property

> Read this note first. Greedy is easy to code and easy to get wrong. The skill is knowing **when** it is correct.

#### 1. What Is It?

A **greedy algorithm** makes the best choice **right now** at each step and **never goes back**.

A problem has the **greedy choice property** when these local best choices add up to the best answer overall. Many problems do **not** have it, and then greedy gives a wrong answer without any warning.

```text
Coins {1, 5, 10, 25}, make 41:   25 + 10 + 5 + 1 = 4 coins   greedy is correct
Coins {1, 3, 4},      make 6:    4 + 1 + 1 = 3 coins          greedy is WRONG (3 + 3 = 2 coins)
```

Why interviewers like greedy: the code is short (often a sort and one loop), but you must **explain why it is correct**.

#### 2. How It Works

Use this 3-step check every time:

1. **Propose a rule.** "Always take the earliest-ending / biggest / cheapest option."
2. **Try to break it** with a small tricky example (3 to 5 items).
3. **Justify it** with an exchange argument (note 03), or say it out loud if it is a well-known problem.

How to **identify** a greedy problem:

| Signal in the question | Think |
|---|---|
| "minimum number of ..." or "maximum number of ..." and sorting makes it obvious | greedy |
| intervals, meetings, ranges | sort, then greedy |
| "can you reach / finish ...?" with a single scan | greedy (running value) |
| each item is used at most once and cannot be split | be careful, often DP |
| "count the number of ways" | DP, not greedy |
| a small example breaks the "obvious" rule | DP or backtracking |

#### 3. Brute Force vs Optimized

| | Brute force | Greedy |
|---|---|---|
| Idea | try every combination of choices | make the best local choice, move on |
| Time | exponential | `O(n log n)` (a sort) or `O(n)` |
| Correct for all inputs | yes | only if the greedy property holds |

```kotlin
// Greedy: take the biggest coin first. Correct only for "nice" coin systems.
fun greedyCoins(coins: IntArray, amount: Int): Int {
    var remaining = amount
    var count = 0
    for (coin in coins.sortedDescending()) {
        count += remaining / coin
        remaining %= coin
    }
    return if (remaining == 0) count else -1
}

// Brute force: try every coin at every step. Always correct, but exponential.
fun bruteCoins(coins: IntArray, amount: Int): Int {
    if (amount == 0) return 0
    var best = Int.MAX_VALUE
    for (coin in coins) {
        if (coin <= amount) {
            val sub = bruteCoins(coins, amount - coin)
            if (sub != Int.MAX_VALUE) best = minOf(best, sub + 1)
        }
    }
    return best
}
```

Checks: `greedyCoins([1, 5, 10, 25], 41)` → `4`. `greedyCoins([1, 3, 4], 6)` → `3`, but `bruteCoins([1, 3, 4], 6)` → `2`, so greedy is wrong for this coin set.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Typical greedy (sort + one pass) | `O(n log n)` | `O(1)` to `O(n)` |
| Greedy with a heap | `O(n log n)` | `O(n)` |
| Brute force over all choices | exponential | recursion depth |

Complexity is rarely the hard part of greedy. **Correctness** is.

#### 5. Common Mistakes

1. Trusting a greedy idea because it works on the sample in the question.
2. Using greedy coin change on an arbitrary coin set (use DP, note 09).
3. Skipping the counter-example check in an interview.
4. Sorting by the wrong key (start time instead of end time for intervals).
5. Not saying **why** the rule is correct. A correct answer with no reason sounds like a guess.

#### 6. Say This in the Interview

1. "My greedy rule is: always pick ... Let me test it on a small tricky example first."
2. "I cannot find a counter-example, and here is the exchange argument: swapping the greedy choice into any optimal answer does not make it worse."
3. "If the rule breaks, I will switch to DP."

#### 7. Quick Check

1. Is greedy correct for coins {1, 3, 4} and amount 6?
2. What is the first thing to do after you think of a greedy rule?

<details>
<summary>Answers</summary>

1. No. Greedy gives 3 coins (4, 1, 1) but the best is 2 coins (3, 3).
2. Try to break it with a small counter-example.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | sort, match smallest with smallest |
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) (Easy) | give the biggest bill first |
| 1710 | [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) (Easy) | best value first |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | track the farthest reach |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | greedy fails, use DP |
