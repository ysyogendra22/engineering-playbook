# Coin Change with Canonical Coin Systems

#### 1. What Is It?

A **canonical coin system** is a set of coins where "take the biggest coin that fits, repeat" always gives the fewest coins. Real money (1, 5, 10, 25 or 1, 2, 5, 10, 20, 50, 100) is canonical.

For an arbitrary set like `{1, 3, 4}` it is **not** canonical. The general question *Coin Change* (LeetCode 322) needs DP (note 09).

In interviews you meet two things:

1. A question that says "use the biggest bill / coin first" (Lemonade Change, Integer to Roman). Greedy is the intended answer.
2. A question where an interviewer asks "is greedy correct for these coins?" You answer by trying a counter-example, or by comparing with DP.

#### 2. How It Works

```text
Make 41 with {25, 10, 5, 1}:
  41 / 25 = 1 coin,  remaining 16
  16 / 10 = 1 coin,  remaining 6
   6 /  5 = 1 coin,  remaining 1
   1 /  1 = 1 coin,  remaining 0       total 4 coins
```

**Lemonade Change** (LeetCode 860). Bills are 5, 10, 20. A drink costs 5. Give change to every customer in order.

- Pay 5: no change.
- Pay 10: give back one 5.
- Pay 20: give back 15. **Prefer `10 + 5`** over `5 + 5 + 5`. 5s are more useful (they are needed for 10s too), so keep them.

**Integer to Roman** (LeetCode 12). Use the values `1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1`. Take the biggest value that fits, append its symbol, repeat.

#### 3. Brute Force vs Optimized

How to **check** whether greedy works for a coin set: compare it with DP for amounts up to a limit.

```kotlin
fun coinChangeDP(coins: IntArray, amount: Int): Int {
    val dp = IntArray(amount + 1) { amount + 1 }              // amount + 1 means "impossible"
    dp[0] = 0
    for (a in 1..amount) {
        for (c in coins) if (c <= a) dp[a] = minOf(dp[a], dp[a - c] + 1)
    }
    return if (dp[amount] > amount) -1 else dp[amount]
}

fun greedyCoins(coins: IntArray, amount: Int): Int {
    var remaining = amount
    var count = 0
    for (c in coins.sortedDescending()) { count += remaining / c; remaining %= c }
    return if (remaining == 0) count else -1
}

fun isGreedyCorrect(coins: IntArray, limit: Int): Boolean =
    (1..limit).all { greedyCoins(coins, it) == coinChangeDP(coins, it) }
```

Checks: `isGreedyCorrect([1, 5, 10, 25], 100)` → `true`. `isGreedyCorrect([1, 3, 4], 10)` → `false` (fails at 6).

| | Greedy | DP |
|---|---|---|
| Time | `O(coins)` | `O(amount × coins)` |
| Correct for | canonical coin sets | any coin set |

#### 4. Kotlin Code

```kotlin
// Lemonade Change (LeetCode 860)
fun lemonadeChange(bills: IntArray): Boolean {
    var fives = 0
    var tens = 0
    for (bill in bills) {
        when (bill) {
            5 -> fives++
            10 -> {
                if (fives == 0) return false
                fives--; tens++
            }
            else -> {                                         // 20: prefer one 10 + one 5
                if (tens > 0 && fives > 0) { tens--; fives-- }
                else if (fives >= 3) fives -= 3
                else return false
            }
        }
    }
    return true
}

// Integer to Roman (LeetCode 12)
fun intToRoman(num: Int): String {
    val values = intArrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    var n = num
    val sb = StringBuilder()
    for (i in values.indices) {
        while (n >= values[i]) { sb.append(symbols[i]); n -= values[i] }
    }
    return sb.toString()
}
```

Checks: `lemonadeChange([5,5,5,10,20])` → `true`. `lemonadeChange([5,5,10,10,20])` → `false`. `intToRoman(1994)` → `"MCMXCIV"`. `intToRoman(58)` → `"LVIII"`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Greedy coin change | `O(c)` (`c` = number of coin types, coins sorted) | `O(1)` |
| Lemonade Change | `O(n)` | `O(1)` |
| Integer to Roman | `O(1)` (at most 13 steps of bounded loops) | `O(1)` |
| DP check | `O(amount × c)` | `O(amount)` |

#### 6. Common Mistakes

1. **Using greedy for any coin set.** `{1, 3, 4}` breaks it.
2. **Lemonade Change:** giving `5 + 5 + 5` when `10 + 5` is possible.
3. **Not sorting the coins** (descending) before the loop.
4. **Returning a count when the amount cannot be made** (check `remaining == 0`).
5. **Roman numerals:** forgetting the special values (`900, 400, 90, 40, 9, 4`).

#### 7. Say This in the Interview

1. "Greedy is correct for real-world coin systems. For an arbitrary coin set I would use DP, and here is a counter-example: coins 1, 3, 4 and amount 6."
2. "For 20 dollars in Lemonade Change I prefer a 10 and a 5, because 5s are more flexible."

#### 8. Quick Check

1. Is greedy right for coins `{1, 5, 10, 25}`?
2. In Lemonade Change, which change do you prefer for a 20 bill?

<details>
<summary>Answers</summary>

1. Yes. This is a canonical system.
2. One 10 and one 5, if you have them.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) (Easy) | biggest bill first |
| 2144 | [Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) (Easy) | sort, take two, free third |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) (Medium) | biggest symbol first |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | DP, greedy fails |
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) (Medium) | count ways, DP |
