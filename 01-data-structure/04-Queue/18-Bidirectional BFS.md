# Bidirectional BFS

#### 1. What Is It?

**Bidirectional BFS** runs BFS from the **start** and from the **target** at the same time. It stops when the two searches **meet**.

It needs:

- a known target,
- moves that can be **reversed** (an undirected graph, or a way to go backwards).

Why it is faster: a normal BFS explores about `b^d` nodes (`b` = how many neighbours each node has, `d` = distance). Two searches, each going half the way, explore about `2 × b^(d/2)`.

Example: `b = 10`, `d = 6`. One-sided: `1,000,000` nodes. Bidirectional: about `2,000`.

```text
One-sided:      start ●────────────────────────────● target     (one big circle)
Bidirectional:  start ●─────────●●─────────● target             (two small circles that meet)
```

#### 2. How It Works

Keep two sets: `front` (the frontier from the start) and `back` (the frontier from the target). Each round:

1. **Always expand the smaller set.** This keeps the work small.
2. For each node in it, look at its neighbours.
3. If a neighbour is in the **other** set, the searches have met. The answer is the steps so far + 1.
4. Otherwise, mark the neighbour visited and put it in the next frontier.

Word Ladder (`hit → cog`) with words `hot, dot, dog, lot, log, cog`:

```text
front = {hit}                   back = {cog}
expand front → {hot}                                      steps 2
front = {hot}                   back = {cog}
expand front → {dot, lot}                                 steps 3
front is bigger than back → swap: front = {cog}, back = {dot, lot}
expand front (cog) → {dog, log}                           steps 4
now expand {dog, log}: dog's neighbour dot is in back → they MEET

answer = 5
```

#### 3. Kotlin Code

```kotlin
// Word Ladder with bidirectional BFS (LeetCode 127): number of words in the shortest chain
fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
    val words = wordList.toHashSet()
    if (endWord !in words) return 0
    words.remove(beginWord)
    words.remove(endWord)                          // the word set doubles as the "unvisited" set

    var front = hashSetOf(beginWord)
    var back = hashSetOf(endWord)
    var steps = 1

    while (front.isNotEmpty() && back.isNotEmpty()) {
        if (front.size > back.size) {              // always expand the smaller side
            val temp = front; front = back; back = temp
        }
        val next = HashSet<String>()
        for (word in front) {
            val chars = word.toCharArray()
            for (i in chars.indices) {
                val original = chars[i]
                for (c in 'a'..'z') {
                    if (c == original) continue
                    chars[i] = c
                    val candidate = String(chars)
                    if (candidate in back) return steps + 1           // the two searches met
                    if (words.remove(candidate)) next.add(candidate)  // new word: visit it once
                }
                chars[i] = original
            }
        }
        front = next
        steps++
    }
    return 0
}

// Any undirected graph: shortest distance between two nodes
fun bidirectionalDistance(graph: List<List<Int>>, src: Int, dst: Int): Int {
    if (src == dst) return 0
    var front = hashSetOf(src)
    var back = hashSetOf(dst)
    val visited = hashSetOf(src, dst)
    var distance = 0

    while (front.isNotEmpty() && back.isNotEmpty()) {
        if (front.size > back.size) { val t = front; front = back; back = t }
        distance++
        val next = HashSet<Int>()
        for (node in front) {
            for (neighbour in graph[node]) {
                if (neighbour in back) return distance
                if (visited.add(neighbour)) next.add(neighbour)
            }
        }
        front = next
    }
    return -1
}
```

Check: `ladderLength("hit", "cog", [hot, dot, dog, lot, log, cog])` → `5`. If `cog` is not in the list → `0`.

#### 4. Complexity

| | Time | Space |
|---|---|---|
| One-sided BFS | `O(b^d)` | `O(b^d)` |
| **Bidirectional BFS** | **`O(b^(d/2))`** | `O(b^(d/2))` |

In the worst case (a graph that is just a line), the gain is small.

#### 5. Common Mistakes

1. **Checking for the meeting only when taking a node out.** Check when you **generate** a neighbour.
2. **Not expanding the smaller side**, so the speed-up is lost.
3. **Off-by-one in `steps`.** Decide whether you count words or moves.
4. **Not removing visited words**, so the frontier grows forever.
5. **The end word is not in the list.** The answer is `0`.
6. **Using it when moves are one-way** and you did not build the reverse edges.
7. **Forgetting to put the target into the `back` set** at the start.

#### 6. Say This in the Interview

1. "Plain BFS explores about `b^d` nodes. Searching from both ends explores about `b^(d/2)`."
2. "I keep two frontiers, always expand the smaller one, and stop when a neighbour is in the other frontier."
3. "It needs a known target and reversible moves."

#### 7. Quick Check

1. Why expand the smaller frontier?
2. Name two things bidirectional BFS needs.

<details>
<summary>Answers</summary>

1. The work in a round depends on the size of the frontier, so a smaller frontier means less work.
2. A known target, and moves that can be reversed.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 127 | Word Ladder (Hard) | this note |
| 752 | Open the Lock (Medium) | start `0000` and a known target |
| 433 | Minimum Genetic Mutation (Medium) | like Word Ladder |
| 773 | Sliding Puzzle (Hard) | start board and goal board |
| 1197 | Minimum Knight Moves (Medium, premium) | knight moves on an infinite board |
