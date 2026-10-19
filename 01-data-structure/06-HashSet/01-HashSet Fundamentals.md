# HashSet Fundamentals

#### 1. Definition — Must Know

1. A **HashSet** is a collection that stores **unique** values. Adding a value that is already there changes nothing.
2. It uses **hashing**, so `add`, `contains` and `remove` take **`O(1)` on average**.
3. It has **no index** and **no guaranteed order**. You ask "is it in the set?", not "what is at position 3?".
4. In Kotlin/JVM, `HashSet<T>` (and `hashSetOf(...)`) is `java.util.HashSet`, which is built on a `HashMap` inside.

#### 2. Why It Is Used — Must Know

1. **Fast membership check:** is this value already known?
2. **Remove duplicates:** keep one copy of each value.
3. **Track what you have seen:** visited nodes, seen numbers, seen states.
4. It replaces slow `list.contains(x)` (`O(n)`) with `set.contains(x)` (`O(1)` average). This turns many `O(n²)` solutions into `O(n)`.

#### 3. How It Works — Must Know

```text
value  →  hashCode()  →  bucket index  →  look inside that bucket, compare with equals()

add(42):   hash(42) → bucket 2 → empty → store 42
add(7):    hash(7)  → bucket 7 → empty → store 7
add(42):   hash(42) → bucket 2 → found equal value → do nothing, return false
contains(7): hash(7) → bucket 7 → found → true
```

```text
bucket 0: -
bucket 1: -
bucket 2: [42]
bucket 3: -
...
bucket 7: [7]
```

Two different values can land in the same bucket (a **collision**). The bucket then holds a small chain. With a good hash function, chains stay short, so the average cost stays `O(1)`.

#### 4. Core Concepts — Must Know

1. **Uniqueness is decided by `equals()` and `hashCode()`.** Two values count as the same if they are equal and have the same hash.
2. **`add` returns a `Boolean`:** `true` if the value was new, `false` if it was already there. This is very useful.
3. **Iteration order is not defined** for `HashSet`. Do not rely on it.
4. **Kotlin set types:**

| Type | Order | Speed | Use when |
|---|---|---|---|
| `HashSet` / `hashSetOf()` | none | `O(1)` avg | Most interview problems |
| `LinkedHashSet` / `mutableSetOf()` | insertion order | `O(1)` avg | You need uniqueness and the original order |
| `TreeSet` / `sortedSetOf()` | sorted | `O(log n)` | You need sorted values, floor/ceiling |
| `setOf()` | insertion order | `O(1)` avg | Read-only set |

5. **`mutableSetOf()` returns a `LinkedHashSet`**, not a plain `HashSet`.
6. A `HashSet` allows **one `null`**.

#### 5. Algorithm — Must Know

The usual shape of a HashSet solution:

```text
seen = empty set
for each item:
    if item is already in seen → handle it (duplicate / found / skip)
    else add item to seen
```

#### 6. Kotlin Implementation — Must Know

```kotlin
val set = HashSet<Int>()           // empty
val nums = hashSetOf(1, 2, 3)      // with values
val fromList = listOf(1, 2, 2, 3).toHashSet()   // {1, 2, 3}

set.add(10)                // true  (new)
set.add(10)                // false (already there)
println(10 in set)         // true   — same as set.contains(10)
set.remove(10)             // true  (it was there)
println(set.size)          // 0
println(set.isEmpty())     // true

for (x in nums) println(x) // order is not guaranteed
```

Remove duplicates from a list:

```kotlin
val unique = listOf(3, 1, 3, 2, 1).toSet()     // keeps first-seen order: [3, 1, 2]
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average | Worst |
|---|---:|---:|
| `add` | `O(1)` | `O(n)`* |
| `contains` | `O(1)` | `O(n)`* |
| `remove` | `O(1)` | `O(n)`* |
| Iterate all | `O(n + capacity)` | — |
| Space | `O(n)` | — |

\*Worst case happens only with very bad hashing. Modern Java turns long chains into balanced trees, so it is rarely a problem. Quote `O(1)` average in interviews.

#### 8. Common HashSet Patterns — Must Know

1. **Duplicate detection** — "does any value appear twice?"
2. **Fast lookup** — "is X in this group?"
3. **Unique elements** — "how many distinct values?"
4. **Complement lookup** — "is `target - x` already seen?"
5. **Visited / seen** — graphs, grids, cycles.
6. **Consecutive sequence** — "is `x + 1` in the set?"

#### 9. Edge Cases / Common Mistakes

1. Expecting a `HashSet` to keep insertion order. Use `LinkedHashSet` for that.
2. Using `list.contains()` inside a loop when a set would be `O(1)`.
3. Putting `IntArray` or `Array` in a set. They compare by reference, so duplicates are not detected.
4. Changing an object after it is in the set. Its hash changes and it can no longer be found.
5. Expecting `get(index)`. A set has no index.
6. Forgetting that `add` already tells you whether the value was new.

#### 10. When to Use / When Not to Use

**Use when:**

1. You only need to know whether a value exists.
2. You need uniqueness.
3. You need `O(1)` lookups.

**Avoid when:**

1. You need to store a **value** or a **count** with each key. Use a `HashMap`.
2. You need sorted order. Use a `TreeSet`.
3. You need positions or duplicates. Use a `List`.

#### 11. Related Topics

1. HashSet Operations & Complexity
2. HashSet vs HashMap
3. HashMap (`01-data-structure/05-HashMap`)
4. Array and String basics

#### 12. Interview Must Remember

1. **HashSet = unique values + `O(1)` average add/contains/remove.**
2. `add()` returns `false` for a duplicate. Use it as a free duplicate check.
3. No order, no index. `mutableSetOf()` is a `LinkedHashSet`.
4. Needs correct `equals()` and `hashCode()` for custom objects.
