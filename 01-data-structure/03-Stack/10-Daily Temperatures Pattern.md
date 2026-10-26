# Daily Temperatures Pattern

#### 1. What Is It?

You get the temperature of each day. For every day, find **how many days you must wait for a warmer day**. If no warmer day comes, the answer is `0`.

```text
temps  = [73, 74, 75, 71, 69, 72, 76, 73]
answer = [ 1,  1,  4,  2,  1,  1,  0,  0]
```

Day 2 (75°): the next warmer day is day 6 (76°), so you wait `6 - 2 = 4` days.

This is *Daily Temperatures* (LeetCode 739). It is **Next Greater Element**, but the answer is a **distance** (a number of days), not a value. It is one of the most common stack questions.

#### 2. How It Works

Use a stack of **day indexes** for days still waiting for a warmer day. Their temperatures go down from bottom to top.

When today is warmer than the day on top, that day has found its answer: `today - thatDay`.

```text
i=0 (73): push 0                                       waiting: [0]
i=1 (74): 74 > 73 → pop 0, answer[0] = 1-0 = 1.  push  waiting: [1]
i=2 (75): 75 > 74 → pop 1, answer[1] = 1.  push        waiting: [2]
i=3 (71): 71 < 75 → push                               waiting: [2, 3]
i=4 (69): 69 < 71 → push                               waiting: [2, 3, 4]
i=5 (72): 72 > 69 → pop 4, answer[4] = 5-4 = 1
          72 > 71 → pop 3, answer[3] = 5-3 = 2
          72 < 75 → stop.  push                        waiting: [2, 5]
i=6 (76): 76 > 72 → pop 5, answer[5] = 1
          76 > 75 → pop 2, answer[2] = 6-2 = 4
          push                                         waiting: [6]
i=7 (73): 73 < 76 → push                               waiting: [6, 7]

Days 6 and 7 never get popped → answer stays 0.
```

#### 3. Brute Force vs Optimized

| | Brute force | Optimized |
|---|---|---|
| Idea | for each day, look ahead for a warmer day | stack of waiting days |
| Time | `O(n²)` | `O(n)` |
| Space | `O(1)` extra | `O(n)` |

The brute force is easy to write, and it is a good first answer to say out loud:

```kotlin
fun dailyTemperaturesBrute(temps: IntArray): IntArray {
    val answer = IntArray(temps.size)
    for (i in temps.indices) {
        for (j in i + 1 until temps.size) {
            if (temps[j] > temps[i]) { answer[i] = j - i; break }
        }
    }
    return answer
}
```

Say it in the interview: "brute force is `O(n²)`; a monotonic stack makes it `O(n)`."

#### 4. Kotlin Code

```kotlin
fun dailyTemperatures(temperatures: IntArray): IntArray {
    val answer = IntArray(temperatures.size)               // all 0 at the start
    val stack = ArrayDeque<Int>()                          // indexes of days waiting
    for (i in temperatures.indices) {
        while (stack.isNotEmpty() && temperatures[stack.last()] < temperatures[i]) {
            val day = stack.removeLast()
            answer[day] = i - day                          // days to wait
        }
        stack.addLast(i)
    }
    return answer
}
```

Checks: `dailyTemperatures([73,74,75,71,69,72,76,73])` → `[1,1,4,2,1,1,0,0]`. `dailyTemperatures([30,40,50,60])` → `[1,1,1,0]`. `dailyTemperatures([30,60,90])` → `[1,1,0]`.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Monotonic stack | `O(n)` | `O(n)` |
| Brute force | `O(n²)` | `O(1)` |

#### 6. Common Mistakes

1. **Storing temperatures in the stack.** You then cannot compute `i - day`. Store **indexes**.
2. **Writing the temperature as the answer.** The answer is a **distance**: `i - day`.
3. **`<=` instead of `<`.** The day must be **strictly** warmer.
4. **Forgetting that waiting days stay `0`.**
5. **Reading `stack.last()` on an empty stack.** Check `isNotEmpty()`.

#### 7. Say This in the Interview

1. "Brute force is `O(n²)`. I will use a monotonic stack of day indexes."
2. "When today is warmer than the top day, I pop it and set its answer to the difference of indexes."
3. "Each day is pushed and popped once. Time `O(n)`, space `O(n)`."
4. "Days left in the stack have no warmer day, so they stay `0`."

#### 8. Quick Check

1. What is the answer for `[50, 40, 30]`?
2. What is the answer for `[30, 30, 30]`?

<details>
<summary>Answers</summary>

1. `[0, 0, 0]`. It only gets colder.
2. `[0, 0, 0]`. Equal is not warmer.

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium) | this note |
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) (Easy) | value instead of distance |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) (Medium) | circular array |
| 1475 | [Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) (Easy) | next smaller or equal |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) (Medium) | the previous direction |
