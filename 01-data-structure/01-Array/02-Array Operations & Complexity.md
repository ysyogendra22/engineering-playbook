# Array Operations & Complexity

#### 1. What Is It?

The basic things you do with an array, and what each one costs. Interviewers expect you to know these without thinking.

| Operation | Plain `IntArray` | `ArrayList` (`MutableList`) | Why |
|---|---|---|---|
| Access `a[i]` | `O(1)` | `O(1)` | direct address |
| Update `a[i] = x` | `O(1)` | `O(1)` | direct address |
| Search a value (unsorted) | `O(n)` | `O(n)` | check each item |
| Search (sorted) | `O(log n)` | `O(log n)` | binary search |
| Add at the end | not possible (fixed size) | `O(1)` on average | spare capacity |
| Insert at the front / middle | `O(n)` (shift) | `O(n)` | items shift right |
| Delete from the front / middle | `O(n)` (shift) | `O(n)` | items shift left |
| Delete the last item | — | `O(1)` | no shifting |
| Memory | `O(n)` | `O(n)` | |

Remember: **anything in the middle that moves items costs `O(n)`**.

#### 2. How It Works

Insert `8` at index `2`:

```text
[7, 3, 9, 1, 5]   shift from the end:  5 → right, 1 → right, 9 → right
[7, 3, _, 9, 1, 5]  → put 8 in the gap →  [7, 3, 8, 9, 1, 5]
```

Delete index `1`:

```text
[7, 3, 9, 1, 5]   shift left:  9 → left, 1 → left, 5 → left
[7, 9, 1, 5, _]   → the array is one item shorter
```

`ArrayList` grows by allocating a bigger array (about 1.5×) and copying. One resize costs `O(n)`, but it happens rarely, so adding at the end is `O(1)` **on average** ("amortized").

#### 3. Kotlin Code

```kotlin
// Insert into an IntArray: we need a bigger array, so we return a new one
fun insertAt(a: IntArray, index: Int, value: Int): IntArray {
    val result = IntArray(a.size + 1)
    for (i in 0 until index) result[i] = a[i]
    result[index] = value
    for (i in index until a.size) result[i + 1] = a[i]          // shift the rest
    return result
}

// Delete at an index: shift everything after it to the left
fun deleteAt(a: IntArray, index: Int): IntArray {
    val result = IntArray(a.size - 1)
    for (i in 0 until index) result[i] = a[i]
    for (i in index + 1 until a.size) result[i - 1] = a[i]
    return result
}

// With ArrayList
val list = mutableListOf(7, 3, 9, 1, 5)
list.add(2, 8)                  // insert at index 2: O(n)
list.removeAt(1)                // delete index 1: O(n)
list.add(4)                     // add at the end: O(1) on average
list.removeAt(list.size - 1)    // delete the last: O(1)
println(list.indexOf(9))        // search: O(n)
println(list.contains(9))       // search: O(n)
```

Tip: if the order does not matter, you can delete in `O(1)` by overwriting the item with the last item and shrinking the size.

#### 4. Complexity

This whole note is the table in section 1. A loop that runs an `O(n)` operation inside it (for example `list.removeAt(0)` in a loop) is `O(n²)`.

#### 5. Common Mistakes

1. **`list.removeAt(0)` or `list.add(0, x)` in a loop.** Each call is `O(n)`, so the loop is `O(n²)`.
2. **Using `contains` / `indexOf` in a loop.** Use a `HashSet` or `HashMap` for `O(1)` lookups.
3. **Deleting while looping forward.** Items shift, so you skip one. Loop backwards or use `removeIf`.
4. **Forgetting that a plain array cannot grow.**
5. **Out-of-range index** when inserting at `size` or deleting at `size`.

#### 6. Say This in the Interview

1. "Access is `O(1)`, but inserting or deleting in the middle is `O(n)` because of shifting."
2. "Appending to an `ArrayList` is amortized `O(1)`."
3. "To avoid `O(n)` searches inside a loop, I will keep a `HashSet` of seen values."

#### 7. Quick Check

1. What is the cost of `list.add(0, x)`?
2. What is the cost of removing the last item of an `ArrayList`?

<details>
<summary>Answers</summary>

1. `O(n)`. Every other item shifts one place.
2. `O(1)`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) (Easy) | build a bigger array |
| 1480 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (Easy) | one pass |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) (Easy) | delete without shifting each time |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (Easy) | in-place delete |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy) | in-place move |
