# Advanced Monotonic Queue Patterns

#### 1. Definition — Must Know

1. The basic monotonic queue finds the **max or min of a sliding window** (`Monotonic Queue` note).
2. The **advanced** patterns use the same deque to speed up:
   - **two limits at once** (window max *and* min),
   - **dynamic programming** that needs the best earlier value in a window,
   - **prefix sums** with a "shortest subarray" rule, where the window size is not fixed.
3. The rule stays the same: keep only the candidates that can still become the answer, in sorted order.

#### 2. Why It Is Used — Must Know

1. These problems have a nested loop solution (`O(n²)` or `O(n · k)`) that times out. A monotonic deque makes them `O(n)`.
2. They are common medium–hard interview problems.
3. Seeing the "best earlier value in a window" shape is the main skill.

#### 3. How It Works — Must Know

**Pattern A — two deques.** *Longest Continuous Subarray With Absolute Diff ≤ Limit* (LeetCode 1438): the window is valid when `max - min <= limit`.

```text
nums = [8, 2, 4, 7], limit = 4

maxDeque (decreasing) and minDeque (increasing) track the window's max and min.

right=0 [8]          max 8, min 8, diff 0           length 1
right=1 [8,2]        max 8, min 2, diff 6 > 4 → move left: [2]   length 1
right=2 [2,4]        max 4, min 2, diff 2           length 2
right=3 [2,4,7]      max 7, min 2, diff 5 > 4 → move left: [4,7] diff 3   length 2

answer 2
```

**Pattern B — DP with a window max.** *Jump Game VI* (LeetCode 1696): from index `i` you can jump to `i + 1 … i + k`. Maximise the total score.

```text
dp[i] = nums[i] + max(dp[i-k], …, dp[i-1])
The inner max is a sliding window maximum over dp → keep a decreasing deque of indexes.
```

**Pattern C — prefix sums, variable window.** *Shortest Subarray with Sum at Least K* (LeetCode 862), numbers can be negative.

```text
prefix[j] - prefix[i] >= k   with the smallest j - i.
Keep a deque of indexes whose prefix sums are INCREASING.
- Front: while prefix[j] - prefix[front] >= k → record j - front, pop front (a later j can't be shorter).
- Back: while prefix[back] >= prefix[j] → pop back (j is later and has a smaller-or-equal prefix, so it is a better start).
```

#### 4. Core Concepts — Must Know

1. **Same machinery:** store indexes, pop the back while it is "worse", pop the front when it expires or is used up.
2. **Two deques** give window max and min together (one decreasing, one increasing).
3. **DP + deque:** when `dp[i]` depends on the best `dp` in the last `k` positions.
4. **Prefix sums + increasing deque:** a start that is *later* and has a *smaller or equal* prefix always beats an earlier, larger one.
5. **Popping from the front can mean "used up"**, not only "expired" (Pattern C).
6. **Why linear:** each index is pushed once and popped once.

| Pattern | Deque order | Pop front when | Pop back when |
|---|---|---|---|
| Window max | decreasing values | index leaves the window | back ≤ new value |
| Window min | increasing values | index leaves the window | back ≥ new value |
| DP window max (Jump Game VI) | decreasing `dp` | index `< i - k` | `dp[back] ≤ dp[i]` |
| Shortest subarray (862) | increasing prefix | `prefix[j] - prefix[front] ≥ K` | `prefix[back] ≥ prefix[j]` |

#### 5. Algorithm — Must Know

