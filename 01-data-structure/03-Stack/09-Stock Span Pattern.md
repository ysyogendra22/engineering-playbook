# Stock Span Pattern

#### 1. What Is It?

The **span** of today's stock price is the number of **days in a row, ending today, with a price less than or equal to today's price**. Today counts as one day.

```text
prices: 100, 80, 60, 70, 60, 75, 85
spans :   1,  1,  1,  2,  1,  4,  6
```

Why `75` has span `4`: going back from today, the prices `60`, `70`, `60`, `75` are all `<= 75`. Then `80` is bigger, so we stop.

The prices arrive **one at a time** (online). You must answer each day immediately.

This is *Online Stock Span* (LeetCode 901). It is the **previous greater element** problem: span = today's index − index of the previous bigger price.

#### 2. How It Works

Keep a stack of `(price, span)` with **prices going down** from bottom to top. When a new price arrives:

1. Start with `span = 1` (today).
2. While the top price is `<=` today's price, **pop it and add its span**. Those earlier days are not bigger than the popped price, so they are not bigger than today either.
3. Push `(today's price, span)`.

```text
Day 5, price 75.   Stack before: (100,1) (80,1) (70,2) (60,1)

span = 1
top (60,1): 60 <= 75 → pop, span = 1 + 1 = 2
top (70,2): 70 <= 75 → pop, span = 2 + 2 = 4
top (80,1): 80 >  75 → stop

push (75, 4)    Stack: (100,1) (80,1) (75,4)
```

Adding the popped spans lets us skip days we have already counted. We never walk back one day at a time.

#### 3. Kotlin Code

```kotlin
class StockSpanner {
    private val stack = ArrayDeque<IntArray>()          // each entry: [price, span]

    fun next(price: Int): Int {
        var span = 1
        while (stack.isNotEmpty() && stack.last()[0] <= price) {
            span += stack.removeLast()[1]
        }
        stack.addLast(intArrayOf(price, span))
        return span
    }
}

// Usage
val spanner = StockSpanner()
for (p in intArrayOf(100, 80, 60, 70, 60, 75, 85)) print("${spanner.next(p)} ")   // 1 1 1 2 1 4 6
```

If you already have the whole array, use indexes instead:

```kotlin
fun stockSpans(prices: IntArray): IntArray {
    val spans = IntArray(prices.size)
    val stack = ArrayDeque<Int>()                       // indexes, prices decreasing
    for (i in prices.indices) {
        while (stack.isNotEmpty() && prices[stack.last()] <= prices[i]) stack.removeLast()
        val previousGreater = if (stack.isEmpty()) -1 else stack.last()
        spans[i] = i - previousGreater
        stack.addLast(i)
    }
    return spans
}
```

#### 4. Complexity

| | Time | Space |
|---|---|---|
| One call to `next` | `O(1)` on average | — |
| `n` calls | `O(n)` | `O(n)` |
| Brute force per call | `O(n)` | — |

Each price is pushed once and popped once. That is why the average is `O(1)` per call.

#### 5. Common Mistakes

1. **Using `<` instead of `<=`.** Days with an **equal** price must count.
2. **Starting `span` at 0.** Today always counts, so start at 1.
3. **Not adding the popped span.** You would count those days again or miss them.
4. **Keeping the stack as a local variable.** It must live in the class between calls.
5. **`if` instead of `while`.** Several entries may need to be popped.

#### 6. Say This in the Interview

1. "Span is today's index minus the index of the previous greater price."
2. "I keep a stack of price and span. I pop prices that are `<=` today and add their spans."
3. "Each price is pushed and popped once, so each call is `O(1)` on average."

#### 7. Quick Check

1. What is the span of the very first price?
2. Prices `10, 20, 30`. What are the spans?

<details>
<summary>Answers</summary>

1. `1`. Only today counts.
2. `1, 2, 3`. Each new price is bigger than all the earlier ones.

</details>

#### 8. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 901 | Online Stock Span (Medium) | this note |
| 739 | Daily Temperatures (Medium) | next greater, distance forward |
| 1944 | Number of Visible People in a Queue (Hard) | stack with both sides |
| 84 | Largest Rectangle in Histogram (Hard) | previous smaller bars |
