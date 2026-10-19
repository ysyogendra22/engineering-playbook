# Designing a Simple HashMap — Concept

#### 1. Definition — Must Know

1. Designing a simple HashMap means building `put`, `get` and `remove` yourself, with an **array of buckets** and **chaining**.
2. It is the problem *Design HashMap* (LeetCode 706).
3. It tests whether you understand hashing, buckets, collisions, and resizing. It is **not** about writing production code.

#### 2. Why It Is Used — Must Know

1. It is a common design question, often as a follow-up to "how does `HashMap` work?".
2. Writing it makes hashing and collisions easy to remember.
3. A short, correct version is enough in interviews.

#### 3. How It Works — Must Know

```text
buckets (array of lists), size 5

put(7, "x"):   index = hash(7) % 5 = 2  → bucket 2: [(7, x)]
put(12, "y"):  index = 12 % 5 = 2       → bucket 2: [(7, x), (12, y)]     ← collision, chained
get(12):       index 2 → walk the list → key 12 found → "y"
remove(7):     index 2 → delete (7, x) → bucket 2: [(12, y)]
```

Steps for every operation:

```text
1. index = (hashCode & 0x7fffffff) % bucketCount
2. walk the list in that bucket and compare keys with equals()
3. put: replace or append.  get: return or null.  remove: delete if found.
```

**Resizing:** when `size > bucketCount × 0.75`, create a bucket array twice as large and place every entry again (**rehash**). This keeps the chains short.

#### 4. Core Concepts — Must Know

1. **Bucket array:** `Array<MutableList<Entry>>`.
2. **Entry:** holds `key` and `value`.
3. **Index:** `(key.hashCode() and 0x7fffffff) % buckets.size` — the mask removes the sign bit so the index is never negative.
4. **Chaining:** each bucket is a small list of entries that landed there.
5. **Load factor 0.75:** when exceeded, double the buckets and re-place all entries.
6. **Sizes:** a prime number of buckets spreads keys better with a simple `%`. Java uses a power of two with bit masking.
7. **Update vs insert:** `put` with an existing key replaces its value; `size` changes only for new keys.

| Choice | Simple version | Production (Java) |
|---|---|---|
| Bucket size | fixed prime (e.g. 1009) | power of 2, grows |
| Collisions | list per bucket | list, then tree at 8+ entries |
| Resize | optional in interviews | yes, at 0.75 load |
| Null keys | not handled | one `null` key allowed |

#### 5. Algorithm — Must Know

```text
put(key, value):
    bucket = buckets[indexFor(key)]
    for entry in bucket: if entry.key == key: entry.value = value; return
    bucket.add(Entry(key, value)); size++
    if size > buckets.size * 0.75: resize()

get(key):
    for entry in buckets[indexFor(key)]: if entry.key == key: return entry.value
    return null

remove(key):
    delete the entry with that key from its bucket (size-- if found)
```

#### 6. Kotlin Implementation — Must Know

**LeetCode style (Int keys, fixed buckets)**

```kotlin
class MyHashMap {
    private class Entry(val key: Int, var value: Int)

    private val buckets = Array(1009) { mutableListOf<Entry>() }
    private fun index(key: Int) = key % 1009           // keys are non-negative in this problem

    fun put(key: Int, value: Int) {
        val bucket = buckets[index(key)]
        for (e in bucket) {
            if (e.key == key) { e.value = value; return }
        }
        bucket.add(Entry(key, value))
    }

    fun get(key: Int): Int {
        for (e in buckets[index(key)]) if (e.key == key) return e.value
        return -1
    }

    fun remove(key: Int) {
        buckets[index(key)].removeAll { it.key == key }
    }
}
```

**Generic version with resizing**

