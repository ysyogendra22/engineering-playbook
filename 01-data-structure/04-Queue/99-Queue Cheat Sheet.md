# Queue Cheat Sheet

> One-page revision for the night before an interview. The full explanations are in notes 01–19.

#### 1. Key Takeaways

1. A queue is **FIFO**: add at the back, remove from the front. All main operations are `O(1)`.
2. In Kotlin use `ArrayDeque`: `addLast` (enqueue), `removeFirst` (dequeue), `first()` (peek). **Never** use `list.removeAt(0)` (`O(n)`).
3. Think "queue" for **BFS**, **level by level**, **shortest path with equal costs**, **spreading from many sources**, and **sliding window max/min** (monotonic deque).
4. In BFS **mark visited when you enqueue**, not when you dequeue.
5. To process **one level at a time**, read `queue.size` **once** before the inner loop.
6. A deque (double-ended queue) gives `O(1)` at both ends. It powers **0-1 BFS** and the **monotonic queue**.
7. Say the brute force first, then the queue: "`O(n · k)` becomes `O(n)`", "all paths becomes BFS".

#### 2. Kotlin Operations and Complexity

| Action | Kotlin | If empty | Time |
|---|---|---|---|
| enqueue | `addLast(x)` | — | `O(1)` |
| dequeue | `removeFirst()` / `removeFirstOrNull()` | crash / `null` | `O(1)` |
| peek front | `first()` / `firstOrNull()` | crash / `null` | `O(1)` |
| push front (deque) | `addFirst(x)` | — | `O(1)` |
| pop back (deque) | `removeLast()` | crash | `O(1)` |
| size / empty | `size`, `isNotEmpty()` | — | `O(1)` |
| contains | `contains(x)` | — | `O(n)` |

`java.util.LinkedList` also works but `ArrayDeque` is faster and uses less memory.

#### 3. Patterns and How to Identify Them

| Signal in the question | Pattern | Complexity | Note |
|---|---|---|---|
| "level order", "row by row", "side view" | BFS with a level loop (`repeat(size)`) | `O(n)` | 05, 06 |
| "minimum steps / moves / changes" (equal cost) | BFS on states | `O(V + E)` | 07, 09 |
| grid: shortest path, 4 or 8 directions | grid BFS with a `dirs` array | `O(R·C)` | 09 |
| "distance to the nearest X", "spreads every minute" | multi-source BFS (all sources start at distance 0) | `O(R·C)` | 08 |
| edges cost 0 or 1 | 0-1 BFS (deque: front for 0, back for 1) | `O(V + E)` | 17 |
| start and target both known, big branching | bidirectional BFS | `O(b^(d/2))` | 18 |
| max / min of every window of size `k` | monotonic deque of indexes | `O(n)` | 13, 19 |
| DP needs the best of the last `k` states | monotonic deque | `O(n)` | 19 |
| add / remove at both ends | deque | `O(1)` | 12 |
| fixed-size buffer, reuse space | circular queue | `O(1)` | 11 |
| implement a queue with stacks | two stacks, lazy transfer | `O(1)` amortised | 14 |
| implement a stack with queues | one queue, rotate on `push` | `push` `O(n)` | 15 |
| producer and consumer threads | blocking queue | | 16 |

#### 4. Templates to Memorise

**BFS with levels (graph)**

```kotlin
val visited = BooleanArray(n); val queue = ArrayDeque<Int>()
queue.addLast(start); visited[start] = true
var steps = 0
while (queue.isNotEmpty()) {
    repeat(queue.size) {
        val u = queue.removeFirst()
        if (u == target) return steps
        for (v in graph[u]) if (!visited[v]) { visited[v] = true; queue.addLast(v) }
    }
    steps++
}
```

**Grid BFS**

```kotlin
val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
// neighbour: nr in 0 until rows && nc in 0 until cols && !visited[nr][nc] && grid[nr][nc] == 0
```

**Multi-source BFS**

```kotlin
for (r in 0 until rows) for (c in 0 until cols)
    if (grid[r][c] == 0) { dist[r][c] = 0; queue.addLast(intArrayOf(r, c)) }   // all sources first
// then run the normal BFS: dist[nr][nc] = dist[r][c] + 1
```

**0-1 BFS**

