# Drill: Word → Line Numbers Index

## Description
Map each unique word in a text file to the line numbers where it appears.  
Example output: `{"the": [1, 3, 5], "data": [2, 7]}`

## Concepts Practiced
- Using `enumerate()` to pair each line of a file with its line number  
- Multi-value mappings with `defaultdict(set)` or `setdefault()`  
- Tokenizing text line by line with `re.findall(r"\w+")`  
- Handling duplicates using a `set()` for unique line numbers  
- File iteration with `.readlines()` vs `.read()` for line-based processing

## Key Idioms
- `for lineno, line in enumerate(lines, start=1):`  
  Creates `(line_number, line_text)` pairs automatically  
- `index[word].add(lineno)`  
  Adds a line number to the existing set for that word  
- `re.findall(r"\w+", line.lower())`  
  Extracts lowercase alphanumeric words from each line

## Notes
- `enumerate()` yields tuples `(index, element)` — the counter always comes **first**.  
- `.read()` returns one large string; `.readlines()` or iterating directly over the file yields individual lines suitable for enumeration.  
- `set()` removes duplicate line numbers automatically; `list()` can be used instead if duplicates or order are needed.  
- This drill extends the accumulator pattern from counting to **indexing**, forming a foundational idea behind search and retrieval systems.
