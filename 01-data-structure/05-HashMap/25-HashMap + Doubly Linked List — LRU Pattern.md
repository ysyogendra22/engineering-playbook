# HashMap + Doubly Linked List — LRU Pattern

> **LRU Cache** is one of the most asked FAANG design questions. Be able to write it from memory.

#### 1. What Is It?

An **LRU cache** (Least Recently Used) holds at most `capacity` items. When it is full and a new item arrives, it **removes the item that was used the longest time ago**.

Both `get(key)` and `put(key, value)` must run in **`O(1)`**.

The design:

- a **HashMap** `key → node` for instant lookup,
- a **doubly linked list** ordered by use: **front = most recent, back = least recent**.

Why a **doubly** linked list? To remove a node from the middle in `O(1)` you need its `prev` and `next`. The map gives you the node directly, so no searching.

Real uses: image caches, API response caches, `android.util.LruCache`.

#### 2. How It Works

Capacity 2. The list is shown from most recent to least recent.

```text
put(1, A)     list: [1]
put(2, B)     list: [2, 1]
get(1) → A    move 1 to the front:  [1, 2]
put(3, C)     full! remove the least recent (the back: 2), add 3 at the front:  [3, 1]
get(2) → -1   2 was removed
```

Picture of the list with two **dummy nodes** (`head` and `tail`) so there are no special cases:

```text
head ⇄ [3] ⇄ [1] ⇄ tail
```

Rules:

1. **`get`**: if the key exists, move its node to the front and return the value. Otherwise `-1`.
2. **`put` on an existing key**: update the value and move the node to the front.
3. **`put` on a new key**: if full, remove the node before `tail` (the least recent) and delete its key from the map. Then add the new node at the front.

Each node stores its **key** too, so you can delete the right entry from the map when evicting.

#### 3. Kotlin Code

**By hand (what interviewers expect)**

```kotlin
class LRUCache(private val capacity: Int) {

    private class Node(val key: Int, var value: Int) {
        var prev: Node? = null
        var next: Node? = null
    }

    private val map = HashMap<Int, Node>()
    private val head = Node(0, 0)            // dummy: the most recent side
    private val tail = Node(0, 0)            // dummy: the least recent side

    init {
        head.next = tail
        tail.prev = head
    }

    private fun remove(node: Node) {
        node.prev!!.next = node.next
        node.next!!.prev = node.prev
    }

    private fun addToFront(node: Node) {
        node.next = head.next
        node.prev = head
        head.next!!.prev = node
        head.next = node
    }

    fun get(key: Int): Int {
        val node = map[key] ?: return -1
        remove(node)
        addToFront(node)
        return node.value
    }

    fun put(key: Int, value: Int) {
        val existing = map[key]
        if (existing != null) {
            existing.value = value
            remove(existing)
            addToFront(existing)
            return
        }
        if (map.size == capacity) {
            val lru = tail.prev!!            // the least recently used
            remove(lru)
            map.remove(lru.key)
        }
        val node = Node(key, value)
        map[key] = node
        addToFront(node)
    }
}
```

Trace with capacity 2: `put(1,1)`, `put(2,2)`, `get(1)` → `1`, `put(3,3)` (removes 2), `get(2)` → `-1`, `put(4,4)` (removes 1), `get(1)` → `-1`, `get(3)` → `3`, `get(4)` → `4`.

**The shortcut with `LinkedHashMap`**

```kotlin
class LRUCacheShort(private val capacity: Int) {
    private val map = object : LinkedHashMap<Int, Int>(capacity, 0.75f, true) {   // true = access order
        override fun removeEldestEntry(eldest: MutableMap.MutableEntry<Int, Int>?): Boolean =
            size > capacity
    }

    fun get(key: Int): Int = map[key] ?: -1
    fun put(key: Int, value: Int) { map[key] = value }
}
```

Say in the interview: "I can use `LinkedHashMap`, but I will write the list by hand to show how it works." In Android, `android.util.LruCache` is the ready-made class.

#### 4. Complexity

| Action | Time |
|---|---|
| `get` | `O(1)` |
| `put` | `O(1)` |
| Memory | `O(capacity)` |

#### 5. Common Mistakes

1. **`put` on an existing key must update and move**, not evict.
2. **Not storing the key inside the node.** You cannot delete the evicted key from the map.
3. **Not removing the node from the list before adding it to the front.**
4. **Wrong pointer order in `addToFront`.**
5. **No dummy `head` and `tail`.** You get many `null` checks and bugs.
6. **Using a singly linked list.** Removing from the middle becomes `O(n)`.
7. **`LinkedHashMap` with the default access order (`false`)** behaves like FIFO, not LRU.
8. **A `get` of a missing key must not change the order.**

#### 6. Say This in the Interview

1. "I need `O(1)` lookup and `O(1)` reordering. A HashMap gives the lookup. A doubly linked list gives the reordering."
2. "The map goes from key to node. The front of the list is the most recent. I evict the node before the tail."
3. "I use dummy head and tail nodes to avoid edge cases."
4. "In production on Android I would use `LruCache`."

#### 7. Quick Check

1. Capacity 2: `put(1)`, `put(2)`, `get(1)`, `put(3)`. Which key is evicted?
2. Why does each node store its key?

<details>
<summary>Answers</summary>

1. Key `2`. After `get(1)`, key `1` is the most recent, so `2` is the least recent.
2. When you evict the last node, you need its key to remove the entry from the map.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 146 | LRU Cache (Medium) | this note |
| 460 | LFU Cache (Hard) | least frequently used: a map of frequency → list |
| 432 | All O(1) Data Structure (Hard) | map + linked list of buckets |
| 380 | Insert Delete GetRandom O(1) (Medium) | map + array |
| 981 | Time Based Key-Value Store (Medium) | map + binary search |
