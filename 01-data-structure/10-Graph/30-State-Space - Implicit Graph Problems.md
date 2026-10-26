# State-Space / Implicit Graph Problems

> A favourite FAANG trick: the question does not mention a graph, but it is one.

#### 1. What Is It?

In an **implicit graph** the nodes and edges are not given as a list. They come from **rules**:

- a **node** is a **state** (a word, a lock code, a board layout, a number),
- an **edge** is **one allowed move** from one state to another.

You never build the whole graph. You **generate the neighbours** of a state when you need them, and you search with BFS (or DFS / Dijkstra).

Signs in a question: "minimum number of moves/steps/changes", "transform A into B one step at a time", "reach the target state".

| Question | State | One move |
|---|---|---|
| Word Ladder | a word | change one letter (the new word must be in the list) |
| Open the Lock | a 4-digit code | turn one wheel up or down |
| Sliding Puzzle | the board as a string | slide a tile into the empty space |
| Perfect Squares | a number | subtract a square |
| Jug problems | (amount in jug A, amount in jug B) | fill, empty, or pour |

#### 2. How It Works

Steps:

1. Decide what a **state** is. It must contain **everything** that affects the future.
2. Write how to produce the **neighbours** of a state.
3. Run **BFS** from the start state, with a **visited** set of states. BFS gives the fewest moves.
4. Stop when you reach the target.

*Open the Lock* (LeetCode 752): a lock has 4 wheels `0–9`. Start at `"0000"`. Each move turns one wheel one step (`9` wraps to `0`). Some codes are **dead ends** (the lock gets stuck). Find the fewest moves to reach `target`.

```text
state: "0000".  Neighbours (8): 1000, 9000, 0100, 0900, 0010, 0090, 0001, 0009
Each state has 8 neighbours. Skip dead ends and visited states.
BFS level 1: the 8 neighbours.  Level 2: their neighbours ... until we reach the target.
```

Treat the dead ends as already visited, so BFS never enters them.

#### 3. Kotlin Code

```kotlin
// Open the Lock (LeetCode 752)
fun openLock(deadends: Array<String>, target: String): Int {
    val visited = HashSet<String>(deadends.toList())          // dead ends count as visited
    if ("0000" in visited) return -1
    val queue = ArrayDeque<String>()
    queue.addLast("0000")
    visited.add("0000")
    var moves = 0

    while (queue.isNotEmpty()) {
        repeat(queue.size) {
            val code = queue.removeFirst()
            if (code == target) return moves
            for (i in 0 until 4) {
                for (delta in intArrayOf(1, 9)) {                    // +1 or -1 (mod 10)
                    val digit = (code[i] - '0' + delta) % 10
                    val next = code.substring(0, i) + digit + code.substring(i + 1)
                    if (visited.add(next)) queue.addLast(next)       // add() is false if already visited
                }
            }
        }
        moves++
    }
    return -1
}

// Word Ladder (LeetCode 127): the number of words in the shortest chain
fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
    val words = wordList.toHashSet()
    if (endWord !in words) return 0
    words.remove(beginWord)
    val queue = ArrayDeque<String>()
    queue.addLast(beginWord)
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
                    if (words.remove(next)) queue.addLast(next)      // remove = mark visited
                }
                chars[i] = original
            }
        }
        steps++
    }
    return 0
}

// Perfect Squares (LeetCode 279): the fewest perfect squares that sum to n (the state is the remaining number)
fun numSquares(n: Int): Int {
    val queue = ArrayDeque<Int>()
    val visited = BooleanArray(n + 1)
    queue.addLast(n)
    visited[n] = true
    var steps = 0
    while (queue.isNotEmpty()) {
        steps++
        repeat(queue.size) {
            val remaining = queue.removeFirst()
            var s = 1
            while (s * s <= remaining) {
                val next = remaining - s * s
                if (next == 0) return steps
                if (!visited[next]) { visited[next] = true; queue.addLast(next) }
                s++
            }
        }
    }
    return steps
}
```

Checks: `openLock(["0201","0101","0102","1212","2002"], "0202")` → `6`. `ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])` → `5`. `numSquares(12)` → `3` (4 + 4 + 4). `numSquares(13)` → `2` (4 + 9).

For Word Ladder, the faster two-sided search is in the Queue folder (note 18, bidirectional BFS).

#### 4. Complexity

| Problem | Time | Space |
|---|---|---|
| Open the Lock | `O(10⁴ · 4 · 2)` (at most 10,000 states) | `O(10⁴)` |
| Word Ladder (`n` words of length `L`) | `O(n · L · 26 · L)` (building each string costs `L`) | `O(n · L)` |
| Perfect Squares | `O(n · √n)` | `O(n)` |
| General | `O(number of states × moves per state)` | `O(number of states)` |

#### 5. Common Mistakes

1. **Putting too little in the state.** If the future depends on something (keys collected, steps left), include it, or you merge different situations.
2. **No visited set**, so states repeat and the search explodes.
3. **Marking visited when dequeuing.** Mark when you add the state.
4. **Counting steps off by one.** Decide whether the start counts as step 0 or 1.
5. **Using DFS** for the fewest moves.
6. **Mutable state objects** (arrays) as set keys. Use a `String`, `List` or `data class`.
7. **The target is not allowed** (not in the word list). Return `0` / `-1`.

#### 6. Say This in the Interview

1. "I will treat each state as a node and each allowed move as an edge. I need the fewest moves, so BFS."
2. "My state is ..., and its neighbours are ..."
3. "A visited set prevents repeating states. The number of states bounds the work."

#### 7. Quick Check

1. What is the "node" in Word Ladder?
2. Why BFS and not DFS?

<details>
<summary>Answers</summary>

1. A word.
2. The question asks for the fewest moves, and BFS reaches each state by the shortest route first.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 752 | Open the Lock (Medium) | lock codes are states |
| 127 | Word Ladder (Hard) | words are states |
| 433 | Minimum Genetic Mutation (Medium) | like Word Ladder |
| 279 | Perfect Squares (Medium) | numbers are states |
| 773 | Sliding Puzzle (Hard) | board strings are states |
| 365 | Water and Jug Problem (Medium) | `(a, b)` amounts are states |
| 864 | Shortest Path to Get All Keys (Hard) | state = `(row, col, keys)` |
