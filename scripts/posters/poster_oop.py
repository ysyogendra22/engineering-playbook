from poster_lib import *
from poster_svg import *

stack_heap = """<svg viewBox="0 0 330 116" width="300"><g fill="#fff" stroke-width="2"><rect x="6" y="8" width="62" height="26" rx="6" stroke="#27479b"/><rect x="6" y="45" width="62" height="26" rx="6" stroke="#27479b"/><rect x="6" y="82" width="62" height="26" rx="6" stroke="#27479b"/><rect x="190" y="26" width="130" height="28" rx="6" stroke="#17703a"/><rect x="190" y="80" width="130" height="28" rx="6" stroke="#b3261e"/></g>
<g stroke="#444" stroke-width="2" fill="none"><path d="M68 21 L190 36"/><path d="M68 58 L190 46"/><path d="M68 95 L190 94"/></g>
<g font-size="14" text-anchor="middle"><text x="37" y="26">p1</text><text x="37" y="63">alias</text><text x="37" y="100">p2</text><text x="255" y="45">Person(Asha)</text><text x="255" y="99">Person(Ravi)</text></g>
<text x="255" y="19" font-size="12" fill="#b3261e" text-anchor="middle">p1 + alias: one object</text></svg>"""

boxes = [
 box(1, "Classes & Objects", "r", stack_heap + ul(["Class = blueprint · object = instance on the **heap**", "Variable holds a **reference**: `b = a` shares", "Fields default `0` `false` `null`; locals don't", "Static parts once, then **parent → child**"])),
 box(2, "Encapsulation", "g", ul(["**Private** state + methods that enforce rules", "Method named for the action: `withdraw`", "No getter/setter by habit", "Return a **copy** or read-only view", "Start `private`; Kotlin `private set`"]) + callout("Tell, don't ask.", "g")),
 box(3, "Inheritance & Polymorphism", "b", table(["", "Override", "Overload"], [["Chosen", "**runtime**", "**compile time**"], ["By", "real object", "declared types"], ["Same", "signature", "name only"]]) + ul(["Is-a only · 1 parent class", "`@Override` always", "Fields are not polymorphic", "No overridable call in a constructor"])),
 box(4, "Abstract Class vs Interface", "p", table(["", "Abstract class", "Interface"], [["State", "yes", "constants"], ["Ctor", "yes", "no"], ["Parents", "one", "many"], ["Means", "is-a, shared", "can-do"]]) + ul(["**Start with an interface**", "Clashing `default`: `X.super.m()`", "Functional = 1 abstract method"])),

 box(5, "Composition vs Inheritance", "r", ul(["has-a beats is-a", "Subclass sees the parent's **insides**", "Wrap library classes, don't extend", "Swap parts at runtime (strategy)", "Kotlin `by` delegates"]) + callout("CountingSet extends HashSet\naddAll(3 items) → added = 6", "")),
 box(6, "equals · hashCode · toString", "g", kv([("equal", "⇒ same `hashCode`"), ("same hash", "⇏ equal"), ("rule", "override **both**")]) + pre("""hashCode = Objects.hash(x, y)
// Objects.hash(1, 2) = 994
record Pt(int x, int y) {}
data class Pt(val x: Int, val y: Int)""") + mut("Mutable key → lost in a HashSet.")),
 box(7, "== vs equals", "b", pre("""a == b      // same object?
a.equals(b) // same content?
"java" == "java"            true
new String("java")=="java"  false
Integer 127  == 127         true
Integer 1000 == 1000        false""") + ul(["Kotlin: `==` equals · `===` identity", "Doubles: `abs(a - b) < 1e-9`"])),
 box(8, "Pass-by-Value", "p", ul(["Java **always** copies the argument", "Objects: a copy of the **reference**"]) + pre("""arr[0] = 99;        // seen
n = 99;             // not seen
sb.append("!");     // seen
arr = new int[]{7}; // not seen""") + callout("`swap(a, b)` is impossible", "")),

 box(9, "Immutability", "r", flow(["final", "no setters", "copy in/out"]) + ul(["`final` fixes the **reference**, not the object", "`String` is immutable", "Immutable map keys", "Value object: `Money(cents, cur)`", "View follows changes; copy does not"])),
 box(10, "static · final · enum · nested", "g", ul(["`static` = per class; no `this`", "`final`: assign once · no override · no extend", "**Enum** for fixed sets; never store `ordinal()`", "Inner class holds the outer → Android leak", "Kotlin: `companion object`, `const val`, `object`"])),
 box(11, "Exceptions", "b", flow(["try", "catch", "finally"], ["#27479b", "#b3261e", "#17703a"]) + ul(["Checked = must handle · unchecked = bug", "Never swallow; keep the **cause**", "`finally`: cleanup, never `return`", "try-with-resources / `use {}`: reverse order", "Kotlin: no checked exceptions"])),
 box(12, "Generics", "p", ul(["Compile-time safety; **erased** at runtime", "No `new T()` · no `instanceof List<String>`", "`List<String>` ≠ `List<Object>`", "Never raw types"]) + table(["PECS", "Use"], [["read", "`? extends T`"], ["write", "`? super T`"]]) + mut("Kotlin: `out` producer · `in` consumer")),

 box(13, "Java vs Kotlin", "o", table(["Idea", "Java", "Kotlin"], [["Inherit", "open", "`final` by default"], ["Content equal", "`equals`", "`==`"], ["Identity", "`==`", "`===`"], ["Static", "`static`", "`companion object`"], ["Singleton", "enum / holder", "`object`"], ["Value class", "`record`", "`data class`"], ["Checked exc.", "yes", "no"], ["Null safety", "annotations", "in the type `T?`"]]), 2),
 box(0, "Golden Rules", "t", ul(["Interface first", "Composition over inheritance", "`equals` + `hashCode` together", "Immutable by default", "`equals` for objects", "Never swallow exceptions", "Wrap, don't extend, library classes", "Copy mutable data in and out", "Enum, not magic strings"], ok=True)),
 box(0, "Say Out Loud", "r", '<div class="big">"Private state, small<br>interfaces, composition,<br>equals + hashCode,<br>pass-by-value."</div>'),

 box(0, "Traps Cheat Table (all outputs run on JDK 21)", "o", row(
     table(["Code", "Result"], [["`HashSet.contains` (equals only)", "`false`"], ["`0.1 + 0.2 == 0.3`", "`false`"], ["`Objects.hash(1, 2)`", "`994`"], ["`Integer.valueOf(1).equals(1L)`", "`false`"]]),
     table(["Code", "Result"], [["`dg.meet(an)` (overload)", "`animal meets animal`"], ["`new Derived()` (ctor trap)", "`label=null`"], ["`try {return 1} finally {return 2}`", "`2`"], ["`CountingSet.addAll(3)`", "`added = 6`"]]),
     table(["Code", "Result"], [["`final List` + `add`", "allowed"], ["`Plan.valueOf(\"GOLD\")`", "`IllegalArgumentException`"], ["try-with-resources A, B", "close B, then A"], ["`List<String>` as `List<Object>`", "compile error"]])), 4),
]
meta = dict(left="Objects, not magic<br>Know the traps.", right="Explain. Run it.<br>Pass! ☺", title="<b>OOP &amp; JAVA</b> CHEATSHEET", sub="for <u>FAANG interviews</u> · 2026")
if __name__ == "__main__":
    import sys; print(render(page(meta, boxes), sys.argv[1]))
