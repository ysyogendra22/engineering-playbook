# Copy List with Random Pointer

> A very popular Medium question. It tests whether you understand **deep copy** and can use a HashMap, then improve to `O(1)` space.

#### 1. What Is It?

Each node has two pointers: `next` and `random` (it can point to any node in the list, or `null`). Make a **deep copy**: all nodes are **new**, and the new `next` / `random` pointers must point to the **new** nodes, not to the old ones.

```text
A → B → C            next pointers
A.random = C,  B.random = A,  C.random = B
```

The hard part: when you create a copy of `A`, the copy of `C` (its random target) may not exist yet. This is *Copy List with Random Pointer* (LeetCode 138).

#### 2. How It Works

**Method 1 — HashMap (two passes).** `O(n)` space.

1. Pass 1: for every old node, create a new node. Store `old → new` in a map.
2. Pass 2: for every old node, set `new.next = map[old.next]` and `new.random = map[old.random]`.

The map answers "which new node matches this old node?"

**Method 2 — weave the copies (`O(1)` space).** No map. Three passes:

1. **Insert** each copy right after its original: `A → A' → B → B' → C → C'`.
2. **Set random:** `A'.random = A.random.next` (the node after the original random target is its copy).
3. **Split** the two lists apart and restore the original.

```text
step 1:  A → A' → B → B' → C → C'
step 2:  A.random = C  →  A'.random = C.next = C'
step 3:  A → B → C      and      A' → B' → C'
```

#### 3. Brute Force vs Optimized

| | HashMap | Weave |
|---|---|---|
| Time | `O(n)` | `O(n)` |
| Space | `O(n)` | `O(1)` extra (besides the copy) |
| Changes the input | no | temporarily (restored) |
| Easy to explain | yes | needs care |

A brute force that searches for the random target of each node by walking the list (`O(n)` each) is `O(n²)`. The map removes that search. **Start with the HashMap answer.** Mention the weave method as an improvement.

#### 4. Kotlin Code

```kotlin
class RNode(var `val`: Int) {
    var next: RNode? = null
    var random: RNode? = null
}

// Method 1: HashMap
fun copyRandomList(head: RNode?): RNode? {
    if (head == null) return null
    val map = HashMap<RNode, RNode>()                       // old node → new node
    var cur: RNode? = head
    while (cur != null) {                                    // pass 1: create copies
        map[cur] = RNode(cur.`val`)
        cur = cur.next
    }
    cur = head
    while (cur != null) {                                    // pass 2: set the pointers
        val copy = map[cur]!!
        copy.next = cur.next?.let { map[it] }
        copy.random = cur.random?.let { map[it] }
        cur = cur.next
    }
    return map[head]
}

// Method 2: weave, O(1) extra space
fun copyRandomListWeave(head: RNode?): RNode? {
    if (head == null) return null

    var cur: RNode? = head                                   // 1. insert a copy after each node
    while (cur != null) {
        val copy = RNode(cur.`val`)
        copy.next = cur.next
        cur.next = copy
        cur = copy.next
    }

    cur = head                                               // 2. set the random pointers
    while (cur != null) {
        cur.next!!.random = cur.random?.next
        cur = cur.next!!.next
    }

    val newHead = head.next                                  // 3. split the lists
    cur = head
    while (cur != null) {
        val copy = cur.next!!
        cur.next = copy.next
        copy.next = copy.next?.next
        cur = cur.next
    }
    return newHead
}
```

Check (works for both methods):

```kotlin
val a = RNode(1); val b = RNode(2)
a.next = b; a.random = b; b.random = b
val c = copyRandomList(a)!!
println(c !== a)                       // true: a new node
println(c.random === c.next)           // true: points to the NEW second node
println(c.next!!.random === c.next)    // true
println(a.next === b)                  // true: the original is unchanged
```

`HashMap<RNode, RNode>` uses object identity here, because `RNode` does not override `equals` / `hashCode`. That is what we want.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| HashMap | `O(n)` | `O(n)` |
| Weave | `O(n)` | `O(1)` extra |

#### 6. Common Mistakes

1. **Shallow copy:** pointing the new node's `random` at an **old** node.
2. **Creating copies while walking and setting `random`** in one pass. The random target may not exist yet.
3. **Weave, step 2:** forgetting that `random` may be `null` (`cur.random?.next`).
4. **Weave, step 3:** not restoring the original list.
5. **Weave:** using `cur.next` after changing it. Save the copy first.
6. **Map keys:** keying by value. Values repeat. Key by the **node**.

#### 7. Say This in the Interview

1. "The problem is that a node's random target may not be copied yet. I do it in two passes with a HashMap: first create every copy, then connect `next` and `random` through the map."
2. "To use `O(1)` space, I put each copy right after its original. Then `copy.random = original.random.next`. Then I split the lists."

#### 8. Quick Check

1. In the weave method, what is `A'.random` if `A.random = C`?
2. Why is a deep copy not just `val copy = head`?

<details>
<summary>Answers</summary>

1. `C.next`, which is `C'` (the copy of `C`).
2. That only copies the reference. Both variables point to the same nodes, so a change to one changes the other.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (Medium) | this note |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium) | the same "old → new" map on a graph |
| 1485 | [Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) (Medium, premium) | map on a tree |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) | warm-up (note 05) |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | map + list together (note 25) |
