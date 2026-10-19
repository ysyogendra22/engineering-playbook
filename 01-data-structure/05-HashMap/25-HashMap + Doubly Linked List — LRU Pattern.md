# HashMap + Doubly Linked List — LRU Pattern

#### 1. Definition — Must Know

1. An **LRU cache** (Least Recently Used) holds at most `capacity` items. When it is full, it **removes the item that was used longest ago**.
2. Both `get(key)` and `put(key, value)` must run in **`O(1)`**.
3. The classic design: a **HashMap** (`key → node`) for instant lookup, plus a **doubly linked list** ordered by recent use (most recent at the front).

#### 2. Why It Is Used — Must Know

1. *LRU Cache* (LeetCode 146) is one of the most asked design questions.
2. Real systems use it: image caches, API response caches, memory caches in Android apps.
3. It combines two data structures, which interviewers like to see.

#### 3. How It Works — Must Know

Capacity 2.

```text
list order: most recent → least recent        map: key → node

put(1, A)        list: [1]
put(2, B)        list: [2, 1]
get(1)  → A      move 1 to the front:  [1, 2]
put(3, C)        full! remove the least recent (the back: 2), add 3 at the front:  [3, 1]
get(2)  → -1     2 was removed
```

Why a **doubly** linked list? To remove a node from the middle in `O(1)`, you need its `prev` and `next`. The map gives you the node, so no searching.

```text
head ⇄ [3] ⇄ [1] ⇄ tail          head and tail are dummy nodes (no edge cases)
```

#### 4. Core Concepts — Must Know

1. **Map:** `key → node`. Finds a node in `O(1)`.
2. **Doubly linked list:** keeps the order of use. **Front = most recent. Back = least recent.**
3. **Dummy `head` and `tail` nodes** remove the special cases for empty, first, and last positions.
4. **Every `get` and every `put` of an existing key moves the node to the front.**
5. **When full, evict `tail.prev`** and remove its key from the map. This is why the node stores its **key**.
6. **Three small helpers:** `remove(node)`, `addToFront(node)`, and move = remove + add.
7. **Kotlin shortcut:** `LinkedHashMap` with `accessOrder = true` already does this.
8. **Android:** `android.util.LruCache` is the ready-made class.

| Part | Job | Cost |
|---|---|---:|
| HashMap | find a node by key | `O(1)` |
| Doubly linked list | reorder and evict | `O(1)` |

#### 5. Algorithm — Must Know

```text
get(key):
    if key not in map: return -1
    node = map[key]; move node to the front; return node.value

put(key, value):
    if key in map: update value; move node to the front; return
    if map.size == capacity: evict tail.prev (remove it from the list and from the map)
    create node; add to the front; map[key] = node
```

#### 6. Kotlin Implementation — Must Know

**Manual version (what interviewers expect)**

```kotlin
class LRUCache(private val capacity: Int) {

    private class Node(val key: Int, var value: Int) {
        var prev: Node? = null
        var next: Node? = null
    }

    private val map = HashMap<Int, Node>()
    private val head = Node(0, 0)          // dummy: most recent side
    private val tail = Node(0, 0)          // dummy: least recent side

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
            val lru = tail.prev!!              // least recently used
            remove(lru)
            map.remove(lru.key)
        }
        val node = Node(key, value)
        map[key] = node
        addToFront(node)
    }
}
```

Trace with capacity 2: `put(1,1)`, `put(2,2)`, `get(1)` → `1`, `put(3,3)` (evicts 2), `get(2)` → `-1`, `put(4,4)` (evicts 1), `get(1)` → `-1`, `get(3)` → `3`, `get(4)` → `4`.

**Shortcut with `LinkedHashMap`**

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

Say in the interview: "I can use `LinkedHashMap`, but I will write the list by hand to show how it works."

#### 7. Time & Space Complexity — Must Know

| Operation | Time |
|---|---:|
| `get` | `O(1)` |
| `put` | `O(1)` |
| Space | `O(capacity)` |

#### 8. Common LRU / Cache Patterns — Must Know

1. **LRU Cache** (LeetCode 146).
2. **LFU Cache** (LeetCode 460) — least frequently used; a map of frequency → list.
3. **Design a time-based cache** — map of key → list of (time, value); binary search.
4. **TTL cache** — entries expire after a time; check on read or clean in the background.
5. **Android:** `LruCache<K, V>` for bitmaps, `ViewModel` caches, in-memory response caches.
6. **Thread safety:** wrap in `synchronized` or use a concurrent cache library. `LinkedHashMap` is not thread-safe.

#### 9. Edge Cases / Common Mistakes

1. `put` on an existing key must **update and move** the node. It must not evict.
2. Not storing the **key inside the node**, so you cannot remove the evicted key from the map.
3. Forgetting to remove the node from the list before re-adding it.
4. Wrong pointer order in `addToFront`.
5. Not using dummy nodes, which leads to many `null` checks and bugs.
6. Capacity `0` or `1`. (Capacity `1`: every new key evicts the previous one.)
7. `get` of a missing key must not change the order.
8. Using a singly linked list (removal from the middle is `O(n)`).
9. `LinkedHashMap` with `accessOrder = false` (the default) behaves like FIFO, not LRU.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need a fixed-size cache that keeps recent items.

**Use a library class when:**

1. In production Android code, use `LruCache`. Do not hand-write it.

**Avoid when:**

1. Access patterns are frequency-based. LFU may suit better.
2. The data is small and unbounded growth is acceptable.

#### 11. Related Topics

1. HashMap + Linked List Pattern
2. Linked List (`01-data-structure/02-LinkedList`)
3. LRU Cache (study separately)
4. Caching strategies (`05-system-design`)

#### 12. Interview Must Remember

1. **HashMap (`key → node`) + doubly linked list (order of use).**
2. Front = most recent. Evict `tail.prev`. Dummy head and tail.
3. Both `get` and `put` are **`O(1)`**.
4. `LinkedHashMap(capacity, 0.75f, true)` with `removeEldestEntry` is the shortcut.
