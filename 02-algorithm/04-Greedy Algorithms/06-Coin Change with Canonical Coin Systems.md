# Coin Change with Canonical Coin Systems

#### 1. Definition — Must Know

1. Given a target amount and a set of coin denominations, find the **minimum number of coins** needed to make that amount.
2. A **canonical coin system** (like standard currency: 1, 5, 10, 25) is one where the greedy "always take the biggest coin that fits" strategy actually gives the optimal answer. Not all coin systems are canonical (topic 9).

#### 2. Why It Is Used — Must Know

1. It's the second-most common example (after Activity Selection) used to teach when greedy works and when it doesn't.
2. Real-world currency systems are usually designed to be canonical on purpose, which is why the greedy cashier approach "just works" in everyday life.

#### 3. How It Works — Must Know

```text
Coins: [25, 10, 5, 1]   Target: 63

Take 25: 63 - 25 = 38, count = 1
Take 25: 38 - 25 = 13, count = 2
Take 10: 13 - 10 = 3,  count = 3
Take 1:  3 - 1 = 2,    count = 4
Take 1:  2 - 1 = 1,    count = 5
Take 1:  1 - 1 = 0,    count = 6

Result: 6 coins (25, 25, 10, 1, 1, 1)
```

#### 4. Algorithm — Must Know

```text
sort coins descending
count = 0
remaining = target
for coin in sorted coins:
    count += remaining / coin      # take as many of this coin as fit
    remaining = remaining % coin
return count if remaining == 0 else "not possible"
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun minCoinsGreedy(coins: List<Int>, target: Int): Int {
    var remaining = target
    var count = 0
    for (coin in coins.sortedDescending()) {
        count += remaining / coin
        remaining %= coin
    }
    return if (remaining == 0) count else -1
}
```

#### 6. Complexity — Must Know

| Step | Cost |
|---|---|
| Sort coins | O(k log k), k = number of coin types (usually tiny) |
| Divide-and-mod loop | O(k) |
| Total | Effectively O(k), very fast |

Compare with the Dynamic Programming version needed for a non-canonical system: O(target × k) (topic 9, and `05` in this folder).

#### 7. Common Mistakes — Must Know

1. **Using this greedy approach without checking the coin system is canonical** — this is the single biggest trap in coin change problems.
2. Assuming any set of coins that includes `1` is automatically canonical — it is not (see the {1, 3, 4} example in topic 1).
3. Not handling the "not possible" case when the coins can't exactly make the target.

#### 8. Related Topics

1. `1` The Greedy Choice Property — the {1, 3, 4} counter-example lives here
2. `9` Why Greedy Fails — 0/1 Knapsack & General Coin Change — the non-canonical case
3. `5` Dynamic Programming (its own folder) — the general, always-correct solution

#### 9. Interview Must Remember

1. Greedy coin change is only correct for **canonical** coin systems — real currency, not an arbitrary coin list.
2. If the interviewer gives you an unusual coin set, assume it's **not** canonical unless you can prove otherwise — reach for DP.
3. "Take the biggest coin that fits, repeat" is the whole algorithm — the hard part is knowing when it's actually safe to use.
