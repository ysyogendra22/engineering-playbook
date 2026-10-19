# Mapping / Index Tracking

#### 1. Definition — Must Know

1. **Index tracking** stores **where** each value was seen: `value → index`.
2. You can keep the **first** index (store only if missing) or the **last** index (always overwrite).
3. It lets you jump from a value to its position in `O(1)`, instead of searching the array.

#### 2. Why It Is Used — Must Know

1. Many problems depend on **distance** or **position**: "within `k` positions", "longest gap", "next greater".
2. It replaces a second loop that searches for a value.
3. It is the base of Two Sum, Contains Duplicate II, and "longest subarray with a property".

#### 3. How It Works — Must Know

*Contains Duplicate II* (LeetCode 219): are there two equal numbers at most `k` positions apart?

`nums = [1, 2, 3, 1]`, `k = 3`

```text
last = {}                                 value → last index
i=0  x=1   not in last          → last[1]=0
i=1  x=2   not in last          → last[2]=1
i=2  x=3   not in last          → last[3]=2
i=3  x=1   last[1]=0, distance 3-0=3 ≤ 3 → TRUE
```

If the distance were too big, store the **new** index (`last[x] = i`) and continue. The latest index is always the closest one for the next match.

#### 4. Core Concepts — Must Know

1. **First occurrence:** `map.putIfAbsent(x, i)`. Used for the **longest** range between equal states.
2. **Last occurrence:** `map[x] = i`. Used for the **shortest** distance to an earlier equal item.
3. **Use the stored index** to compute a distance (`i - j`) or to return a position.
4. **Map a value to an object** (not only an index) when more data is needed.
5. **Rank / position maps:** `value → its position in a sorted copy` (coordinate compression).
6. **Index of array B inside array A:** a map from `A[i]` to `i` replaces searching.

| Goal | Store |
|---|---|
| Longest range between equal states | first index |
| Shortest distance to an earlier equal item | last index |
| Position of a value | its index |
| Value → count and index | an object or two maps |

#### 5. Algorithm — Must Know

```text
index = empty map
for i, x in array:
    if x in index: use index[x] (distance / position)
    index[x] = i          // or keep the first: store only if missing
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Contains Duplicate II — keep the LAST index
fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    val last = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) {
        val j = last[x]
        if (j != null && i - j <= k) return true
        last[x] = i
    }
    return false
}

// Next Greater Element I — map each value to its next greater value
fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
    val nextGreater = HashMap<Int, Int>()
    val stack = ArrayDeque<Int>()
    for (n in nums2) {
        while (stack.isNotEmpty() && stack.last() < n) {
            nextGreater[stack.removeLast()] = n
        }
        stack.addLast(n)
    }
    return IntArray(nums1.size) { nextGreater[nums1[it]] ?: -1 }
}

// Position lookup: where is each number in the array?
fun indexMap(nums: IntArray): Map<Int, Int> =
    nums.withIndex().associate { (i, x) -> x to i }     // the last index wins for repeats

// Keep the FIRST index of each value
fun firstIndexMap(nums: IntArray): Map<Int, Int> {
    val first = HashMap<Int, Int>()
    for ((i, x) in nums.withIndex()) first.putIfAbsent(x, i)
    return first
}

// Rank of each value (coordinate compression)
fun ranks(nums: IntArray): Map<Int, Int> {
    val sorted = nums.distinct().sorted()
    return sorted.withIndex().associate { (rank, x) -> x to rank }
}
```

Check: `nextGreaterElement([4,1,2], [1,3,4,2])` → `[-1, 3, -1]`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| One pass with an index map | `O(n)` | `O(u)` |
| Next Greater Element (stack + map) | `O(n + m)` | `O(m)` |
| Coordinate compression (sort) | `O(n log n)` | `O(n)` |

#### 8. Common Index-Tracking Patterns — Must Know

1. **Two Sum** — `value → index`.
2. **Contains Duplicate II** (LeetCode 219) — last index.
3. **Next Greater Element I** (LeetCode 496) — value → next greater.
4. **Longest Substring Without Repeating Characters** — last index lets `left` jump (see HashMap + Sliding Window).
5. **Subarray problems with first-index maps** — longest subarray with a given sum (see Subarray Sum Patterns).
6. **Shortest Word Distance** (LeetCode 243, premium) — track the latest index of each word.
7. **Index Mapping in lists** — id → position in an adapter list (Android).

#### 9. Edge Cases / Common Mistakes

1. Using `put` when you want the first index, which overwrites it. Use `putIfAbsent`.
2. Using `putIfAbsent` when you want the last index.
3. Not checking `null` before using the index.
4. Off-by-one in the distance (`i - j` vs `i - j - 1`).
5. `associate` over duplicates silently keeps the last index.
6. Storing indices from one array and using them on a different array.
7. Storing the index of a list that you later modify (inserts shift indices).

#### 10. When to Use / When Not to Use

**Use when:**

1. The answer needs positions or distances between equal values.

**Avoid when:**

1. Only existence matters. Use a set.
2. The array is sorted and a binary search is enough.

#### 11. Related Topics

1. Two Sum Pattern
2. Subarray Sum Patterns
3. HashMap + Two Pointers / Sliding Window
4. Monotonic Stack (`03-leetcode-patterns`, topic 10)

#### 12. Interview Must Remember

1. **First index → `putIfAbsent`. Last index → `map[x] = i`.**
2. Longest range → first index. Closest repeat → last index.
3. Always check for `null` before using a stored index.
4. `value → index` turns searching into a lookup.
