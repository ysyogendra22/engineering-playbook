# Coding Interview Answer Points

> A correct solution is not enough. You also need to show how you think, so the interviewer can say "hire".

#### 1. What Is It?

Interviewers usually score four things:

| Area | What they look for |
|---|---|
| Communication | you explain your thinking, ask questions, take hints well |
| Problem solving | you find the pattern, compare approaches, and know the trade-offs |
| Coding | clean, correct, readable Kotlin |
| Testing | you check your own code with examples and edge cases |

The structure of a strong answer:

1. **Restate** the problem and confirm input and output.
2. **Brute force first**, with its complexity.
3. **Name the pattern** and say *why* (the signal).
4. **Plan** in plain words. Get a nod before coding.
5. **Code** while narrating. Use clear names and small helpers.
6. **Dry-run** an example, then edge cases.
7. **State complexity** and where it comes from.
8. **Discuss** follow-ups and trade-offs.

#### 2. How It Works

**A short sample (Longest Substring Without Repeating Characters).**

> **You:** "So given a string, I return the length of the longest substring with no repeated characters. Can the string be empty? What characters can it contain?"
> **Interviewer:** "Could be empty. ASCII."
> **You:** "A brute force checks every substring for duplicates, which is `O(n²)` to `O(n³)`. The problem asks for a contiguous range with a condition, so I'll use a sliding window. I grow the right end, and if I see a repeated character, I jump `left` past its previous position."
> **You (before coding):** "I store each character's last index in a map. For `abcabcbb` that gives 3. Does that plan sound good?"
> **You (after coding):** "Trace `pwwkew`: at the second `w`, `left` moves to index 2. The window is `w`, then `wk`, then `wke`: length 3. For the empty string the loop never runs and I return 0. Time `O(n)`, space `O(min(n, alphabet))`."

**Follow-up questions and how to answer**

| Follow-up | Good answer |
|---|---|
| "Can you do better?" | Say where time or space is spent and what could remove it (a map, a sort, an invariant) |
| "What if the input is huge or streaming?" | Process in one pass, keep only counters or a window, or use a heap of size K |
| "What if there are duplicates?" | Say what changes (sort and skip, count with a map) |
| "Can you do it in place?" | Two pointers, swaps, or reuse the input array; note the trade-off (mutating input) |
| "What about negative numbers?" | Sliding window sums may fail; use prefix sum + map |
| "Would this work with `10⁹` items?" | Discuss memory, sorting on disk, a heap or sketch |
| "How would you test it?" | Normal case, empty, one element, duplicates, extremes, invalid input |

**When you get a hint:** thank them, repeat it in your own words, and say what it changes ("So the order matters, which suggests sorting").

**When you are stuck:** say it. "I'm stuck on the second half. Let me try a smaller example." Silence is worse than a wrong idea said out loud.

#### 3. Weak Answer vs Strong Answer

| | Weak | Strong |
|---|---|---|
| Start | codes in the first minute | restates, asks about constraints |
| Approach | jumps to one idea | brute force, then a better idea, with Big-O |
| Pattern | "I remember this one" | "Sorted input and a target, so two pointers" |
| Coding | silent, long single function | narrates, small helpers, clear names |
| Testing | "I think it works" | traces an example and an edge case |
| Ending | stops when code compiles | states complexity and one improvement |

#### 4. Kotlin Code

**Write code that is easy to test.** Small pure functions, no hidden state, and a few quick checks at the bottom.

```kotlin
// Valid Anagram (LeetCode 242)
fun isAnagram(s: String, t: String): Boolean {
    if (s.length != t.length) return false             // quick exit: different lengths
    val count = IntArray(26)
    for (i in s.indices) {
        count[s[i] - 'a']++
        count[t[i] - 'a']--
    }
    return count.all { it == 0 }
}

fun main() {
    check(isAnagram("anagram", "nagaram"))             // normal
    check(!isAnagram("rat", "car"))                    // same length, different letters
    check(isAnagram("", ""))                           // empty
    check(!isAnagram("a", "ab"))                       // different length
}
```

Run the checks mentally before you say "done": `isAnagram("anagram","nagaram")` → `true`, `isAnagram("rat","car")` → `false`, `isAnagram("","")` → `true`, `isAnagram("a","ab")` → `false`.

**Naming and style**

- Say what a variable means: `left`, `right`, `farthest`, `seen`, not `a`, `b`, `x`.
- Extract a helper when one idea needs a name (`isPalindrome(l, r)`, `inBounds(r, c)`).
- Keep one idea per line. Avoid clever one-liners you can't explain.
- Handle the edge case at the top (`if (nums.isEmpty()) return ...`).

#### 5. Complexity

How to state it in one breath:

| Say | Meaning |
|---|---|
| "Time `O(n log n)` because of the sort, then one `O(n)` pass." | add costs, keep the largest |
| "Time `O(n)`: each element enters and leaves the window once." | amortized loop-in-loop |
| "Space `O(n)` for the map, `O(h)` for recursion." | list every structure |
| "Output space is not counted." | when you build the answer list |

Always give **both** time and space, and say which input variable each depends on.

#### 6. Common Mistakes (Traps)

1. **Coding too early.** You may solve the wrong problem.
2. **Going silent** for minutes.
3. **Ignoring edge cases** (empty, one item, duplicates, negatives).
4. **Arguing with a hint** or ignoring it.
5. **Over-engineering.** Solve the stated problem first.
6. **Not testing**, or testing only the example from the statement.
7. **Giving up the brute force** when you can't find the optimal. A correct brute force beats a broken optimal one.
8. **Memorised answers.** If the interviewer changes one rule, you can't adapt.
9. **Leaving complexity unsaid.**
10. **Rushing the last five minutes.** Leave time to test.

#### 7. Say This in the Interview

1. "Let me restate the problem to be sure I've understood it."
2. "A simple solution is ..., which takes `O(...)`. Let me see if we can do better."
3. "Because the array is sorted and I need a pair, I'll use two pointers."
4. "Here's my plan ... Does that sound right before I code?"
5. "I'll trace `[...]` through the code."
6. "Time is ..., space is ... The trade-off is ..."
7. "If I had more time, I would ..."

#### 8. Quick Check

1. You can't find the optimal solution with 10 minutes left. What do you do?
2. What do you say after the code is written?

<details>
<summary>Answers</summary>

1. Code the correct brute force, test it, say its complexity, then explain how you'd improve it. A working answer plus a clear direction scores far better than an unfinished one.
2. "Let me trace an example and an edge case," then give the time and space complexity.

</details>

#### 9. Related LeetCode Questions

Rehearse these **out loud**, following the 8 steps, with a timer:

| # | Question | Rehearse |
|---|---|---|
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) | the whole routine on a small problem |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) (Easy) | brute force to hash map |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) | naming the pattern |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) | explaining the sort |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) | edge cases on a grid |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) | explaining state and transition |
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) | design trade-offs |
