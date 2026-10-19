# Daily Temperatures Pattern

#### 1. Definition — Must Know

1. Given daily temperatures, for each day find **how many days you must wait for a warmer temperature**. If there is no warmer day, the answer is `0`.
2. It is *Daily Temperatures* (LeetCode 739). If a number and a title ever disagree, trust the title.
3. It is **Next Greater Element**, but the answer is a **distance** (in days), not a value.

#### 2. Why It Is Used — Must Know

1. It is the most common monotonic-stack interview question.
2. It shows the "distance to the next bigger item" pattern: `answer[i] = j - i`.
3. The brute force is `O(n²)`; the stack is `O(n)`.

#### 3. How It Works — Must Know

`temps = [73, 74, 75, 71, 69, 72, 76, 73]`

The stack holds **indexes of days still waiting for a warmer day** (their temperatures are decreasing).

```text
i=0 (73): push 0                                  stack idx: [0]
i=1 (74): 73 < 74 → pop 0: answer[0] = 1-0 = 1    push 1     [1]
i=2 (75): 74 < 75 → pop 1: answer[1] = 1          push 2     [2]
i=3 (71): 75 > 71 → push 3                        [2, 3]
i=4 (69): 71 > 69 → push 4                        [2, 3, 4]
i=5 (72): 69 < 72 → pop 4: answer[4] = 5-4 = 1
          71 < 72 → pop 3: answer[3] = 5-3 = 2
          75 > 72 → stop, push 5                  [2, 5]
i=6 (76): 72 < 76 → pop 5: answer[5] = 1
          75 < 76 → pop 2: answer[2] = 6-2 = 4    push 6     [6]
i=7 (73): 76 > 73 → push 7                        [6, 7]

Left: idx6, idx7 → answer 0

answer: [1, 1, 4, 2, 1, 1, 0, 0]
```

#### 4. Core Concepts — Must Know

1. **Decreasing stack of indexes** (temperatures decrease from bottom to top).
2. **When day `i` is warmer than the top, the top has found its answer:** `i - top`.
3. **The answer array starts at all `0`.** Days that never get popped stay `0`.
4. **Strictly warmer:** pop while `temps[top] < temps[i]`.
5. **Alternative from the right:** `answer[i]` can be found by jumping through already-computed answers (`i + answer[j]`), using `O(1)` extra space.
6. **Same engine, other questions:** next greater value, stock span (previous), days until a price drop.

#### 5. Algorithm — Must Know

```text
answer = all 0; stack = empty
for i in 0 until n:
    while stack not empty and temps[stack.top] < temps[i]:
        j = stack.pop()
        answer[j] = i - j
    stack.push(i)
return answer
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Daily Temperatures — monotonic stack
fun dailyTemperatures(temperatures: IntArray): IntArray {
    val answer = IntArray(temperatures.size)
    val stack = ArrayDeque<Int>()                            // indexes, temperatures decreasing
    for (i in temperatures.indices) {
        while (stack.isNotEmpty() && temperatures[stack.last()] < temperatures[i]) {
            val j = stack.removeLast()
            answer[j] = i - j
        }
        stack.addLast(i)
    }
    return answer
}

// O(1) extra space: scan from the right and jump using known answers
fun dailyTemperaturesNoStack(temps: IntArray): IntArray {
    val n = temps.size
    val answer = IntArray(n)
    for (i in n - 2 downTo 0) {
        var j = i + 1
        while (j < n && temps[j] <= temps[i]) {
            if (answer[j] == 0) { j = n; break }             // no warmer day after j either
            j += answer[j]                                   // jump straight to j's next warmer day
        }
        if (j < n) answer[i] = j - i
    }
    return answer
}
```

Checks: `dailyTemperatures([73,74,75,71,69,72,76,73])` → `[1,1,4,2,1,1,0,0]`. `dailyTemperatures([30,40,50,60])` → `[1,1,1,0]`. `dailyTemperatures([30,60,90])` → `[1,1,0]`.

#### 7. Time & Space Complexity — Must Know

| Approach | Time | Space |
|---|---:|---:|
| Brute force | `O(n²)` | `O(1)` |
| **Monotonic stack** | **`O(n)`** | `O(n)` |
| Right-to-left jumping | `O(n)` amortized | `O(1)` extra |

#### 8. Common Variations — Must Know

1. **Daily Temperatures** (LeetCode 739).
2. **Next Greater Element** (value instead of distance).
3. **Days until a lower price** — flip the comparison.
4. **Final Prices With a Special Discount** (LeetCode 1475).
5. **Car Fleet** (LeetCode 853) — a related stack idea with times.
6. **Number of Visible People in a Queue** (LeetCode 1944).
7. **Online Stock Span** — the previous-direction mirror.
8. **Android example:** time until the next higher frame time, or the next larger battery drop.

#### 9. Edge Cases / Common Mistakes

1. Storing temperatures in the stack and being unable to compute `i - j`. Store indexes.
2. Using `<=` when the problem wants **strictly** warmer (equal temperatures would pop wrongly).
3. Writing `answer[j] = temps[i]` (a value) instead of `i - j` (a distance).
4. Forgetting that days left in the stack stay `0`.
5. Using a `while` loop condition that does not check `isNotEmpty()`.
6. Off-by-one: the answer for the day after a warmer day is `1`, not `0`.
7. Single-element array: answer `[0]`.
8. All equal or all decreasing temperatures: all zeros.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need the distance to the next larger item for every position.

**Avoid when:**

1. You need the answer within a fixed window (deque).
2. You can use the `O(1)` space scan and memory is tight.

#### 11. Related Topics

1. Next Greater Element
2. Monotonic Stack
3. Stock Span Pattern
4. Monotonic Stack pattern (`03-leetcode-patterns`, topic 10)

#### 12. Interview Must Remember

1. **Decreasing stack of indexes; when `temps[i] > temps[top]`, `answer[top] = i - top`.**
2. Leftover days → `0`.
3. Strictly warmer → pop on `<`.
4. `O(n)` time, `O(n)` space (or `O(1)` with the right-to-left jump).
