# Difference Array

#### 1. What Is It?

A **difference array** makes many **range updates** cheap. Suppose you must "add `v` to every item from index `l` to `r`", and you must do it many times.

Instead of touching `r - l + 1` items each time, you change only **two** numbers in a helper array:

```text
diff[l]     += v        "from here, everything is v higher"
diff[r + 1] -= v        "from here, it goes back to normal"
```

At the end, a **prefix sum** of `diff` gives the final array.

It is the opposite of a prefix sum: the prefix sum turns **an array into running totals**, and the difference array turns **range updates into single-point changes**.

How to spot it: many updates of the form "add to a range", and you only need the final array (or the values after all updates). Examples: bookings, car pooling, range addition.

#### 2. How It Works

Array of 5 zeros. Updates: add 3 to `[1, 3]`, then add 2 to `[2, 4]`.

```text
diff = [0, 0, 0, 0, 0, 0]          (one extra slot for r + 1)

update 1: diff[1] += 3, diff[4] -= 3   →  [0, 3, 0, 0, -3, 0]
update 2: diff[2] += 2, diff[5] -= 2   →  [0, 3, 2, 0, -3, -2]

prefix sum of diff:
index 0: 0
index 1: 0 + 3 = 3
index 2: 3 + 2 = 5
index 3: 5 + 0 = 5
index 4: 5 - 3 = 2
final array = [0, 3, 5, 5, 2]
```

Check by hand: indexes 1–3 got +3, indexes 2–4 got +2 → `[0, 3, 5, 5, 2]` ✓.

#### 3. Brute Force vs Optimized

| | Brute force | Difference array |
|---|---|---|
| Idea | add `v` to every item in the range | change 2 numbers, rebuild once |
| `q` updates on length `n` | `O(q · n)` | `O(q + n)` |
| Space | `O(1)` extra | `O(n)` |

```kotlin
fun rangeAddBrute(n: Int, updates: Array<IntArray>): IntArray {
    val result = IntArray(n)
    for ((l, r, v) in updates) for (i in l..r) result[i] += v        // O(range) every time
    return result
}
```

#### 4. Kotlin Code

```kotlin
// Range additions: updates are [l, r, v]
fun applyUpdates(n: Int, updates: Array<IntArray>): IntArray {
    val diff = IntArray(n + 1)
    for ((l, r, v) in updates) {
        diff[l] += v
        diff[r + 1] -= v
    }
    val result = IntArray(n)
    var running = 0
    for (i in 0 until n) {
        running += diff[i]
        result[i] = running
    }
    return result
}

// Corporate Flight Bookings (LeetCode 1109): bookings are [first, last, seats], flights are 1..n
fun corpFlightBookings(bookings: Array<IntArray>, n: Int): IntArray {
    val diff = IntArray(n + 1)
    for ((first, last, seats) in bookings) {
        diff[first - 1] += seats                 // 1-based flights → 0-based index
        diff[last] -= seats
    }
    val answer = IntArray(n)
    var running = 0
    for (i in 0 until n) { running += diff[i]; answer[i] = running }
    return answer
}

// Car Pooling (LeetCode 1094): trips are [passengers, from, to]
fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
    val diff = IntArray(1002)
    for ((passengers, from, to) in trips) {
        diff[from] += passengers
        diff[to] -= passengers                    // they get off at `to`
    }
    var onBoard = 0
    for (change in diff) {
        onBoard += change
        if (onBoard > capacity) return false
    }
    return true
}
```

Checks: `applyUpdates(5, [[1,3,3],[2,4,2]])` → `[0,3,5,5,2]`. `corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)` → `[10,55,45,25,25]`. `carPooling([[2,1,5],[3,3,7]], 4)` → `false`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| `q` range updates + rebuild | `O(q + n)` | `O(n)` |
| One update | `O(1)` | — |

#### 6. Common Mistakes

1. **Forgetting the extra slot** for `r + 1` (index out of bounds when `r = n - 1`).
2. **Off-by-one with 1-based ranges** (flights, positions).
3. **Reading the array between updates.** The values are only correct after the prefix sum. If you need values in between, use a Fenwick tree.
4. **Mixing up the end index:** for "get off at `to`" subtract at `to`, not `to + 1`.
5. **`Int` overflow** with many large updates.

#### 7. Say This in the Interview

1. "Brute force updates every item in each range, which is `O(q · n)`. With a difference array each update is `O(1)`, and one prefix sum at the end gives the result in `O(n)`."
2. "I add `v` at `l` and subtract `v` at `r + 1`."

#### 8. Quick Check

1. To add 5 to indexes 2–4, which two cells of `diff` change?
2. What gives the final array?

<details>
<summary>Answers</summary>

1. `diff[2] += 5` and `diff[5] -= 5`.
2. The running sum (prefix sum) of `diff`.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1854 | [Maximum Population Year](https://leetcode.com/problems/maximum-population-year/) (Easy) | +1 at birth, −1 at death |
| 1109 | [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) (Medium) | range add |
| 1094 | [Car Pooling](https://leetcode.com/problems/car-pooling/) (Medium) | passengers on board |
| 370 | [Range Addition](https://leetcode.com/problems/range-addition/) (Medium, premium) | the base problem |
| 2381 | [Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/) (Medium) | range shifts on a string |
