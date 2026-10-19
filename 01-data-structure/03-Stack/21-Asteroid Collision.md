# Asteroid Collision

#### 1. Definition — Must Know

1. Asteroids are in a row. Each number is an asteroid: its **absolute value is the size** and its **sign is the direction** (positive → moving right, negative → moving left). All move at the same speed.
2. When two asteroids meet, the **smaller one explodes**. If they have the **same size, both explode**. Asteroids moving in the same direction never meet.
3. Return the asteroids that remain after all collisions.
4. It is *Asteroid Collision* (LeetCode 735). If a number and a title ever disagree, trust the title.

#### 2. Why It Is Used — Must Know

1. It is a popular stack question that tests careful case handling.
2. A collision only happens between a **right-moving asteroid on the stack top** and a **new left-moving asteroid**. The stack holds the survivors so far.
3. The same "new item may remove several earlier items" shape appears in many problems.

#### 3. How It Works — Must Know

`asteroids = [5, 10, -5]`

```text
5   moving right → push                    stack: [5]
10  moving right → push                    stack: [5, 10]
-5  moving left; top is 10 (right-moving)
    10 > 5 → the -5 asteroid explodes      stack: [5, 10]

result: [5, 10]
```

`asteroids = [10, 2, -5]`

```text
10 → push           [10]
2  → push           [10, 2]
-5: top 2 < 5 → 2 explodes (pop)           [10]
    top 10 > 5 → -5 explodes               [10]

result: [10]
```

`asteroids = [8, -8]` → both explode → `[]`. `asteroids = [-2, -1, 1, 2]` → nothing collides (left-movers are first, right-movers go away) → `[-2, -1, 1, 2]`.

#### 4. Core Concepts — Must Know

1. **When does a collision happen?** Only if the **top is positive** (moving right) and the **new one is negative** (moving left).
2. **Compare sizes** with `top` and `-new`:
   - `top < -new` → top explodes (pop) and **keep checking** with the next top.
   - `top == -new` → both explode (pop, and the new one dies).
   - `top > -new` → the new one explodes.
3. **The new asteroid survives** only if it destroys every right-moving asteroid it meets (or meets none). Then push it.
4. **A positive new asteroid, or a negative one with an empty stack/negative top, is simply pushed.**
5. **Use a `while` loop**, because one big left-mover can destroy many.
6. **A `alive` flag** records whether the new asteroid is still alive.
7. **The stack holds the final answer**, from bottom to top.

| Top | New | Result |
|---|---|---|
| any | positive | push |
| negative or empty | negative | push |
| positive | negative | collide |

#### 5. Algorithm — Must Know

```text
for each asteroid a:
    alive = true
    while alive and a < 0 and stack not empty and stack.top > 0:
        if stack.top < -a: stack.pop()                 // top explodes, keep checking
        elif stack.top == -a: stack.pop(); alive = false // both explode
        else: alive = false                             // a explodes
    if alive: stack.push(a)
return stack
```

#### 6. Kotlin Implementation — Must Know

```kotlin
fun asteroidCollision(asteroids: IntArray): IntArray {
    val stack = ArrayDeque<Int>()
    for (a in asteroids) {
        var alive = true
        while (alive && a < 0 && stack.isNotEmpty() && stack.last() > 0) {
            val top = stack.last()
            when {
                top < -a -> stack.removeLast()          // the right-mover explodes; keep checking
                top == -a -> { stack.removeLast(); alive = false }   // both explode
                else -> alive = false                   // the left-mover explodes
            }
        }
        if (alive) stack.addLast(a)
    }
    return stack.toIntArray()
}
```

Checks: `asteroidCollision([5,10,-5])` → `[5,10]`. `asteroidCollision([8,-8])` → `[]`. `asteroidCollision([10,2,-5])` → `[10]`. `asteroidCollision([-2,-1,1,2])` → `[-2,-1,1,2]`. `asteroidCollision([3,5,-6,2,-1,4])` → `[-6,2,4]`.

Trace of the last example:

```text
3  push [3]       5 push [3,5]
-6: 5 < 6 pop; 3 < 6 pop; stack empty → push -6        [-6]
2  push [-6,2]
-1: top 2 > 1 → -1 explodes                              [-6,2]
4  push [-6,2,4]
```

#### 7. Time & Space Complexity — Must Know

| Part | Cost |
|---|---:|
| Time | `O(n)` — each asteroid is pushed once and popped at most once |
| Space | `O(n)` |

#### 8. Common Collision / Chain-Reaction Patterns — Must Know

1. **Asteroid Collision** (LeetCode 735).
2. **Car Fleet** (LeetCode 853) — cars that catch up merge.
3. **Remove Adjacent Duplicates** — pair removal.
4. **Valid Parentheses** — matching and cancelling.
5. **Robot Collisions** (LeetCode 2751) — sort by position, then the same stack idea.
6. **Dota2 Senate**, **Remove Colored Pieces** — simulation with a queue or counters.
7. **Android example:** cancelling opposite actions in an event log (add then remove the same item).

#### 9. Edge Cases / Common Mistakes

1. Checking collision when the **top is negative** or when the **new one is positive**. Neither collides.
2. Using `if` instead of `while`. One large left-mover may destroy several.
3. Forgetting the **equal size** case (both explode).
4. Pushing the new asteroid even after it exploded.
5. Comparing `top < a` instead of `top < -a` (sign mistake).
6. Not stopping after a mutual explosion.
7. Using absolute values for the stack and losing the direction.
8. Empty input returns an empty array.

#### 10. When to Use / When Not to Use

**Use when:**

1. A new item can cancel or remove several earlier items, in order from the nearest.

**Avoid when:**

1. Items interact in more complex ways (different speeds, 2D). Use a simulation or a priority queue by collision time.

#### 11. Related Topics

1. Remove Adjacent Duplicates
2. Valid / Balanced Parentheses
3. Monotonic Stack
4. Stack Operations & Complexity

#### 12. Interview Must Remember

1. **Collision only when `top > 0` and `new < 0`.**
2. Loop with `while`: pop smaller tops; equal sizes remove both; bigger top destroys the new one.
3. Push the new asteroid only if it is still alive.
4. `O(n)` time and space.
