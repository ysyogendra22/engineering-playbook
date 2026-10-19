# Queue Traversal / Processing

#### 1. Definition — Must Know

1. **Queue processing** means taking items out in order and handling them, one by one.
2. **Queue traversal** means looking at the items from front to back **without** removing them.
3. The core loop is `while (queue.isNotEmpty()) { removeFirst() … }`. Handling an item may **add new items** to the back.

#### 2. Why It Is Used — Must Know

1. It is the shape of almost every queue solution: BFS, simulations, task runners.
2. Simulation questions (recent calls, ticket queue, hot potato) test if you can keep the order and the counts right.
3. Knowing the difference between **reading** and **draining** a queue avoids bugs.

#### 3. How It Works — Must Know

*Number of Recent Calls* (LeetCode 933): count the requests in the last 3000 ms. The queue holds recent timestamps.

```text
ping(1)     queue [1]              remove anything older than 1-3000 → none        → 1
ping(100)   queue [1, 100]                                                          → 2
ping(3001)  queue [1, 100, 3001]   remove while front < 3001-3000=1 → none          → 3
ping(3002)  queue [1,100,3001,3002] remove while front < 2 → remove 1               → 3
```

Because times only increase, the old items are always at the **front**, so a queue is perfect.

*Hot potato / Josephus style:* **rotate** the queue by moving the front to the back.

```text
[A, B, C, D], pass 2 times and remove the holder:
rotate 2:  [C, D, A, B]   remove front C   → [D, A, B]
```

#### 4. Core Concepts — Must Know

1. **Drain loop:** take from the front until empty.
2. **Producing work while processing:** new items go to the back and are handled later.
3. **Expire old items:** `while (queue.isNotEmpty() && queue.first() < limit) queue.removeFirst()`.
4. **Rotate:** `queue.addLast(queue.removeFirst())`.
5. **Traverse without removing:** `for (x in queue)` or `queue.forEach { }`. The order is front to back.
6. **Batch:** `repeat(k) { removeFirst() }` to take `k` items.
7. **Counting time:** many simulation problems keep a counter that increases per "round".

| Goal | Pattern |
|---|---|
| Handle all items in order | drain loop |
| Keep only recent items | expire from the front |
| Round-robin | rotate |
| Level by level | `repeat(queue.size)` (see Level-by-Level Processing) |
| Just read | iterate with `for` |

#### 5. Algorithm — Must Know

```text
while queue is not empty:
    item = removeFirst()
    handle(item)
    for each new item produced: addLast(new item)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Number of Recent Calls
class RecentCounter {
    private val calls = ArrayDeque<Int>()

    fun ping(t: Int): Int {
        calls.addLast(t)
        while (calls.first() < t - 3000) calls.removeFirst()
        return calls.size
    }
}

// Moving average of the last `size` numbers
class MovingAverage(private val size: Int) {
    private val window = ArrayDeque<Int>()
    private var sum = 0L

    fun next(value: Int): Double {
        window.addLast(value)
        sum += value
        if (window.size > size) sum -= window.removeFirst()
        return sum.toDouble() / window.size
    }
}

// Hot potato: pass the potato `k` times, remove the holder, repeat
fun lastPlayer(players: List<String>, k: Int): String {
    val queue = ArrayDeque(players)
    while (queue.size > 1) {
        repeat(k) { queue.addLast(queue.removeFirst()) }
        queue.removeFirst()                      // the holder leaves
    }
    return queue.first()
}

// Time Needed to Buy Tickets (LeetCode 2073)
fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
    val queue = ArrayDeque<Int>()                // indexes of people
    for (i in tickets.indices) queue.addLast(i)
    var time = 0
    while (true) {
        val person = queue.removeFirst()
        time++
        tickets[person]--
        if (tickets[person] == 0) {
            if (person == k) return time
        } else {
            queue.addLast(person)
        }
    }
}

// Read without removing
fun printQueue(queue: ArrayDeque<Int>) {
    for (x in queue) print("$x ")
    println()
}
```

Checks: `RecentCounter` with pings `1, 100, 3001, 3002` → `1, 2, 3, 3`. `timeRequiredToBuy([2, 3, 2], 2)` → `6`.

#### 7. Time & Space Complexity — Must Know

| Task | Time | Space |
|---|---:|---:|
| Drain `n` items | `O(n)` | `O(n)` |
| Recent calls (each ping) | `O(1)` amortized | `O(window)` |
| Hot potato, `n` players, `k` passes | `O(n · k)` | `O(n)` |
| Print / traverse | `O(n)` | `O(1)` |

Each item is added once and removed once, so the total work of an expiring queue is `O(n)`.

#### 8. Common Processing Patterns — Must Know

1. **Number of Recent Calls** (LeetCode 933).
2. **Moving Average from Data Stream** (LeetCode 346, premium).
3. **Time Needed to Buy Tickets** (LeetCode 2073).
4. **Hot potato / Find the Winner of the Circular Game** (LeetCode 1823).
5. **Task processing** — a work queue where tasks create more tasks.
6. **Rate limiting** — keep timestamps of recent requests in a queue.
7. **Android:** a list of pending UI events, handled in order.

#### 9. Edge Cases / Common Mistakes

1. Calling `first()` on an empty queue inside the expire loop. The loop is safe when the new item is added first, otherwise check `isNotEmpty()`.
2. Wrong boundary on the time window (`<` vs `<=`).
3. Integer overflow in a running sum. Use `Long`.
4. Changing the queue inside `for (x in queue)`.
5. Rotating `k` times when `k` is far larger than the size. Use `k % size` (or know the result is the same).
6. Infinite loop when nothing ever leaves the queue.
7. Forgetting to re-add a person who still needs tickets.
8. Dividing by zero for an empty window.

#### 10. When to Use / When Not to Use

**Use when:**

1. Items arrive in time order and old ones must be dropped from the front.
2. You simulate people or tasks being served in turn.

**Avoid when:**

1. You need the item with the highest priority. Use a heap.
2. You need to remove from the middle often. Use a linked list with a map.

#### 11. Related Topics

1. Queue Operations
2. Level-by-Level Processing
3. BFS
4. Sliding Window (`03-leetcode-patterns`, topic 5)

#### 12. Interview Must Remember

1. **Drain loop: `while (queue.isNotEmpty()) { removeFirst() … }`.**
2. Expire old items from the **front**; rotate with `addLast(removeFirst())`.
3. Each item enters and leaves once, so the total is `O(n)`.
4. Do not change a queue while iterating it with `for`.
