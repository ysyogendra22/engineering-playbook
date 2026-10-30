# Task Scheduler & Reorganize String

> Greedy with a **max-heap or counts**: always deal with the **most frequent** item first.

#### 1. What Is It?

Two questions with the same idea:

- **Task Scheduler (621).** Tasks are letters. The same letter must be at least `n` slots apart (idle slots are allowed). Return the **minimum total time** to finish all tasks.
- **Reorganize String (767).** Rearrange a string so **no two adjacent characters are equal**. Return `""` if impossible.

```text
tasks = A A A B B B, n = 2   →  A B _ A B _ A B   = 8 slots
"aab" → "aba"      "aaab" → ""
```

#### 2. How It Works

**The idea:** the most frequent item causes the trouble, so place it first and use the others to fill the gaps.

**Task Scheduler — formula.** Let `maxFreq` be the highest count and `countMax` how many tasks have that count.

```text
(maxFreq − 1) blocks of length (n + 1), then the last row of countMax tasks
time = (maxFreq − 1) × (n + 1) + countMax
answer = max(tasks.size, time)        (if there are many tasks, no idle time is needed)
```

```text
A A A B B B, n = 2:   maxFreq = 3, countMax = 2
(3 − 1) × (2 + 1) + 2 = 8        tasks.size = 6      answer = 8
```

**Task Scheduler — simulation.** Keep a max-heap of counts. Each time slot, run the task with the largest count. A task you ran goes to a cool-down queue and returns to the heap after `n` slots.

**Reorganize String — heap.** Put `(count, letter)` in a max-heap. Each round, take the **two** most frequent different letters, append both, reduce their counts, and push them back if they still have a count.

```text
"aab": a=2, b=1.   take a, b → "ab".  a=1 returns.   one letter left → "aba"
```

Impossible when the most frequent letter appears more than `(length + 1) / 2` times.

#### 3. Brute Force vs Optimized

| | Brute force | Greedy |
|---|---|---|
| Task Scheduler | try all orders of tasks, `O(n!)` | formula `O(n)`, or heap simulation `O(T log 26)` |
| Reorganize String | try all permutations, `O(n!)` | heap `O(n log 26)` |

```kotlin
import java.util.PriorityQueue

// Task Scheduler by simulation (easier to explain than the formula)
fun leastIntervalSim(tasks: CharArray, n: Int): Int {
    val count = IntArray(26)
    for (t in tasks) count[t - 'A']++
    val heap = PriorityQueue<Int>(compareByDescending<Int> { it })
    for (c in count) if (c > 0) heap.add(c)
    val cooldown = ArrayDeque<IntArray>()                 // [remaining count, time it is ready]
    var time = 0
    while (heap.isNotEmpty() || cooldown.isNotEmpty()) {
        time++
        if (heap.isNotEmpty()) {
            val left = heap.poll() - 1
            if (left > 0) cooldown.addLast(intArrayOf(left, time + n))
        }
        if (cooldown.isNotEmpty() && cooldown.first()[1] == time) {
            heap.add(cooldown.removeFirst()[0])
        }
    }
    return time
}
```

Check: `leastIntervalSim("AAABBB", 2)` → `8`.

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

// Task Scheduler (LeetCode 621): formula
fun leastInterval(tasks: CharArray, n: Int): Int {
    val count = IntArray(26)
    for (t in tasks) count[t - 'A']++
    val maxFreq = count.maxOrNull()!!
    val countMax = count.count { it == maxFreq }
    return maxOf(tasks.size, (maxFreq - 1) * (n + 1) + countMax)
}

// Reorganize String (LeetCode 767)
fun reorganizeString(s: String): String {
    val count = IntArray(26)
    for (c in s) count[c - 'a']++
    if (count.maxOrNull()!! > (s.length + 1) / 2) return ""

    val heap = PriorityQueue<IntArray>(compareByDescending<IntArray> { it[0] })   // [count, letter]
    for (i in 0 until 26) if (count[i] > 0) heap.add(intArrayOf(count[i], i))

    val sb = StringBuilder()
    while (heap.size >= 2) {
        val a = heap.poll()
        val b = heap.poll()
        sb.append('a' + a[1]).append('a' + b[1])
        if (--a[0] > 0) heap.add(a)
        if (--b[0] > 0) heap.add(b)
    }
    if (heap.isNotEmpty()) sb.append('a' + heap.poll()[1])           // one letter with count 1 is left
    return sb.toString()
}
```

Checks (tasks written as strings here, pass `"AAABBB".toCharArray()`): `leastInterval("AAABBB", 2)` → `8`. `leastInterval("AAABBB", 0)` → `6`. `leastInterval("AAAAAABCDEFG", 2)` → `16`. `reorganizeString("aab")` → `"aba"`. `reorganizeString("aaab")` → `""`. `reorganizeString("aaabbc")` gives a valid string such as `"ababac"` (several answers are valid).

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Task Scheduler formula | `O(T)` | `O(1)` (26 counters) |
| Task Scheduler simulation | `O(total time × log 26)` | `O(26)` |
| Reorganize String | `O(n log 26)`, which is `O(n)` | `O(26)` |

#### 6. Common Mistakes

1. **Forgetting `max(tasks.size, formula)`.** With many different tasks there is no idle time.
2. **Counting `countMax` wrongly.** It is the number of tasks tied for the highest count.
3. **Reorganize String:** not checking the impossible case first.
4. **Taking the same letter twice in a row** (take two different letters per round).
5. **Using a min-heap** instead of a max-heap.
6. **Not pushing letters back** after reducing the count.

#### 7. Say This in the Interview

1. "The most frequent task decides the length: `(maxFreq − 1)` full blocks of `n + 1` slots plus the final tasks. The answer is at least the number of tasks."
2. "For Reorganize String, if one letter is more than half (rounded up) the answer is impossible. Otherwise a max-heap places the two most frequent different letters each round."

#### 8. Quick Check

1. `AAAB`, `n = 2`. What is the answer?
2. Why check `(length + 1) / 2`?

<details>
<summary>Answers</summary>

1. `maxFreq = 3`, `countMax = 1`: `(3 − 1) × 3 + 1 = 7` (A B _ A _ _ A).
2. If one letter is more than that, even placing it in every second slot leaves two of them adjacent.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Easy) | max-heap warm-up |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) | most frequent first |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) (Medium) | max-heap, two letters per round |
| 1054 | [Distant Barcodes](https://leetcode.com/problems/distant-barcodes/) (Medium) | same as Reorganize String |
| 358 | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) (Hard, premium) | heap + cool-down |
