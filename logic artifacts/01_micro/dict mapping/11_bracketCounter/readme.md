# Drill: Log Counter

## Description
Count how many times bracketed text such as `[INFO]` or `[ERROR]` appears in a given string or file.

## Concepts Practiced
- The main difference from the word and letter frequency counters is the use of `re.findall()` for token extraction.  
- Practiced using escape characters `\[`, `\]`, and the capture group `(\w+)` to extract text inside brackets.  
- Used `from collections import Counter` to simplify accumulation — `Counter()` functions like the accumulator pattern for building a dictionary of `{key: count}` pairs.

## Notes
- Regex pattern `r"\[(\w+)\]"` captures only the text between brackets.  
- `Counter()` automatically initializes and increments counts, making it a clean alternative to `dict.get()` or `defaultdict(int)`.  
- `.upper()` normalization ensures consistent casing for log levels (e.g., `INFO`, `ERROR`, `WARN`).
