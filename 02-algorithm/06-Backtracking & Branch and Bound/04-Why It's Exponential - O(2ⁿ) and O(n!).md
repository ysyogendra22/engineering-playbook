# Why It's Exponential: O(2ⁿ) and O(n!)

#### 1. Definition — Must Know

Backtracking explores a decision tree (topic 2), and the number of leaves in that tree — the number of possible answers — is usually **exponential** or **factorial** in the input size, which is why backtracking's time complexity is almost always O(2ⁿ), O(n!), or similar.

#### 2. Why It Is Used — Must Know

1. Knowing *why* the complexity is what it is (not just memorising "backtracking is O(2ⁿ)") lets you correctly state the complexity for a *new* backtracking problem you haven't seen before.
2. It also tells you the practical limit: backtracking is usually only workable for small n (often n ≤ 20 or so), which is worth saying in an interview.

#### 3. How It Works — Must Know

```text
Subsets: at each of n elements, you choose "include" or "exclude" — 2 options.
         Total subsets = 2 × 2 × 2 × ... (n times) = 2ⁿ

Permutations: for the 1st position, n choices. For the 2nd, n-1 remain.
              For the 3rd, n-2 remain. And so on.
              Total permutations = n × (n-1) × (n-2) × ... × 1 = n!

Combinations (choose k of n): fewer than 2ⁿ, but still large —
              n! / (k! × (n-k)!)
```

`n! ` grows even faster than `2ⁿ` — for `n = 20`, `2ⁿ ≈ 1,000,000`, but `n! ≈ 2.4 × 10¹⁸`.

#### 4. Algorithm — Must Know

```text
To work out the rough complexity of a NEW backtracking problem:
1. What is the branching factor at each level? (how many choices at each step)
2. What is the depth of the tree? (how many decisions are made total)
3. Complexity ≈ (branching factor) ^ (depth), or the exact count if it shrinks
   per level (like permutations)
```

#### 5. Kotlin Implementation — Must Know

*(Nothing to implement — this is an analysis, applied to the code already shown in topics 1 through 3.)*

#### 6. Complexity — Must Know

| Problem | Branching pattern | Complexity |
|---|---|---|
| Subsets | 2 choices at every position | O(2ⁿ) |
| Permutations | n, then n-1, then n-2, ... choices | O(n!) |
| Combinations (choose k of n) | Fewer branches, bounded by k | O(n choose k), smaller than 2ⁿ |
| N-Queens | n choices per row, pruned heavily | Much less than n^n in practice, thanks to pruning (topic 3) |

#### 7. Common Mistakes — Must Know

1. Assuming all backtracking problems are O(2ⁿ) — permutation-style problems are O(n!), which is a different (larger) growth rate.
2. Forgetting that pruning (topic 3) reduces the *actual* runtime without changing the *stated* worst-case complexity in most cases.
3. Proposing a backtracking solution for a large n (hundreds or thousands) without flagging that it won't finish in reasonable time — this is a real design smell to call out.

#### 8. Related Topics

1. `2` Modelling Choices as a Decision Tree — where the branching factor and depth come from
2. `3` Pruning — Stopping a Branch Early — reduces the real-world cost, not the worst case
3. `11` Complexity Classes (P, NP, NP-Complete) (its own folder) — why some problems have no known fast solution at all

#### 9. Interview Must Remember

1. **Subsets → O(2ⁿ). Permutations → O(n!).** Know both, and know why they differ.
2. Complexity ≈ branching factor raised to the depth, or the exact count for shrinking branching factors.
3. Say explicitly when input size makes a backtracking solution impractical — that awareness is itself a strong signal in an interview.
