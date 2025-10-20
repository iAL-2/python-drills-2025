# Drill: Word Frequency Counter (Basic + Advanced)

## Description
Take a string and create a dictionary that maps how many times each word shows up.  
Includes an advanced variation explored earlier.

## Concepts Practiced
- Main logic: the mapping accumulator pattern  
  `freq[word] = freq.get(word, default) + 1`
- Creating an iterable of words using either `.split()` or `re.findall()`
- Normalizing text using `.lower()`

## Key Idioms
- `dict[x]` – dictionary lookup  
- `dict.get(key, default) + 1` – accumulator pattern that assigns a default value if none found  
- `.split()` – splits text on whitespace  
- `.isalpha()` – checks if the string contains only alphabetic characters  
- `''.join()` – rebuilds a string from a sequence of characters  

### Advanced Version
- `import re` and `re.findall(r"[a-z]+", text)` – regex-based tokenization  
- File I/O:  
  `with open(input, "r", encoding="utf-8") as f:` → `.read()`  
- Sorting and slicing:  
  `sorted(counts.items(), key=lambda kv: kv[1], reverse=True)`  
  `[:n]` for top-N results  
- CSV writing:  
  `csv.writer()`, `.writerow()`  
- Other idioms:  
  `len()`, f-strings, `assert`, `dict.values()`

## Notes
### Key similarities
1. Both rely on the same mapping accumulator pattern.  
2. Both iterate through normalized word tokens and count occurrences.

### Key differences
1. The basic version is monolithic; the advanced version is modular, with helper functions.  
2. The basic version defines words using `.split()` and needs manual cleanup.  
3. The advanced version uses `re.findall()`, which defines word boundaries precisely.  
4. The advanced version imports `re` and `csv`, performs file I/O, includes assertions, and functions as a small data-processing pipeline.
5. Advanced version uses `DATA_DIR` import from paths.py to keep folder clean