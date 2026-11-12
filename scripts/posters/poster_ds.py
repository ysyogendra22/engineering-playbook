from poster_lib import *
from poster_svg import *

stack = """<svg viewBox="0 0 220 124" width="190"><g fill="#fff" stroke="#27479b" stroke-width="2"><rect x="80" y="12" width="64" height="30" rx="5"/><rect x="80" y="44" width="64" height="30" rx="5"/><rect x="80" y="76" width="64" height="30" rx="5"/></g>
<g font-size="15" text-anchor="middle"><text x="112" y="33">3</text><text x="112" y="65">2</text><text x="112" y="97">1</text></g>
<path d="M170 60 V20" stroke="#b3261e" stroke-width="2"/><path d="M164 28 L170 18 L176 28" fill="none" stroke="#b3261e" stroke-width="2"/>
<text x="150" y="12" font-size="13" fill="#b3261e">top</text><text x="4" y="64" font-size="12">push ↓ pop ↑</text></svg>"""

queue = """<svg viewBox="0 0 300 72" width="290"><g fill="#fff" stroke="#17703a" stroke-width="2"><rect x="70" y="10" width="46" height="30" rx="5"/><rect x="118" y="10" width="46" height="30" rx="5"/><rect x="166" y="10" width="46" height="30" rx="5"/></g>
<g font-size="15" text-anchor="middle"><text x="93" y="31">1</text><text x="141" y="31">2</text><text x="189" y="31">3</text></g>
<g font-size="12.5" text-anchor="middle" fill="#b3261e"><text x="93" y="58">FRONT</text><text x="189" y="58">REAR</text></g>
<g font-size="12" ><text x="2" y="30">dequeue ←</text><text x="222" y="30">← enqueue</text></g></svg>"""

chain = """<svg viewBox="0 0 330 74" width="290"><g fill="#fff" stroke="#27479b" stroke-width="2">
<circle cx="30" cy="30" r="14"/><circle cx="95" cy="30" r="14"/><circle cx="160" cy="30" r="14"/><circle cx="225" cy="30" r="14"/><circle cx="290" cy="30" r="14"/></g>
<g stroke="#444" stroke-width="1.8" fill="none"><path d="M44 30 H81 M109 30 H146 M174 30 H211 M239 30 H276"/><path d="M290 44 C290 70 160 70 160 46" stroke="#b3261e" stroke-dasharray="4 3"/></g>
<g font-size="14" text-anchor="middle"><text x="30" y="35">1</text><text x="95" y="35">2</text><text x="160" y="35">3</text><text x="225" y="35">4</text><text x="290" y="35">5</text></g>
<text x="165" y="72" font-size="11.5" text-anchor="middle" fill="#b3261e">cycle: 5 → 3</text></svg>"""

graph = """<svg viewBox="0 0 280 120" width="230"><g stroke="#666" stroke-width="1.8"><path d="M40 60 L120 24 M40 60 L120 96 M120 24 L120 96 M120 24 L220 24 M120 96 L220 96 M220 24 L220 96"/></g>
<g fill="#fff" stroke="#6a2c91" stroke-width="2"><circle cx="40" cy="60" r="15"/><circle cx="120" cy="24" r="15"/><circle cx="120" cy="96" r="15"/><circle cx="220" cy="24" r="15"/><circle cx="220" cy="96" r="15"/></g>
<g font-size="14" text-anchor="middle"><text x="40" y="65">1</text><text x="120" y="29">2</text><text x="120" y="101">3</text><text x="220" y="29">4</text><text x="220" y="101">5</text></g></svg>"""

