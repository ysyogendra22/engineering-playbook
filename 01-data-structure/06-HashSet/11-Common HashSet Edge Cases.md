# Common HashSet Edge Cases

#### 1. Definition — Must Know

1. These are the situations where HashSet code most often **breaks or gives wrong answers**.
2. Most come from four places: **equality**, **mutation**, **order**, and **empty or extreme input**.
3. Checking this list before submitting an answer saves many failed tests.

#### 2. Why It Is Used — Must Know

1. Interviewers watch whether you think about edge cases before they point them out.
2. Many "mystery bugs" in real apps come from broken `equals`/`hashCode` or from changing an item inside a set.
3. A short mental checklist is faster than debugging.

#### 3. How It Works — Must Know

The mutable-key bug, step by step:

```text
class Box(var v: Int)  with equals/hashCode based on v

b = Box(1)
set.add(b)           → stored in the bucket for hash(1)
b.v = 2              → hash is now hash(2), but b still sits in the bucket for hash(1)
set.contains(b)      → looks in the bucket for hash(2) → NOT FOUND   (but the object is still inside!)
```

The item is lost: the set still holds it, but you cannot find or remove it.

#### 4. Core Concepts — Must Know

| # | Edge case | What happens | Fix |
|---|---|---|---|
| 1 | Empty input | Loops do nothing, `first()` throws | Check `isEmpty()` first |
| 2 | Single element | Duplicate checks return `false` | Test with one element |
| 3 | All elements equal | Set has size 1 | Do not assume `size == n` |
| 4 | `IntArray` / `Array` as an element | Compared by reference, duplicates not found | Use `List<Int>`, a `String` key, or a `data class` |
| 5 | Class without `equals`/`hashCode` | Two equal-looking objects count as different | Use a `data class` or override both |
| 6 | Mutating an item in a set | Item becomes unfindable | Use immutable items (`val` fields) |
| 7 | Expecting order from `HashSet` | Order can change | Use `LinkedHashSet` or `TreeSet` |
| 8 | Removing inside a `for` loop | `ConcurrentModificationException` | Use `removeIf` or an `Iterator` |
| 9 | `Double` / `Float` elements | `NaN` equals `NaN` in a set, but `0.0` and `-0.0` differ | Avoid; round or use `Long` |
| 10 | Case or whitespace | `"A"` and `"a"` differ | Normalize with `lowercase()` / `trim()` |
| 11 | `null` elements | Allowed in `HashSet`, but unsafe in `TreeSet` | Avoid or handle explicitly |
| 12 | Integer overflow in `target - x`, `n - 1`, `n + 1` | Wrong lookup value | Use `Long` when values are extreme |
| 13 | Huge input | Boxed `Integer`s use a lot of memory | Use `BitSet`/`BooleanArray` for dense ints |
| 14 | Shared set in several threads | Corrupted state | Use `ConcurrentHashMap.newKeySet()` or synchronize |
| 15 | `Set` returned as read-only | `add` fails to compile or throws | Know `Set` vs `MutableSet` |

#### 5. Algorithm — Must Know

A quick checklist to run before you finish:

```text
1. Empty input?
2. One element? All the same?
3. Are my set items immutable and do they have correct equals/hashCode?
4. Does the answer depend on order? Then do I use LinkedHashSet / TreeSet?
5. Do I change the set while looping over it?
6. Could a number overflow when I add 1, subtract 1, or add two values?
7. Do I need counts (map) rather than existence (set)?
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// 1. Arrays as elements: the duplicate is NOT detected
val bad = hashSetOf(intArrayOf(1, 2), intArrayOf(1, 2))
println(bad.size)                              // 2  (different objects)

val good = hashSetOf(listOf(1, 2), listOf(1, 2))
println(good.size)                             // 1  (List compares by content)

// 2. A class without equals/hashCode
class Tag(val name: String)
println(hashSetOf(Tag("a"), Tag("a")).size)    // 2

data class Label(val name: String)
println(hashSetOf(Label("a"), Label("a")).size) // 1

// 3. Mutating a key
data class Box(var v: Int)
val s = hashSetOf<Box>()
val b = Box(1)
s.add(b)
b.v = 2
println(b in s)                                // false — the item is lost (usually)

// 4. Remove while looping
val nums = hashSetOf(1, 2, 3, 4)
nums.removeIf { it % 2 == 0 }                  // safe
// for (n in nums) if (n % 2 == 0) nums.remove(n)   // ConcurrentModificationException

// 5. Doubles
val d = hashSetOf(0.0, -0.0, Double.NaN, Double.NaN)
println(d.size)                                // 3: 0.0 and -0.0 are different, the two NaN are the same

// 6. Overflow: n - 1 for Int.MIN_VALUE wraps to Int.MAX_VALUE
val n = Int.MIN_VALUE
println(n - 1)                                 // 2147483647
```

#### 7. Time & Space Complexity — Must Know

| Concern | Impact |
|---|---|
| Bad `hashCode` (all items hash to the same bucket) | Operations drop toward `O(n)` (Java trees help to about `O(log n)`) |
| Boxed `Integer` in `HashSet<Int>` | About 16–40 bytes per element, versus 4 bytes in an `IntArray` |
| Many resizes | Pre-size with `HashSet(capacity)` when the size is known |

#### 8. Common Patterns of Bugs — Must Know

1. **Equality bugs:** arrays, classes without `equals`.
2. **Mutation bugs:** changing a key after adding it.
3. **Order bugs:** assuming `HashSet` is ordered.
4. **Loop bugs:** modifying a set during iteration.
5. **Value bugs:** floats, case, whitespace, overflow.
6. **Choice bugs:** a set where a map is needed (counts or indices).

#### 9. Edge Cases / Common Mistakes

1. Testing only the example from the problem.
2. Using `set.first()` on an empty set (throws `NoSuchElementException`). Use `firstOrNull()`.
3. Assuming `mutableSetOf()` is a plain `HashSet`. It is a `LinkedHashSet`.
4. Casting a read-only `Set` to `MutableSet`. It may fail.
5. Forgetting that `toSet()` returns a new copy and does not change the original.
6. Comparing two sets with `==`. This works for content (`setOf(1,2) == setOf(2,1)` is `true`), which is usually what you want.

#### 10. When to Use / When Not to Use

**Use this checklist when:**

1. You finish writing any HashSet solution.
2. You review code that stores objects in a set.

**Remember:**

1. A set is only as correct as the `equals()` and `hashCode()` of its items.

#### 11. Related Topics

1. HashSet with Custom Objects
2. HashSet Operations & Complexity
3. Duplicate Detection
4. Deduplication of Complex States

#### 12. Interview Must Remember

1. **Arrays do not work as set elements.** Use `List`, `String`, or a `data class`.
2. **Never mutate an item that is inside a set.**
3. `HashSet` has no order. `removeIf` for removal while looping.
4. Check empty input, single element, overflow, and case.
