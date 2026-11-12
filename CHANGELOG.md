# Changelog

All notable changes to this repository. Dates are `YYYY-MM-DD`.

## [Unreleased]

### Added
- **`09-architecture` topics 23–25** (code-level foundations): `23-OOP-and-Java-Basics`, `24-SOLID-in-Code`, `25-Design-Patterns-in-Code`. Java and Kotlin, with a worked bad → better example for each idea, 8 diagrams, LeetCode design problems, and class-design (LLD) interview steps. Java versions of the examples were compiled and run on JDK 21; the Kotlin versions were not compiled.
- Section 9 (OOP and class design) in `Mock-Interview-Bank.md`.
- **`11-oop-and-java-basics`** (new folder): `00-Content`, 13 topic notes (classes and objects, encapsulation, inheritance and polymorphism, abstract class vs interface, composition vs inheritance, `equals`/`hashCode`/`toString`, `==` vs `equals` with the string pool and Integer cache, pass-by-value, immutability, `static`/`final`/nested/enums, exceptions, generics, Java vs Kotlin), `99-OOP-and-Java-Cheat-Sheet` and `oop_cheatsheet.png`. Each note has the nine-section layout, Java and Kotlin code, 1–3 diagrams and LeetCode design problems. Java examples were compiled and run on JDK 21; the Kotlin versions were not compiled.
- `01-data-structure/data_structure_cheatsheet.png`: a complete, Kotlin-based DSA poster with 18 numbered boxes: Big-O for ten structures, sorting with stability and space, a deeper Graphs box (shortest-path variants, cycle and bipartite checks, MST, SCC), Trie, Union-Find, Recursion and Backtracking, Greedy and Intervals, an 18-row signal → pattern table with LeetCode IDs, bit tricks, formulas, edge cases and Kotlin tools. The original `data_structure.jpeg` is kept as is.
- `scripts/posters/`: the renderer and generators for the `01`, `02`, `03`, `09`, `10` and `11` posters.

### Changed
- New logo: a liquid-glass "EP" mark (one fused glyph: a P-bowl on an E-base) on a warm sunset colour mesh, with "playbook" in solid magenta. `assets/logo-mark.svg`, `logo-mark.png`, `logo.png`, `logo-dark.png` and `social-preview.png` are regenerated from `scripts/logo/make_logo.py`. The social card also lists the new `11-oop-and-java-basics` folder.
- `09-architecture`: the roadmap (`00-Content.md`), cheat sheet and poster now include topics 23–25; notes 04 and 06 link to the new code-level notes.
- `09-architecture/24-SOLID-in-Code`: expanded from 5 to 15 worked examples (signup, notifiers, payments, bird, stronger precondition, Worker/Robot, listeners, ViewModel, `Clock`, and a step-by-step checkout refactor), plus a smell → principle table, sealed vs interface guidance, a "which principle?" exercise, and 2 more diagrams. Java versions of the new examples were run on JDK 21.

### Fixed
- `02-algorithm` poster: the power-of-two check was written C-style (`x & (x-1) == 0`, which has a precedence bug and is not Kotlin). It is now `(x and (x - 1)) == 0`.
- Posters with code (`02`, `03`, `10`): the code font no longer turns `===`, `!=` and `=>` into "≡", "≠" and "⇒".

## [1.0.0] - 2026-11-05

The full rewrite for FAANG-style interview preparation, in simple beginner-friendly English with Kotlin code.

### Added
- **Notes in one nine-section layout** for `03-leetcode-patterns` (22), `04-backend-engineering` (12), `05-system-design` (21), `06-mobile-engineering` (22), `07-behavioral-leadership` (21), `08-artificial-intelligence` (22), `09-architecture` (22) and `10-database` (23): what it is and how to spot it, how it works with a diagram, naive vs better, code with checked outputs, complexity or numbers, mistakes and edge cases, what to say, quick check, practice with LeetCode links.
- **A `99-*-Cheat-Sheet.md` for every folder**, and a one-page **poster image** of each (`*_cheatsheet.png`).
- **Per-folder indexes** (`00-Content.md`) with marks, a "short on time" list, a study path and a glossary.
- **`10-database`**: a new folder on data modeling, SQL, indexes, internals, transactions, NoSQL, scaling, backups, security and mobile databases.
- **README** with a start-here plan, a short-on-time path, status, and cheat-sheet table.
- **`Mock-Interview-Bank.md`**: timed practice prompts across all folders.
- **Logo and social preview** in `assets/`, a `LICENSE` (MIT) and a `.gitignore`.
- **`scripts/validate_notes.py`** and a GitHub Action that runs it on every push.

### Changed
- `02-algorithm` and `01-data-structure` keep their earlier per-topic layout.

### Notes
- SQL examples were run on SQLite; numbers were checked in Python. Kotlin, Room, PostgreSQL-only, Redis and cloud snippets are marked "not run" or "check current".
