# Partition Labels & Stock Profit

> Short greedy scans that show up often as warm-ups: one pass, a few variables.

#### 1. What Is It?

Four small questions with the same shape: **scan once and keep the best local information.**

| Question | Goal |
|---|---|
| **Partition Labels (763)** | cut a string into the most parts so each letter appears in only one part |
| **Best Time to Buy and Sell Stock (121)** | one buy and one sell, maximize profit |
| **Best Time to Buy and Sell Stock II (122)** | unlimited trades, maximize profit |
| **Is Subsequence (392)** | is `s` a subsequence of `t`? |

#### 2. How It Works

**Partition Labels.** Record the **last index** of every letter. Scan the string with `end` = the farthest last index of letters seen in the current part. When `i == end`, the part is closed.

```text
"ababcbacadefegdehijhklij"

a last = 8, b last = 5, c last = 7 ...
part 1: i=0..8   end becomes 8 → size 9   ("ababcbaca")
part 2: i=9..15  end 15       → size 7   ("defegde")
part 3: i=16..23 end 23       → size 8   ("hijhklij")
answer [9, 7, 8]
```

**Stock I (121).** Keep the lowest price so far. At each day, the best profit is `price − minSoFar`.

**Stock II (122).** With unlimited trades, collect **every rise**: add `price[i] − price[i−1]` whenever it is positive. Buying and selling on the same rising run gives the same total as many small trades.

```text
[7, 1, 5, 3, 6, 4]
rises: 1→5 (+4), 3→6 (+3)       total 7
```

**Is Subsequence.** Walk through `t` with a pointer on `s`. When characters match, move the pointer on `s`. Greedy: always match the earliest possible character.

#### 3. Brute Force vs Optimized

| Problem | Brute force | Greedy |
|---|---|---|
| Stock I | all pairs `(buy, sell)`, `O(n²)` | running minimum, `O(n)` |
| Stock II | try buy/sell choices recursively, `O(2^n)` | sum of rises, `O(n)` |
| Partition Labels | try all cut positions, checking each, `O(n²)` or worse | last index + one scan, `O(n)` |

```kotlin
fun maxProfitBrute(prices: IntArray): Int {
    var best = 0
    for (i in prices.indices) {
        for (j in i + 1 until prices.size) best = maxOf(best, prices[j] - prices[i])
    }
    return best
}
```

#### 4. Kotlin Code

```kotlin
// Partition Labels (LeetCode 763)
fun partitionLabels(s: String): List<Int> {
    val last = IntArray(26)
    for (i in s.indices) last[s[i] - 'a'] = i
    val sizes = mutableListOf<Int>()
    var start = 0
    var end = 0
    for (i in s.indices) {
        end = maxOf(end, last[s[i] - 'a'])
        if (i == end) {                                  // no letter of this part appears later
            sizes.add(end - start + 1)
            start = i + 1
        }
    }
    return sizes
}

// Best Time to Buy and Sell Stock (LeetCode 121)
fun maxProfit(prices: IntArray): Int {
    var minPrice = Int.MAX_VALUE
    var best = 0
    for (p in prices) {
        minPrice = minOf(minPrice, p)
        best = maxOf(best, p - minPrice)
    }
    return best
}

// Best Time to Buy and Sell Stock II (LeetCode 122)
fun maxProfitUnlimited(prices: IntArray): Int {
    var profit = 0
    for (i in 1 until prices.size) {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1]
    }
    return profit
}

// Is Subsequence (LeetCode 392)
fun isSubsequence(s: String, t: String): Boolean {
    var i = 0
    for (ch in t) {
        if (i < s.length && s[i] == ch) i++
    }
    return i == s.length
}
```

Checks: `partitionLabels("ababcbacadefegdehijhklij")` → `[9, 7, 8]`. `partitionLabels("eccbbbbdec")` → `[10]`. `maxProfit([7,1,5,3,6,4])` → `5`. `maxProfit([7,6,4,3,1])` → `0`. `maxProfitUnlimited([7,1,5,3,6,4])` → `7`. `maxProfitUnlimited([1,2,3,4,5])` → `4`. `isSubsequence("abc", "ahbgdc")` → `true`. `isSubsequence("axc", "ahbgdc")` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Partition Labels | `O(n)` | `O(1)` (26 letters) |
| Stock I / II | `O(n)` | `O(1)` |
| Is Subsequence | `O(n)` | `O(1)` |

#### 6. Common Mistakes

1. **Partition Labels:** closing a part at the first repeated letter instead of the **last** occurrence.
2. **Stock I:** updating the best profit **before** updating the minimum, or using a future price as the buy price.
3. **Stock I:** returning a negative profit. The minimum is `0` (do nothing).
4. **Stock II:** trying to find the exact buy and sell days. You only need the sum of rises.
5. **Is Subsequence:** moving the pointer on `t` only when it matches (it must move every time).
6. **Stock with a fee or cooldown** is not greedy-simple. Use DP.

#### 7. Say This in the Interview

1. "For Partition Labels I store the last index of each letter. I extend the current part to the farthest last index. When I reach it, I can cut."
2. "For one transaction I keep the lowest price so far. For unlimited transactions I add every price rise."

#### 8. Quick Check

1. `maxProfitUnlimited([1, 5, 3, 8])`?
2. When do you close a part in Partition Labels?

<details>
<summary>Answers</summary>

1. `4 + 5 = 9` (the rises 1→5 and 3→8).
2. When the index `i` equals the farthest last index seen in the part.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) | running minimum |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) (Easy) | two pointers |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Medium) | sum of rises |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium) | last occurrence |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) (Medium) | same "farthest reach" idea (note 11) |
