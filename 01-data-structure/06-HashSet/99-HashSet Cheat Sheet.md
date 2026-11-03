# HashSet Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–18.

#### 1. Key Takeaways

1. A `HashSet` stores **unique** items. `add`, `contains`, `remove` are **`O(1)` average**, `O(n)` worst.
2. Its superpower: **"have I seen this before?"** in `O(1)`. It turns many `O(n²)` pair or scan problems into `O(n)`.
3. **`add` returns `false`** for a duplicate: `if (!seen.add(x)) return true` is the cleanest duplicate check.
4. A set has **no order**. Need insertion order → `LinkedHashSet`. Need sorted / nearest → `TreeSet`.
5. Need a **count, index or list** per key → use a **`HashMap`**, not a set.
6. **Check the complement first, then add** (Two Sum), so an element can't pair with itself.
7. Arrays in a set compare by **identity**. Use `List`, a `String` key, or a data class.
8. Mark visited when you **add** to the BFS queue, and put **all** of the state in the key.

#### 2. Complexity Table

| Operation | `HashSet` | `LinkedHashSet` | `TreeSet` |
|---|---|---|---|
| `add` / `contains` / `remove` | `O(1)` avg | `O(1)` avg | `O(log n)` |
| Order | none | insertion | sorted |
| `first` / `last` / `floor` / `ceiling` | no | no | `O(log n)` |
| Build from `n` items | `O(n)` | `O(n)` | `O(n log n)` |
| Space | `O(n)` | `O(n)` | `O(n)` |

Set operations (`union`, `intersect`, `subtract`): `O(m + n)`.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Note |
|---|---|---|
| "duplicate", "appears twice" | `if (!set.add(x))` | 04 |
| "duplicate within `k` positions" | set of the last `k` values | 04 |
| "values close and indexes close" | `TreeSet` + `ceiling` | 04 |
| "is x in this list?" repeated | build a set once | 05 |
| "distinct", "unique", "how many different" | `toHashSet().size` | 06 |
| "remove duplicates, keep order" | `LinkedHashSet` | 06 |
| "pair with sum / difference" | complement in a set (check, then add) | 07 |
| "common elements", "in both" | two sets, `intersect` | 08 |
| "intersection with duplicates" | count map | 08 |
| "longest consecutive run, O(n)" | set + start only at run starts | 09 |
| "cycle", "visited", "first repeated" | seen set | 10 |
| "union / difference of two arrays" | `union`, `subtract` | 12 |
| "all characters unique", "pangram" | `HashSet<Char>` or `BooleanArray(26)` | 13 |
| "longest window with all distinct" | set + sliding window (`while (!add)`) | 14 |
| "O(1) space" instead of a set | two pointers / Floyd | 15 |
| "set of points / objects" | data class, or an encoded `Int` | 16 |
| "minimum moves between states" | BFS + visited set of states | 17 |
| "state has extra info", "unique shapes" | full-state key, canonical key | 18 |

#### 4. Templates to Memorise

**Duplicate check**

```kotlin
val seen = HashSet<Int>()
for (x in nums) if (!seen.add(x)) return true
```

**Complement lookup (check first, then add)**

```kotlin
val seen = HashSet<Int>()
for (x in nums) {
    if (target - x in seen) return true
    seen.add(x)
}
```

**Longest consecutive sequence**

```kotlin
val set = nums.toHashSet(); var best = 0
for (x in set) {
    if (x - 1 in set) continue
    var end = x
    while (end + 1 in set) end++
    best = maxOf(best, end - x + 1)
}
```

**Distinct window**

```kotlin
val window = HashSet<Char>(); var left = 0
for (right in s.indices) {
    while (!window.add(s[right])) { window.remove(s[left]); left++ }
    best = maxOf(best, right - left + 1)
}
```

**BFS with a visited set**

```kotlin
val visited = HashSet<String>(deadends.toList())
visited.add(start); queue.addLast(start)
while (queue.isNotEmpty()) {
    val s = queue.removeFirst()
    for (n in neighbours(s)) if (visited.add(n)) queue.addLast(n)
}
```

**Set operations and TreeSet**

```kotlin
a union b;  a intersect b;  a subtract b;  b.containsAll(a)
val t = TreeSet<Long>(); t.ceiling(x - d)   // smallest >= x - d
```

**Compact grid key**

```kotlin
val key = r * cols + c           // decode: r = key / cols, c = key % cols
```

#### 5. Brute Force to Optimized

| Problem | Brute force | HashSet |
|---|---|---|
| Contains duplicate | all pairs `O(n²)` | `O(n)` |
| Pair with a sum | all pairs `O(n²)` | `O(n)` |
| Intersection | nested loops `O(m·n)` | `O(m + n)` |
| Longest consecutive | sort `O(n log n)` | set + starts `O(n)` |
| Longest distinct window | all substrings `O(n²)` to `O(n³)` | set window `O(n)` |
| Cycle in a sequence | step cap, or `O(n²)` | seen set `O(n)` |
| Shortest moves between states | DFS over everything | BFS + visited |
| Distinct shapes | compare all pairs | canonical key in a set |
| Membership repeated | `list.contains` `O(n)` each | `O(1)` each |

#### 6. Common Mistakes and Edge Cases

1. **Adding before checking the complement** (an element pairs with itself).
2. **`HashSet<IntArray>`** (identity equality). Use `List<Int>` or a string key.
3. **Expecting order** from a `HashSet`.
4. **Removing from a set while looping** over it. Use `removeAll { }`.
5. **A set where a count or index is needed** (use a map).
6. **Visited marked on pop** instead of on push (BFS duplicates).
7. **A state key that leaves out part of the state**, or shapes with absolute coordinates.
8. **`Int` overflow** in `target − x`, `x + 1`.
9. **`if` instead of `while`** when shrinking a window.
10. **Normalisation** forgotten (case, spaces).
11. **A normal class** without `equals`/`hashCode` as a set element.
12. **Edge cases:** empty input, one element, all duplicates, negatives, `Int.MIN_VALUE`/`MAX_VALUE`.

#### 7. What to Say Out Loud

1. "I need to know if I've seen a value, so a `HashSet` gives me `O(1)` average membership. The whole thing is `O(n)` time and `O(n)` space."
2. "I check the complement before adding, so a number can't pair with itself."
3. "If memory matters, I could sort and use two pointers, but I'd lose the original indexes."
4. "A set has no order. If I need insertion order I'd use a `LinkedHashSet`, and for the nearest value a `TreeSet`."
5. "For BFS I mark states visited when I enqueue them, and the key includes everything that affects the future."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | `add` returns false |
| Easy | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | two sets |
| Easy | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | membership |
| Easy | [Happy Number](https://leetcode.com/problems/happy-number/) | seen set |
| Easy | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | window set |
| Easy | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | normalise + set |
| Easy | [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | `subtract` |
| Easy | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | count map |
| Easy | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | complement + traversal |
| Medium | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | set + run starts |
| Medium | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | set window |
| Medium | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | sets per unit |
| Medium | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | visited set (Easy) |
| Medium | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | BFS + visited states |
| Medium | [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) | window + sum |
| Medium | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | canonical key |
| Hard | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | `TreeSet` ceiling |
| Hard | [Word Ladder](https://leetcode.com/problems/word-ladder/) | state graph |
| Hard | [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | full-state key |
