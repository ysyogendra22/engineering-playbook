# Heap for Scheduling / Processing by Priority

#### 1. Definition — Must Know

1. **Scheduling with a heap** means keeping tasks in a priority queue and always processing the **most important** one next.
2. "Important" can mean highest priority, earliest deadline, shortest duration, or earliest start time.
3. New tasks can arrive at any time. The heap puts them in the right place in `O(log n)`.

#### 2. Why It Is Used — Must Know

1. It is the direct, real-world use of a priority queue: job queues, operating system schedulers, event loops, simulations.
2. It avoids re-sorting the whole list every time a new task arrives.
3. In interviews it is the base for problems such as Task Scheduler, Meeting Rooms II, and Dijkstra.

#### 3. How It Works — Must Know

Tasks have a priority (higher number = more important) and arrive in this order:

```text
add("A", priority 1)
add("B", priority 5)
add("C", priority 5)
add("D", priority 3)

next() → B     (priority 5, added before C)
next() → C     (priority 5)
next() → D     (priority 3)
next() → A     (priority 1)
```

`B` and `C` have the same priority. A **sequence number** makes the older one come first.

#### 4. Core Concepts — Must Know

1. **Priority key** — the field the heap compares (priority, deadline, duration).
2. **Tie-break** — equal priorities have no guaranteed order. Add a counter to keep first-in-first-out among equals.
3. **Processing loop** — `while queue is not empty: take the best task, run it, add any new tasks`.
4. **Time-based scheduling** — keep tasks in a min-heap by start or end time (earliest first).
5. **Starvation** — low-priority tasks may wait forever if high-priority tasks keep arriving. Some systems raise the priority of waiting tasks over time ("aging").

#### 5. Algorithm — Must Know

```text
heap = priority queue ordered by (priority descending, arrival order ascending)

on new task:  heap.add(task)

worker loop:
    while heap is not empty:
        task = heap.poll()
        run(task)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
import java.util.PriorityQueue

data class Task(val name: String, val priority: Int, val order: Long)

class TaskQueue {

    private var counter = 0L

    private val heap = PriorityQueue<Task>(
        compareByDescending<Task> { it.priority }   // most important first
            .thenBy { it.order }                    // then oldest first
    )

    fun add(name: String, priority: Int) {
        heap.add(Task(name, priority, counter++))
    }

    fun next(): Task? = heap.poll()

    fun isEmpty() = heap.isEmpty()
}

// Usage
val queue = TaskQueue()
queue.add("A", 1); queue.add("B", 5); queue.add("C", 5); queue.add("D", 3)
while (!queue.isEmpty()) println(queue.next()!!.name)   // B, C, D, A
```

The `PriorityQueue` is not thread-safe. If several threads add and take tasks, use `PriorityBlockingQueue` or guard it with a lock.

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| Add a task | `O(log n)` |
| Take the next task | `O(log n)` |
| Look at the next task | `O(1)` |
| Space | `O(n)` |

Running `n` tasks through the queue costs `O(n log n)`.

#### 8. Common Scheduling Patterns — Must Know

1. **Task Scheduler** (LeetCode 621) — a max-heap of remaining counts, with a cooldown.
2. **Meeting Rooms II** — a min-heap of end times (see "Meeting Rooms / Scheduling with Heap").
3. **Dijkstra's shortest path** — always expand the closest node (`02-algorithm/07-Graph Algorithms`).
4. **Event simulation** — always handle the event with the earliest time.
5. **Shortest job first** — a min-heap by duration.
6. Your own app: a download or upload queue where user-visible items go before background items. Keep the comparator simple and tested.

#### 9. Edge Cases / Common Mistakes

1. Relying on first-in-first-out among equal priorities. Add a sequence number.
2. Changing a task's priority after it is in the heap. Remove it and add it again, or use lazy deletion.
3. Starvation of low-priority tasks.
4. Using a min-heap when a larger number means higher priority.
5. Polling an empty queue (`null`).
6. Using one `PriorityQueue` from several threads without protection.
7. A comparator that is not consistent (for example, one that depends on the current time). The heap order breaks.

#### 10. When to Use / When Not to Use

**Use when:**

1. Tasks differ in importance or deadline.
2. Tasks keep arriving while you work.

**Avoid when:**

1. All tasks have the same importance and order is by arrival. Use a plain queue.
2. The set is small and fixed. Sort once.
3. You must cancel or reprioritise tasks often. Add a map and lazy deletion.

#### 11. Related Topics

1. Priority Queue
2. Kotlin `PriorityQueue`
3. Meeting Rooms / Scheduling with Heap
4. Lazy Deletion with Heap
5. Queue (`01-data-structure/04-Queue`)
6. Greedy Algorithms (`02-algorithm/04-Greedy Algorithms`)

#### 12. Interview Must Remember

1. Process the **best item first**. Add a **sequence number** to break ties.
2. `O(log n)` per add and per take.
3. Do not change a priority in place.
4. Heaps are not thread-safe. Name the risk of starvation.