```kotlin
class SimpleHashMap<K, V>(initialCapacity: Int = 16) {

    private class Node<K, V>(val key: K, var value: V)

    private var buckets = Array(initialCapacity) { mutableListOf<Node<K, V>>() }
    var size = 0
        private set

    private fun indexFor(key: K, bucketCount: Int): Int =
        (key.hashCode() and 0x7fffffff) % bucketCount

    operator fun get(key: K): V? {
        for (node in buckets[indexFor(key, buckets.size)]) {
            if (node.key == key) return node.value
        }
        return null
    }

    operator fun set(key: K, value: V) {
        val bucket = buckets[indexFor(key, buckets.size)]
        for (node in bucket) {
            if (node.key == key) { node.value = value; return }
        }
        bucket.add(Node(key, value))
        size++
        if (size > buckets.size * 3 / 4) resize()
    }

    fun remove(key: K): V? {
        val iterator = buckets[indexFor(key, buckets.size)].iterator()
        while (iterator.hasNext()) {
            val node = iterator.next()
            if (node.key == key) {
                iterator.remove()
                size--
                return node.value
            }
        }
        return null
    }

    private fun resize() {
        val old = buckets
        buckets = Array(old.size * 2) { mutableListOf<Node<K, V>>() }
        for (bucket in old) {
            for (node in bucket) {
                buckets[indexFor(node.key, buckets.size)].add(node)
            }
        }
    }
}

// Usage
val m = SimpleHashMap<String, Int>()
m["a"] = 1
m["a"] = 2
println(m["a"])       // 2
println(m.size)       // 1
m.remove("a")
println(m["a"])       // null
```

#### 7. Time & Space Complexity — Must Know

| Operation | Average | Worst |
|---|---:|---:|
| `put` | `O(1)` amortized | `O(n)` (all keys in one bucket, or a resize) |
| `get` | `O(1)` | `O(n)` |
| `remove` | `O(1)` | `O(n)` |
| Resize | `O(n)` | — |
| Space | `O(n + buckets)` | — |

#### 8. Common Design Ideas — Must Know

1. **Design HashMap** (LeetCode 706) and **Design HashSet** (LeetCode 705).
2. **Bucket array + chaining** — the standard answer.
3. **Open addressing** (probing) — an alternative; mention it, do not code it unless asked.
4. **Resize and rehash** at load factor `0.75`.
5. **Related designs:** LRU Cache, LFU Cache, Insert Delete GetRandom O(1) (map + array), Time-based Key-Value Store.
6. **Thread safety:** `ConcurrentHashMap` splits locks per bucket.

#### 9. Edge Cases / Common Mistakes

1. Negative indices from `hashCode() % n`. Mask the sign bit first.
2. `put` on an existing key adds a second entry. Always search the bucket first.
3. Increasing `size` on update.
4. `remove` while iterating without an `Iterator` (use `iterator.remove()` or `removeAll`).
5. Not handling a missing key (`get` should return `null` / `-1`).
6. Forgetting to resize, so chains grow and everything becomes `O(n)`.
7. Using `==` on keys. In Kotlin `==` already calls `equals()`, but `===` does not.
8. Using a bucket count of `0`.
9. Null keys: decide and state how you handle them (usually "not supported").

#### 10. When to Use / When Not to Use

**Use this knowledge when:**

1. The interviewer asks you to design or explain a HashMap.

**Do not:**

1. Write your own map in real code. Use the standard one.
2. Spend interview time on open addressing or advanced hashing unless asked.

#### 11. Related Topics

1. Hashing / Hash Function — Basic Concept
2. Collision Handling — Basic Concept
3. HashMap + Doubly Linked List — LRU Pattern
4. Linked List (`01-data-structure/02-LinkedList`)

#### 12. Interview Must Remember

1. **Array of buckets + chaining. Index = `(hash and 0x7fffffff) % size`.**
2. `put`: search the bucket first, replace or append.
3. Resize at load factor `0.75`: double the buckets and re-place all entries.
4. Say average `O(1)`, worst `O(n)`.
