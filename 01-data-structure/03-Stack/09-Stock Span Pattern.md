# Stock Span Pattern

#### 1. Definition — Must Know

1. The **span** of a stock price on a day is the number of **consecutive days up to and including today** on which the price was **less than or equal** to today's price.
2. It is *Online Stock Span* (LeetCode 901). The prices come **one at a time** (online), and you must answer each day at once.
3. Span = `today's index − index of the previous day with a strictly greater price`.

#### 2. Why It Is Used — Must Know

1. It is the standard example of **previous greater element** with a stack.
2. The "online" form (one price per call) tests if you can keep state between calls.
3. The same idea counts "how many previous items are not bigger than me".

#### 3. How It Works — Must Know

Prices: `100, 80, 60, 70, 60, 75, 85`.

```text
day 0: 100   no greater before            span 1
day 1:  80   100 > 80 → stop              span 1
day 2:  60   80 > 60 → stop               span 1
day 3:  70   60 <= 70 (counts), 80 > 70   span 2
day 4:  60   70 > 60 → stop               span 1
day 5:  75   60, 70, 60 are <= 75, 80 > 75   span 4
day 6:  85   80, 60, 70, 60, 75 are all <= 85; 100 > 85 stops   span 6

spans: [1, 1, 1, 2, 1, 4, 6]
```

Efficient method: keep a stack of `(price, span)` with **decreasing prices**. When a new price arrives, **pop every entry with a price <= today's price and add its span** to today's span. Those days are already "covered" by the popped entries.

```text
day 5 (75): stack before: (100,1) (80,1) (70,2) (60,1)
   pop (60,1): span = 1 + 1 = 2
   pop (70,2): span = 2 + 2 = 4
   (80,1) > 75 → stop
   push (75, 4)  → stack: (100,1) (80,1) (75,4)
```

#### 4. Core Concepts — Must Know

1. **Decreasing stack** of `(price, span)` (bottom to top: big → small prices).
2. **Today's span starts at 1** (today counts itself).
3. **Pop while `top.price <= price`** and add `top.span` to today's span.
4. **Push `(price, span)`.**
5. **Why add spans instead of counting days?** A popped entry already represents a whole block of earlier days that were not bigger than it, so they are not bigger than today either.
6. **Index version:** keep a stack of indexes and use `span = i - previousGreaterIndex`. This is the version for arrays given up front.
7. **Amortized `O(1)` per call**, since each price is pushed and popped once.

| Version | When |
|---|---|
| Stack of `(price, span)` | online, prices arrive one by one |
| Stack of indexes + `i - prev` | whole array available |

#### 5. Algorithm — Must Know

```text
next(price):
    span = 1
    while stack not empty and stack.top.price <= price:
        span += stack.pop().span
    stack.push((price, span))
    return span
```

#### 6. Kotlin Implementation — Must Know

```kotlin
// Online Stock Span (LeetCode 901)
class StockSpanner {
    private val stack = ArrayDeque<IntArray>()           // each entry: [price, span]

    fun next(price: Int): Int {
        var span = 1
        while (stack.isNotEmpty() && stack.last()[0] <= price) {
            span += stack.removeLast()[1]
        }
        stack.addLast(intArrayOf(price, span))
        return span
    }
}

// Offline version: the whole array is known
fun stockSpans(prices: IntArray): IntArray {
    val spans = IntArray(prices.size)
    val stack = ArrayDeque<Int>()                         // indexes, prices decreasing
    for (i in prices.indices) {
        while (stack.isNotEmpty() && prices[stack.last()] <= prices[i]) stack.removeLast()
        val previousGreater = if (stack.isEmpty()) -1 else stack.last()
        spans[i] = i - previousGreater
        stack.addLast(i)
    }
    return spans
}

// Usage
val spanner = StockSpanner()
for (p in intArrayOf(100, 80, 60, 70, 60, 75, 85)) print("${spanner.next(p)} ")   // 1 1 1 2 1 4 6
```

#### 7. Time & Space Complexity — Must Know

| Operation | Time | Space |
|---|---:|---:|
| One `next(price)` | `O(1)` amortized | — |
| `n` calls | `O(n)` | `O(n)` worst case (strictly decreasing prices) |
| Brute force per call | `O(n)` | — |

#### 8. Common Span Patterns — Must Know

1. **Online Stock Span** (LeetCode 901).
2. **Daily Temperatures** (LeetCode 739) — next greater, distance forward.
3. **Number of Visible People in a Queue** (LeetCode 1944).
4. **Count of subarrays where the last element is the maximum** — same span idea.
5. **Previous greater element** (the building block).
6. **Consecutive days of a metric** (e.g. days with a value at or below today) in dashboards.
7. **Android example:** how many recent screen loads were faster than or equal to the current one.

#### 9. Edge Cases / Common Mistakes

1. Using `<` instead of `<=`. The span must include days with an **equal** price.
2. Starting `span` at 0 instead of 1.
3. Not adding the popped span, and counting the popped days again by walking back.
4. Forgetting that the stack must be kept between calls (a class field, not a local).
5. Popping only one entry (it must be a `while` loop).
6. First call: stack empty, span `1`.
7. Mixing the offline `i - prev` formula with the `(price, span)` stack.

#### 10. When to Use / When Not to Use

**Use when:**

1. You need "how many consecutive previous items are not larger than me", and data arrives over time.

**Avoid when:**

1. You need sliding-window answers (limited number of days). The stack does not forget old entries; use a deque for windows.

#### 11. Related Topics

1. Previous Greater / Smaller Element
2. Monotonic Stack
3. Daily Temperatures Pattern
4. Design questions that keep state across calls

#### 12. Interview Must Remember

1. **Stack of `(price, span)`; pop while `top.price <= price`, add spans.**
2. Span starts at 1 and includes equal prices.
3. Amortized `O(1)` per call.
4. Offline: `span = i - previousGreaterIndex`.
