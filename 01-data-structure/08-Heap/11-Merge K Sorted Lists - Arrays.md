# Merge K Sorted Lists / Arrays

#### 1. Definition — Must Know

1. **Merge K Sorted Lists** (LeetCode 23) asks you to merge `k` sorted linked lists into one sorted linked list.
2. The same idea merges `k` sorted **arrays**.
3. It is the standard concrete problem for the K-Way Merge pattern. If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is a very common interview problem, and a direct test of heap knowledge.
2. It shows the jump from merging 2 lists (two pointers) to merging `k` lists (a heap).
3. It has a second good answer, divide and conquer, and you should know both.

#### 3. How It Works — Must Know

Lists: `[1, 4, 5]`, `[1, 3, 4]`, `[2, 6]`.

```text
Heap starts with the head of each list:  1(L1)  1(L2)  2(L3)

poll 1 (L1) → output 1 → push L1's next, 4
poll 1 (L2) → output 1 → push L2's next, 3
poll 2 (L3) → output 2 → push L3's next, 6
poll 3 (L2) → output 3 → push 4
poll 4 (L1) → output 4 → push 5
poll 4 (L2) → output 4 → L2 has no more
poll 5 (L1) → output 5
poll 6 (L3) → output 6

Result: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

For linked lists, the heap holds the **nodes themselves**. A node already knows its `next`, so no extra index is needed.

#### 4. Core Concepts — Must Know

1. **Heap of nodes** (lists) or **heap of `[value, arrayIndex, position]`** (arrays).
2. Use a **dummy head** node to build the result list without special cases.
3. Reuse the existing nodes. Do not create new ones, so extra space stays `O(k)`.
4. **Two solutions:**

| Approach | Time | Extra space |
|---|---:|---:|
| Min-heap of `k` heads | `O(N log k)` | `O(k)` |
| Divide and conquer (merge pairs repeatedly) | `O(N log k)` | `O(1)` extra for the merge |
| Merge one list into the result, one by one | `O(N · k)` | `O(1)` |

#### 5. Algorithm — Must Know

```text
heap = min-heap of nodes, ordered by node value
add the head of every non-empty list

dummy = new node; tail = dummy
while heap is not empty:
    node = heap.poll()
    tail.next = node; tail = node
    if node.next != null: heap.add(node.next)

return dummy.next
```

#### 6. Kotlin Implementation — Must Know

**Linked lists with a heap**

```kotlin
import java.util.PriorityQueue

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

fun mergeKLists(lists: Array<ListNode?>): ListNode? {
    val heap = PriorityQueue<ListNode>(compareBy<ListNode> { it.`val` })
    for (head in lists) {
        if (head != null) heap.add(head)
    }

    val dummy = ListNode(0)
    var tail = dummy
    while (heap.isNotEmpty()) {
        val node = heap.poll()
        tail.next = node
        tail = node
        node.next?.let { heap.add(it) }
    }
    return dummy.next
}
```

**Arrays with a heap**

```kotlin
fun mergeKArrays(arrays: List<IntArray>): IntArray {
    val result = IntArray(arrays.sumOf { it.size })
    val heap = PriorityQueue<IntArray>(compareBy<IntArray> { it[0] })   // [value, arrayIndex, position]
    for ((i, arr) in arrays.withIndex()) {
        if (arr.isNotEmpty()) heap.add(intArrayOf(arr[0], i, 0))
    }

    var index = 0
    while (heap.isNotEmpty()) {
        val (value, arrayIndex, position) = heap.poll()
        result[index++] = value
        val next = position + 1
        if (next < arrays[arrayIndex].size) {
            heap.add(intArrayOf(arrays[arrayIndex][next], arrayIndex, next))
        }
    }
    return result
}
```

**Divide and conquer (no heap)**

```kotlin
fun mergeTwo(a: ListNode?, b: ListNode?): ListNode? {
    val dummy = ListNode(0)
    var tail = dummy
    var x = a
    var y = b
    while (x != null && y != null) {
        if (x.`val` <= y.`val`) { tail.next = x; x = x.next }
        else { tail.next = y; y = y.next }
        tail = tail.next!!
    }
    tail.next = x ?: y
    return dummy.next
}

fun mergeKListsDivide(lists: Array<ListNode?>): ListNode? {
    if (lists.isEmpty()) return null
    var current: List<ListNode?> = lists.toList()
    while (current.size > 1) {
        current = current.chunked(2).map { pair -> mergeTwo(pair[0], pair.getOrNull(1)) }
    }
    return current[0]
}
```

#### 7. Time & Space Complexity — Must Know

`N` = total number of nodes or items, `k` = number of lists.

| Approach | Time | Space |
|---|---:|---:|
| Heap | `O(N log k)` | `O(k)` |
| Divide and conquer | `O(N log k)` | `O(k)` for the list of heads, `O(1)` for merging |

Why `O(N log k)`?

```text
Every item is added to and removed from a heap of at most k items once: log k each.
In divide and conquer: log k rounds, and each round touches N items.
```

#### 8. Common Variations — Must Know

1. **Merge Two Sorted Lists** (LeetCode 21) — the building block.
2. **Merge Sorted Array** (LeetCode 88) — two arrays, solved with two pointers, no heap.
3. **Kth Smallest Element in a Sorted Matrix** (LeetCode 378) — stop after `k` polls.
4. **Find K Pairs with Smallest Sums** (LeetCode 373).
5. **Sort a nearly sorted array** — a heap of size `k + 1` (items are at most `k` places from their final position).

#### 9. Edge Cases / Common Mistakes

1. An empty input array, or lists that are `null`. Skip empty lists when filling the heap.
2. Adding a `null` node to the heap (`PriorityQueue` throws on `null`).
3. Forgetting to push `node.next` after polling.
4. Creating new nodes instead of reusing them, and using extra space.
5. Returning `dummy` instead of `dummy.next`, which adds a fake `0` at the front.
6. Using `compareBy { it.val }` without naming the type, which fails to compile in some cases. Write `compareBy<ListNode> { it.`val` }`.

#### 10. When to Use / When Not to Use

**Use the heap when:**

1. `k` is large, or the lists arrive as streams.

**Use divide and conquer when:**

1. You want `O(1)` extra merge space, and all lists are in memory.

**Avoid merging one list at a time** when `k` is large. It is `O(N · k)`.

#### 11. Related Topics

1. K-Way Merge Pattern
2. Heap Fundamentals
3. Linked List (`01-data-structure/02-LinkedList`)
4. Divide and Conquer (`02-algorithm/03-Recursion & Divide and Conquer`)
5. Merge Sort (`02-algorithm/01-sorting/04-Merge Sort.md`)

#### 12. Interview Must Remember

1. Heap of `k` list heads: poll the smallest, push its `next`. `O(N log k)`.
2. Use a **dummy head**, and reuse the nodes.
3. Know the second answer: **divide and conquer**, also `O(N log k)`.
4. Skip `null` heads before adding to the heap.
