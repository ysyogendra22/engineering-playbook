# HashSet with Custom Objects

#### 1. Definition — Must Know

1. A HashSet can hold **your own classes**, such as `Point`, `User`, or `Task`.
2. To work correctly, the class needs **`equals()`** and **`hashCode()`** that match each other.
3. In Kotlin, a **`data class`** gives you both automatically.

#### 2. Why It Is Used — Must Know

1. Many problems use coordinates, pairs, or states as set items: `(row, col)`, `(x, y, direction)`.
2. App code stores model objects in sets: selected items, unique users, seen messages.
3. A broken `equals`/`hashCode` is one of the most common hidden bugs.

#### 3. How It Works — Must Know

```text
set.add(obj):
    1. hash = obj.hashCode()                    → picks the bucket
    2. in that bucket, for each existing item:  compare with equals()
    3. if an equal item exists → not added      (duplicate)
       else                    → added
```

**The contract:**

```text
If a.equals(b) is true  →  a.hashCode() MUST equal b.hashCode()
(the opposite is allowed: equal hash codes do not require equal objects)
```

If this is broken, equal objects land in different buckets, and the set stores both.

#### 4. Core Concepts — Must Know

1. **Default behaviour** (a normal class with no overrides): equality is **identity**. Two separate objects are always different.
2. **`data class`**: `equals`, `hashCode`, `toString`, `copy` are generated from the **constructor properties**.
3. **Use only `val` properties** (immutable) in anything stored in a set.
4. **Do not mutate a key** after adding it. The item can no longer be found.
5. **Arrays do not work** (`IntArray`, `Array<T>`). They compare by reference. Use `List`, `Pair`, `Triple`, or a `data class`.
6. **Only properties in the primary constructor** count for a `data class`. Body properties are ignored.
7. **Custom rule:** override `equals`/`hashCode` yourself when only some fields define identity (for example, by `id`).

| Choice | Equality is based on |
|---|---|
| Normal class | Reference (same object) |
| `data class` | All primary-constructor properties |
| Class with your own `equals`/`hashCode` | Whatever you choose (like only `id`) |
| `Pair`, `Triple`, `List` | Contents |

#### 5. Algorithm — Must Know

```text
1. Decide what makes two objects "the same" (the key).
2. Make the class a data class with val fields, or override equals + hashCode on exactly those fields.
3. Put the objects in the set.
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. data class as a key
data class Point(val x: Int, val y: Int)

val visited = HashSet<Point>()
visited.add(Point(1, 2))
println(Point(1, 2) in visited)        // true  (equal by content)
println(visited.add(Point(1, 2)))      // false (duplicate)

// 2. Pair / Triple work too
val seen = HashSet<Pair<Int, Int>>()
seen.add(3 to 4)
println((3 to 4) in seen)              // true

// 3. A normal class does NOT work as expected
class Tag(val name: String)
println(hashSetOf(Tag("a"), Tag("a")).size)      // 2

// 4. Manual equals/hashCode — identity by id only
class User(val id: Int, var name: String) {
    override fun equals(other: Any?): Boolean =
        this === other || (other is User && id == other.id)

    override fun hashCode(): Int = id.hashCode()
}
val users = hashSetOf(User(1, "Asha"), User(1, "Asha K"))
println(users.size)                              // 1

// 5. Remove duplicates by a property
data class Message(val id: Int, val text: String)
val messages = listOf(Message(1, "Hi"), Message(2, "Yo"), Message(1, "Hi again"))
val uniqueMessages = messages.distinctBy { it.id }     // keeps ids 1 and 2

// 6. Arrays inside a data class: compare contents yourself
data class Grid(val cells: List<Int>)            // List compares by content — good
// data class Bad(val cells: IntArray)           // IntArray compares by reference — bad
```

**Android note.** Model classes used in a `Set` or as `DiffUtil` keys should be `data class` with `val` fields. A `var` in the constructor invites the mutation bug.

#### 7. Time & Space Complexity — Must Know

| Operation | Cost |
|---|---|
| `add` / `contains` / `remove` | `O(1)` average, plus the cost of `hashCode()` and `equals()` |
| `hashCode()` of a data class | `O(number of fields)`; for a `List` field, `O(list size)` |
| Space | One object per element, plus set overhead |

A big key (a long list or string) makes every operation slower, because hashing must read all of it.

#### 8. Common Custom-Object Patterns — Must Know

1. **Coordinates:** `data class Point(val r: Int, val c: Int)` in grid problems.
2. **State objects:** `data class State(val row: Int, val col: Int, val keys: Int)` in BFS.
3. **Edges / pairs:** `Pair(a, b)` to remember visited edges.
4. **Deduplicate models:** `distinctBy { it.id }`.
5. **Sorted lists as keys:** `Set<List<Int>>` for unique triples or combinations.
6. **Performance trick:** for very large grids, an `Int` or `Long` id (`r * cols + c`) is lighter than a `Point` object.

#### 9. Edge Cases / Common Mistakes

1. Using a normal class and expecting content equality.
2. Overriding `equals` but not `hashCode` (or the other way around).
3. Using `var` fields in the key and changing them later.
4. Including a mutable field (like a list that changes) in `hashCode`.
5. Putting arrays in a data class and expecting `==` to compare contents.
6. A `hashCode` that returns a constant (`return 1`). It is legal but makes every operation `O(n)`.
7. Using fields in `equals` that are not in `hashCode`.
8. Floating-point fields. Equality is exact; `0.1 + 0.2` is not `0.3`.
9. Relying on `toString()` as a key without a good reason. It is slow and fragile.

#### 10. When to Use / When Not to Use

**Use a data class key when:**

1. The key is naturally several values (coordinates, state).
2. You want readable, correct code.

**Use an encoded `Int`/`Long`/`String` key when:**

1. Speed and memory matter (very large grids, millions of states).

**Avoid when:**

1. The objects are mutable and shared. Copy the needed fields into a key instead.

#### 11. Related Topics

1. Common HashSet Edge Cases
2. Deduplication of Complex States
3. HashSet in Graph / State-Space Problems
4. Kotlin Data Classes (`03-leetcode-patterns`, topic 3)

#### 12. Interview Must Remember

1. **A set needs `equals()` and `hashCode()` that agree.**
2. **`data class` + `val` fields** is the safe default.
3. Arrays and normal classes compare by reference. They break sets.
4. Never mutate an object after it is in a set.
