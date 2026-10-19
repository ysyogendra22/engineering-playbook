# HashSet Operations & Complexity

#### 1. Definition — Must Know

1. The core operations of a HashSet are **add**, **contains** and **remove**.
2. All three run in **`O(1)` average** time.
3. Extra operations: `size`, `isEmpty`, `clear`, iteration, and bulk operations (`addAll`, `removeAll`, `retainAll`).

#### 2. Why It Is Used — Must Know

1. Interviewers often ask "what is the complexity of your solution?". You must know the cost of each set operation.
2. Most set-based solutions are `O(n)` because each of the `n` items costs `O(1)`.
3. Knowing the worst case and the memory cost shows depth.

#### 3. How It Works — Must Know

Each operation follows the same steps: **hash → bucket → equals check**.

```text
add(x)       hash x → go to bucket → if an equal value is there: return false
                                   → else insert x, return true
contains(x)  hash x → go to bucket → look for an equal value
remove(x)    hash x → go to bucket → if found: delete it, return true
                                   → else return false
```

**Resizing.** Java's `HashSet` starts with 16 buckets and a **load factor of 0.75**. When it is 75% full it doubles the buckets and moves every item to a new place (**rehash**). One resize costs `O(n)`, but it is rare, so `add` stays `O(1)` **amortized**.

#### 4. Core Concepts — Must Know

1. **Add**
   - Returns `true` if added, `false` if the value already existed.
2. **Contains**
   - Returns `true` or `false`. Use `x in set`.
3. **Remove**
   - Returns `true` if something was removed.
4. **Bulk operations** work on whole collections and cost `O(m)` for `m` items passed in.
5. **Iteration** visits every bucket, so it costs `O(n + capacity)`.
6. **Size** is stored, so `size` is `O(1)`.

#### 5. Algorithm — Must Know

Pseudo-steps for a safe "add if new":

```text
if set.add(x):   // true → new
    process the new value
else:
    handle the duplicate
```

This does one hash lookup instead of two (`contains` then `add`).

#### 6. Kotlin Implementation — Must Know

```kotlin
val set = hashSetOf<String>()

// Add
set.add("apple")              // true
set.add("apple")              // false
set += "banana"               // operator form (same as add)
set.addAll(listOf("cherry", "date"))

// Contains
println("apple" in set)       // true
println(set.contains("fig"))  // false
println(set.containsAll(listOf("apple", "banana")))   // true

// Remove
set.remove("apple")           // true
set -= "banana"               // operator form
set.removeAll(listOf("cherry"))
set.retainAll(setOf("date"))  // keep only items that are also in the other collection

// Other
println(set.size)
println(set.isEmpty())
set.clear()
```

Remove while looping — the safe way:

```kotlin
val nums = hashSetOf(1, 2, 3, 4, 5, 6)
nums.removeIf { it % 2 == 0 }        // safe, keeps the odd numbers
// for (n in nums) if (n % 2 == 0) nums.remove(n)   // ConcurrentModificationException
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average | Worst case |
|---|---:|---:|
| `add(x)` | `O(1)` amortized | `O(n)` (resize, or very bad hash) |
| `contains(x)` | `O(1)` | `O(n)` |
| `remove(x)` | `O(1)` | `O(n)` |
| `size`, `isEmpty` | `O(1)` | `O(1)` |
| `addAll(m items)` | `O(m)` | — |
| `containsAll(m items)` | `O(m)` | — |
| Iteration | `O(n + capacity)` | — |
| Space | `O(n)` | — |

Notes:

1. Java 8+ turns very long chains into balanced trees, so the real worst case is about `O(log n)` per operation for keys that are `Comparable`.
2. `HashSet<Int>` boxes each number into an `Integer` object. It uses much more memory than an `IntArray`.
3. `TreeSet` operations are `O(log n)`, not `O(1)`.

#### 8. Common Operation Patterns — Must Know

1. **Build a set from an array:** `nums.toHashSet()` — `O(n)`.
2. **Check then act:** `if (!seen.add(x)) return true`.
3. **Delete as you go:** `words.remove(w)` returning `true` doubles as a "visited" mark.
4. **Count distinct:** `set.size` after adding everything.
5. **Pre-size to avoid resizes:** `HashSet<Int>(expectedSize * 2)` for very large inputs.

#### 9. Edge Cases / Common Mistakes

1. Calling `contains` and then `add` (two lookups) instead of using the result of `add`.
2. Removing items while iterating with a `for` loop. Use `removeIf` or an `Iterator`.
3. Saying `contains` is always `O(1)`. Say "average".
4. Using `list.contains` and thinking it is the same cost.
5. Using `retainAll` and `removeAll` on the same set you are looping over.
6. Forgetting that a resize makes one `add` expensive.

#### 10. When to Use / When Not to Use

**Use when:**

1. Most work is `add` and `contains`.
2. You need the best average speed.

**Avoid when:**

1. You need the smallest, largest, or a range query. Use `TreeSet` (`O(log n)`).
2. Memory is very tight and values are small integers. Use a `BooleanArray` or `BitSet`.

#### 11. Related Topics

1. HashSet Fundamentals
2. HashSet vs HashMap
3. Duplicate Detection
4. Set Union / Intersection / Difference

#### 12. Interview Must Remember

1. `add`, `contains`, `remove` are **`O(1)` average**.
2. `add` returns a `Boolean` — use it.
3. Never modify a set while looping with `for`. Use `removeIf`.
4. Space is `O(n)`. Resizing makes `add` amortized `O(1)`.