hashsvg = """<svg viewBox="0 0 330 124" width="290"><g fill="#fff" stroke-width="2"><rect x="4" y="46" width="64" height="30" rx="6" stroke="#444"/><circle cx="118" cy="61" r="24" stroke="#b3261e"/></g>
<g stroke="#444" stroke-width="1.8" fill="none"><path d="M68 61 H94 M142 61 H196"/></g>
<g fill="#fff" stroke="#27479b" stroke-width="2"><rect x="200" y="4" width="120" height="22"/><rect x="200" y="28" width="120" height="22"/><rect x="200" y="52" width="120" height="22" fill="#eaf0ff"/><rect x="200" y="76" width="120" height="22"/><rect x="200" y="100" width="120" height="22"/></g>
<g font-size="13" text-anchor="middle"><text x="36" y="66">"cat"</text><text x="118" y="56" font-size="11">hash</text><text x="118" y="70" font-size="11">% size</text></g>
<g font-size="12.5"><text x="206" y="20">0</text><text x="206" y="44">1</text><text x="206" y="68">2: cat → 7</text><text x="206" y="92">3</text><text x="206" y="116">4</text></g></svg>"""


trie = """<svg viewBox="0 0 300 176" width="250"><g stroke="#666" stroke-width="1.8"><path d="M150 30 V60 M150 80 V108 M138 126 L118 146 M162 126 L182 146"/></g>
<g fill="#fff" stroke="#6a2c91" stroke-width="2"><circle cx="150" cy="18" r="13"/><circle cx="150" cy="68" r="13"/><circle cx="150" cy="116" r="13"/><circle cx="112" cy="156" r="13"/><circle cx="188" cy="156" r="13"/></g>
<circle cx="112" cy="156" r="9" fill="none" stroke="#b3261e" stroke-width="1.6"/><circle cx="188" cy="156" r="9" fill="none" stroke="#b3261e" stroke-width="1.6"/>
<g font-size="13" text-anchor="middle"><text x="150" y="22" font-size="10">root</text><text x="150" y="73">c</text><text x="150" y="121">a</text><text x="112" y="161">t</text><text x="188" y="161">r</text></g>
<text x="228" y="160" font-size="12" fill="#b3261e">= word ends</text></svg>"""

