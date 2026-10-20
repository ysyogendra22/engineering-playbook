# Collision Handling — Basic Concept

> A basic idea. Interviewers ask "what happens when two keys collide?". Give a short, correct answer.

#### 1. What Is It?

A **collision** happens when two different keys get the **same bucket**.

It is unavoidable: there are far more possible keys than buckets. A good HashMap still stores and finds both keys correctly.

Java's `HashMap` uses **chaining**: each bucket holds a small **list** of pairs. If one bucket gets too long (8 or more pairs), Java turns it into a balanced **tree**, so even a bad bucket stays fast.

#### 2. How It Works

`"Aa"` and `"BB"` have the **same** hash code (`2112`), so they share a bucket.

```text
bucket 3:  (empty)
bucket 4:  [ "Aa" → 1 ] → [ "BB" → 2 ]       ← a chain of two pairs
bucket 5:  (empty)

get("BB"):
   1. hash "BB" → bucket 4
   2. walk the chain: "Aa".equals("BB")? no.  "BB".equals("BB")? yes → return 2
```

This is why `equals()` is always checked: the hash only finds the **bucket**, and `equals()` finds the **exact key**.

Two ways to handle collisions:

| Method | Idea | Used by |
|---|---|---|
| **Chaining** | each bucket holds a list (or tree) | Java `HashMap`, `HashSet` |
| **Open addressing** | if the bucket is taken, probe the next free slot | some other languages (not needed for interviews) |

**Load factor:** Java doubles the table when it is 75% full. This keeps the chains short.

#### 3. Kotlin Code

```kotlin
// Two different keys with the same hash code still work
val map = HashMap<String, Int>()
map["Aa"] = 1
map["BB"] = 2
println("Aa".hashCode() == "BB".hashCode())     // true: a collision
println(map["Aa"])                               // 1
println(map["BB"])                               // 2

// A deliberately bad hash: correct, but slow
class BadKey(val id: Int) {
    override fun equals(other: Any?) = other is BadKey && id == other.id
    override fun hashCode(): Int = 1             // every key lands in the same bucket
}
val slow = HashMap<BadKey, Int>()
for (i in 0 until 5) slow[BadKey(i)] = i
println(slow[BadKey(3)])                         // 3: found by walking the chain
```

A tiny chaining table (to show the idea):

```kotlin
class ChainTable(private val size: Int = 8) {
    private val buckets = Array(size) { mutableListOf<Pair<String, Int>>() }

    private fun index(key: String) = (key.hashCode() and 0x7fffffff) % size

    fun put(key: String, value: Int) {
        val bucket = buckets[index(key)]
        val i = bucket.indexOfFirst { it.first == key }
        if (i >= 0) bucket[i] = key to value else bucket.add(key to value)
    }

    fun get(key: String): Int? =
        buckets[index(key)].firstOrNull { it.first == key }?.second
}
```

#### 4. Complexity

| Case | Time per operation |
|---|---|
| Good hash, short chains | `O(1)` on average |
| All keys in one bucket (chain) | `O(n)` |
| All keys in one bucket (Java tree bucket) | `O(log n)` |
| Resize | `O(n)`, but rare |

#### 5. Common Mistakes

1. **Thinking a collision loses data.** It does not. Both pairs are kept.
2. **Thinking equal hash codes mean equal keys.** They do not.
3. **Writing `hashCode()` that returns a constant.** It is legal but makes the map slow.
4. **Using different fields** in `equals` and `hashCode`.
5. **Saying the worst case is always `O(n)`.** In Java 8+ it is about `O(log n)`.

#### 6. Say This in the Interview

1. "Two keys can land in the same bucket. Java chains them in a list, or a tree if the list gets long."
2. "The hash picks the bucket. `equals()` finds the exact key."
3. "Resizing at a load factor of 0.75 keeps the chains short, so operations are `O(1)` on average."

#### 7. Quick Check

1. If two keys collide, are both stored?
2. Why does `get` still call `equals()`?

<details>
<summary>Answers</summary>

1. Yes. They sit in the same bucket, in a chain.
2. Several keys can be in one bucket. `equals()` tells which one is the key you asked for.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 706 | Design HashMap (Easy) | buckets with chaining (note 26) |
| 705 | Design HashSet (Easy) | same idea |
| 49 | Group Anagrams (Medium) | choose a key that avoids unwanted collisions |
