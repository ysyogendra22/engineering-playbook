# Proving Correctness with an Exchange Argument

#### 1. Definition — Must Know

1. An **exchange argument** proves a greedy algorithm is correct by showing that any other (non-greedy) solution can be turned into the greedy one, step by step, without ever making it worse.
2. In plain words: "if a better solution existed, I could swap in my greedy choice and the answer wouldn't get worse — so greedy is at least as good as anything else."

#### 2. Why It Is Used — Must Know

1. It's the standard way to justify a greedy algorithm properly, instead of just saying "it seemed to work on my examples".
2. In an interview, giving even a short version of this argument makes your greedy answer far more convincing.

#### 3. How It Works — Must Know

Worked example: Activity Selection, proving "always pick the meeting that ends earliest" is correct.

```text
Claim: picking the activity that ends earliest is always part of some optimal solution.

Suppose an optimal solution picks some other first activity, X, instead of the
earliest-ending activity, E (where E.end <= X.end).

Since E ends no later than X, swapping X for E in that solution cannot cause any
conflict with whatever came after X — E frees up at least as much time as X did.

So we can exchange X for E, and the solution is still valid and no smaller.

This means an optimal solution containing E always exists — so the greedy choice
(pick E first) is safe.
```

#### 4. Algorithm — Must Know

*(A proof method, not code.)* The general shape of an exchange argument:

```text
1. Assume some optimal solution does NOT make the greedy choice at step one.
2. Show that swapping in the greedy choice keeps the solution valid.
3. Show the swap doesn't make the solution worse (it stays the same size or cost, or improves).
4. Conclude: an optimal solution exists that DOES start with the greedy choice.
5. Repeat the same argument for the remaining steps (often by induction).
```

#### 5. Kotlin Implementation — Must Know

*(Nothing to implement — this section explains why the code in topic 2 and topic 4 is correct, not a new algorithm.)*

#### 6. Complexity — Must Know

Not applicable — an exchange argument is about **correctness**, not the running time of the algorithm.

#### 7. Common Mistakes — Must Know

1. Skipping this step entirely and only testing a couple of examples — examples can't prove a greedy algorithm always works.
2. Writing an exchange argument that only shows the swap is *valid*, without also showing it isn't *worse* — both parts are needed.
3. Trying to force an exchange argument onto a problem that genuinely doesn't have the greedy choice property (topic 1) — if you can't complete the argument, that's a signal greedy may be wrong.

#### 8. Related Topics

1. `1` The Greedy Choice Property — what the exchange argument is proving
2. `4` Activity / Interval Selection — the example used here in full
3. `9` Why Greedy Fails — 0/1 Knapsack & General Coin Change — where the argument breaks down

#### 9. Interview Must Remember

1. The short version to say out loud: **"if a better solution didn't include my greedy choice, I could swap it in without making things worse — so it's safe to make greedily."**
2. You don't need a formal proof in an interview — a clear one- or two-sentence version of this argument is usually enough.
3. If you can't construct this argument, that's a warning sign your greedy idea might be wrong.
