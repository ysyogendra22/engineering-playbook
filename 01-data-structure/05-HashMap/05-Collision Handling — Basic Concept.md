# Collision Handling — Basic Concept

#### 1. Definition — Must Know

1. A **collision** happens when two different keys get the **same bucket**.
2. **Collision handling** is how the map still stores and finds both.
3. Java's `HashMap` uses **chaining**: each bucket holds a small list (and, if it grows too long, a balanced tree).

#### 2. Why It Is Used — Must Know

1. Collisions are unavoidable. There are far more possible keys than buckets.
2. Interviewers ask "what happens when two keys collide?". You need a short, correct answer.
3. It explains why a bad `hashCode()` makes a map slow.

#### 3. How It Works — Must Know

`"Aa"` and `"BB"` both have `hashCode()` `2112`, so they share a bucket.

```text
bucket 0:  -
bucket 1:  -
bucket 2:  -
bucket 3:  -
bucket 4:  [ "Aa" → 1 ]  →  [ "BB" → 2 ]       ← chain of two entries
bucket 5:  -
```

```text
get("BB"):
   1. hash "BB" → bucket 4
   2. walk the chain: "Aa".equals("BB")? no  →  "BB".equals("BB")? yes → return 2
```

That is why `equals()` is always checked: the hash only finds the bucket, `equals()` finds the exact key.

#### 4. Core Concepts — Must Know

1. **Chaining (separate chaining):** each bucket stores a list of entries. Java's `HashMap` uses this.
2. **Treeification (Java 8+):** if one bucket gets 8 or more entries (and the table has at least 64 buckets), the chain becomes a balanced tree. The worst case drops from `O(n)` to about `O(log n)`.
3. **Load factor:** default `0.75`. When `size > capacity × 0.75`, the table doubles and entries are spread out again, which keeps chains short.
4. **Open addressing:** another approach — if the bucket is taken, probe the next free slot (linear, quadratic, double hashing). Java's `HashMap` does not use it. (Low priority.)
5. **Quality of hashCode:** a good hash spreads keys evenly, so most chains have 0–2 entries.

| Method | Idea | Used by |
|---|---|---|
| Chaining | Bucket = list/tree of entries | Java `HashMap`, `HashSet` |
| Open addressing | Probe for the next free slot | Some other languages / custom tables |

#### 5. Algorithm — Must Know

```text
put(key, value):
    i = bucketIndex(key)
    for each entry in bucket[i]:
        if entry.key equals key: replace value; return
    add new entry to bucket[i]
    size++
    if size > capacity * 0.75: resize (double and re-place all entries)
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Two different keys with the same hash still work correctly in a HashMap
val map = HashMap<String, Int>()
map["Aa"] = 1
map["BB"] = 2
println("Aa".hashCode() == "BB".hashCode())    // true — a collision
println(map["Aa"])                              // 1
println(map["BB"])                              // 2

// A deliberately bad hash — still correct, but slow
class BadKey(val id: Int) {
    override fun equals(other: Any?) = other is BadKey && id == other.id
    override fun hashCode(): Int = 1            // every key collides
}
val slow = HashMap<BadKey, Int>()
for (i in 0 until 5) slow[BadKey(i)] = i
println(slow[BadKey(3)])                        // 3 — found, but by scanning the chain
```

A tiny chaining table (the idea only):

```kotlin
class ChainTable(private val size: Int = 8) {
    private val buckets = Array(size) { mutableListOf<Pair<String, Int>>() }

    fun put(key: String, value: Int) {
        val bucket = buckets[(key.hashCode() and 0x7fffffff) % size]
        val index = bucket.indexOfFirst { it.first == key }
        if (index >= 0) bucket[index] = key to value else bucket.add(key to value)
    }

    fun get(key: String): Int? =
        buckets[(key.hashCode() and 0x7fffffff) % size].firstOrNull { it.first == key }?.second
}
```

#### 7. Time & Space Complexity — Must Know

| Case | Time per operation |
|---|---:|
| Good hash, load factor ≤ 0.75 | `O(1)` average |
| All keys in one bucket, chain list | `O(n)` |
| All keys in one bucket, Java tree bucket | `O(log n)` |
| Resize | `O(n)`, but rare (amortized `O(1)`) |

Space: `O(n)` entries plus the bucket array.

#### 8. Common Collision Ideas — Must Know

1. **Chaining** — default in Java.
2. **Treeify long chains** — Java 8+.
3. **Resize on load factor** — keeps chains short.
4. **Equal hash ≠ equal key** — always compare with `equals()`.
5. **Hash-flooding attacks:** an attacker sends many keys with the same hash to slow a server. Treeifying reduces the damage. (Background only.)

#### 9. Edge Cases / Common Mistakes

1. Thinking a collision loses data. It does not; both entries are kept.
2. Thinking equal hash codes mean equal keys.
3. Writing `hashCode()` that returns a constant. It is legal but makes the map slow.
4. Writing `hashCode()` with different fields than `equals()`.
5. Forgetting that keys must not change while in the map; the entry would sit in the wrong bucket.
6. Saying the worst case is always `O(n)`. In modern Java it is `O(log n)` for comparable keys.
7. Explaining collisions with too much theory. A short chain example is enough.

#### 10. When to Use / When Not to Use

**Know this when:**

1. You explain how `HashMap` works.
2. You design a custom key class.

**Skip deep details when:**

1. The question is about solving a coding problem, not about implementing a map.

#### 11. Related Topics

1. Hashing / Hash Function — Basic Concept
2. Designing a Simple HashMap — Concept
3. HashMap with Custom Objects / Keys
4. HashSet Fundamentals (`01-data-structure/06-HashSet`)

#### 12. Interview Must Remember

1. **Collision = two keys, one bucket.** Java uses **chaining**.
2. Long chains become **trees** (Java 8+).
3. Resize at load factor `0.75` keeps chains short.
4. The hash finds the bucket; **`equals()` finds the key.**
