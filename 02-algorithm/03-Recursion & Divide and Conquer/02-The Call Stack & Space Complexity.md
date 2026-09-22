# The Call Stack & Space Complexity

#### 1. Definition — Must Know

1. The **call stack** is where the program keeps track of function calls that are in progress.
2. Each time a function calls another function (or itself), a new **stack frame** is pushed. When that call returns, its frame is popped.

#### 2. Why It Is Used — Must Know

1. It is how recursion actually runs under the hood — you don't manage it yourself, the language runtime does.
2. Understanding it explains two real things: why recursion has a space cost, and why very deep recursion can crash.

#### 3. How It Works — Must Know

```text
factorial(3)
 → calls factorial(2)
    → calls factorial(1)
       → base case, returns 1
    ← returns 2 * 1 = 2
 ← returns 3 * 2 = 6
```

```text
Stack while factorial(1) is running:

| factorial(1) |  ← top of stack (most recent call)
| factorial(2) |
| factorial(3) |  ← bottom (first call)
```

1. Frames stack up as calls go deeper (the arrows going in).
2. Frames pop off as calls return (the arrows coming out), in reverse order — last in, first out.
3. Each frame holds that call's local variables and where to resume after the call returns.

#### 4. Algorithm — Must Know

There is nothing to implement — the call stack is managed automatically. What you control is the **depth**:

```text
depth = how many nested calls happen before reaching the base case
```

1. `factorial(n)` has depth `n`.
2. A recursive tree search has depth equal to the height of the tree.

#### 5. Kotlin Implementation — Must Know

```kotlin
fun sumTo(n: Int): Int {
    if (n == 0) return 0
    return n + sumTo(n - 1)   // n stack frames deep at most
}
```

Each call to `sumTo` stays on the stack, waiting for `sumTo(n - 1)` to return, before it can compute `n + ...` and return itself.

#### 6. Complexity — Must Know

| What | Cost |
|---|---|
| Space per recursive call | O(1) extra (a small stack frame) |
| Total space | O(depth) — one frame per level of recursion |

1. **Space complexity of recursion is about depth, not about how many total calls happen.** `factorial(n)` makes `n` calls and also has depth `n`, so its space is O(n). A divide-and-conquer function can make many more total calls but stay shallow (topic 3).
2. A very deep, non-tail recursive call (for example `factorial(1_000_000)`) can throw a `StackOverflowError`, because the call stack has a fixed, limited size.

#### 7. Common Mistakes — Must Know

1. Assuming recursion is "free" — it always costs stack space proportional to its depth.
2. Recursing on large input without checking whether the depth could exceed the stack limit.
3. Confusing the number of calls with the depth of the stack — they are not the same thing.
4. Not realising that an iterative loop uses O(1) space where the equivalent recursion uses O(n).

#### 8. Related Topics

1. `1` Base Case & Recursive Case — what stops the stack from growing forever
2. `6` Tail Recursion — a case Kotlin can optimise to avoid growing the stack
3. `7` Recursion to Iteration — replacing the call stack with your own explicit stack

#### 9. Interview Must Remember

1. Every recursive call pushes a **stack frame**; every return pops one.
2. **Space complexity of recursion = its depth**, not its total number of calls.
3. Deep recursion can overflow the stack — mention this as a downside when you propose a recursive solution.
