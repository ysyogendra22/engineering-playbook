# Poster generators

Python scripts that draw the one-page cheat-sheet posters with headless Chrome.

```bash
cd scripts/posters
python3 poster_ds.py ../../01-data-structure/data_structure_cheatsheet.png
python3 poster_algorithm.py ../../02-algorithm/algorithm_cheatsheet.png
python3 poster_leetcode.py ../../03-leetcode-patterns/leetcode_patterns_cheatsheet.png
python3 poster_arch.py ../../09-architecture/architecture_cheatsheet.png
python3 poster_database.py ../../10-database/database_cheatsheet.png
```

Needs Google Chrome (set `CHROME=/path/to/chrome` if it is not at the macOS default), Pillow (`pip install pillow`) and internet access for the Google Fonts (Plus Jakarta Sans, JetBrains Mono).

`poster_lib.py` has the layout and styles, `poster_svg.py` the small diagrams. Only these five posters have generators here; the others were generated earlier and their scripts were not saved.
