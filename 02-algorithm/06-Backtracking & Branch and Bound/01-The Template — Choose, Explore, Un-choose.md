# The Template — Choose, Explore, Un-choose

#### 1. Definition — Must Know

Every backtracking solution follows the same three-step template at each step of its recursion: **choose** an option, **explore** what happens next (recurse), then **un-choose** it (undo) before trying the next option.

#### 2. Why It Is Used — Must Know

1. It's the one template that solves an enormous range of "generate all ___" problems: subsets, permutations, combinations, valid arrangements.
2. Once memorised, you can adapt it to a new problem by changing only what "choose" and "valid" mean — the surrounding structure barely changes.

#### 3. How It Works — Must Know

Generating all subsets of `[1, 2, 3]`:

```text
path = []
choose 1 → path = [1]
    choose 2 → path = [1, 2]
        choose 3 → path = [1, 2, 3]   ← record this subset
        un-choose 3 → path = [1, 2]
    un-choose 2 → path = [1]
    choose 3 → path = [1, 3]          ← record this subset
    un-choose 3 → path = [1]
un-choose 1 → path = []
... continues for subsets not starting with 1
```

Every subset gets found because the template systematically tries "include this element" and "don't", at every position.

#### 4. Algorithm — Must Know

```text
function backtrack(path, choices remaining):
    if path is a complete/valid answer:
        record a COPY of path
        return
    for each option in choices remaining:
        path.add(option)              # choose
        backtrack(path, updated choices)  # explore
        path.removeLast()             # un-choose
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun subsets(nums: IntArray): List<List<Int>> {
    val result = mutableListOf<List<Int>>()
    val path = mutableListOf<Int>()

    fun backtrack(start: Int) {
        result.add(path.toList())          // record a COPY, every path is a valid subset
        for (i in start until nums.size) {
            path.add(nums[i])              // choose
            backtrack(i + 1)               // explore
            path.removeAt(path.size - 1)   // un-choose
        }
    }

    backtrack(0)
    return result
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Time | Proportional to the number of paths explored — often O(2ⁿ) or O(n!), see topic 4 |
| Space | O(depth) for the recursion, plus the space to store all the results |

#### 7. Common Mistakes — Must Know

1. **The most common bug:** adding `path` to the results directly instead of a copy (`path.toList()`), so every stored result changes later as `path` is mutated.
2. Forgetting the "un-choose" step — without it, choices from one branch leak into the next.
3. Not defining a clear stopping condition ("this path is complete"), so the recursion doesn't know when to record a result.

#### 8. Related Topics

1. `2` Modelling Choices as a Decision Tree — the mental picture behind this template
2. `3` Pruning — Stopping a Branch Early — the optimisation layered on top of this template
3. `LC 14` Backtracking (in `03-leetcode-patterns`) — practice problems using this exact template

#### 9. Interview Must Remember

1. **Choose, explore, un-choose** — say this out loud as you write the code, it keeps you from missing the undo step.
2. Always store a **copy** of the path, never a reference to the mutable list you keep changing.
3. This template barely changes between problems — what changes is what counts as a "valid" or "complete" path.
