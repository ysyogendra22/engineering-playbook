# Fractional Knapsack

#### 1. Definition — Must Know

1. You have a knapsack with a weight limit, and a set of items, each with a weight and a value. You may take **any fraction** of an item (not just whole items).
2. Goal: fill the knapsack to maximise total value.

#### 2. Why It Is Used — Must Know

1. It's the one classic knapsack variant that greedy actually solves correctly — because you can take fractions, there's no "do I include this whole item or not" decision to get stuck on.
2. It's a useful contrast to **0/1 Knapsack** (topic 9), where greedy fails and Dynamic Programming is needed instead.

#### 3. How It Works — Must Know

```text
Capacity = 50
Items (value, weight): (60, 10) (100, 20) (120, 30)

Value per unit weight: 60/10 = 6, 100/20 = 5, 120/30 = 4

Sort by value per weight, descending: (60,10) (100,20) (120,30)

Take item 1 fully:  weight used 10/50, value 60
Take item 2 fully:  weight used 30/50, value 160
Item 3 remaining capacity = 20, item weighs 30 → take 20/30 of it:
   value added = 120 * (20/30) = 80

Total value = 60 + 100 + 80 = 240
```

#### 4. Algorithm — Must Know

```text
sort items by (value / weight), descending
remainingCapacity = capacity
totalValue = 0
for each item in sorted order:
    if item.weight <= remainingCapacity:
        take it fully
        totalValue += item.value
        remainingCapacity -= item.weight
    else:
        take the fraction that fits
        totalValue += item.value * (remainingCapacity / item.weight)
        remainingCapacity = 0
        break
return totalValue
```

#### 5. Kotlin Implementation — Must Know

```kotlin
data class Item(val value: Double, val weight: Double)

fun fractionalKnapsack(capacity: Double, items: List<Item>): Double {
    val sorted = items.sortedByDescending { it.value / it.weight }
    var remaining = capacity
    var totalValue = 0.0
    for (item in sorted) {
        if (remaining <= 0) break
        if (item.weight <= remaining) {
            totalValue += item.value
            remaining -= item.weight
        } else {
            totalValue += item.value * (remaining / item.weight)
            remaining = 0.0
        }
    }
    return totalValue
}
```

#### 6. Complexity — Must Know

| Step | Cost |
|---|---|
| Sort by value/weight | O(n log n) |
| Single pass | O(n) |
| Total | O(n log n) |

#### 7. Common Mistakes — Must Know

1. Sorting by value alone, or by weight alone, instead of the **ratio** value/weight.
2. Applying this same greedy approach to **0/1 Knapsack** (where items can't be split) — it gives a wrong answer there (topic 9).
3. Forgetting to stop once the capacity is fully used.

#### 8. Related Topics

1. `1` The Greedy Choice Property — why fractions make this one solvable greedily
2. `9` Why Greedy Fails — 0/1 Knapsack & General Coin Change — the version where this approach breaks
3. `5` Dynamic Programming (its own folder) — the correct approach for 0/1 Knapsack

#### 9. Interview Must Remember

1. Sort by **value per unit weight**, take greedily until the capacity runs out, and take a fraction of the last item if needed.
2. This greedy approach is correct **only** because fractional items are allowed — say this explicitly, it's the key distinction interviewers check for.
3. If the problem says "you can't split items", you're no longer solving Fractional Knapsack — you need DP (topic 9).