```kotlin
val dq = ArrayDeque<Int>(); dist[src] = 0; dq.addFirst(src)
while (dq.isNotEmpty()) {
    val u = dq.removeFirst()
    for ((v, w) in graph[u]) if (dist[u] + w < dist[v]) {
        dist[v] = dist[u] + w
        if (w == 0) dq.addFirst(v) else dq.addLast(v)
    }
}
```

**Sliding window maximum (monotonic deque)**

```kotlin
val dq = ArrayDeque<Int>()
for (i in nums.indices) {
    if (dq.isNotEmpty() && dq.first() <= i - k) dq.removeFirst()
    while (dq.isNotEmpty() && nums[dq.last()] < nums[i]) dq.removeLast()
    dq.addLast(i)
    if (i >= k - 1) result[i - k + 1] = nums[dq.first()]
}
```

**Queue with two stacks (amortised `O(1)`)**

```kotlin
fun push(x: Int) { inStack.addLast(x) }
fun pop(): Int { if (outStack.isEmpty()) while (inStack.isNotEmpty()) outStack.addLast(inStack.removeLast()); return outStack.removeLast() }
```

**Circular queue indexes**

```kotlin
tail = (tail + 1) % capacity        // enqueue
head = (head + 1) % capacity        // dequeue
```

#### 5. Brute Force to Optimized

| Problem | Brute force | Queue |
|---|---|---|
| Shortest path | try every path (exponential) | BFS `O(V + E)` |
| Nearest zero for every cell | BFS from each cell `O((R·C)²)` | multi-source BFS `O(R·C)` |
| Window maximum | scan each window `O(n·k)` | monotonic deque `O(n)` |
| Queue operations | `list.removeAt(0)` `O(n)` | `ArrayDeque` `O(1)` |
| Queue from stacks | move everything each time `O(n)` | lazy transfer `O(1)` amortised |
| Costs 0 or 1 | Dijkstra `O(E log V)` | 0-1 BFS `O(V + E)` |
| Long search with a known target | one BFS `O(b^d)` | bidirectional `O(b^(d/2))` |
| Producer and consumer | busy waiting | blocking queue |

#### 6. Common Mistakes and Edge Cases

1. **`list.removeAt(0)`** as a dequeue (`O(n)`).
2. **Marking visited on dequeue** (duplicates in the queue).
3. **Reading `queue.size` inside the level loop.**
4. **BFS on a weighted graph** (use Dijkstra, or 0-1 BFS for costs 0/1).
5. **No `visited`** on a graph with cycles (infinite loop).
6. **Forgetting to mark the start** as visited.
7. **Grid:** reading a cell before the bounds check, or wrong `rows`/`cols`.
8. **Monotonic deque:** storing values instead of indexes, or not removing expired indexes from the front.
9. **`removeFirst()` on an empty queue** (throws).
10. **Edge cases:** empty graph, start equals target, target unreachable (return `-1`), one node, all cells blocked.

#### 7. What to Say Out Loud

1. "I need the minimum number of steps and every move costs the same, so BFS gives the shortest path in `O(V + E)`."
2. "I mark a node visited when I add it to the queue, so each node is queued once."
3. "To separate levels I read the queue size before the inner loop."
4. "For the window maximum a monotonic deque keeps indexes in decreasing value order, so each index is added and removed once: `O(n)`."
5. "If the edges cost 0 or 1, a deque gives me 0-1 BFS in `O(V + E)`."

#### 8. Practice Order (Easy → Medium)

| Level | Question | Pattern |
|---|---|---|
| Easy | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | two stacks |
| Easy | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | rotate |
| Easy | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | queue as a window |
| Easy | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | level loop |
| Medium | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | level loop |
| Medium | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | last of each level |
| Medium | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | multi-source BFS |
| Medium | [01 Matrix](https://leetcode.com/problems/01-matrix/) | multi-source BFS |
| Medium | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | grid BFS, 8 directions |
| Medium | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | state BFS |
| Medium | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | multi-source (premium) |
| Medium | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | circular buffer |
| Medium | [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) | deque |
| Hard | [Word Ladder](https://leetcode.com/problems/word-ladder/) | state BFS / bidirectional |
| Hard | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | monotonic deque |
| Hard | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | 0-1 BFS |
