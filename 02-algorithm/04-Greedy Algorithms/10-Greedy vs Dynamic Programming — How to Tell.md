# Greedy vs Dynamic Programming — How to Tell

#### 1. Definition — Must Know

1. Both greedy and Dynamic Programming solve optimisation problems ("find the minimum/maximum/best"), but they work differently: greedy makes one pass with irreversible choices; DP considers subproblems and remembers their best answers.
2. Telling them apart quickly is a core interview skill — most "optimize this" problems are one or the other.

#### 2. Why It Is Used — Must Know

1. Trying greedy first is usually faster to reason about, but using it on a problem that needs DP gives a wrong answer with no warning.
2. Knowing the checklist below turns "let me just try something" into a deliberate, explainable decision.

#### 3. How It Works — Must Know

```text
Ask: "If I make the locally best choice now, could a different choice earlier
      have opened up a better option later that I've now locked out?"

If NO  (the greedy choice never closes off a better future option)  → try greedy
If YES (an earlier choice can trap you into a worse later outcome)  → use DP
```

| Signal | Points to |
|---|---|
| Sorting the input makes the answer obvious | Greedy |
| You can prove correctness with an exchange argument (topic 3) | Greedy |
| A small example breaks the "obvious" greedy rule | Dynamic Programming |
| The problem says "items can't be split" or "each item used once" | Often DP (0/1 Knapsack shape) |
| The same subproblem clearly gets solved more than once | Dynamic Programming |
| The problem is about *counting ways*, not just the best single value | Dynamic Programming |

#### 4. Algorithm — Must Know

```text
1. Propose the obvious greedy rule.
2. Try to break it with a small, deliberately tricky example (topic 1).
3. If it breaks: switch to DP — define the state and recurrence (see `05-Dynamic Programming`).
4. If it survives a few attempts: try to justify it with an exchange argument (topic 3).
5. Say your reasoning out loud either way — that's the actual skill being tested.
```

#### 5. Kotlin Implementation — Must Know

*(Nothing to implement — this is a decision process, not an algorithm.)*

#### 6. Complexity — Must Know

| | Typical complexity |
|---|---|
| Greedy (when correct) | O(n log n) |
| Dynamic Programming | O(n × states), often much larger |

This is part of why it's worth checking for greedy first — it's usually cheaper, when it's actually correct.

#### 7. Common Mistakes — Must Know

1. Committing to greedy without testing a counter-example, then running out of time when it turns out wrong.
2. Assuming a problem needs DP just because it sounds hard — many "hard-sounding" problems are simple greedy once sorted correctly.
3. Not noticing the tell-tale DP phrases: "each item can be used once", "count the number of ways", "subsequence" (as opposed to "subarray" or "substring", which are often greedy or sliding-window).

#### 8. Related Topics

1. `1` The Greedy Choice Property
2. `9` Why Greedy Fails — 0/1 Knapsack & General Coin Change
3. `5` Dynamic Programming (its own folder) — full topic index

#### 9. Interview Must Remember

1. **Try greedy first, but always test it with a counter-example before committing.**
2. "Can't be split" / "used once" / "count the ways" are strong signals for DP.
3. Saying "let me check if the greedy choice can trap me into a worse option later" is the exact reasoning interviewers want to hear.
