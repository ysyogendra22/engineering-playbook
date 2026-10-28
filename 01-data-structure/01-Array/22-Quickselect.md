# Quickselect

> The standard answer to "find the k-th largest/smallest element" when the interviewer wants better than sorting.

#### 1. What Is It?

**Quickselect** finds the **k-th smallest (or largest) element** without sorting the whole array. It uses the same **partition** step as quicksort, but it follows only **one** side.

**Partition:** pick a pivot. Move everything smaller than the pivot to its left and everything bigger to its right. The pivot then sits in its **final sorted position**.

```text
after partition: [ smaller... | pivot | ...bigger ]
                               ↑ final position p
```

- If `p` is the index you want → done.
- If `p` is too small → search the right part only.
- If `p` is too big → search the left part only.

Because it follows only one side, the average work is `n + n/2 + n/4 + ... = O(n)`.

How to spot it: "k-th largest/smallest", "top k elements (unordered is fine)", "median", and you want `O(n)` average.

#### 2. How It Works

Find the 2nd largest in `[3, 2, 1, 5, 6, 4]`. That is index `n - k = 4` in sorted order (`[1,2,3,4,5,6]`).

```text
partition around pivot 4 (the last item): [3, 2, 1, 4, 6, 5]    pivot lands at index 3
   index 3 < target 4 → search the right part [6, 5] (indexes 4..5)
partition around pivot 5:                [5, 6]               pivot lands at index 4
   index 4 == target 4 → answer is 5
```

Compare the ways to get the k-th largest:

| Way | Time | Space | Note |
|---|---|---|---|
| Sort | `O(n log n)` | `O(1)` | simplest |
| Min-heap of size `k` | `O(n log k)` | `O(k)` | works on streams |
| **Quickselect** | `O(n)` average, `O(n²)` worst | `O(1)` | changes the array |

The worst case happens with bad pivots (an already sorted array and a fixed pivot). A **random pivot** makes it very unlikely.

#### 3. Brute Force vs Optimized

| | Brute force | Quickselect |
|---|---|---|
| Idea | sort everything, take index `n - k` | partition, follow one side |
| Time | `O(n log n)` | `O(n)` average |
| Space | `O(1)` | `O(1)` |

```kotlin
fun findKthLargestSort(nums: IntArray, k: Int): Int {
    nums.sort()
    return nums[nums.size - k]
}
```

#### 4. Kotlin Code

```kotlin
import kotlin.random.Random

// Kth Largest Element in an Array (LeetCode 215)
fun findKthLargest(nums: IntArray, k: Int): Int {
    val target = nums.size - k                       // index in the sorted array
    var lo = 0
    var hi = nums.size - 1
    while (lo <= hi) {
        val p = partition(nums, lo, hi)
        when {
            p == target -> return nums[p]
            p < target -> lo = p + 1
            else -> hi = p - 1
        }
    }
    return -1
}

// Lomuto partition with a random pivot. Returns the final index of the pivot.
private fun partition(nums: IntArray, lo: Int, hi: Int): Int {
    val randomIndex = Random.nextInt(lo, hi + 1)
    swap(nums, randomIndex, hi)                       // move the pivot to the end
    val pivot = nums[hi]
    var i = lo                                        // everything before i is smaller than the pivot
    for (j in lo until hi) {
        if (nums[j] < pivot) { swap(nums, i, j); i++ }
    }
    swap(nums, i, hi)                                 // put the pivot in its final place
    return i
}

private fun swap(a: IntArray, i: Int, j: Int) { val t = a[i]; a[i] = a[j]; a[j] = t }

// With a heap (works for streams and does not change the array)
fun findKthLargestHeap(nums: IntArray, k: Int): Int {
    val heap = java.util.PriorityQueue<Int>()         // min-heap
    for (x in nums) {
        heap.add(x)
        if (heap.size > k) heap.poll()                // keep only the k largest
    }
    return heap.peek()
}
```

Checks: `findKthLargest([3,2,1,5,6,4], 2)` → `5`. `findKthLargest([3,2,3,1,2,4,5,5,6], 4)` → `4`. The heap version gives the same answers.

K Closest Points to Origin (LeetCode 973) uses the same idea: partition by distance and stop when the pivot lands at index `k`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Quickselect | `O(n)` average, `O(n²)` worst | `O(1)` |
| Heap of size `k` | `O(n log k)` | `O(k)` |
| Sort | `O(n log n)` | `O(1)` |

#### 6. Common Mistakes

1. **Mixing "k-th largest" and "k-th smallest".** For the k-th largest the target index is `n - k`.
2. **Searching both sides** (that is quicksort). Follow only one side.
3. **Many equal values** with Lomuto partition can slow it down. A 3-way partition (note 20) helps.
4. **Always using the first or last item as the pivot** on sorted input, which gives `O(n²)`. Use a random pivot.
5. **Changing the array** when the question says not to. Use the heap.
6. **Off-by-one in the loop bounds.**

#### 7. Say This in the Interview

1. "Sorting is `O(n log n)`. A min-heap of size `k` is `O(n log k)`. Quickselect is `O(n)` on average because it partitions and follows only one side."
2. "I use a random pivot to avoid the `O(n²)` worst case."
3. "Quickselect changes the array. If I must not change it, I use the heap."

#### 8. Quick Check

1. What is the target index for the 3rd largest in an array of 10 numbers?
2. After partition, where is the pivot?

<details>
<summary>Answers</summary>

1. `10 - 3 = 7`.
2. In its final sorted position.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (Easy) | min-heap of size `k` |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) | quickselect |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) | partition by distance |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) | counts + heap or quickselect |
| 324 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) (Medium) | median with quickselect |
