# Divide and Conquer — Split, Solve, Combine

#### 1. Definition — Must Know

1. **Divide and conquer** solves a problem by splitting it into smaller pieces of the same problem, solving each piece recursively, and combining their results.
2. Three steps, always: **divide**, **conquer** (recurse), **combine**.

#### 2. Why It Is Used — Must Know

1. Many problems shrink cleanly into smaller versions of themselves, and solving the small versions is easier than solving the whole thing at once.
2. It is the technique behind some of the most important algorithms: Merge Sort, Quick Sort, Binary Search.

#### 3. How It Works — Must Know

Example: Merge Sort on `[5, 2, 4, 1]`.

```text
Divide:
[5, 2, 4, 1]  →  [5, 2]  and  [4, 1]
[5, 2]        →  [5]     and  [2]
[4, 1]        →  [4]     and  [1]

Conquer (base case — one element is already sorted):
[5], [2], [4], [1]

Combine (merge sorted halves back together):
[5] + [2]  →  [2, 5]
[4] + [1]  →  [1, 4]
[2, 5] + [1, 4]  →  [1, 2, 4, 5]
```

#### 4. Algorithm — Must Know

```text
function solve(problem):
    if problem is small enough:
        return the direct answer          # base case
    left, right = split problem in half   # divide
    leftAnswer = solve(left)              # conquer
    rightAnswer = solve(right)            # conquer
    return combine(leftAnswer, rightAnswer)  # combine
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun mergeSort(arr: IntArray): IntArray {
    if (arr.size <= 1) return arr                    // base case
    val mid = arr.size / 2
    val left = mergeSort(arr.copyOfRange(0, mid))     // divide + conquer
    val right = mergeSort(arr.copyOfRange(mid, arr.size))
    return merge(left, right)                         // combine
}

fun merge(left: IntArray, right: IntArray): IntArray {
    val result = IntArray(left.size + right.size)
    var i = 0; var j = 0; var k = 0
    while (i < left.size && j < right.size) {
        result[k++] = if (left[i] <= right[j]) left[i++] else right[j++]
    }
    while (i < left.size) result[k++] = left[i++]
    while (j < right.size) result[k++] = right[j++]
    return result
}
```

#### 6. Complexity — Must Know

| Step | Cost |
|---|---|
| Divide | Usually O(1) or O(n) to split |
| Conquer | Recursive calls on smaller pieces |
| Combine | Often the most expensive step (O(n) to merge, for example) |

The overall complexity comes from the **recurrence relation** the divide and combine steps create — worked out properly in topic 5 (Master Theorem). Merge Sort is O(n log n): log n levels of splitting, O(n) work to combine at each level.

#### 7. Common Mistakes — Must Know

1. Forgetting the combine step and assuming solving the pieces is enough.
2. Splitting unevenly by accident (for example, always taking one element off instead of halving), which can turn O(log n) depth into O(n) depth.
3. An expensive combine step that quietly dominates the whole algorithm's cost.
4. Not defining a clear base case for the smallest possible piece.

#### 8. Related Topics

1. `1` Sorting — Merge Sort and Quick Sort are the classic examples
2. `2` Searching — Binary Search is divide and conquer with no real "combine" step
3. `5` Recurrence Relations & the Master Theorem — how to work out the complexity
4. `9` Classic Divide & Conquer — more problems that use this shape

#### 9. Interview Must Remember

1. **Divide, conquer, combine** — say all three steps, not just "split it up".
2. The **combine step's cost** is often the key to the algorithm's complexity — check it.
3. If the split is uneven, the complexity gets worse. A balanced split is what gives you O(log n) levels.
