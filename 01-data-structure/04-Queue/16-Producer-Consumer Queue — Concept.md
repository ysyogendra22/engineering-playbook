# Producer-Consumer Queue — Concept

> Asked in Android interviews and in system design. Know the idea and the Kotlin tools.

#### 1. What Is It?

In the **producer-consumer** pattern:

- **Producers** create work and put it in a **queue**.
- **Consumers** take work from the queue and process it.

The queue sits **between** them, so they can run at different speeds, on different threads or coroutines.

A **blocking queue** makes this simple and safe:

- `take()` **waits** if the queue is empty,
- `put()` **waits** if a bounded queue is full.

Why it is used:

- **Decoupling:** the producer does not need to know how the work is done.
- **Smoothing:** a burst of work waits in the queue instead of being lost.
- **Back-pressure:** a *bounded* queue slows a fast producer down, so memory does not grow without limit.

You already use this in Android: the main-thread `Looper` and `MessageQueue`, `WorkManager`, and `Channel` / `Flow` buffers.

#### 2. How It Works

```text
Producer 1 ─┐                              ┌─ Consumer 1
Producer 2 ─┼─►  [ job ][ job ][ job ]  ─►─┤
Producer 3 ─┘     (bounded queue, size 3)  └─ Consumer 2

queue empty → consumers wait
queue full  → producers wait
```

With a blocking queue of size 2:

```text
producer: put(A)    queue [A]
producer: put(B)    queue [A, B]
producer: put(C)    queue is full → the producer WAITS
consumer: take()    returns A      queue [B]      → the producer wakes up
producer: put(C)    queue [B, C]
```

A plain `ArrayDeque` is **not safe** when several threads use it. Use these instead:

| Tool | Use for |
|---|---|
| `ArrayBlockingQueue(n)` | bounded queue, threads |
| `LinkedBlockingQueue()` | blocking queue, threads |
| `ConcurrentLinkedQueue` | non-blocking, threads |
| `Channel<T>(capacity)` | **coroutines** (`send` suspends instead of blocking a thread) |

To stop the consumers, send a special **poison pill** value, or **close** the channel.

#### 3. Kotlin Code

**Threads with `BlockingQueue`**

```kotlin
import java.util.concurrent.ArrayBlockingQueue
import kotlin.concurrent.thread

fun main() {
    val queue = ArrayBlockingQueue<Int>(5)        // put() waits when 5 items are waiting
    val STOP = -1                                  // poison pill

    val producer = thread {
        for (i in 1..10) {
            queue.put(i)                           // waits if the queue is full
            println("produced $i")
        }
        queue.put(STOP)
    }

    val consumer = thread {
        while (true) {
            val item = queue.take()                // waits if the queue is empty
            if (item == STOP) break
            println("consumed $item")
        }
    }

    producer.join()
    consumer.join()
}
```

**Coroutines with `Channel`** (what you would use in Android)

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel

fun main() = runBlocking {
    val channel = Channel<Int>(capacity = 5)       // bounded buffer

    val producer = launch {
        for (i in 1..10) channel.send(i)           // suspends when the buffer is full
        channel.close()                            // tells the consumer: no more items
    }

    val consumer = launch {
        for (item in channel) {                    // ends when the channel is closed and empty
            println("consumed $item")
        }
    }

    producer.join()
    consumer.join()
}
```

Android: a `ViewModel` that handles UI events one at a time, in order.

```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.launch

class EventViewModel : ViewModel() {
    private val events = Channel<String>(Channel.BUFFERED)

    init {
        viewModelScope.launch {
            for (event in events) handle(event)    // one consumer, events handled in order
        }
    }

    fun post(event: String) { events.trySend(event) }   // does not block the UI thread

    private suspend fun handle(event: String) { /* work */ }
}
```

#### 4. Complexity

| Action | Time |
|---|---|
| `put`, `take`, `send`, `receive` | `O(1)` (plus any waiting time) |
| Memory | `O(capacity)` for a bounded queue, `O(backlog)` for an unbounded one |

#### 5. Common Mistakes

1. **A plain `ArrayDeque` shared by threads.** It is not thread-safe.
2. **An unbounded queue with a slow consumer.** Memory grows until the app crashes.
3. **Consumers that never stop.** Use a poison pill (one per consumer) or `close()`.
4. **Calling blocking `put()` / `take()` on the Android main thread.** It freezes the UI.
5. **Losing items when the process dies.** An in-memory queue is not durable. For important work use `WorkManager` or a database.
6. **A consumer crashing silently** while producers keep adding.

#### 6. Say This in the Interview

1. "A queue between producers and consumers decouples them and absorbs bursts."
2. "I would make the queue bounded, so a slow consumer applies back-pressure instead of running out of memory."
3. "Plain collections are not thread-safe, so I use a `BlockingQueue` on threads or a `Channel` with coroutines."
4. "To stop, I close the channel or send a poison pill."

#### 7. Quick Check

1. What does `put()` do on a full `ArrayBlockingQueue`?
2. Why prefer a bounded queue?

<details>
<summary>Answers</summary>

1. It waits (blocks) until a consumer makes space.
2. A fast producer cannot fill memory. It is slowed down to the speed of the consumer (back-pressure).

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1188 | Design Bounded Blocking Queue (Medium, premium) | blocking queue with locks |
| 1114 | Print in Order (Easy) | thread ordering |
| 1115 | Print FooBar Alternately (Medium) | two threads taking turns |
| 622 | Design Circular Queue (Medium) | the buffer inside many bounded queues |
