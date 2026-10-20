# Queue Traversal / Processing

#### 1. What Is It?

**Processing** a queue means taking items out in order and handling them one by one. While handling an item, you may **add new items** to the back.

**Traversing** a queue means looking at the items front to back **without** removing them.

Interview questions that are really "queue simulations":

- keep only the **recent** events (Number of Recent Calls),
- pass something around a **circle** (hot potato),
- serve people in turns (Time Needed to Buy Tickets).

#### 2. How It Works

**Number of Recent Calls** (LeetCode 933): count the calls in the last 3000 ms. The queue holds the recent call times. Old times are at the **front**, so remove them from the front.

```text
ping(1)     queue [1]                       remove times < 1 - 3000 → none         → 1
ping(100)   queue [1, 100]                                                          → 2
ping(3001)  queue [1, 100, 3001]            remove times < 3001 - 3000 = 1 → none   → 3
ping(3002)  queue [1, 100, 3001, 3002]      remove times < 2 → remove 1             → 3
```

**Hot potato**: pass the potato `k` times, then the holder leaves. **Rotate** the queue to pass it.

```text
players [A, B, C, D], k = 2

rotate 2 times:  [C, D, A, B]      the front (C) holds the potato
C leaves:        [D, A, B]
```

#### 3. Kotlin Code

```kotlin
// Number of Recent Calls (LeetCode 933)
class RecentCounter {
    private val calls = ArrayDeque<Int>()

    fun ping(t: Int): Int {
        calls.addLast(t)
        while (calls.first() < t - 3000) calls.removeFirst()   // drop old calls
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

// Hot potato: the last player left wins
fun lastPlayer(players: List<String>, k: Int): String {
    val queue = ArrayDeque(players)
    while (queue.size > 1) {
        repeat(k) { queue.addLast(queue.removeFirst()) }       // pass the potato
        queue.removeFirst()                                    // the holder leaves
    }
    return queue.first()
}

// Time Needed to Buy Tickets (LeetCode 2073)
fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
    val queue = ArrayDeque<Int>()                              // positions of the people
    for (i in tickets.indices) queue.addLast(i)
    var time = 0
    while (true) {
        val person = queue.removeFirst()
        time++                                                 // each purchase takes 1 second
        tickets[person]--
        if (tickets[person] == 0) {
            if (person == k) return time                       // our person is done
        } else {
            queue.addLast(person)                              // go to the back of the line
        }
    }
}
```

Checks: `RecentCounter` with pings `1, 100, 3001, 3002` → `1, 2, 3, 3`. `timeRequiredToBuy([2, 3, 2], 2)` → `6`.

#### 4. Complexity

| Task | Time | Space |
|---|---|---|
| Drain `n` items | `O(n)` | `O(n)` |
| `ping` (amortized) | `O(1)` | `O(window)` |
| Hot potato, `n` players, `k` passes | `O(n · k)` | `O(n)` |

Each item is added once and removed once, so an "expire from the front" queue costs `O(n)` in total.

#### 5. Common Mistakes

1. **Wrong boundary** on the time window (`<` vs `<=`). Read the question.
2. **Calling `first()` on an empty queue** in the expire loop.
3. **Changing the queue inside `for (x in queue)`.**
4. **Integer overflow** in a running sum. Use `Long`.
5. **Forgetting to put a person back** in the line when they still need tickets.
6. **Dividing by zero** for an empty window.

#### 6. Say This in the Interview

1. "Events arrive in time order, so the oldest are at the front. I remove them from the front while they are too old."
2. "Each item enters and leaves once, so the total time is `O(n)`."
3. "To pass something around a circle I rotate: `addLast(removeFirst())`."

#### 7. Quick Check

1. In `RecentCounter`, why remove from the **front**?
2. What does rotating a queue of `[1, 2, 3]` once give?

<details>
<summary>Answers</summary>

1. Times only increase, so the oldest time is always at the front.
2. `[2, 3, 1]`.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 933 | Number of Recent Calls (Easy) | expire from the front |
| 2073 | Time Needed to Buy Tickets (Easy) | rotate and count |
| 1823 | Find the Winner of the Circular Game (Medium) | hot potato |
| 346 | Moving Average from Data Stream (Easy, premium) | window with a running sum |
| 649 | Dota2 Senate (Medium) | two queues of indexes |
