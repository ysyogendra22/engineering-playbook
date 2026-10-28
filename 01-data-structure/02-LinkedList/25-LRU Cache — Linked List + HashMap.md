# LRU Cache — Linked List + HashMap

> One of the most asked design questions in FAANG interviews. It joins two structures: a **HashMap** for fast lookup and a **doubly linked list** for fast ordering.

#### 1. What Is It?

An **LRU (Least Recently Used) cache** holds at most `capacity` items. When it is full and you add a new item, it removes the item that was **used longest ago**.

You must support, both in **`O(1)`**:

- `get(key)` — return the value, or `-1` if missing. The key becomes the **most recent**.
- `put(key, value)` — insert or update. The key becomes the most recent. If the cache is over `capacity`, remove the **least recent** key.

This is *LRU Cache* (LeetCode 146). On Android the same idea is `android.util.LruCache`, used for image caches.

#### 2. How It Works

Why two structures?

| Need | Structure | Why |
|---|---|---|
| find a key in `O(1)` | `HashMap<Int, Node>` | direct lookup |
| move a node to the front, and remove the oldest, in `O(1)` | doubly linked list | a node can be removed if you hold it (note 17) |

The map stores `key → node`. The list keeps the order: **front = most recent, back = least recent.** Use sentinel `head` and `tail` nodes.

```text
head ⇄ [3] ⇄ [1] ⇄ [2] ⇄ tail
        ↑ most recent         ↑ least recent (evict this)
```

**get(key):** look up the node in the map. Move it to the front. Return its value.
**put(key, value):**
- if the key exists: update the value, move to the front;
- else: if full, remove the node before `tail` (and from the map); then add a new node at the front and in the map.

Trace with `capacity = 2`:

```text
put(1,1)   list: 1
put(2,2)   list: 2, 1
get(1)  →1 list: 1, 2
put(3,3)   full: evict 2.   list: 3, 1
get(2)  →-1
put(4,4)   full: evict 1.   list: 4, 3
get(1)  →-1
get(3)  →3  list: 3, 4
get(4)  →4  list: 4, 3
```

#### 3. Brute Force vs Optimized

| Approach | get | put | Note |
|---|---|---|---|
| `ArrayList` of pairs, scan to find, remove, re-add | `O(n)` | `O(n)` | simple, too slow |
| `HashMap` + a list of keys (remove a key from the list by value) | `O(1)` / `O(n)` | `O(n)` | the list search is slow |
| **HashMap + doubly linked list** | **`O(1)`** | **`O(1)`** | the expected answer |

```kotlin
class LRUCacheBrute(private val capacity: Int) {
    private val keys = ArrayList<Int>()                      // front = least recent
    private val map = HashMap<Int, Int>()

    fun get(key: Int): Int {
        if (key !in map) return -1
        keys.remove(key); keys.add(key)                      // O(n): search and shift
        return map[key]!!
    }

    fun put(key: Int, value: Int) {
        if (key in map) keys.remove(key)
        else if (map.size == capacity) { map.remove(keys.removeAt(0)) }
        keys.add(key)
        map[key] = value
    }
}
```

`keys.remove(key)` on `ArrayList<Int>` removes the **value** `key` (not an index), because `key` is an `Int` object here. It costs `O(n)`.

#### 4. Kotlin Code

```kotlin
class LRUCache(private val capacity: Int) {

    private class Node(val key: Int, var value: Int) {
        var prev: Node? = null
        var next: Node? = null
    }

    private val map = HashMap<Int, Node>()
    private val head = Node(0, 0)                            // sentinel: the front is head.next
    private val tail = Node(0, 0)                            // sentinel: the back is tail.prev

    init {
        head.next = tail
        tail.prev = head
    }

    private fun remove(node: Node) {
        node.prev!!.next = node.next
        node.next!!.prev = node.prev
    }

    private fun addToFront(node: Node) {
        node.prev = head
        node.next = head.next
        head.next!!.prev = node
        head.next = node
    }

    fun get(key: Int): Int {
        val node = map[key] ?: return -1
        remove(node)
        addToFront(node)                                     // now the most recent
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
            val lru = tail.prev!!                            // the least recently used
            remove(lru)
            map.remove(lru.key)                              // that is why the node stores its key
        }
        val node = Node(key, value)
        map[key] = node
        addToFront(node)
    }
}
```

Check (the trace above):

```kotlin
val cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
println(cache.get(1))      // 1
cache.put(3, 3)            // evicts key 2
println(cache.get(2))      // -1
cache.put(4, 4)            // evicts key 1
println(cache.get(1))      // -1
println(cache.get(3))      // 3
println(cache.get(4))      // 4
```

**Kotlin / Android shortcut.** `LinkedHashMap` keeps an order and can sort by *access*. In an interview, build it by hand first. Then you may mention this:

```kotlin
class LRUCacheShort(private val capacity: Int) :
    LinkedHashMap<Int, Int>(capacity, 0.75f, true) {          // true = access order
    override fun removeEldestEntry(eldest: MutableMap.MutableEntry<Int, Int>?): Boolean =
        size > capacity
}
// get: cache[key] ?: -1       put: cache[key] = value
```

#### 5. Complexity

| | Time | Space |
|---|---|---|
| `get` | `O(1)` | — |
| `put` | `O(1)` | — |
| Whole cache | — | `O(capacity)` |

#### 6. Common Mistakes

1. **A singly linked list.** You cannot remove a node in `O(1)` without its `prev`.
2. **The node does not store its key.** When you evict a node you cannot remove it from the map.
3. **Not moving the node to the front on `get`.** A read counts as a use.
4. **On `put` with an existing key,** adding a second node instead of updating.
5. **Evicting before checking for an existing key.** Update first. Evict only for a new key.
6. **No sentinel nodes,** which causes `null` checks at the ends.
7. **Wrong order of pointer updates in `addToFront`.**

#### 7. Say This in the Interview

1. "I need `O(1)` lookup and `O(1)` reorder. A HashMap gives lookup. A doubly linked list gives removal and move-to-front without scanning. So I keep a map from key to node."
2. "Front is the most recent, back is the least recent. On `get` and `put` I move the node to the front. When over capacity I remove the node before the tail and its key from the map."
3. "In production on Android I would use `LruCache` or `LinkedHashMap` with access order."

#### 8. Quick Check

1. Why does each node store its key?
2. What happens on `get` for an existing key?

<details>
<summary>Answers</summary>

1. When you evict the last node, you must also delete its key from the map.
2. The node is removed from its place and added to the front, then its value is returned.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | this note |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) (Hard) | the same idea with frequency lists |
| 432 | [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) (Hard) | map + linked buckets |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) | list navigation |
| 706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) (Easy) | build the map yourself |
