# Fractional Knapsack

#### 1. What Is It?

You have items, each with a **value** and a **weight**, and a bag with a weight limit. You may take **a fraction** of an item. Maximize the total value.

```text
items (value, weight): (60, 10), (100, 20), (120, 30)    capacity = 50
```

Because you can split items, greedy is **correct**. If you cannot split them (0/1 knapsack), greedy fails and you need DP (note 09).

#### 2. How It Works

**Rule: take items with the highest value per weight first.**

1. Compute `value / weight` for every item.
2. Sort by this ratio, highest first.
3. Take whole items while they fit. Take a fraction of the next one to fill the bag.

```text
ratios: 60/10 = 6,  100/20 = 5,  120/30 = 4

take all of item 1:   weight 10, value  60   (capacity left 40)
take all of item 2:   weight 20, value 100   (capacity left 20)
take 20/30 of item 3: value 120 × 20/30 = 80 (capacity left 0)

total = 60 + 100 + 80 = 240
```

Why it works: every unit of weight should carry as much value as possible. A unit used on a lower ratio item could always be swapped for a unit of a higher ratio item.

#### 3. Brute Force vs Optimized

A tempting wrong rule is **highest value first**. Compare:

```text
items (value, weight): (100, 50), (60, 10), (60, 10)    capacity = 50

highest value first: take 100 (weight 50) → total 100
best ratio first:    60 and 60 (weight 20), then 30/50 of the 100 item = 60 → total 180
```

```kotlin
class Item(val value: Int, val weight: Int)

fun fractionalByValue(items: List<Item>, capacity: Int): Double {     // WRONG rule
    var left = capacity.toDouble()
    var total = 0.0
    for (item in items.sortedByDescending { it.value }) {
        val take = minOf(left, item.weight.toDouble())
        total += item.value * (take / item.weight)
        left -= take
    }
    return total
}

fun fractionalKnapsack(items: List<Item>, capacity: Int): Double {   // RIGHT rule
    var left = capacity.toDouble()
    var total = 0.0
    for (item in items.sortedByDescending { it.value.toDouble() / it.weight }) {
        if (left <= 0) break
        val take = minOf(left, item.weight.toDouble())
        total += item.value * (take / item.weight)
        left -= take
    }
    return total
}
```

#### 4. Kotlin Code

The code is above. Checks:

```kotlin
val items = listOf(Item(60, 10), Item(100, 20), Item(120, 30))
println(fractionalKnapsack(items, 50))            // 240.0

val tricky = listOf(Item(100, 50), Item(60, 10), Item(60, 10))
println(fractionalByValue(tricky, 50))            // 100.0   (wrong rule)
println(fractionalKnapsack(tricky, 50))           // 180.0   (right rule)
```

The **Maximum Units on a Truck** question (LeetCode 1710) is the same idea with whole boxes: sort box types by units per box (the "value") and take the biggest first. There each box has weight 1, so no fractions are needed.

```kotlin
fun maximumUnits(boxTypes: Array<IntArray>, truckSize: Int): Int {   // [boxes, unitsPerBox]
    var left = truckSize
    var units = 0
    for (type in boxTypes.sortedByDescending { it[1] }) {
        val take = minOf(left, type[0])
        units += take * type[1]
        left -= take
        if (left == 0) break
    }
    return units
}
```

Check: `maximumUnits([[1,3],[2,2],[3,1]], 4)` → `8` (1 box × 3 + 2 boxes × 2 + 1 box × 1).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Sort by ratio, one pass | `O(n log n)` | `O(1)` extra |
| Pick the best ratio without sorting (heap) | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Highest value first** instead of the highest ratio.
2. **Integer division** for the ratio (`60 / 10` is fine, `100 / 30` loses the decimals). Use `Double`.
3. **Using greedy on 0/1 knapsack.** It is wrong there.
4. **Not stopping** when the bag is full (negative capacity).
5. **Zero weight items** (divide by zero). Ask about the constraints.

#### 7. Say This in the Interview

1. "Items can be split, so I take the best value-per-weight first. `O(n log n)` for the sort."
2. "If items could not be split, greedy would fail and I would use DP."

#### 8. Quick Check

1. Is greedy correct for 0/1 knapsack?
2. What do you sort by?

<details>
<summary>Answers</summary>

1. No. It only works when items can be split.
2. `value / weight`, highest first.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1710 | [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) (Easy) | best units per box first |
| 2279 | [Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/) (Medium) | fill the nearly-full bags first |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy) | greedy matching |
| 2144 | [Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) (Easy) | sort, skip every third |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium) | 0/1 choice, DP |