boxes = [
 box(1, "Complexity (Big-O)", "r",
     table(["Big-O", "Name", "n = 1,000"], [["`O(1)`", "constant", "1"], ["`O(log n)`", "logarithmic", "≈ 10"], ["`O(√n)`", "square root", "≈ 32"], ["`O(n)`", "linear", "1,000"], ["`O(n log n)`", "linearithmic", "≈ 10,000"], ["`O(n²)`", "quadratic", "1,000,000"], ["`O(n³)`", "cubic", "10⁹"], ["`O(2ⁿ)`", "exponential", "≈ 10³⁰¹"], ["`O(n!)`", "factorial", "even bigger"]]) +
     ul(["Drop constants and lower terms", "Sequential loops **add**, nested **multiply**", "Best / average / worst case: say which", "**Amortized**: dynamic array append is `O(1)`", "Space = extra memory + call stack", "Recursion depth `d` → `O(d)` space"]) + callout("n ≤ 20 → `2ⁿ` · n ≤ 500 → `n³`\nn ≤ 5,000 → `n²` · n ≤ 10⁵ → `n log n`\nn ≤ 10⁶ → `n`", "")),
 box(2, "Data Structures: Big-O", "g",
     table(["Structure", "Access", "Search", "Insert", "Delete"], [
         ["Array (fixed)", "`1`", "`n`", "`n`", "`n`"],
         ["Dynamic array (`ArrayList`)", "`1`", "`n`", "end `1`*, middle `n`", "`n`"],
         ["Sorted array", "`1`", "`log n`", "`n`", "`n`"],
         ["Singly / doubly linked list", "`n`", "`n`", "`1` at head or known node", "`1` known node"],
         ["Stack / Queue / Deque", "ends only", "`n`", "`1` at an end", "`1` at an end"],
         ["Hash table / HashSet", "-", "`1` avg", "`1` avg", "`1` avg"],
         ["Balanced BST (`TreeMap`)", "-", "`log n`", "`log n`", "`log n`"],
         ["Heap (`PriorityQueue`)", "peek `1`", "`n`", "`log n`", "`log n`"],
         ["Trie (word length `L`)", "-", "`L`", "`L`", "`L`"],
         ["Union-Find", "-", "find ≈ `1`", "union ≈ `1`", "-"]]) +
     mut("* append is amortized O(1). Hash worst case O(n). An unbalanced BST degrades to O(n). Union-Find: ≈ O(α(n)) with path compression + union by size.") +
     row(ul(["**Linear:** Array, Linked List, Stack, Queue, Deque, String"]), ul(["**Non-linear:** Tree, BST, Heap, Trie, Graph, Hash Table"])), 2),
 box(3, "Sorting & Searching", "b",
     table(["Sort", "Time", "Note"], [["Bubble / Selection / Insertion", "`n²`", "insertion: `n` if nearly sorted"], ["Merge", "`n log n`", "stable, `O(n)` space"], ["Quick", "`n log n` avg", "worst `n²`, in place"], ["Heap", "`n log n`", "in place, not stable"], ["Counting", "`n + k`", "small integer range"], ["Radix", "`d(n + k)`", "d = digits"], ["Bucket", "`n + k` avg", "uniform data"], ["TimSort (JVM objects)", "`n log n`", "stable, best `n`"]]) +
     ul(["Comparison sorts cannot beat `n log n`", "JVM: primitives → dual-pivot quicksort, objects → TimSort", "Linear search `O(n)` · binary search `O(log n)`, sorted data only", "Binary search **on the answer**: monotonic yes/no", "Lower / upper bound, first / last occurrence", "Quickselect: k-th element, avg `O(n)`"])),

 box(4, "Array / String", "p",
     ul(["Access `1` · append `1` amortized · insert / delete middle `n`", "Prefix sum: range sum `P[r] − P[l−1]`", "Difference array: many range updates in `O(1)` each", "Two pointers · sliding window", "In-place reverse; rotate = reverse 3 times", "Dutch flag: sort 0/1/2 in one pass", "Kadane: max subarray sum", "String: use `StringBuilder` in loops (`+=` is `O(n²)`)", "Anagram: count array of 26 · palindrome: two pointers"]) +
     pre("""fun maxSubArray(a: IntArray): Int {
  var best = a[0]; var cur = a[0]
  for (i in 1 until a.size) {
    cur = maxOf(a[i], cur + a[i])
    best = maxOf(best, cur)
  }
  return best
}""")),
 box(5, "Linked List", "r", chain +
     ul(["Traverse · insert · delete · reverse · merge two sorted", "Dummy head removes head special cases", "Middle: fast / slow pointers", "Remove n-th from end: gap of n between pointers", "Cycle start: after meeting, restart one pointer at head", "Palindrome list: middle + reverse second half", "LRU cache = hash map + doubly linked list"]) +
     pre("""// Floyd: cycle detection
var slow = head; var fast = head
while (fast?.next != null) {
  slow = slow?.next
  fast = fast.next?.next
  if (slow === fast) return true
}
return false""") +
     pre("""// reverse a list
var prev: ListNode? = null; var cur = head
while (cur != null) {
  val next = cur.next
  cur.next = prev
  prev = cur; cur = next
}
return prev""")),
 box(6, "Stack & Queue", "g", stack + queue +
     ul(["Stack **LIFO**: push, pop, peek", "Queue **FIFO**: enqueue, dequeue, front", "Deque: add / remove at both ends, all `O(1)`", "Valid parentheses · undo · DFS (explicit stack)", "Monotonic stack: next greater, histogram, temperatures", "Monotonic deque: sliding window maximum", "Queue: BFS, level order, task scheduling", "Queue from two stacks; min stack stores running min", "Use `ArrayDeque`, not legacy `java.util.Stack`"]) +
     pre("""val s = ArrayDeque<Int>()
s.addLast(1); s.removeLast()
val q = ArrayDeque<Int>()
q.addLast(1); q.removeFirst()""")),
 box(7, "Trees", "b", tree(("8", "3", "10", "1", "6", "9", "14"), "#27479b") +
     ul(["Inorder LNR (BST → sorted) · Preorder NLR · Postorder LRN", "Level order = BFS with a queue; all traversals `O(n)`", "Space `O(h)`: `log n` balanced, `n` skewed", "BST search / insert / delete `O(h)`", "Self-balancing: AVL, red-black (`TreeMap`)", "Full · complete · perfect (`2ʰ⁺¹ − 1` nodes)", "Height · diameter · LCA · valid BST · path sum", "Range queries: segment tree / Fenwick tree `O(log n)`"]) +
     pre("""fun maxDepth(n: TreeNode?): Int {
  if (n == null) return 0
  return 1 + maxOf(maxDepth(n.left),
                   maxDepth(n.right))
}""")),

 box(8, "Graphs", "p", graph +
     ul(["Directed · undirected · weighted · DAG; degree; components",
         "Adjacency list: space `V + E` (default) · matrix `V²` · edge list",
         "Grid = graph: 4 or 8 neighbours; multi-source BFS",
         "BFS / DFS: `O(V + E)`; BFS = shortest path when edges have equal cost",
         "0-1 BFS: deque, edge weights 0 or 1, `O(V + E)`",
         "Dijkstra: `O((V+E) log V)`, no negative edges",
         "Bellman-Ford: `O(VE)`, negatives OK, detects negative cycles",
         "Floyd-Warshall: all pairs, `O(V³)`",
         "Topological sort (Kahn / DFS): `O(V + E)`, DAG only",
         "Cycle: undirected → parent check or Union-Find; directed → 3 colours or Kahn",
         "Bipartite: 2-colour with BFS · Components: DFS or Union-Find",
         "MST: Kruskal `O(E log E)` (+ Union-Find) · Prim `O(E log V)`",
         "Strongly connected components: Tarjan / Kosaraju `O(V + E)`"]) +
     pre("""val adj = Array(n) { mutableListOf<Int>() }
adj[u].add(v); adj[v].add(u)   // undirected""")),
 box(9, "Heap (Priority Queue)", "r", tree(("1", "3", "2", "7", "6", "5", "4"), "#b3261e") +
     ul(["Min-heap: parent ≤ child · max-heap: parent ≥ child", "Complete tree stored in an array: children `2i+1`, `2i+2`, parent `(i−1)/2`", "insert (sift up) / extract (sift down): `O(log n)` · peek: `O(1)`", "Build from array (heapify): `O(n)` · heap sort: `O(n log n)`", "Top K: min-heap of size K → `O(n log k)`", "Running median: max-heap + min-heap", "Merge K sorted lists: `O(N log k)`", "Dijkstra, Prim, task scheduling, meeting rooms", "`remove(x)` on `PriorityQueue` is `O(n)`"]) +
     pre("""val minHeap = PriorityQueue<Int>()
val maxHeap = PriorityQueue<Int>(
  compareByDescending { it })
val pq = PriorityQueue<Pair<Int, Int>>(
  compareBy { it.first })""")),
 box(10, "Hash Table (Map / Set)", "g", hashsvg +
     ul(["key → value; avg `O(1)` insert / get / delete; worst `O(n)` (JVM treeifies long buckets)", "`HashSet`: membership, dedupe, seen-before", "Collision: chaining or open addressing (probing)", "Load factor (JVM default 0.75) → resize and rehash", "Keys need consistent `hashCode()` and `equals()`", "`LinkedHashMap`: insertion order, LRU · `TreeMap`: sorted, `O(log n)`", "Patterns: frequency count, Two Sum, group anagrams, prefix-sum map, cache"]) +
     pre("""val count = HashMap<Int, Int>()
count[x] = (count[x] ?: 0) + 1
val freq = list.groupingBy { it }.eachCount()""")),
 box(11, "Dynamic Programming", "b",
     h3("Steps", "b") + ul(["1. Define the **state**: what does `dp[i]` mean?", "2. Write the recurrence (transition)", "3. Base cases and fill order", "4. Memoize (top-down) or tabulate (bottom-up)", "5. Shrink space with a rolling array"]) +
     pre("""val memo = HashMap<Int, Long>()
fun fib(n: Int): Long =
  if (n < 2) n.toLong()
  else memo.getOrPut(n) { fib(n-1) + fib(n-2) }""") +
     table(["Type", "Classics"], [["1D", "climbing stairs, house robber, coin change, LIS, word break"], ["2D / grid", "unique paths, min path sum, LCS, edit distance"], ["Knapsack", "0/1 knapsack, subset sum, partition equal subset"], ["Intervals / strings", "longest palindromic substring, matrix chain"]]) +
     mut("Cost = states × work per state. Overlapping subproblems + optimal substructure.")),

 box(12, "Trie (Prefix Tree)", "p", trie +
     ul(["insert / search / startsWith: `O(L)`, L = word length", "Space: up to `total chars × alphabet`", "Autocomplete, prefix count, spell check, Word Search II", "Mark word end with a flag or count"]) +
     pre("""class Node {
  val next = HashMap<Char, Node>()
  var end = false
}
fun insert(root: Node, w: String) {
  var cur = root
  for (c in w)
    cur = cur.next.getOrPut(c) { Node() }
  cur.end = true
}""")),
 box(13, "Union-Find (DSU)", "r",
     ul(["Tracks which items are in the same group", "`find` with path compression; `union` by size", "≈ `O(α(n))` per operation, practically `O(1)`", "Connected components, redundant connection, Kruskal, accounts merge, cycle in undirected graph"]) +
     pre("""val parent = IntArray(n) { it }
fun find(x: Int): Int {
  if (parent[x] != x)
    parent[x] = find(parent[x])
  return parent[x]
}
fun union(a: Int, b: Int) {
  parent[find(a)] = find(b)
}""") + mut("Add a size array and attach the smaller tree to get the `O(α(n))` bound.")),
 box(14, "Recursion & Backtracking", "g",
     ul(["Base case → recursive case → combine", "Call stack = `O(depth)` space; very deep recursion overflows", "Memoize repeated subproblems → DP", "`tailrec` in Kotlin for tail calls", "Backtracking: choose → explore → un-choose, prune early", "Subsets `2ⁿ` · permutations `n!` · N-Queens, Sudoku, word search", "Skip duplicates: sort first, skip equal neighbours"]) +
     pre("""fun go(path: MutableList<Int>) {
  if (done(path)) { save(path); return }
  for (c in choices(path)) {
    path.add(c)       // choose
    go(path)          // explore
    path.removeLast() // undo
  }
}""")),
 box(15, "Greedy & Intervals", "o",
     ul(["Greedy: best local choice, prove it with an **exchange argument**", "Interval scheduling: sort by **end** time", "Merge intervals: sort by start, merge if `start ≤ prevEnd`", "Meeting rooms: min-heap of end times", "Jump Game, gas station, task scheduler", "Coin change: greedy only for canonical coin sets, else DP"]) +
     pre("""val s = iv.sortedBy { it[0] }
val out = mutableListOf(s[0])
for (cur in s.drop(1)) {
  val last = out.last()
  if (cur[0] <= last[1])
    last[1] = maxOf(last[1], cur[1])
  else out.add(cur)
}""")),

 box(16, "Common Patterns: Signal → Pattern", "o",
     table(["If you see…", "Try", "Example"], [
         ["sorted data, pair or target", "two pointers · binary search", "167 · 704"],
         ["longest / shortest contiguous part", "sliding window", "3 · 76"],
         ["subarray sum equals K", "prefix sum + hash map", "560"],
         ["cycle, middle of a list", "fast and slow pointers", "141 · 876"],
         ["intervals, meetings", "sort + merge · heap", "56 · 253"],
         ["next greater / smaller", "monotonic stack", "739"],
         ["max / min in a sliding window", "monotonic deque", "239"],
         ["K largest / smallest / most frequent", "heap (top K)", "215 · 347"],
         ["median of a stream", "two heaps", "295"],
         ["shortest path, levels, grid", "BFS (Dijkstra if weighted)", "102 · 994"],
         ["connected? merge groups?", "Union-Find", "684"],
         ["dependencies, order", "topological sort", "207"],
         ["prefix search, dictionary", "trie", "208"],
         ["all combinations / arrangements", "backtracking", "78 · 46"],
         ["count ways, min or max cost", "dynamic programming", "70 · 322"],
         ["minimize the maximum / first true", "binary search on the answer", "875"],
         ["single / missing number", "XOR · cyclic sort", "136 · 268"],
         ["cache with eviction", "hash map + linked list", "146"]]) +
     mut("Numbers are LeetCode problem IDs."), 2),
 box(17, "Bit Manipulation", "g",
     kv([("`x and y`", "AND · check a bit"), ("`x or y`", "OR · set a bit"), ("`x xor y`", "XOR · toggle a bit"), ("`x.inv()`", "invert bits"), ("`x shl k`", "× 2ᵏ"), ("`x shr k`", "÷ 2ᵏ (keeps sign)"), ("`x ushr k`", "unsigned shift (zero fill)")], True) +
     ul(["Check bit i: `(x shr i) and 1`", "Set bit i: `x or (1 shl i)`", "Clear bit i: `x and (1 shl i).inv()`", "Lowest set bit: `x and -x`", "Clear lowest set bit: `x and (x - 1)`", "Power of two: `x > 0 && (x and (x - 1)) == 0`", "Count set bits: `x.countOneBits()`", "Low k bits: `x and ((1 shl k) - 1)`", "XOR rules: `a xor a = 0`, `a xor 0 = a` → find the single number", "All subsets of n items: loop `mask` in `0 until (1 shl n)`", "Two's complement: `-x == x.inv() + 1`", "`Int` is 32-bit, `Long` is 64-bit"])),
 box(18, "Formulas", "t",
     kv([("1 + 2 + … + n", "`n(n+1)/2`"), ("1² + … + n²", "`n(n+1)(2n+1)/6`"), ("1 + 2 + 4 + … + 2ᵏ", "`2ᵏ⁺¹ − 1`"), ("arithmetic series", "`n/2 × (first + last)`"), ("nCr", "`n! / (r!(n−r)!)`"), ("pairs from n", "`n(n−1)/2`"), ("subarrays of n", "`n(n+1)/2`"), ("subsets / orders", "`2ⁿ` / `n!`"), ("log(ab) · log(a/b)", "`log a ± log b`"), ("change of base", "`log_b x = ln x / ln b`"), ("perfect tree, height h", "`2ʰ⁺¹ − 1` nodes"), ("balanced tree height", "≈ `log₂ n`"), ("gcd · lcm", "`lcm = a·b / gcd`"), ("modular", "`(a+b) mod m = ((a mod m)+(b mod m)) mod m`")], True)),

 box(0, "Interview Flow", "o", flow(["Restate", "Brute force", "Pattern", "Code", "Test"], w=470) +
     ul(["Ask about input size, duplicates, empty input, negatives", "Say time and space out loud", "Dry-run one normal and one edge case", "Then discuss improvements and trade-offs"]) +
     callout("\"Sorted + pair → two pointers. O(n) time, O(1) space.\"", "g") +
     h3("Edge cases to check", "o") + table(None, [["empty · one item · two items", "all equal · duplicates"], ["negatives · zero", "sorted · reverse sorted"], ["`Int` overflow → use `Long`", "off-by-one at both ends"]]), 2),
 box(0, "Golden Rules", "t", ul(["Understand the problem", "Brute force first, then optimize", "Pick the structure for the operation you repeat most", "Dry run before you say \"done\"", "Test: empty, one item, duplicates", "Practise a little every day"], ok=True)),
 box(0, "Kotlin Tools", "p", ul(["`IntArray(n)` · `Array(n) { IntArray(m) }`", "`mutableListOf` · `HashMap` · `HashSet` · `ArrayDeque`", "`PriorityQueue` · `TreeMap` (sorted)", "`sortedBy { }` · `sortedWith(compareBy(...))`", "`StringBuilder` for building strings", "`maxOf` · `minOf` · `coerceIn`", "`windowed(k)` · `zipWithNext()` · `chunked(k)`", "`list.contains` is `O(n)`, `set.contains` is `O(1)`", "`Int.MAX_VALUE` · use `Long` for sums", "`0 until n` excludes n; `0..n` includes n"])),
]
meta = dict(left="Focus &gt; Motivation<br>Discipline = Freedom", right="Code. Debug. Learn.<br>Repeat! ☺", title="<b>DSA</b> CHEATSHEET", sub="Data Structures &amp; Algorithms · Kotlin · for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
