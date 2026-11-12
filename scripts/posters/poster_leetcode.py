from poster_lib import *
from poster_svg import *

boxes = [
 box(1, "Constraints → Big-O", "r", table(["n up to", "Aim for"], [["20", "`2ⁿ`, `n!` backtracking / bitmask"], ["500", "`n³`"], ["5,000", "`n²` nested loops, 2D DP"], ["100,000", "`n log n` / `n`"], ["1,000,000", "`n` one pass"], ["`10⁹`+", "`log n` or a formula"]])),
 box(2, "Two Pointers", "g", boxes_row(["1", "3", "4", "6", "9"], "#17703a", ["L", "", "", "", "R"]) + ul(["Sorted + pair / triplet", "Palindrome, in-place remove", "Move the pointer that helps"]) + mut("167 · 15 · 11 · 125")),
 box(3, "Sliding Window", "b", pre("""var l = 0
for (r in s.indices) {
  add(s[r])
  while (invalid()) {
    remove(s[l]); l++
  }
  best = maxOf(best, r - l + 1)
}""") + mut("Contiguous + condition · 3 · 76 · 424")),
 box(4, "Fast & Slow", "p", ul(["Cycle in a list (Floyd)", "Middle of a list", "Duplicate in `1..n`"]) + pre("""var s = head; var f = head
while (f?.next != null) {
  s = s?.next
  f = f.next?.next
  if (s === f) return true
}
return false""") + mut("141 · 142 · 876 · 287")),

 box(5, "Prefix Sum + Map", "r", pre("""var sum = 0; var cnt = 0
val seen = hashMapOf(0 to 1)
for (x in a) {
  sum += x
  cnt += seen[sum - k] ?: 0
  seen[sum] = (seen[sum] ?: 0) + 1
}""") + ul(["Range sum = `P[r] − P[l−1]`", "Works with negatives (window doesn't)"]) + mut("560 · 525 · 238")),
 box(6, "Binary Search", "g", pre("""var lo = 0; var hi = n   // answer space
while (lo < hi) {
  val mid = lo + (hi - lo) / 2
  if (ok(mid)) hi = mid else lo = mid + 1
}
return lo   // first true""") + ul(["Sorted, rotated, or yes/no flips once", "\"Minimum X such that…\""]) + mut("704 · 33 · 875 · 1011")),
 box(7, "Intervals & Stack", "b", ul(["Sort by start, merge if `s ≤ prevEnd`", "Meeting rooms: heap of end times", "Monotonic stack: next greater / histogram"]) + callout("[1,3] [2,6] [8,10]\n→ [1,6] [8,10]", "b") + mut("56 · 57 · 253 · 739 · 84")),
 box(8, "Heap / Top K", "p", ul(["K largest → **min-heap** of size K", "K smallest → max-heap of size K", "Cost `O(n log k)`", "Merge K lists, running median (two heaps)"]) + mut("215 · 347 · 23 · 295")),

 box(9, "BFS", "r", pre("""val q = ArrayDeque(listOf(s))
val seen = hashSetOf(s)
var d = 0
while (q.isNotEmpty()) {
  repeat(q.size) {
    val u = q.removeFirst()
    for (v in adj[u])
      if (seen.add(v)) q.add(v)
  }
  d++   // one level done
}""") + mut("Shortest path, equal cost · 102 · 127 · 994")),
 box(10, "DFS & Trees", "g", tree(("8", "3", "10", "1", "6", "9", "14"), "#17703a") + ul(["Return values up, pass state down", "Inorder BST = sorted", "Height, diameter, LCA, path sum"]) + mut("104 · 236 · 98 · 124")),
 box(11, "Backtracking", "b", ul(["All subsets / perms / combinations", "choose → explore → un-choose", "Prune early; skip duplicates by sorting", "`n ≤ 20` hint"]) + mut("78 · 46 · 39 · 51 · 79")),
 box(12, "Graph, Topo, Union-Find", "p", ul(["Islands / components → DFS or BFS", "Prerequisites → topological sort (Kahn)", "\"Connected?\" → Union-Find", "Cycle → visiting / visited states"]) + mut("200 · 207 · 210 · 133 · 684")),

 box(13, "Dynamic Programming", "r", h3("5 steps", "r") + ul(["State  ·  Recurrence", "Base  ·  Order  ·  Answer", "Memo → table → rolling array"]) + kv([("70 / 198", "1D: stairs, rob"), ("322 / 300", "coin, LIS"), ("1143 / 72", "2D: LCS, edit")], True)),
 box(14, "Greedy", "g", ul(["Local best is safe? Try a counter-example", "Sort + scan", "Jump Game, intervals, gas station"]) + mut("55 · 45 · 435 · 134 · 763")),
 box(15, "Other Tools", "b", ul(["Hash map / set: seen, count, group", "Trie: prefix search (208)", "Cyclic sort / XOR: missing, single (136)", "Bit mask: subsets state", "Pointer rewiring: reverse list (206)"])),
 box(16, "Interview Flow", "o", kv([("1", "restate + ask"), ("2", "brute force + Big-O"), ("3", "name the pattern"), ("4", "plan, get a nod"), ("5", "code, narrate"), ("6", "dry-run + edges"), ("7", "time + space"), ("8", "follow-ups")], True)),

 box(0, "Signal → Pattern", "o", table(["If you see…", "Try"], [["sorted array, pair with a target", "two pointers"], ["longest / shortest contiguous …", "sliding window"], ["cycle, middle of a list", "fast & slow"], ["subarray sum equals K", "prefix sum + map"], ["minimum X such that …", "binary search on the answer"], ["K best / next greater", "heap / monotonic stack"], ["all arrangements", "backtracking"], ["count ways / min cost", "DP"], ["prerequisites, order", "topological sort"]]), 2),
 box(0, "Golden Rules", "t", ul(["Pattern first, code second", "Brute force + Big-O first", "Constraints pick the Big-O", "Test: normal, empty, one, duplicates", "A working brute force beats a broken optimal"], ok=True)),
 box(0, "Say Out Loud", "r", '<div class="big">"Sorted + pair<br>→ two pointers.<br>O(n) time, O(1) space."</div>'),
]
meta = dict(left="Patterns &gt; Problems<br>Signal → Template", right="Solve. Review.<br>Repeat! ☺", title="<b>LEETCODE PATTERNS</b> CHEATSHEET", sub="for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
