# Queue Fundamentals

> Start here. Read this note slowly once. Every other Queue note builds on it.

#### 1. What Is a Queue?

A **queue** is a list where you **add at the back** and **remove from the front**.

The first item you add is the first item that comes out. This is **FIFO**: **F**irst **I**n, **F**irst **O**ut.

Picture a line at a ticket counter. New people join at the back. The person at the front is served first.

A **stack** is the opposite (last in, first out).

#### 2. Words You Must Know

| Word | Meaning |
|---|---|
| **Enqueue** | add an item at the back |
| **Dequeue** | remove and return the item at the front |
| **Peek** | look at the front item, do not remove it |
| **Front / Back** | the oldest item / the newest item |
| **`O(1)`** | the work stays the same however big the queue is (fast) |

#### 3. How It Works

```text
Start: empty

enqueue(1)   →  [1]
enqueue(2)   →  [1, 2]
enqueue(3)   →  [1, 2, 3]       front = 1, back = 3
peek()       →  1               queue stays [1, 2, 3]
dequeue()    →  1               queue is now [2, 3]
dequeue()    →  2               queue is now [3]
```

Common kinds of queues you will meet:

| Kind | What is different |
|---|---|
| Simple queue | plain FIFO |
| **Deque** | add and remove at **both** ends (notes 12, 13) |
| **Circular queue** | a fixed-size array that wraps around (note 11) |
| **Priority queue** | the **best** item leaves first, not the oldest (this is a heap, see the Heap folder) |
| **Blocking queue** | waits when empty or full, used between threads (note 16) |

#### 4. Kotlin Code

Use `ArrayDeque`. Add at the **back**, remove from the **front**.

```kotlin
val queue = ArrayDeque<Int>()

queue.addLast(10)                  // enqueue
queue.addLast(20)
queue.addLast(30)

println(queue.first())             // peek → 10
println(queue.removeFirst())       // dequeue → 10
println(queue)                     // [20, 30]
println(queue.size)                // 2

// Popping an empty queue crashes. These versions return null instead:
println(queue.removeFirstOrNull()) // 20
println(queue.firstOrNull())       // 30
```

The loop you will write again and again:

```kotlin
while (queue.isNotEmpty()) {
    val item = queue.removeFirst()
    // handle item; you may add new items to the back with queue.addLast(...)
}
```

Do **not** use a list with `removeAt(0)` as a queue. It shifts every item, so it costs `O(n)` each time.

#### 5. How to Spot a Queue Problem

| If the question has... | Think... |
|---|---|
| "shortest path", "minimum number of steps/moves" (all steps cost the same) | BFS with a queue |
| "level by level", "by depth" | BFS with `repeat(queue.size)` |
| "spreads from many places at once" (rot, fire, water) | multi-source BFS |
| "process in the order they arrive" | plain queue |
| "max/min of every window" | monotonic queue (deque) |
| "last N events", fixed memory | circular queue |

#### 6. Complexity

| Action | Time |
|---|---|
| `addLast`, `removeFirst`, `first`, `isEmpty` | `O(1)` |
| Search for a value | `O(n)` |
| Memory for `n` items | `O(n)` |

#### 7. Common Mistakes

1. **Dequeue from an empty queue.** It crashes. Check `isNotEmpty()` or use `removeFirstOrNull()`.
2. **Using `removeAt(0)`** on a list as a dequeue. It is `O(n)`.
3. **Mixing up queue and stack.** Queue: `addLast` + `removeFirst`. Stack: `addLast` + `removeLast`.
4. **Changing a queue while looping over it** with `for (x in queue)`. It crashes. Use a `while` loop.

#### 8. Say This in the Interview

1. "The order matters (oldest first), so I will use a queue."
2. "For the fewest steps I will use BFS with a queue and a visited set."
3. "Each item is added once and removed once, so the time is `O(n)`."

#### 9. Quick Check

1. You enqueue `1`, `2`, `3` and then dequeue once. What is at the front?
2. Why is `list.removeAt(0)` a bad dequeue?

<details>
<summary>Answers</summary>

1. `2`.
2. It moves every other item one place to the left, so it takes `O(n)` time. `ArrayDeque.removeFirst()` is `O(1)`.

</details>

#### 10. Related LeetCode Questions (Often Asked)

Solve them in this order. Search by title if a number looks wrong.

**Start here — Easy**

| # | Question | Main idea | Note |
|---|---|---|---|
| 933 | Number of Recent Calls | drop old times from the front | 04 |
| 232 | Implement Queue using Stacks | two stacks | 14 |
| 225 | Implement Stack using Queues | rotate the queue | 15 |
| 733 | Flood Fill | BFS on a grid | 09 |

**Most often asked — Medium**

| # | Question | Main idea | Note |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | `repeat(queue.size)` | 06 |
| 199 | Binary Tree Right Side View | last node of each level | 06 |
| 994 | Rotting Oranges | multi-source BFS | 08 |
| 542 | 01 Matrix | multi-source BFS | 08 |
| 1091 | Shortest Path in Binary Matrix | grid BFS | 09 |
| 127 | Word Ladder | BFS on words | 07, 18 |
| 752 | Open the Lock | BFS on states | 07, 18 |
| 622 | Design Circular Queue | ring buffer | 11 |
| 641 | Design Circular Deque | ring buffer with two ends | 11, 12 |

**Hard — these separate strong candidates**

| # | Question | Main idea | Note |
|---|---|---|---|
| 239 | Sliding Window Maximum | monotonic deque | 13 |
| 862 | Shortest Subarray with Sum at Least K | monotonic deque on prefix sums | 19 |
| 1438 | Longest Subarray, Absolute Diff ≤ Limit | two monotonic deques | 19 |
| 2290 | Minimum Obstacle Removal to Reach Corner | 0-1 BFS | 17 |

**If you have little time, do these 8 first:** 102, 994, 542, 1091, 127, 239, 232, 622.
