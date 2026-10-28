# Binary Search on Answer

> A very common Medium pattern: "find the minimum/maximum value that works". You binary search the **answer**, not the array.

#### 1. What Is It?

Sometimes the array is **not sorted**, but the **answer** lives in a range of numbers, and the answers have a **yes/no pattern**:

```text
answer:     1   2   3   4   5   6   7   8
works?      no  no  no  YES YES YES YES YES        ← once it works, bigger values also work
```

If you can write a function `canDo(x)` that says whether `x` is enough, then the smallest `x` where `canDo(x)` is true can be found by **binary search over the possible answers**.

How to spot it:

- "Minimise the maximum" or "maximise the minimum" (split an array, ship packages, eat bananas).
- "The smallest speed / capacity / time such that it can be done".
- You can easily **check** one answer, but finding the best one directly is hard.

The steps:

```text
1. Decide the range of answers: lo (smallest possible) to hi (largest possible).
2. Write canDo(mid): is this answer enough?
3. Binary search: if canDo(mid) → try smaller (hi = mid); else try bigger (lo = mid + 1).
```

#### 2. How It Works

*Koko Eating Bananas* (LeetCode 875): piles of bananas, `h` hours. Find the **smallest eating speed** `k` (bananas per hour) so Koko finishes in `h` hours. Each hour she eats from one pile only.

`piles = [3, 6, 7, 11]`, `h = 8`

```text
Range for k: 1 .. 11 (the biggest pile).
canDo(k) = total hours = sum of ceil(pile / k) <= h

k = 6: hours = 1 + 1 + 2 + 2 = 6 ≤ 8  → works, try smaller
k = 3: hours = 1 + 2 + 3 + 4 = 10 > 8 → too slow, try bigger
k = 4: hours = 1 + 2 + 2 + 3 = 8 ≤ 8  → works
k = 3 failed, so the answer is 4
```

Binary search finds it in about `log(max pile)` checks instead of trying every speed.

#### 3. Brute Force vs Optimized

| | Brute force | Binary search on the answer |
|---|---|---|
| Idea | try every possible answer from `lo` up | binary search the answer range |
| Time | `O(range × check)` | `O(log(range) × check)` |
| Space | `O(1)` | `O(1)` |

```kotlin
fun minEatingSpeedBrute(piles: IntArray, h: Int): Int {
    var speed = 1
    while (true) {
        var hours = 0L
        for (p in piles) hours += (p + speed - 1) / speed          // ceil(p / speed)
        if (hours <= h) return speed
        speed++
    }
}
```

#### 4. Kotlin Code

```kotlin
// Koko Eating Bananas (LeetCode 875)
fun minEatingSpeed(piles: IntArray, h: Int): Int {
    var lo = 1
    var hi = 0
    for (p in piles) hi = maxOf(hi, p)
    while (lo < hi) {
        val mid = lo + (hi - lo) / 2
        var hours = 0L
        for (p in piles) hours += (p + mid - 1) / mid               // ceil(p / mid)
        if (hours <= h) hi = mid else lo = mid + 1                  // works → try smaller
    }
    return lo
}

// Capacity To Ship Packages Within D Days (LeetCode 1011)
fun shipWithinDays(weights: IntArray, days: Int): Int {
    var lo = 0                                                      // at least the heaviest package
    var hi = 0                                                      // at most the total weight
    for (w in weights) { lo = maxOf(lo, w); hi += w }
    while (lo < hi) {
        val mid = lo + (hi - lo) / 2
        var needed = 1
        var load = 0
        for (w in weights) {
            if (load + w > mid) { needed++; load = 0 }              // start a new day
            load += w
        }
        if (needed <= days) hi = mid else lo = mid + 1
    }
    return lo
}

// Sqrt(x) (LeetCode 69): the biggest m with m * m <= x
fun mySqrt(x: Int): Int {
    var lo = 0
    var hi = x
    var answer = 0
    while (lo <= hi) {
        val mid = lo + (hi - lo) / 2
        if (mid.toLong() * mid <= x) { answer = mid; lo = mid + 1 } else hi = mid - 1
    }
    return answer
}

// First Bad Version (LeetCode 278) uses the same shape: isBad(v) is false...false true...true
fun firstBadVersion(n: Int, isBadVersion: (Int) -> Boolean): Int {
    var lo = 1
    var hi = n
    while (lo < hi) {
        val mid = lo + (hi - lo) / 2
        if (isBadVersion(mid)) hi = mid else lo = mid + 1
    }
    return lo
}
```

Checks: `minEatingSpeed([3,6,7,11], 8)` → `4`. `shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)` → `15`. `mySqrt(8)` → `2`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Binary search on the answer | `O(n · log(range))` (`n` for the check) | `O(1)` |

#### 6. Common Mistakes

1. **Wrong range.** `lo` must be the smallest *possible* answer (for shipping: the heaviest package) and `hi` the largest.
2. **Using it when there is no yes/no pattern** (the check is not monotonic).
3. **Wrong update for "minimise":** if `canDo(mid)` is true, use `hi = mid` (not `mid - 1`).
4. **Infinite loop** from mixing `lo <= hi` with `hi = mid`.
5. **Overflow** in the check (hours or loads). Use `Long`.
6. **A slow `canDo`.** It is called about `log(range)` times, so it should be `O(n)`.

#### 7. Say This in the Interview

1. "I can test one answer easily, and if an answer works then every bigger one works too. So I binary search the answer."
2. "The range is `lo..hi`, the check is `O(n)`, and I need about `log(range)` checks."
3. "Time `O(n log range)`, space `O(1)`."

#### 8. Quick Check

1. For "smallest speed that works", if `canDo(mid)` is true, which side do you keep?
2. Why can't you binary search an answer without a monotonic check?

<details>
<summary>Answers</summary>

1. The left side including `mid` (`hi = mid`).
2. If a bigger answer can fail while a smaller one works, one test does not tell you which half to discard.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy) | largest `m` with `m * m <= x` |
| 278 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) (Easy) | first true |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (Medium) | smallest speed |
| 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) (Medium) | smallest capacity |
| 1482 | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) (Medium) | smallest day |
| 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) (Hard) | minimise the largest sum |
