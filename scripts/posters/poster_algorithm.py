from poster_lib import *
from poster_svg import *

boxes = [
 box(1, "Complexity (Big-O)", "r",
     kv([("`O(1)`", "constant"), ("`O(log n)`", "halving"), ("`O(n)`", "one pass"), ("`O(n log n)`", "sort"), ("`O(n²)`", "nested loops"), ("`O(2ⁿ)`", "subsets"), ("`O(n!)`", "permutations")], True) +
     ul(["Drop constants & lower terms", "Sequential loops **add**, nested **multiply**", "Recursion: calls × work per call", "Space = extra memory + call stack"]) +
     callout("State time AND space. Say where each comes from.", "")),
 box(2, "Sorting", "g",
     table(["Sort", "Time", "Note"], [["Bubble/Select/Insert", "`n²`", "insertion `n` if sorted"], ["Merge", "`n log n`", "stable, `O(n)` space"], ["Quick", "`n log n` avg", "worst `n²`"], ["Heap", "`n log n`", "in place"], ["Counting", "`n + k`", "small int range"], ["Radix", "`d(n + k)`", "digits"]]) +
     mut("Stable = equal items keep their order.")),
 box(3, "Searching", "b",
     pre("""var lo = 0; var hi = n - 1
while (lo <= hi) {
  val mid = lo + (hi - lo) / 2
  if (a[mid] == t) return mid
  if (a[mid] < t) lo = mid + 1
  else hi = mid - 1
}
return -1""") + ul(["Linear `O(n)`, binary `O(log n)`", "Lower / upper bound, first / last", "Binary search **on the answer**", "Quickselect: avg `O(n)`"])),
 box(4, "Recursion & D&C", "p",
     p("Base case → recursive case → combine.") +
     table(["Recurrence", "Result"], [["`T(n)=2T(n/2)+n`", "`n log n` (merge sort)"], ["`T(n)=T(n/2)+1`", "`log n` (binary search)"], ["`T(n)=T(n-1)+1`", "`n`"], ["`T(n)=2T(n-1)+1`", "`2ⁿ`"]]) +
     ul(["Call stack = `O(depth)` space", "Deep recursion → stack overflow", "Convert to loop + explicit stack"])),

 box(5, "Greedy", "r",
     ul(["Sort, then pick the best local choice", "Prove it: **exchange argument**", "Interval scheduling: sort by end time", "Huffman, Jump Game, gas station"]) +
     callout("Greedy fails for coins {1,3,4}, target 6:\ngreedy 4+1+1 = 3 coins, best 3+3 = 2", "") + mut("Counter-example? Use DP.")),
 box(6, "Dynamic Programming", "g",
     h3("Steps", "g") + ul(["Define the **state**", "Write the recurrence", "Base cases & order", "Memoize or tabulate"]) +
     table(None, [["Fibonacci / stairs", "1D"], ["Knapsack 0/1", "2D → 1D"], ["LCS / edit distance", "2D grid"], ["Coin change", "unbounded"]]) + mut("Cost = states × work per state.")),
 box(7, "Backtracking", "b",
     pre("""fun go(path) {
  if (done) { save(path); return }
  for (c in choices) {
    if (!ok(c)) continue   // prune
    path.add(c)            // choose
    go(path)               // explore
    path.removeLast()      // undo
  }
}""") + ul(["Subsets `2ⁿ`, permutations `n!`", "N-Queens, Sudoku, word search"])),
 box(8, "Graph Algorithms", "p",
     table(["Algorithm", "Time"], [["BFS / DFS", "`V + E`"], ["Dijkstra (no negatives)", "`(V+E) log V`"], ["Bellman-Ford", "`V·E`"], ["Floyd-Warshall", "`V³`"], ["Kruskal MST", "`E log E`"], ["Topological sort", "`V + E`"], ["Union-Find", "≈ `O(1)` amortized"]])),

 box(9, "Strings", "r",
     ul(["KMP / Z: `O(n + m)` matching", "Rabin-Karp: rolling hash, avg `O(n + m)`", "Trie: prefix search `O(len)`", "Palindrome: expand center `O(n²)`, Manacher `O(n)`", "Anagram: count array of 26", "Sliding window for substrings"])),
 box(10, "Bit Tricks (Kotlin)", "g",
     kv([("`x and (x - 1)`", "clear lowest set bit"), ("`x and -x`", "isolate lowest set bit"), ("`x xor x`", "= 0 → find single number"), ("`1 shl k`", "bit k mask"), ("`x shr 1`", "divide by 2"), ("`x and 1`", "odd check")], True) +
     callout("Power of two: `x > 0 && (x and (x - 1)) == 0`", "g")),
 box(11, "Math & Numbers", "b",
     ul(["GCD (Euclid): `O(log n)`", "Prime test up to `√n`", "Sieve: `O(n log log n)`", "Fast power: `O(log n)`", "Mod `10⁹ + 7` after every multiply", "Use `Long`: `Int` overflows at ~2.1×10⁹"])),
 box(12, "Complexity Classes", "p",
     ul(["**P**: solvable fast (sort, shortest path)", "**NP**: answer is checked fast", "**NP-complete**: SAT, subset sum, TSP (decision)", "**NP-hard**: at least as hard"]) +
     callout("n ≤ 20 and \"try everything\"?\nSay: exact is exponential;\nuse DP / bitmask / approximation.", "b")),

 box(13, "Which Algorithm?", "o",
     table(["Signal", "Use"], [["Sorted + target", "binary search / two pointers"], ["Min / max over choices", "DP or greedy"], ["All combinations", "backtracking"], ["Shortest path, equal cost", "BFS"], ["Weighted shortest path", "Dijkstra"], ["Dependencies", "topological sort"], ["Groups merging", "Union-Find"]]), 2),
 box(14, "Formulas", "t",
     kv([("1+2+…+n", "`n(n+1)/2`"), ("1²+…+n²", "`n(n+1)(2n+1)/6`"), ("1+2+4+…+2ᵏ", "`2ᵏ⁺¹ − 1`"), ("nCr", "`n! / (r!(n−r)!)`"), ("log(ab)", "`log a + log b`")], True)),
 box(15, "Golden Rules", "r", ul(["Brute force first, then improve", "Name the pattern & why", "Dry-run + edge cases", "Time and space out loud", "Empty, one item, duplicates"], ok=True)),
]
meta = dict(left="Pattern &gt; Memory<br>Think. Then code.", right="Brute force.<br>Optimize. Repeat! ☺", title="<b>ALGORITHMS</b> CHEATSHEET", sub="for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
