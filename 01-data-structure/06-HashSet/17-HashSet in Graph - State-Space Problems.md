# HashSet in Graph / State-Space Problems

#### 1. Definition — Must Know

1. A **state-space problem** is a search where each **state** (a word, a board, a position) leads to other states by simple moves. It is a graph that you build as you go.
2. Examples: Word Ladder, Open the Lock, sliding puzzles, shortest path in a maze.
3. A **HashSet of visited states** stops the search from looping and from repeating work.

#### 2. Why It Is Used — Must Know

1. The graph may be huge or hidden. You cannot store it all, but you can remember the states you reached.
2. Without a visited set, BFS can run forever or take exponential time.
3. These are common "medium/hard" questions where the set is the key to the `O(states)` bound.

#### 3. How It Works — Must Know

*Word Ladder* (LeetCode 127): change one letter at a time; every new word must be in the word list. Find the shortest chain from `hit` to `cog`.

```text
words = {hot, dot, dog, lot, log, cog}      begin = hit      end = cog

Level 1: hit
Level 2: hot                     (hit → hot)
Level 3: dot, lot                (hot → dot, lot)
Level 4: dog, log                (dot → dog, lot → log)
Level 5: cog                     (dog → cog)

Chain length = 5
```

Each word is **removed from the set the first time we reach it**, so it can never be queued again. The word set is both the dictionary and the visited marker.

#### 4. Core Concepts — Must Know

1. **State** = everything that decides what can happen next (word; cell; cell + keys collected; board layout).
2. **Neighbours** = states reachable in one move.
3. **BFS** gives the shortest number of moves when each move costs 1.
4. **Visited set** = states already queued. Mark on enqueue.
5. **Remove-from-dictionary trick:** if the state space is already a set (like a word list), `remove` returns `true` only the first time, so it acts as visited.
6. **State key:** an `Int`, a `String`, a `data class`, or a `Pair`. Keep it small and immutable.
7. **Add the missing information to the state.** If keys, direction, or steps left matter, they belong in the key; otherwise two different situations get merged by mistake.

| Problem | State | Neighbours |
|---|---|---|
| Word Ladder | word | change one letter |
| Open the Lock (LeetCode 752) | 4-digit string | turn one wheel up or down |
| Number of Islands | cell | 4 directions |
| Shortest path in a maze | cell | 4 directions |
| Sliding Puzzle (LeetCode 773) | board as a string | swap the empty tile with a neighbour |
| Shortest path with keys | cell + key bitmask | 4 directions |

#### 5. Algorithm — Must Know

```text
queue = [start];  visited = {start};  steps = 0
while queue is not empty:
    for each state currently in the queue (one level):
        if state is the goal: return steps
        for each neighbour of state:
            if visited.add(neighbour): queue.add(neighbour)
    steps++
return not found
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Word Ladder — the word set is also the visited set
fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
    val words = wordList.toHashSet()
    if (endWord !in words) return 0
    words.remove(beginWord)

    val queue = ArrayDeque<String>()
    queue.add(beginWord)
    var steps = 1

    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val word = queue.removeFirst()
            if (word == endWord) return steps
            val chars = word.toCharArray()
            for (i in chars.indices) {
                val original = chars[i]
                for (c in 'a'..'z') {
                    if (c == original) continue
                    chars[i] = c
                    val next = String(chars)
                    if (words.remove(next)) queue.add(next)     // true only the first time
                }
                chars[i] = original
            }
        }
        steps++
    }
    return 0
}
```

Check: `hit → cog` with `[hot, dot, dog, lot, log, cog]` → `5`.

**Open the Lock** (LeetCode 752): dead ends plus visited, both in one set.

```kotlin
fun openLock(deadends: Array<String>, target: String): Int {
    val blocked = deadends.toHashSet()               // dead ends act as already visited
    if ("0000" in blocked) return -1
    val visited = hashSetOf("0000")
    val queue = ArrayDeque<String>()
    queue.add("0000")
    var turns = 0

    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val code = queue.removeFirst()
            if (code == target) return turns
            for (i in 0 until 4) {
                for (delta in intArrayOf(1, 9)) {                      // +1 or -1 (mod 10)
                    val digit = (code[i] - '0' + delta) % 10
                    val next = code.substring(0, i) + digit + code.substring(i + 1)
                    if (next !in blocked && visited.add(next)) queue.add(next)
                }
            }
        }
        turns++
    }
    return -1
}
```

**Grid with extra state (cell + keys)** — the key must include everything that matters:

```kotlin
data class State(val row: Int, val col: Int, val keys: Int)

val visited = HashSet<State>()
// visited.add(State(r, c, keysMask)) — the same cell with different keys is a different state
```

#### 7. Time & Space Complexity — Must Know

| Problem | Time | Space |
|---|---:|---:|
| Word Ladder (`n` words of length `L`) | `O(n × L × 26)` plus string building | `O(n × L)` |
| Open the Lock | `O(10⁴ × 4 × 2)` | `O(10⁴)` |
| Grid `R × C` | `O(R × C)` | `O(R × C)` |
| General | `O(number of states × moves per state)` | `O(number of states)` |

The visited set means each state is expanded once.

#### 8. Common State-Space Patterns — Must Know

1. **Word Ladder** (LeetCode 127) and **Word Ladder II** (LeetCode 126).
2. **Open the Lock** (LeetCode 752).
3. **Sliding Puzzle** (LeetCode 773) — board string as a state.
4. **Minimum Genetic Mutation** (LeetCode 433) — like Word Ladder.
5. **Shortest Path to Get All Keys** (LeetCode 864) — position + key mask.
6. **Jump Game III**, **Perfect Squares** — numbers as states.
7. **Bidirectional BFS** — two sets (front and back) that meet in the middle, much faster for big spaces.

#### 9. Edge Cases / Common Mistakes

1. Marking visited **when dequeuing**. The queue fills with copies.
2. Forgetting the start state in the visited set.
3. Missing information in the state (such as keys), which gives wrong answers.
4. Returning the wrong level count (off by one: 1 vs 0 for the start).
5. The goal not in the allowed words (Word Ladder returns `0`).
6. Using a mutable object (array) as a state. Use a `String` or `List`.
7. Very large state keys that are slow to hash.
8. Using DFS when the shortest path is needed. BFS is the safe choice.

#### 10. When to Use / When Not to Use

**Use when:**

1. The graph is implicit (made from rules, not stored).
2. You need the fewest steps, or whether a goal is reachable.

**Avoid when:**

1. Edges have different costs. Use Dijkstra with a visited/best-distance map.
2. The state space is too large to store. Look for a smarter algorithm or bidirectional search.

#### 11. Related Topics

1. Visited / Seen Pattern
2. Deduplication of Complex States
3. BFS / DFS (`02-algorithm/07-Graph Algorithms`)
4. Queue (`01-data-structure/04-Queue`)

#### 12. Interview Must Remember

1. **State + moves + visited set + BFS.**
2. **Mark visited when you enqueue.**
3. Put everything that matters (keys, direction) into the state.
4. Visited set bounds the work at `O(states × moves)`.
