# Complete Binary Tree Property

#### 1. Definition — Must Know

1. A **complete binary tree** is a binary tree where:
   - every level is completely filled, **except possibly the last**, and
   - the last level is filled **from left to right** with no gaps.
2. This is the **shape rule** of a heap.
3. The shape rule is what lets a heap live in a plain **array**, with no node objects and no pointers.

#### 2. Why It Is Used — Must Know

1. It keeps the tree as short as possible: height is `⌊log₂ n⌋`. That is why heap operations are `O(log n)`.
2. It lets you find a node's parent and children with simple arithmetic.
3. It makes insert simple: the new item always goes to the **next free slot** at the end.

#### 3. How It Works — Must Know

A complete tree and the array that stores it level by level:

```text
        10                      index:  0   1   2   3   4   5
      /    \                    value: [10, 20, 30, 40, 50, 60]
    20      30
   /  \    /
  40  50  60
```

Two trees that are **not** complete:

```text
  Tree A                     Tree B
      10                         10
     /  \                       /  \
   20    30                   20    30
           \                    \
            50                   50

 30 has a right child         20 has a right child
 but no left child           but no left child
```

Rule of thumb: read the nodes level by level, left to right. There must be **no empty slot before a filled one**.

#### 4. Core Concepts — Must Know

For a node at index `i` (0-based array):

| Relation | Formula |
|---|---|
| Left child | `2 * i + 1` |
| Right child | `2 * i + 2` |
| Parent | `(i - 1) / 2` (integer division) |
| Last parent (first node with a child) | `n / 2 - 1` |
| Is a leaf | `i >= n / 2` |

With 1-based indexing the formulas are `2i`, `2i + 1`, and `i / 2`. Most interview code uses 0-based arrays.

Other facts:

1. Height of a heap with `n` nodes = `⌊log₂ n⌋`.
2. About half of the nodes are leaves.
3. The shape rule and the order rule are separate. A complete tree is not automatically a heap.

#### 5. Algorithm — Must Know

How the shape rule is kept:

```text
insert:   append the new item at index n, then sift it up
extract:  move the LAST item to the root, shrink the array, then sift it down
```

Always taking from and adding to the **end** of the array is what preserves the shape. The order rule is then repaired by sifting.

#### 6. Kotlin Implementation — Must Know

```kotlin
fun parent(i: Int) = (i - 1) / 2
fun left(i: Int) = 2 * i + 1
fun right(i: Int) = 2 * i + 2

val heap = intArrayOf(1, 3, 2, 7, 4, 5)   // a valid min-heap stored as an array

// Children of the root (index 0) are at 1 and 2
println(heap[left(0)])    // 3
println(heap[right(0)])   // 2

// Parent of index 4 (value 4) is index 1 (value 3)
println(heap[parent(4)])  // 3
```

#### 7. Time & Space Complexity — Must Know

| Fact | Cost |
|---|---:|
| Find parent or child | `O(1)` (arithmetic) |
| Height | `O(log n)` |
| Extra space for pointers | none |

Why no pointers?

```text
The position in the array already tells you the tree structure.
```

#### 8. Common Patterns — Must Know

1. Store a heap in an `IntArray` or `ArrayList` and move between parent and child with the formulas above.
2. Start heapify at index `n / 2 - 1` and go backwards (see "Build Heap").
3. In heap sort, the sorted part grows at the end while the heap shrinks at the front.

#### 9. Edge Cases / Common Mistakes

1. Mixing 0-based and 1-based formulas. Using `2i` with a 0-based array breaks everything.
2. Forgetting to check `left < n` and `right < n` before reading a child.
3. Thinking a complete tree is a BST or sorted.
4. Using a **full** or **perfect** tree as the definition. Complete is weaker: the last level may be partly filled.
5. Taking the parent of the root. `(0 - 1) / 2` gives `0` in Kotlin, which is the root again, so check `i > 0`.

#### 10. When to Use / When Not to Use

**Use this layout when:**

1. You need a heap. Array storage is smaller and faster than node objects.

**Avoid it when:**

1. The tree is sparse or unbalanced (for example, a skewed BST). An array would waste space.

#### 11. Related Topics

1. Heap Fundamentals
2. Heap Operations & Complexity
3. Heapify — Basic Concept
4. Binary Tree (`01-data-structure/07-Tree/02-Binary Tree.md`)

#### 12. Interview Must Remember

1. Complete = all levels full except the last, which fills **left to right**.
2. 0-based: left `2i + 1`, right `2i + 2`, parent `(i - 1) / 2`.
3. Height is `log n`, which gives `O(log n)` operations.
4. Always add and remove at the **end** of the array to keep the shape.
