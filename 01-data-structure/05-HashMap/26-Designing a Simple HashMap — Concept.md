# Designing a Simple HashMap — Concept

> A common design question, often asked as "how does HashMap work inside?". A short, correct version is enough.

#### 1. What Is It?

Designing a simple HashMap means writing `put`, `get` and `remove` yourself, using:

- an **array of buckets**,
- a **hash function** that picks the bucket,
- **chaining**: each bucket is a small list of pairs.

This is *Design HashMap* (LeetCode 706).

It tests whether you understand hashing, buckets, collisions and resizing. It is **not** about writing production code.

#### 2. How It Works

```text
buckets (array of lists), 5 buckets

put(7, "x"):    index = 7 % 5 = 2   → bucket 2: [(7, x)]
put(12, "y"):   index = 12 % 5 = 2  → bucket 2: [(7, x), (12, y)]      ← a collision, chained
get(12):        index 2 → walk the list → key 12 found → "y"
remove(7):      index 2 → delete (7, x) → bucket 2: [(12, y)]
```

For every operation:

1. `index = (hashCode and 0x7fffffff) % bucketCount` (the mask removes the sign, so the index is never negative).
2. Walk the list in that bucket and compare keys with `equals()`.
3. **put:** replace the value if the key exists, otherwise add a new pair. **get:** return the value or `null`. **remove:** delete the pair if found.

**Resizing:** when `size > bucketCount × 0.75`, create a bucket array twice as big and place every pair again (this is called **rehashing**). This keeps the lists short.

#### 3. Kotlin Code

**The LeetCode version (Int keys, a fixed number of buckets)**

```kotlin
class MyHashMap {
    private class Entry(val key: Int, var value: Int)

    private val buckets = Array(1009) { mutableListOf<Entry>() }      // 1009 is a prime number
    private fun index(key: Int) = key % 1009

    fun put(key: Int, value: Int) {
        val bucket = buckets[index(key)]
        for (e in bucket) {
            if (e.key == key) { e.value = value; return }              // update
        }
        bucket.add(Entry(key, value))                                  // new pair
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

**A generic version with resizing**

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
        if (size > buckets.size * 3 / 4) resize()                      // load factor 0.75
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

#### 4. Complexity

| Action | Average | Worst |
|---|---|---|
| `put`, `get`, `remove` | `O(1)` | `O(n)` (all keys in one bucket, or a resize) |
| Resize | `O(n)`, but rare | — |
| Memory | `O(n + buckets)` | — |

#### 5. Common Mistakes

1. **Negative indexes** from `hashCode() % n`. Mask the sign bit first.
2. **`put` adds a second pair for an existing key.** Search the bucket first.
3. **Increasing `size` on an update.**
4. **Removing from a list inside a `for` loop.** Use an iterator or `removeAll`.
5. **No handling of a missing key.** `get` should return `null` (or `-1`).
6. **Never resizing.** The lists grow and everything becomes `O(n)`.
7. **Not saying how you treat `null` keys.** Say "not supported" and move on.

#### 6. Say This in the Interview

1. "I use an array of buckets. The index is the hash code, with the sign removed, modulo the bucket count."
2. "Each bucket is a list. `put` searches the list first and replaces or appends."
3. "When the load factor passes 0.75 I double the buckets and rehash. That keeps operations `O(1)` on average."
4. "Collisions are handled by chaining. The worst case is `O(n)`."

#### 7. Quick Check

1. Why search the bucket before adding in `put`?
2. Why resize at a load factor of 0.75?

<details>
<summary>Answers</summary>

1. If the key is already there, you must replace its value. Adding a second pair would store the key twice.
2. It keeps the lists short. Short lists mean `O(1)` average time.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 706 | Design HashMap (Easy) | this note |
| 705 | Design HashSet (Easy) | same idea, keys only |
| 146 | LRU Cache (Medium) | HashMap + doubly linked list (note 25) |
| 380 | Insert Delete GetRandom O(1) (Medium) | map + array |
| 981 | Time Based Key-Value Store (Medium) | map of key → list |
