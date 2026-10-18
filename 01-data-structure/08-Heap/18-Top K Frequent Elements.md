# Top K Frequent Elements

#### 1. Definition — Must Know

1. Given an array, return the `k` values that appear **most often**.
2. It is *Top K Frequent Elements* (LeetCode 347). If a number and a title ever disagree, trust the title.
3. It uses two steps:
   - **Count** how often each value appears (a `HashMap`).
   - **Pick the top `k` counts** (a heap of size `k`).

#### 2. Why It Is Used — Must Know

1. It is the standard example that combines a `HashMap` with a heap.
2. It shows that the heap compares a **count**, not the value itself.
3. It extends to words, search queries, and error codes in logs.

#### 3. How It Works — Must Know

Array `[1, 1, 1, 2, 2, 3]`, `k = 2`.

```text
Step 1: count            {1: 3, 2: 2, 3: 1}

Step 2: keep a min-heap of size 2, ordered by count
        add (1, count 3)                  heap: (1:3)
        add (2, count 2)                  heap: (2:2) (1:3)
        add (3, count 1) → size 3 > 2 → remove the smallest count (3:1)
                                          heap: (2:2) (1:3)

Answer: [1, 2]
```

The root of the min-heap is the least frequent of the `k` kept values, so it is the one to drop.

#### 4. Core Concepts — Must Know

1. **Count first.** The heap works on distinct values (at most `m` of them).
2. **Min-heap of size `k`**, ordered by count. This is Top K with "frequency" as the key.
3. The answer can be returned in any order (unless the problem says otherwise).
4. Three ways to solve it:

| Method | Time | Space |
|---|---:|---:|
| Sort the distinct values by count | `O(m log m)` | `O(m)` |
| **Heap of size `k`** | **`O(n + m log k)`** | `O(m)` |
| **Bucket sort** by frequency | `O(n)` | `O(n)` |

`n` = number of items, `m` = number of distinct values.

#### 5. Algorithm — Must Know

```text
count = map from value to number of occurrences
heap = min-heap ordered by count
for each (value, count) in the map:
    heap.add((value, count))
    if heap.size > k: heap.poll()
return the values in the heap
```

#### 6. Kotlin Implementation — Must Know

**Heap**

```kotlin
import java.util.PriorityQueue

fun topKFrequent(nums: IntArray, k: Int): IntArray {
    val freq = HashMap<Int, Int>()
    for (n in nums) freq[n] = (freq[n] ?: 0) + 1

    val heap = PriorityQueue<Map.Entry<Int, Int>>(compareBy<Map.Entry<Int, Int>> { it.value })
    for (entry in freq.entries) {
        heap.add(entry)
        if (heap.size > k) heap.poll()
    }
    return IntArray(heap.size) { heap.poll().key }
}
```

**Bucket sort (`O(n)`)**

```kotlin
fun topKFrequentBucket(nums: IntArray, k: Int): IntArray {
    val freq = HashMap<Int, Int>()
    for (n in nums) freq[n] = (freq[n] ?: 0) + 1

    // buckets[c] holds the values that appear exactly c times
    val buckets = Array(nums.size + 1) { mutableListOf<Int>() }
    for ((value, count) in freq) buckets[count].add(value)

    val result = mutableListOf<Int>()
    for (count in buckets.indices.reversed()) {
        for (value in buckets[count]) {
            result.add(value)
            if (result.size == k) return result.toIntArray()
        }
    }
    return result.toIntArray()
}
```

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Counting | `O(n)` | `O(m)` |
| Heap selection | `O(m log k)` | `O(k)` extra |
| **Total (heap)** | **`O(n + m log k)`** | `O(m)` |
| Total (bucket) | `O(n)` | `O(n)` |

#### 8. Common Variations — Must Know

1. **Top K Frequent Words** (LeetCode 692) — ties are broken alphabetically. The weakest item has the lower count, or the same count and the larger word:

```kotlin
val heap = PriorityQueue<Map.Entry<String, Int>>(
    compareBy<Map.Entry<String, Int>> { it.value }.thenByDescending { it.key }
)
// after selecting, reverse the polled order so the most frequent word comes first
```

2. **Sort Characters by Frequency** (LeetCode 451) — a max-heap, or buckets.
3. **K Most Frequent in a Stream** — keep the map and update the heap with lazy deletion (see "Lazy Deletion with Heap").
4. **Least frequent** — flip the comparison.

#### 9. Edge Cases / Common Mistakes

1. Putting every value in a heap ordered by count without limiting it to `k`. That is `O(m log m)`.
2. Using a max-heap of size `k`. It keeps the wrong end.
3. Comparing the **value** instead of the **count**.
4. Ties at the boundary. The problem says whether the answer is unique; read it carefully.
5. `k` larger than the number of distinct values.
6. Building the map with `map[n]++`. In Kotlin, `HashMap<Int, Int>` has no default, so use `(freq[n] ?: 0) + 1` or `getOrDefault`.
7. Modifying `freq` while holding its `entries` in the heap.

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. `k` is small compared to the number of distinct values.
2. Data may arrive as a stream.

**Use bucket sort when:**

1. You want `O(n)` time and `n` is not huge.

**Use sorting when:**

1. The input is small and clarity matters most.

#### 11. Related Topics

1. Top K Elements Pattern
2. Heap + HashMap Pattern
3. HashMap (`01-data-structure/05-HashMap`)
4. Bucket Sort (`02-algorithm/01-sorting/09-Bucket Sort.md`)

#### 12. Interview Must Remember

1. **Count with a `HashMap`, then keep a min-heap of size `k` by count.**
2. `O(n + m log k)` time. Bucket sort reaches `O(n)`.
3. The heap compares **counts**.
4. State your tie-breaking rule.
