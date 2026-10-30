# Huffman Coding — Name & Idea

> Rarely asked as "write Huffman coding". Often asked in disguise (*Minimum Cost to Connect Sticks*). Know the idea and the heap loop.

#### 1. What Is It?

**Huffman coding** compresses data by giving **short bit codes to frequent characters** and **long codes to rare ones**. It is the best possible prefix code (no code is the start of another code).

```text
character:  f   c   d   e   a   b
frequency:  45  12  13  16  5   9
code:       0   100 101 111 1100 1101
```

The greedy idea: **always merge the two smallest frequencies.**

#### 2. How It Works

1. Put all frequencies in a **min-heap**.
2. Remove the two smallest, merge them into a new node (sum of the two), and push it back.
3. Repeat until one node is left. That is the root of the code tree.
4. Left edge = `0`, right edge = `1`. A character's code is the path to it.

```text
heap: 5 9 12 13 16 45
5 + 9   = 14   heap: 12 13 14 16 45
12 + 13 = 25   heap: 14 16 25 45
14 + 16 = 30   heap: 25 30 45
25 + 30 = 55   heap: 45 55
45 + 55 = 100  heap: 100

total cost of merges = 14 + 25 + 30 + 55 + 100 = 224 = total bits needed
```

Why it works: the rarest characters go deepest in the tree (longest codes), the most frequent stay near the root (shortest codes).

**The interview version** is *Minimum Cost to Connect Sticks* (LeetCode 1167): joining two sticks costs their sum. Join all sticks with the least total cost. It is exactly the merge loop above. *Last Stone Weight* (LeetCode 1046) uses the same heap pattern.

#### 3. Brute Force vs Optimized

| | Brute force | Greedy + heap |
|---|---|---|
| Idea | try every order of merges | always merge the two smallest |
| Time | exponential | `O(n log n)` |
| Space | recursion | `O(n)` |

Joining sticks in the **given order** (e.g. left to right) is a tempting wrong answer:

```text
sticks [1, 8, 3, 5]
in order:   1+8 = 9, 9+3 = 12, 12+5 = 17     cost 38
greedy:     1+3 = 4, 4+5 = 9, 9+8 = 17       cost 30
```

#### 4. Kotlin Code

```kotlin
import java.util.PriorityQueue

// Minimum Cost to Connect Sticks (LeetCode 1167): the Huffman merge loop
fun connectSticks(sticks: IntArray): Int {
    val heap = PriorityQueue<Int>()
    for (s in sticks) heap.add(s)
    var cost = 0
    while (heap.size > 1) {
        val merged = heap.poll() + heap.poll()
        cost += merged
        heap.add(merged)
    }
    return cost
}

// Huffman codes
class HNode(val freq: Int, val ch: Char? = null, val left: HNode? = null, val right: HNode? = null)

fun huffmanCodes(freq: Map<Char, Int>): Map<Char, String> {
    val heap = PriorityQueue<HNode>(compareBy<HNode> { it.freq })
    for ((c, f) in freq) heap.add(HNode(f, c))
    if (heap.size == 1) return mapOf(heap.poll().ch!! to "0")      // one distinct character
    while (heap.size > 1) {
        val a = heap.poll()
        val b = heap.poll()
        heap.add(HNode(a.freq + b.freq, null, a, b))
    }
    val codes = HashMap<Char, String>()
    fun walk(node: HNode, path: String) {
        if (node.ch != null) { codes[node.ch] = path; return }
        walk(node.left!!, path + "0")
        walk(node.right!!, path + "1")
    }
    walk(heap.poll(), "")
    return codes
}
```

Checks: `connectSticks([2,4,3])` → `14`. `connectSticks([1,8,3,5])` → `30`. `connectSticks([5])` → `0`. For `huffmanCodes(f=45, c=12, d=13, e=16, a=5, b=9)` the code lengths are `f:1, c:3, d:3, e:3, a:4, b:4`, so the total bits are `45·1 + (12+13+16)·3 + (5+9)·4 = 224`. The exact bit strings can differ when frequencies tie, but the lengths stay optimal.

#### 5. Complexity

| | Time | Space |
|---|---|---|
| Build the tree (`n` characters) | `O(n log n)` | `O(n)` |
| Connect sticks | `O(n log n)` | `O(n)` |

#### 6. Common Mistakes

1. **Merging in the given order** instead of the two smallest.
2. **Using a max-heap.** You need a **min**-heap.
3. **Not pushing the merged node back.**
4. **One distinct character** (a tree with one node needs a code like `"0"`).
5. **Mixing up the merge cost and the tree** (cost is the sum of all merge results).

#### 7. Say This in the Interview

1. "Huffman is greedy: merge the two least frequent nodes until one is left. The rare characters end up deepest."
2. "I use a min-heap, so each step is `O(log n)` and the total is `O(n log n)`."

#### 8. Quick Check

1. Which two nodes does Huffman merge?
2. What is the cost to connect sticks `[2, 4, 3]`?

<details>
<summary>Answers</summary>

1. The two with the smallest frequency.
2. `14` (2+3 = 5, then 5+4 = 9, total 5 + 9).

</details>

#### 9. Related LeetCode Questions

| # | Question | Idea |
|---|---|---|
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Easy) | heap, take the two largest |
| 1167 | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) (Medium, premium) | Huffman merge loop |
| 2208 | [Minimum Operations to Halve Array Sum](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) (Medium) | always halve the largest |
| 1642 | [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) (Medium) | heap of the biggest jumps |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) | heap by frequency (note 13) |
