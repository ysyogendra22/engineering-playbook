# Kotlin for Coding Interviews

> The small set of Kotlin tools that cover about 95% of LeetCode solutions. Know these cold and you will not lose time on syntax.

#### 1. What Is It?

A cheat sheet of the collections, comparators, map helpers, string tools, and traps you use in interview code. Kotlin is shorter than Java, but a few details (arrays vs lists, comparators, `Char` arithmetic, `Int` overflow) cause most bugs.

#### 2. How It Works

**Collections you need**

| Need | Kotlin |
|---|---|
| Fixed array of ints | `IntArray(n)`, `intArrayOf(1, 2)` |
| 2D grid | `Array(m) { IntArray(n) }` |
| Growable list | `mutableListOf<Int>()`, `ArrayList<Int>()` |
| Map / set | `HashMap<K, V>()`, `HashSet<T>()`, `mutableMapOf()` |
| Sorted map / set | `java.util.TreeMap`, `java.util.TreeSet` |
| Queue / stack / deque | `ArrayDeque<T>()` (Kotlin's own) |
| Heap | `java.util.PriorityQueue<T>()` |

`ArrayDeque`: queue = `addLast` + `removeFirst`; stack = `addLast` + `removeLast`. Peek with `first()` / `last()`. `removeFirst()` on an empty deque **throws**. Check `isNotEmpty()` first.

**Sorting with comparators**

| Task | Code |
|---|---|
| Sort an `IntArray` | `nums.sort()` |
| Sort intervals by start | `intervals.sortBy { it[0] }` |
| By start, then end descending | `intervals.sortedWith(compareBy({ it[0] }, { -it[1] }))` |
| Descending | `list.sortedDescending()` |
| Sort by a computed key | `words.sortedBy { it.length }` |

Avoid hand-written comparators like `{ a, b -> a - b }`. The subtraction can **overflow** with large or negative values. Use `compareBy` or `Integer.compare(a, b)`.

**PriorityQueue**

```kotlin
val minHeap = PriorityQueue<Int>()
val maxHeap = PriorityQueue<Int>(compareByDescending<Int> { it })
val byDist  = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })       // smallest first
```

Operations: `add(x)`, `poll()` (remove top), `peek()` (look), `size`, `isEmpty()`. A heap holding arrays is the usual way to carry `(distance, node)`.

**Map helpers**

| Task | Code |
|---|---|
| Count | `map[k] = (map[k] ?: 0) + 1` or `map.merge(k, 1, Int::plus)` |
| Group into lists | `map.getOrPut(k) { mutableListOf() }.add(v)` |
| Default value | `map.getOrDefault(k, 0)` |
| Frequency of chars | `s.groupingBy { it }.eachCount()` |

**Strings and chars**

| Task | Code |
|---|---|
| Char to index 0..25 | `c - 'a'` (an `Int`) |
| Index to char | `'a' + i` (a `Char`) |
| Digit char to int | `c - '0'` |
| Build a string | `StringBuilder().append(x)`, then `toString()` |
| To array and back | `s.toCharArray()`, `String(chars)` |
| Reverse | `s.reversed()` |
| Letter / digit test | `c.isLetterOrDigit()`, `c.isDigit()` |

**Ranges:** `0 until n` (excludes `n`), `0..n` (includes `n`), `n - 1 downTo 0`, `0 until n step 2`. Off-by-one bugs live here.

**Overflow:** `Int` is 32-bit (about ±2.1 × 10⁹). Use `Long` for sums and products: `a.toLong() * b`.

#### 3. Brute Force vs Optimized

Kotlin choices that change complexity:

| Slow habit | Better |
|---|---|
| `s += c` in a loop, `O(n²)` | `StringBuilder`, `O(n)` |
| `list.contains(x)`, `O(n)` | `HashSet`, `O(1)` |
| `list.removeAt(0)` as a queue, `O(n)` | `ArrayDeque.removeFirst()`, `O(1)` |
| sort to get the maximum, `O(n log n)` | one pass, `O(n)` |
| `s.substring(i)` in a loop, `O(n)` each | pass indexes instead |

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

fun demo() {
    // grid and directions
    val grid = Array(2) { IntArray(3) }
    grid[1][2] = 7
    val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1), intArrayOf(-1, 0))

    // sort intervals: start ascending, then end descending
    val intervals = arrayOf(intArrayOf(2, 3), intArrayOf(1, 5), intArrayOf(1, 9))
    val sorted = intervals.sortedWith(compareBy({ it[0] }, { -it[1] }))
    println(sorted.map { it.toList() })                       // [[1, 9], [1, 5], [2, 3]]

    // max-heap
    val maxHeap = PriorityQueue<Int>(compareByDescending<Int> { it })
    maxHeap.addAll(listOf(3, 9, 4))
    println(maxHeap.poll())                                   // 9

    // heap of (distance, node)
    val pq = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })
    pq.add(intArrayOf(5, 1)); pq.add(intArrayOf(2, 8))
    println(pq.poll().toList())                               // [2, 8]

    // counting and grouping
    val count = HashMap<Char, Int>()
    for (c in "aab") count[c] = (count[c] ?: 0) + 1
    println(count)                                            // {a=2, b=1}
    val groups = HashMap<Int, MutableList<String>>()
    for (w in listOf("hi", "yo", "hey")) groups.getOrPut(w.length) { mutableListOf() }.add(w)
    println(groups)                                           // {2=[hi, yo], 3=[hey]}

    // chars
    println('c' - 'a')                                        // 2
    println('a' + 2)                                          // c
    println('7' - '0')                                        // 7

    // deque as queue and as stack
    val dq = ArrayDeque<Int>()
    dq.addLast(1); dq.addLast(2)
    println(dq.removeFirst())                                 // 1  (queue)
    println(dq.removeLast())                                  // 2  (stack)

    // data class and destructuring
    val (r, c) = Pair(2, 5)
    println("$r $c")                                          // 2 5

    // Long to avoid overflow
    val a = 100000; val b = 100000
    println(a * b)                                            // 1410065408 (overflow)
    println(a.toLong() * b)                                   // 10000000000
}
```

**Common Kotlin traps**

```kotlin
val x = intArrayOf(1, 2)
val y = intArrayOf(1, 2)
println(x == y)                  // false (reference equality)
println(x.contentEquals(y))      // true
println(x.toList() == y.toList())// true

