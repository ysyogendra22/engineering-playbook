# The Four Steps — State, Recurrence, Base Case, Fill Order

#### 1. Definition — Must Know

Every DP problem is solved by answering four questions, in this order:

1. **State** — what does a subproblem look like? What do you need to know to describe it (usually one or two numbers, like an index or a remaining capacity)?
2. **Recurrence** — how does the answer for one state relate to the answers of smaller states?
3. **Base case** — what are the smallest states, whose answers you know directly?
4. **Fill order** — in what order do you compute the states, so that whenever you need a smaller state's answer, it's already been computed?

#### 2. Why It Is Used — Must Know

1. This is the actual **method** for solving a DP problem — not a trick, a repeatable four-step process.
2. Interviewers watch for this structure specifically: candidates who jump straight to code without defining the state usually get stuck or write a subtly wrong recurrence.

#### 3. How It Works — Must Know

Worked example: **Climbing Stairs** — you can climb 1 or 2 steps at a time; how many distinct ways to reach step `n`?

```text
1. State:      dp[i] = number of ways to reach step i
2. Recurrence: dp[i] = dp[i - 1] + dp[i - 2]
               (the last move to reach step i was either a 1-step from i-1,
                or a 2-step from i-2 — add the ways from both)
3. Base case:  dp[0] = 1 (one way: do nothing)
               dp[1] = 1 (one way: a single 1-step)
4. Fill order: compute dp[2], dp[3], ..., dp[n] in increasing order,
               since each one needs the two states before it
```

```text
dp[0]=1  dp[1]=1  dp[2]=2  dp[3]=3  dp[4]=5  dp[5]=8 ...
```

#### 4. Algorithm — Must Know

```text
1. Write in words: "dp[state] = ___"  (this forces you to define the state clearly)
2. Write the recurrence: "dp[state] = f(dp[smaller states])"
3. Write the base case(s): the states too small to use the recurrence
4. Decide the fill order: usually smallest state to largest, but check
   your recurrence to be sure (some 2D problems need row-by-row, others
   need diagonal order)
5. Only now, write the code
```

#### 5. Kotlin Implementation — Must Know

```kotlin
fun climbStairs(n: Int): Int {
    if (n <= 1) return 1
    val dp = IntArray(n + 1)
    dp[0] = 1               // base case
    dp[1] = 1               // base case
    for (i in 2..n) {       // fill order: smallest to largest
        dp[i] = dp[i - 1] + dp[i - 2]   // recurrence
    }
    return dp[n]             // final state
}
```

#### 6. Complexity — Must Know

| | Cost |
|---|---|
| Time | O(number of states) × O(work per recurrence step) |
| Space | O(number of states), often reducible (topic 7) |

For Climbing Stairs: O(n) states, O(1) work each, so O(n) time, O(n) space (or O(1) with space optimisation).

#### 7. Common Mistakes — Must Know

1. Writing code before clearly stating the state — this is the single biggest source of DP bugs.
2. A recurrence that references a state that hasn't been computed yet, because the fill order is wrong.
3. Missing a base case, so the recurrence tries to look up a state that was never set.
4. Confusing "the state" (what varies between subproblems) with "the answer" (the value stored at that state).

#### 8. Related Topics

1. `1` Optimal Substructure & Overlapping Subproblems — confirms DP applies before you start these steps
2. `4` 1D DP — Fibonacci, Climbing Stairs, House Robber — more worked examples of this method
3. `5` 2D DP — Grid Paths, Edit Distance, Longest Common Subsequence — the two-variable version of state

#### 9. Interview Must Remember

1. Say the four steps **out loud, in order**: state, recurrence, base case, fill order.
2. Write "dp[state] = " on the whiteboard or in a comment before writing any loop — it forces clarity.
3. If the recurrence doesn't come easily, you likely haven't defined the state precisely enough yet — go back to step 1.
