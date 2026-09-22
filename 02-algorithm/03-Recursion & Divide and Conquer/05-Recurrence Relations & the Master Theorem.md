# Recurrence Relations & the Master Theorem

#### 1. Definition — Must Know

1. A **recurrence relation** is an equation that describes a recursive function's cost in terms of the cost of its smaller calls.
2. The **Master Theorem** is a shortcut formula that turns many common recurrences straight into a Big-O answer, without expanding the recursion tree by hand every time.

#### 2. Why It Is Used — Must Know

1. It gives you a fast, reliable way to state a divide-and-conquer algorithm's complexity in an interview.
2. It explains *why* Merge Sort is O(n log n) instead of leaving it as something to memorise.

#### 3. How It Works — Must Know

The general shape the Master Theorem covers:

```text
T(n) = a · T(n / b) + f(n)
```

- `a` = how many recursive calls are made
- `n / b` = the size of each smaller call
- `f(n)` = the work done outside the recursive calls (the divide + combine cost)

For Merge Sort: `a = 2` (splits into 2 halves), `b = 2` (each half is size n/2), `f(n) = O(n)` (the merge step).

```text
T(n) = 2·T(n/2) + O(n)   →   O(n log n)
```

#### 4. Algorithm — Must Know

The Master Theorem compares `f(n)` against `n^(log_b a)` and picks one of three cases:

```text
Let critical = n^(log_b a)

Case 1: f(n) grows slower than critical  →  T(n) = O(critical)
Case 2: f(n) grows the same as critical  →  T(n) = O(critical · log n)
Case 3: f(n) grows faster than critical  →  T(n) = O(f(n))
```

Worked example for Merge Sort: `a = 2, b = 2`, so `critical = n^(log₂ 2) = n^1 = n`. Since `f(n) = O(n)` grows at the *same* rate as `critical = n`, this is Case 2: `T(n) = O(n · log n)`.

#### 5. Kotlin Implementation — Must Know

*(There's no code to implement — this is a way to analyse code you've already written.)*

```kotlin
fun mergeSort(arr: IntArray): IntArray {
    if (arr.size <= 1) return arr
    val mid = arr.size / 2
    val left = mergeSort(arr.copyOfRange(0, mid))     // a = 2 calls
    val right = mergeSort(arr.copyOfRange(mid, arr.size)) // each on n/2 → b = 2
    return merge(left, right)                          // f(n) = O(n)
}
```

#### 6. Complexity — Must Know

| Algorithm | Recurrence | Case | Complexity |
|---|---|---|---|
| Merge Sort | T(n) = 2T(n/2) + O(n) | 2 | O(n log n) |
| Binary Search | T(n) = 1·T(n/2) + O(1) | 2 | O(log n) |
| Naive matrix multiply-style split (rare in interviews) | T(n) = 8T(n/2) + O(n²) | 1 | O(n³) |

#### 7. Common Mistakes — Must Know

1. Using the Master Theorem on a recurrence that doesn't fit its shape (for example, one recursive call with a shrinking-by-one pattern like `T(n) = T(n - 1) + O(1)` — that's a simple sum, not a Master Theorem case).
2. Mixing up `a` (number of calls) and `b` (how much smaller each call is) — they are not the same number, even when they happen to match, as in Merge Sort.
3. Forgetting to include the combine step's cost as `f(n)`.

#### 8. Related Topics

1. `3` Divide and Conquer — where this recurrence shape comes from
2. `4` Recursion Tree & Tracing Complexity by Hand — the visual version of the same analysis
3. `1` Sorting — Merge Sort and Quick Sort as worked examples

#### 9. Interview Must Remember

1. Write the recurrence first: `T(n) = a·T(n/b) + f(n)`.
2. You don't need to prove the Master Theorem — just apply it and state the result with the reasoning.
3. If a recurrence doesn't fit the shape, fall back to a recursion tree (topic 4).