val list = mutableListOf(1, 2, 3)
// for (v in list) if (v == 2) list.remove(v)   // ConcurrentModificationException
list.removeAll { it == 2 }       // safe
```

A `data class` is handy for state: `data class State(val r: Int, val c: Int, val steps: Int)`. Data classes give you `equals` and `hashCode`, so they work as `HashSet` keys.

#### 5. Complexity

| Tool | Cost |
|---|---|
| `sortBy`, `sortedWith` | `O(n log n)` |
| `PriorityQueue.add` / `poll` | `O(log n)` |
| `HashMap` ops | `O(1)` average |
| `groupingBy().eachCount()` | `O(n)` |
| `toCharArray`, `reversed`, `substring` | `O(length)` |

Recursion depth: the JVM stack is limited (roughly 10,000 to 20,000 frames). For depth near `10⁵`, such as a skewed tree or a long linked list, convert DFS to an explicit stack.

#### 6. Common Mistakes

1. **`==` on arrays.** Use `contentEquals`, or convert to lists.
2. **Comparator with subtraction** (`a - b`). Use `compareBy`.
3. **Modifying a collection while iterating** over it.
4. **`0..n` when you meant `0 until n`.**
5. **Mixing `Char` and `Int`:** `c + 1` is a `Char`; `c - 'a'` is an `Int`.
6. **`Int` overflow** in sums, products, and `left + right`.
7. **`removeFirst()` on an empty `ArrayDeque`.**
8. **Using `List<Int>` where `IntArray` is needed.** Convert with `toIntArray()` / `toList()`.
9. **Using a mutable list as a map key**, or using an array as a `HashSet` element (identity hash).

#### 7. Say This in the Interview

1. "I'll use an `ArrayDeque` as the queue, because `removeFirst` is `O(1)`."
2. "I use `compareBy` so the comparator can't overflow."
3. "The sum can pass 2 billion, so I use `Long`."

#### 8. Quick Check

1. What does `intArrayOf(1,2) == intArrayOf(1,2)` return?
2. What is the type of `'a' + 2`, and of `'c' - 'a'`?
3. How do you make a max-heap of `Int`?

<details>
<summary>Answers</summary>

1. `false`. Use `contentEquals`.
2. `Char` (`'c'`), and `Int` (`2`).
3. `PriorityQueue<Int>(compareByDescending<Int> { it })`.

</details>

#### 9. Related LeetCode Questions

Easy practice for the syntax (focus on writing clean Kotlin, not on the trick):

| # | Question | Kotlin skill |
|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) (Easy) | `HashMap`, `IntArray` |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) | `c - 'a'`, `IntArray(26)` |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) | `getOrPut`, sort a `CharArray` |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) | map + `PriorityQueue` comparator |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | `sortBy`, `Array<IntArray>` |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium) | heap with `IntArray` |
