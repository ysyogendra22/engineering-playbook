# Producer-Consumer Queue — Concept

#### 1. Definition — Must Know

1. In the **producer-consumer** pattern, some code (**producers**) creates work and puts it in a **queue**. Other code (**consumers**) takes work from the queue and processes it.
2. The queue sits **between** them, so they can run at different speeds and on different threads or coroutines.
3. A **blocking queue** makes this safe and simple: `take()` **waits** when the queue is empty, and `put()` **waits** when a bounded queue is full.

#### 2. Why It Is Used — Must Know

1. **Decoupling:** the producer does not need to know how the consumer works.
2. **Smoothing:** bursts of work wait in the queue instead of being lost or blocking the producer.
3. **Back-pressure:** a *bounded* queue slows the producer down when the consumer is too slow, so memory does not grow without limit.
4. Everywhere in Android: the main-thread `Looper` and `MessageQueue`, `WorkManager`, `Flow` and `Channel` buffers, download queues, analytics batching.

#### 3. How It Works — Must Know

```text
Producer 1 ─┐                              ┌─ Consumer 1
Producer 2 ─┼─►  [ job ][ job ][ job ]  ─►─┼─ Consumer 2
Producer 3 ─┘     (bounded queue)          └─ Consumer 3

queue empty → consumers wait (take blocks)
queue full  → producers wait (put blocks)
```

Steps with a blocking queue of size 2:

```text
producer: put(A)   queue [A]
producer: put(B)   queue [A, B]
producer: put(C)   queue is full → producer WAITS
consumer: take()   → A     queue [B]      ← wakes the producer
producer: put(C)   queue [B, C]
```

#### 4. Core Concepts — Must Know

1. **Producer / consumer:** many of each is allowed.
2. **Bounded vs unbounded queue:**

| Queue | Behaviour | Risk |
|---|---|---|
| Bounded | `put` waits (or fails) when full | slower producer, but memory is safe |
| Unbounded | never full | memory can grow until the app crashes |

3. **Blocking vs non-blocking:** `take()`/`put()` wait. `poll()`/`offer()` return at once (`null` / `false`).
4. **Thread safety:** a normal `ArrayDeque` is **not** safe for several threads. Use `BlockingQueue` classes.
5. **Ending the work:** send a special **poison pill** value, or close the channel, so consumers know to stop.
6. **Ordering:** a single FIFO queue keeps arrival order, but several consumers may finish out of order.
7. **Kotlin coroutines:** use a `Channel`. `send` suspends instead of blocking a thread.

| Tool | Use for |
|---|---|
| `ArrayBlockingQueue(n)` | bounded, threads |
| `LinkedBlockingQueue()` | optionally bounded, threads |
| `PriorityBlockingQueue` | priority order, threads |
| `ConcurrentLinkedQueue` | non-blocking, lock-free, threads |
| `Channel<T>(capacity)` | coroutines |
| `Flow` with `buffer()` | streams of values in coroutines |

#### 5. Algorithm — Must Know

```text
producer:  repeat: create item → queue.put(item)
consumer:  repeat: item = queue.take() → process item
stop:      producer puts a poison pill (or closes the channel); consumer stops when it sees it
```

#### 6. Kotlin Implementation — Must Know

**Threads with `BlockingQueue`**

```kotlin
import java.util.concurrent.ArrayBlockingQueue
import kotlin.concurrent.thread

fun main() {
    val queue = ArrayBlockingQueue<Int>(5)       // bounded: put() waits when 5 items are waiting
    val STOP = -1                                // poison pill

    val producer = thread {
        for (i in 1..10) {
            queue.put(i)                         // waits if the queue is full
            println("produced $i")
        }
        queue.put(STOP)
    }

    val consumer = thread {
        while (true) {
            val item = queue.take()              // waits if the queue is empty
            if (item == STOP) break
            println("consumed $item")
        }
    }

    producer.join()
    consumer.join()
}
```

**Coroutines with `Channel`**

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel

fun main() = runBlocking {
    val channel = Channel<Int>(capacity = 5)     // buffered, bounded

    val producer = launch {
        for (i in 1..10) {
            channel.send(i)                      // suspends when the buffer is full
        }
        channel.close()                          // tells the consumer: no more items
    }

    val consumer = launch {
        for (item in channel) {                  // ends when the channel is closed and empty
            println("consumed $item")
        }
    }

    producer.join()
    consumer.join()
}
```

**Android view of the same idea**

```kotlin
// A ViewModel receiving events from the UI and processing them one at a time
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.launch

class EventViewModel : ViewModel() {
    private val events = Channel<String>(Channel.BUFFERED)

    init {
        viewModelScope.launch {
            for (event in events) handle(event)   // single consumer, events in order
        }
    }

    fun post(event: String) { events.trySend(event) }   // producer: never blocks the UI thread

    private suspend fun handle(event: String) { /* work */ }
}
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `put` / `take` / `send` / `receive` | `O(1)` (plus waiting time) |
| Space | `O(capacity)` for bounded; `O(backlog)` for unbounded |

Throughput depends on the slower side. A bounded queue protects memory by slowing the producer.

#### 8. Common Producer-Consumer Patterns — Must Know

1. **Task / job queue** with a worker pool (`ExecutorService` has a queue inside).
2. **Event pipeline:** UI events → queue → one handler.
3. **Download / upload queue** with limited parallelism.
4. **Log or analytics batching:** producers add events, one consumer flushes in batches.
5. **Message brokers** at system scale (Kafka, RabbitMQ, SQS) — same idea across machines (`05-system-design`).
6. **Back-pressure** with bounded channels or `Flow.buffer`.
7. **Conflated channel:** keep only the latest value (UI state).

#### 9. Edge Cases / Common Mistakes

1. Using a plain `ArrayDeque` or `LinkedList` from several threads.
2. An **unbounded** queue with a slow consumer → out-of-memory.
3. Consumers that never stop. Use a poison pill or `close()`.
4. A poison pill with several consumers: send one per consumer.
5. Calling blocking `put()`/`take()` on the **main thread**. It freezes the UI.
6. Exceptions in a consumer silently killing it, while the producers keep adding.
7. Lost items when the app is killed (an in-memory queue is not durable). Use a persistent queue (`WorkManager`, database) for important work.
8. Deadlock when a consumer also produces into the same full queue.
9. Assuming consumers finish in the order of arrival when there are several.

#### 10. When to Use / When Not to Use

**Use when:**

1. Work arrives and is processed at different speeds or on different threads.
2. You need back-pressure, ordering, or a buffer.

**Avoid when:**

1. One piece of code can just call another directly.
2. Work must survive a process restart (use a durable queue).

#### 11. Related Topics

1. Queue Fundamentals
2. Circular Queue
3. Kotlin coroutines and Flow (`06-mobile-engineering`)
4. Message queues (`05-system-design`)
5. Concurrent / Lock-Free Queue (low priority)

#### 12. Interview Must Remember

1. **Producers `put`, consumers `take`; a bounded blocking queue gives back-pressure.**
2. Plain collections are not thread-safe. Use `BlockingQueue` or `Channel`.
3. Stop consumers with a poison pill or `channel.close()`.
4. Never block the Android main thread on `take()`.
