# Asteroid Collision

#### 1. What Is It?

Asteroids are in a row. Each number is one asteroid:

- the **size** is the absolute value,
- the **sign** is the direction: **positive → moving right**, **negative → moving left**.

All asteroids move at the same speed. When two meet:

- the **smaller one explodes**,
- if they have the **same size, both explode**,
- asteroids moving the same way never meet.

Return the asteroids left after all collisions. This is *Asteroid Collision* (LeetCode 735).

A collision only happens when a **right-moving asteroid is on the left** and a **left-moving asteroid comes after it**. The stack keeps the survivors so far. The newest survivor is on top.

#### 2. How It Works

For each new asteroid `a`:

- If `a` moves right (positive), or the top moves left (negative), or the stack is empty: no collision. **Push `a`.**
- Otherwise (`a` is negative and the top is positive) they collide:
  - top is **smaller** than `a` → the top explodes (**pop**). `a` keeps going, so check the next top.
  - **equal** sizes → both explode (pop, and `a` is gone).
  - top is **bigger** → `a` explodes.

```text
[10, 2, -5]

10   push                             stack: [10]
2    push                             stack: [10, 2]
-5   top 2 < 5 → 2 explodes (pop)     stack: [10]
     top 10 > 5 → -5 explodes         stack: [10]

result: [10]
```

```text
[3, 5, -6, 2, -1, 4]

3    push                    [3]
5    push                    [3, 5]
-6   5 < 6 → pop; 3 < 6 → pop; stack empty → push -6      [-6]
2    push                    [-6, 2]
-1   top 2 > 1 → -1 explodes                              [-6, 2]
4    push                    [-6, 2, 4]

result: [-6, 2, 4]
```

#### 3. Kotlin Code

```kotlin
fun asteroidCollision(asteroids: IntArray): IntArray {
    val stack = ArrayDeque<Int>()
    for (a in asteroids) {
        var alive = true
        while (alive && a < 0 && stack.isNotEmpty() && stack.last() > 0) {
            val top = stack.last()
            when {
                top < -a -> stack.removeLast()                          // top explodes, keep checking
                top == -a -> { stack.removeLast(); alive = false }      // both explode
                else -> alive = false                                    // a explodes
            }
        }
        if (alive) stack.addLast(a)
    }
    return stack.toIntArray()
}
```

Checks: `[5,10,-5]` → `[5,10]`. `[8,-8]` → `[]`. `[10,2,-5]` → `[10]`. `[-2,-1,1,2]` → `[-2,-1,1,2]`. `[3,5,-6,2,-1,4]` → `[-6,2,4]`.

**A similar idea: Car Fleet (LeetCode 853).** Cars drive toward a target on a one-lane road. A faster car that catches a slower one must slow down, and they travel together as one **fleet**. Count the fleets.

Sort cars by position, from the one closest to the target. For each car, compute the time it needs to reach the target. A car behind that needs **less or equal** time than the fleet in front joins that fleet. A car that needs **more** time starts a new fleet.

```kotlin
fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
    val cars = position.indices.sortedByDescending { position[it] }   // closest to the target first
    val times = ArrayDeque<Double>()                                   // arrival time of each fleet
    for (i in cars) {
        val time = (target - position[i]).toDouble() / speed[i]
        if (times.isEmpty() || time > times.last()) times.addLast(time)   // slower than the fleet ahead → new fleet
    }
    return times.size
}
// carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) → 3
```

#### 4. Complexity

| | Time | Space |
|---|---|---|
| Asteroid Collision | `O(n)` | `O(n)` |
| Car Fleet | `O(n log n)` (sorting) | `O(n)` |

In Asteroid Collision each asteroid is pushed once and popped at most once.

#### 5. Common Mistakes

1. **Colliding in the wrong case.** Only when the top is positive and the new one is negative.
2. **Using `if` instead of `while`.** One big left-moving asteroid can destroy several.
3. **Forgetting the equal-size case** (both explode).
4. **Pushing `a` after it exploded.** Use the `alive` flag.
5. **Sign mistake:** compare `top` with `-a`, not `a`.

#### 6. Say This in the Interview

1. "Only a right-moving asteroid on the stack and a new left-moving asteroid can collide."
2. "I loop while the new asteroid is alive and the top is moving right. Smaller tops are popped. Equal sizes remove both. A bigger top destroys the new one."
3. "Each asteroid is pushed once and popped at most once, so it is `O(n)`."

#### 7. Quick Check

1. What does `[-2, -1, 1, 2]` give? Why?
2. What does `[5, -5]` give?

<details>
<summary>Answers</summary>

1. `[-2, -1, 1, 2]`. The left-movers are already on the left, and the right-movers move away. Nothing meets.
2. `[]`. Equal sizes, both explode.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 735 | Asteroid Collision (Medium) | this note |
| 853 | Car Fleet (Medium) | stack of arrival times |
| 1047 | Remove All Adjacent Duplicates In String (Easy) | cancel neighbours |
| 2751 | Robot Collisions (Hard) | sort by position, then the same stack idea |
