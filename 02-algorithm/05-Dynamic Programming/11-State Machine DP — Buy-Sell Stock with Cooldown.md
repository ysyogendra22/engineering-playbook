# State Machine DP — Buy/Sell Stock with Cooldown

#### 1. Definition — Must Know

**State machine DP** adds an extra dimension to the state: not just "where am I" (like a day index), but "which **mode** am I in" (holding a stock, not holding one, in a cooldown period). The recurrence becomes transitions between these modes.

#### 2. Why It Is Used — Must Know

1. Stock-trading problems (buy once, buy and sell multiple times, with a cooldown, with a transaction fee) are a very common DP family, and they're all solved by defining a small state machine of 2-3 modes.
2. It's a useful bridge between simple 1D DP and more complex, multi-condition DP problems.

#### 3. How It Works — Must Know

Buy/Sell Stock with Cooldown: after selling, you must wait one day before buying again.

```text
Three states per day, each holding the best profit so far:

hold[i]    = best profit on day i, currently HOLDING a stock
sold[i]    = best profit on day i, just SOLD today
rest[i]    = best profit on day i, not holding, and not just sold (free to buy)

Transitions:
hold[i] = max(hold[i-1],           # kept holding
              rest[i-1] - price[i]) # bought today, coming from "rest" (not cooldown)

sold[i] = hold[i-1] + price[i]      # sold today, must have been holding yesterday

rest[i] = max(rest[i-1],            # stayed resting
              sold[i-1])            # cooldown day is over
```

Drawing the three states as a small diagram makes the transitions clear:

```text
   ┌────────┐  buy   ┌────────┐  sell  ┌────────┐
   │  rest  │ ─────→ │  hold  │ ─────→ │  sold  │
   └────────┘        └────────┘        └────────┘
        ↑                                   │
        └──────────── (one cooldown day) ───┘
```

#### 4. Algorithm — Must Know

```text
1. Identify the distinct MODES the problem can be in (here: hold, sold, rest).
2. Draw the allowed transitions between modes as a small diagram.
3. Define dp[mode][day] = best value while in that mode on that day.
4. Write one recurrence line per mode, based on which modes can transition into it.
5. The final answer is the best value across modes that don't require holding
   a stock at the end (you can't count unsold stock as profit).
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun maxProfitWithCooldown(prices: IntArray): Int {
    if (prices.isEmpty()) return 0
    var hold = -prices[0]
    var sold = 0
    var rest = 0
    for (i in 1 until prices.size) {
        val prevHold = hold
        val prevSold = sold
        val prevRest = rest
        hold = maxOf(prevHold, prevRest - prices[i])
        sold = prevHold + prices[i]
        rest = maxOf(prevRest, prevSold)
    }
    return maxOf(sold, rest)   // never holding a stock at the very end
}
```

#### 6. Complexity — Must Know

| | Time | Space |
|---|---|---|
| Any fixed number of states | O(n × number of states) | O(number of states), easily space-optimised |

With a small, fixed number of states (2 or 3), this is effectively O(n) time and O(1) space.

#### 7. Common Mistakes — Must Know

1. Forgetting a state (for example, missing the "rest" / cooldown state and only tracking "hold" and "sold") — the cooldown rule can't be enforced without it.
2. Reading the *updated* value of another state within the same day's transitions, instead of the *previous* day's value — save all previous values before overwriting them (as `prevHold`, `prevSold`, `prevRest` above).
3. Forgetting that the final answer must come from a state where you're **not** holding a stock — unsold stock isn't realised profit.

#### 8. Related Topics

1. `4` 1D DP — Fibonacci, Climbing Stairs, House Robber — the simpler, single-state version of this idea
2. `3` The Four Steps — State, Recurrence, Base Case, Fill Order — still applies, just with a mode added to the state
3. `LC 18` Dynamic Programming (in `03-leetcode-patterns`) — more DP practice problems

#### 9. Interview Must Remember

1. When a problem has **rules about what you can do next** (must cooldown, limited transactions, can't do X right after Y), draw a small state diagram first.
2. Each mode gets its own `dp[mode][i]`, and the recurrence for each mode says which modes can transition into it.
3. Watch for reading updated-this-round values by accident — save the previous round's values first.
