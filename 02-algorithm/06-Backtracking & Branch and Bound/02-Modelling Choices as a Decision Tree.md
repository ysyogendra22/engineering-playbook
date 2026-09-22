# Modelling Choices as a Decision Tree

#### 1. Definition — Must Know

A **decision tree**, here, is a way of drawing out every choice a backtracking algorithm could make at each step, as branches of a tree — the same picture as a recursion tree (`03-Recursion & Divide and Conquer/04`), but built from **choices**, not just function calls.

#### 2. Why It Is Used — Must Know

1. Drawing the tree before coding turns a vague problem ("generate all valid arrangements") into a clear structure: what are the branches at each node, and what makes a leaf valid?
2. It's the fastest way to spot where pruning (topic 3) will actually help — branches that clearly can't lead anywhere useful.

#### 3. How It Works — Must Know

Decision tree for generating all permutations of `[1, 2]`:

```text
                    []
                  /    \
              choose 1  choose 2
                /            \
             [1]             [2]
              |                |
          choose 2         choose 1
              |                |
            [1,2]           [2,1]     ← leaves = complete permutations
```

1. Each **level** of the tree represents one decision point (which number goes next).
2. Each **path from root to leaf** is one complete answer.
3. The **branching factor** (how many children each node has) tells you roughly how fast the tree grows — this is where the complexity in topic 4 comes from.

#### 4. Algorithm — Must Know

```text
1. Ask: "what are ALL the choices at this point?" → these are the branches.
2. Ask: "when is a path complete?" → this defines the leaves.
3. Ask: "can I tell early that a branch is invalid?" → this is where pruning (topic 3) attaches.
4. The backtracking template (topic 1) is just code that walks this tree,
   depth-first, undoing each choice on the way back up.
```

#### 5. Kotlin Implementation — Must Know

```kotlin
// The tree itself isn't code — it's what you sketch on paper or a whiteboard
// before writing the backtracking function. The code just walks it:
fun permutations(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()
    val used = BooleanArray(nums.size)

    fun backtrack() {
        if (path.size == nums.size) {          // reached a leaf
            result.add(path.toList())
            return
        }
        for (i in nums.indices) {               // branches at this node
            if (used[i]) continue
            used[i] = true
            path.add(nums[i])
            backtrack()
            path.removeAt(path.size - 1)
            used[i] = false
        }
    }

    backtrack()
    return result
}
```

#### 6. Complexity — Must Know

| Tree shape | Meaning |
|---|---|
| Branching factor `k`, depth `n` | Roughly O(k^n) leaves and nodes |
| Subsets (branching factor 2, depth n) | O(2ⁿ) |
| Permutations (branching factor shrinks: n, n-1, n-2, ...) | O(n!) |

#### 7. Common Mistakes — Must Know

1. Coding directly without sketching the tree first — this is where most backtracking bugs (wrong branches, wrong leaf condition) actually come from.
2. Miscounting the branching factor — permutations have a *shrinking* branching factor (fewer choices remain at each level), which is different from subsets' constant factor of 2.
3. Not distinguishing "a leaf" (a complete, valid answer) from "an invalid dead end" — both stop the recursion, but only one should be recorded.

#### 8. Related Topics

1. `1` The Template — Choose, Explore, Un-choose — the code that walks this tree
2. `3` Pruning — Stopping a Branch Early — cutting parts of this tree before exploring them
3. `4` Why It's Exponential: O(2ⁿ) and O(n!) — where these numbers come from

#### 9. Interview Must Remember

1. **Draw the tree before writing code** — branches at each node, and what a leaf looks like.
2. The branching factor and depth together tell you the rough size of the search — say this out loud when asked for complexity.
3. Subsets tree: branching factor 2 (include or don't). Permutations tree: shrinking branching factor (fewer remaining choices each level).
