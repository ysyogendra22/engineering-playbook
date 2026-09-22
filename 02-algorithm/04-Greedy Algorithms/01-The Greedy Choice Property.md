# The Greedy Choice Property

#### 1. Definition — Must Know

1. A problem has the **greedy choice property** when making the locally best choice at each step, and never reconsidering it, still leads to the globally best answer.
2. This is the one thing you must check before trusting a greedy algorithm — most problems do **not** have this property.

#### 2. Why It Is Used — Must Know

1. When it applies, greedy is usually the simplest and fastest correct solution — often O(n log n) instead of exponential.
2. Recognising whether a problem has this property is what separates "I have a fast idea" from "I have a fast *correct* idea".

#### 3. How It Works — Must Know

Example that **has** the property — giving change with common coin denominations (1, 5, 10, 25):

```text
Make 41 cents:
Take the largest coin that fits: 25  → remaining 16
Take the largest coin that fits: 10  → remaining 6
Take the largest coin that fits: 5   → remaining 1
Take the largest coin that fits: 1   → remaining 0
Result: 25 + 10 + 5 + 1 = 4 coins, and this is optimal for this coin system.
```

Example that **does not** have the property — the same "take the biggest first" idea, with coins {1, 3, 4}, target 6:

```text
Greedy: take 4  → remaining 2 → take 1 → remaining 1 → take 1  = 4, 1, 1   (3 coins)
Better:         take 3 + 3                                     = 3, 3     (2 coins)
```

The locally best choice (take the biggest coin) does **not** lead to the best overall answer here — this coin system does not have the greedy choice property.

#### 4. Algorithm — Must Know

There's no single algorithm — this is a **check**, not a technique:

```text
1. Propose a greedy rule (for example, "always pick the biggest / earliest-ending / cheapest option").
2. Try to break it with a small counter-example by hand.
3. If you can't break it, try to justify it with an exchange argument (topic 3).
4. If you can break it, greedy is not the answer — consider Dynamic Programming (topic 5) instead.
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// Greedy coin change — correct ONLY for coin systems with the greedy choice property
// (like standard currency: 1, 5, 10, 25), not for arbitrary coin sets.
fun greedyCoinChange(coins: List<Int>, amount: Int): Int {
    var remaining = amount
    var count = 0
    for (coin in coins.sortedDescending()) {
        count += remaining / coin
        remaining %= coin
    }
    return if (remaining == 0) count else -1
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Typical greedy algorithm | O(n log n) for the sort, plus O(n) for a single pass |

The complexity is rarely the hard part of greedy — **correctness** is.

#### 7. Common Mistakes — Must Know

1. Assuming a greedy idea is correct just because it works on the example you tried.
2. Using greedy coin change on a coin system that isn't "canonical" (like {1, 3, 4}) — it silently gives a wrong, non-optimal answer.
3. Not testing a small, deliberately tricky counter-example before committing to a greedy solution in an interview.

#### 8. Related Topics

1. `2` Greedy + Sorting — the Usual Pairing
2. `3` Proving Correctness with an Exchange Argument
3. `9` Why Greedy Fails — 0/1 Knapsack & General Coin Change
4. `5` Dynamic Programming (its own folder) — the fallback when greedy doesn't apply

#### 9. Interview Must Remember

1. Greedy is only correct when the problem has the **greedy choice property** — say this out loud, don't assume it.
2. Try to break your own greedy idea with a small counter-example before presenting it as the answer.
3. "Take the biggest / earliest / cheapest" is a common greedy *shape*, but it needs to be justified for the specific problem, every time.
