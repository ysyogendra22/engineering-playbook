# Changelog

All notable changes to this repository. Dates are `YYYY-MM-DD`.

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
