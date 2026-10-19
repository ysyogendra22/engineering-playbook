# Heap + HashMap Pattern

#### 1. Definition — Must Know

1. The **Heap + HashMap pattern** uses two structures together:
   - a **`HashMap`** to count, store, or look up values quickly,
   - a **heap** to pick the best item (most frequent, smallest cost, earliest time) quickly.
2. The map answers "what is the current value of X?". The heap answers "which X is best right now?".
3. A heap alone cannot find an arbitrary item. A map alone cannot give the best item. Together they can do both.

#### 2. Why It Is Used — Must Know

1. Many problems need counts or latest values first and the best choice second.
2. It appears in Top K Frequent, Reorganize String, Task Scheduler, and Dijkstra (distance map + heap).
3. It is also how many real systems work, for example a leaderboard or a "most active users" list.

#### 3. How It Works — Must Know

Example: **Reorganize String** (LeetCode 767). Rearrange a string so that no two neighbouring characters are the same.

```text
s = "aabbc"

Step 1: HashMap counts           {a: 2, b: 2, c: 1}

Step 2: max-heap by count        top is a (2) or b (2)

Step 3: repeat — take the TWO most frequent characters and place them next to each other,
        then put them back with count - 1.

   take a, b   → "ab"      put back a:1, b:1       heap: a:1, b:1, c:1
   take a, b   → "abab"    a and b are used up     heap: c:1
   one left: c → "ababc"

Result: "ababc"   (no two neighbours are equal)
```

Taking two different characters each round guarantees that neighbours differ.

#### 4. Core Concepts — Must Know

1. **Map first, heap second.** Build counts or values in the map. Load the heap from it.
2. **Heap stores a key plus the priority** (a `Pair`, a small class, or an `IntArray`), not only the value.
3. **Keep them in sync.** When the map value changes and the heap holds old data, either push a new entry (and skip stale ones later) or use lazy deletion.
4. **Common combinations:**

| Problem | Map holds | Heap holds |
|---|---|---|
| Top K Frequent | value → count | `k` entries by count |
| Reorganize String | char → count | all entries, max by count |
| Dijkstra | node → best distance | `(distance, node)` candidates |
| Task Scheduler | task → remaining count | tasks by remaining count |
| Stream top-K with updates | id → score | candidates by score |

5. **Impossible check.** For Reorganize String, if one character appears more than `(n + 1) / 2` times, the answer is `""`.

#### 5. Algorithm — Must Know

```text
count = HashMap of item → value
heap = priority queue ordered by what makes an item "best"
for each (item, value) in count:
    heap.add(item with its value)

while there is work to do:
    take the best item(s) from the heap
    use them
    if they still have something left: put them back with the updated value
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

fun reorganizeString(s: String): String {
    val count = HashMap<Char, Int>()
    for (c in s) count[c] = (count[c] ?: 0) + 1

    // Max-heap by remaining count
    val heap = PriorityQueue<Pair<Char, Int>>(compareByDescending<Pair<Char, Int>> { it.second })
    for ((ch, n) in count) heap.add(ch to n)

    val sb = StringBuilder()
    while (heap.size >= 2) {
        val (c1, n1) = heap.poll()
        val (c2, n2) = heap.poll()
        sb.append(c1).append(c2)
        if (n1 > 1) heap.add(c1 to n1 - 1)
        if (n2 > 1) heap.add(c2 to n2 - 1)
    }

    if (heap.isNotEmpty()) {
        val (c, n) = heap.poll()
        if (n > 1) return ""          // the same character would have to touch itself
        sb.append(c)
    }
    return sb.toString()
}
```

Checks: `"aab"` → `"aba"`. `"aaab"` → `""`.

**Another example — most active users from a stream of events**

```kotlin
class ActivityTracker {
    private val counts = HashMap<String, Int>()

    fun record(userId: String) {
        counts[userId] = (counts[userId] ?: 0) + 1
    }

    // Build the top-k list when asked. Cost: O(m log k), m = number of users
    fun topK(k: Int): List<String> {
        val heap = PriorityQueue<Map.Entry<String, Int>>(compareBy<Map.Entry<String, Int>> { it.value })
        for (e in counts.entries) {
            heap.add(e)
            if (heap.size > k) heap.poll()
        }
        return heap.sortedByDescending { it.value }.map { it.key }
    }
}
```

#### 7. Time & Space Complexity — Must Know

| Part | Time | Space |
|---|---:|---:|
| Build counts in the map | `O(n)` | `O(m)` |
| Heap with `m` entries | `O(m log m)` | `O(m)` |
| Heap limited to `k` entries | `O(m log k)` | `O(k)` extra |

`n` = items, `m` = distinct keys.

For Reorganize String, the alphabet is small (26 letters), so the heap cost is almost constant per character: `O(n log 26)`, close to `O(n)`.

#### 8. Common Heap + HashMap Patterns — Must Know

1. **Frequency + best:** Top K Frequent Elements, Top K Frequent Words.
2. **Rearranging by count:** Reorganize String, Task Scheduler (LeetCode 621), Rearrange String k Distance Apart.
3. **Best known value + candidates:** Dijkstra with `dist` map and a heap of `(distance, node)`.
4. **Updates over time:** a map holds the current score and the heap holds possibly stale entries; check the map when popping (lazy deletion).
5. **Lookup of heap position:** an indexed priority queue (key → position in the heap) supports fast decrease-key. This is rare in interviews.

#### 9. Edge Cases / Common Mistakes

1. Not putting the entry back into the heap after using it.
2. Putting it back with the **old** count instead of `count - 1`.
3. Forgetting the impossible case (no valid arrangement) in Reorganize String.
4. Reading the map while changing it.
5. Letting the heap and the map disagree. A stale heap entry must be detected and skipped.
6. Comparing keys (for example characters) instead of counts.
7. Using a `Map.Entry` from a map that you change afterwards. Copy the key and value into a `Pair` when the map will change.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need counts or latest values, plus repeated "best item" queries.
2. You process the best items in rounds.

**Avoid when:**

1. You only need the best once. Scan the map and track the maximum.
2. The number of distinct keys is tiny. Sorting once may be simpler.

#### 11. Related Topics

1. Top K Frequent Elements
2. Lazy Deletion with Heap
3. Heap for Scheduling / Processing by Priority
4. HashMap (`01-data-structure/05-HashMap`)
5. Dijkstra (`02-algorithm/07-Graph Algorithms`)

#### 12. Interview Must Remember

1. **Map = lookup and counts. Heap = best item.**
2. Keep both in sync, or skip stale heap entries.
3. Reorganize String: take the **two most frequent** each round and put them back with `count - 1`.
4. Say the impossible case out loud.