```text
Two deques (window valid while max - min <= limit):
for right in nums:
    push right into maxDeque (pop back while smaller) and minDeque (pop back while larger)
    while nums[maxDeque.first] - nums[minDeque.first] > limit:
        left++; pop fronts whose index < left
    best = max(best, right - left + 1)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Longest Continuous Subarray With Absolute Diff <= limit
fun longestSubarray(nums: IntArray, limit: Int): Int {
    val maxDeque = ArrayDeque<Int>()               // indexes, values decreasing
    val minDeque = ArrayDeque<Int>()               // indexes, values increasing
    var left = 0
    var best = 0

    for (right in nums.indices) {
        while (maxDeque.isNotEmpty() && nums[maxDeque.last()] <= nums[right]) maxDeque.removeLast()
        maxDeque.addLast(right)
        while (minDeque.isNotEmpty() && nums[minDeque.last()] >= nums[right]) minDeque.removeLast()
        minDeque.addLast(right)

        while (nums[maxDeque.first()] - nums[minDeque.first()] > limit) {
            left++
            if (maxDeque.first() < left) maxDeque.removeFirst()
            if (minDeque.first() < left) minDeque.removeFirst()
        }
        best = maxOf(best, right - left + 1)
    }
    return best
}

// Jump Game VI — DP with a sliding window maximum
fun maxResult(nums: IntArray, k: Int): Int {
    val n = nums.size
    val dp = IntArray(n)
    dp[0] = nums[0]
    val deque = ArrayDeque<Int>()                  // indexes, dp values decreasing
    deque.addLast(0)

    for (i in 1 until n) {
        while (deque.first() < i - k) deque.removeFirst()          // out of reach
        dp[i] = nums[i] + dp[deque.first()]                         // best earlier score
        while (deque.isNotEmpty() && dp[deque.last()] <= dp[i]) deque.removeLast()
        deque.addLast(i)
    }
    return dp[n - 1]
}

// Shortest Subarray with Sum at Least K (negative numbers allowed)
fun shortestSubarray(nums: IntArray, k: Int): Int {
    val n = nums.size
    val prefix = LongArray(n + 1)
    for (i in 0 until n) prefix[i + 1] = prefix[i] + nums[i]

    val deque = ArrayDeque<Int>()                  // indexes, prefix values increasing
    var best = Int.MAX_VALUE

    for (j in 0..n) {
        while (deque.isNotEmpty() && prefix[j] - prefix[deque.first()] >= k) {
            best = minOf(best, j - deque.removeFirst())            // this start is used up
        }
        while (deque.isNotEmpty() && prefix[deque.last()] >= prefix[j]) deque.removeLast()
        deque.addLast(j)
    }
    return if (best == Int.MAX_VALUE) -1 else best
}
```

Checks: `longestSubarray([8,2,4,7], 4)` → `2`. `longestSubarray([10,1,2,4,7,2], 5)` → `4`. `maxResult([1,-1,-2,4,-7,3], 2)` → `7`. `shortestSubarray([2,-1,2], 3)` → `3`. `shortestSubarray([1], 1)` → `1`.

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Longest subarray, abs diff ≤ limit | `O(n)` | `O(n)` |
| Jump Game VI | `O(n)` | `O(n)` |
| Shortest subarray, sum ≥ K | `O(n)` | `O(n)` |
| Brute force versions | `O(n²)` or `O(n · k)` | — |

Each index enters and leaves a deque once.

#### 8. Common Advanced Patterns — Must Know

1. **Longest Continuous Subarray With Absolute Diff ≤ Limit** (LeetCode 1438).
2. **Jump Game VI** (LeetCode 1696).
3. **Constrained Subsequence Sum** (LeetCode 1425) — `dp[i] = nums[i] + max(0, window max)`.
4. **Shortest Subarray with Sum at Least K** (LeetCode 862).
5. **Maximum Number of Robots Within Budget** (LeetCode 2398) — window max of costs plus a running sum.
6. **Sliding Window Maximum** (LeetCode 239) — the base case.
7. **Max Value of Equation** (LeetCode 1499) — window max of `y - x`.
8. **Sliding window with a heap instead:** use it when elements do not leave strictly oldest first.

#### 9. Edge Cases / Common Mistakes

1. Popping the front only once when several fronts expire. Use `while` if more than one can expire at a time (in 1438 one pop per deque is enough because `left` moves by one).
2. Storing values and not indexes.
3. Using the wrong comparison direction for max vs min.
4. In 862: forgetting that it needs **prefix sums** and `Long` for them.
5. In 862: not popping the front after recording a length (a later `j` can never give a shorter subarray for that start).
6. Treating 862 like a standard window. With negative numbers a normal sliding window fails.
7. Jump Game VI: the deque may be accessed when empty if you pop too much. The previous index is always valid, so it is never empty at `first()`.
8. Using `<` vs `<=` when popping the back: both work for max/min, but be consistent.

#### 10. When to Use / When Not to Use

**Use when:**

1. The window rule depends on a max, min, or "best earlier value", and elements leave in order.
2. The window size is variable and the answer is a shortest/longest range.

**Avoid when:**

1. Elements leave in an arbitrary order (use a heap with lazy deletion).
2. You need a median or k-th value (two heaps or a balanced tree).

#### 11. Related Topics

1. Monotonic Queue
2. Deque
3. Heap + Sliding Window (`01-data-structure/08-Heap/24-Heap + Sliding Window.md`)
4. Dynamic Programming (`02-algorithm/05-Dynamic Programming`)
5. Prefix Sum (`03-leetcode-patterns`, topic 7)

#### 12. Interview Must Remember

1. **Same deque trick, more uses:** two deques (max + min), DP window max, prefix sums with an increasing deque.
2. Pop the back when a candidate is dominated. Pop the front when it expires or is used.
3. Every index enters and leaves once → `O(n)`.
4. Negative numbers + "at least K" → prefix sums + monotonic deque, not a plain window.
