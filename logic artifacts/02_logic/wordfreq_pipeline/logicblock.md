# Word Frequency Pipeline — Logic Block

**Goal**  
- Process a text file and output a frequency table of words (case-insensitive, cleaned of punctuation).

**Inputs**  
- Path to a `.txt` file.  
- Optional: output file path (CSV or JSON).

**Outputs**  
- Dictionary `{word: count}`.  
- Optional CSV or JSON export file.

**Constraints / Invariants**  
- Treat all words as lowercase.  
- Ignore punctuation and digits.  
- Must handle large files line-by-line (streaming-safe).  
- Maintain deterministic output order if using an ordered dict or sorted export.

**Rules (IF/THEN)**  
- IF file is empty → return `{}`.  
- IF file cannot be opened → raise `FileNotFoundError` or handle gracefully.  
- IF encoding error → open with `errors='ignore'`.  
- ELSE read line by line, normalize text, tokenize, and count.  

**Flow**  
1. **Extraction:** open the input file safely using `with open(path, encoding='utf-8', errors='ignore')`.  
2. **Tokenization:** extract words using regex `re.findall(r"[a-z]+", text.lower())`.  
3. **Counting:**  
   - Option 1: use `collections.Counter` for concise counting.  
   - Option 2: use manual accumulator pattern (`dict.get(word, 0) + 1`).  
4. **Serialization:** return dictionary, print summary, or export to CSV/JSON.  

**Edge Cases**  
- Empty file → `{}`.  
- Non-UTF-8 text → ignore problematic characters.  
- Very large file → process line-by-line to avoid memory overflow.  
- File with only numbers/punctuation → `{}` after tokenization.  

**Tests / Checks**  
| Input | Expected Output |
|-------|-----------------|
| `"hello world hello"` | `{"hello": 2, "world": 1}` |
| `"Data, DATA, data!"` | `{"data": 3}` |
| `""` | `{}` |

**Variations**  
1. Counter() version, requires importing from collections
2. Manual accumulator pattern function

**Notes**  
- There are two implementations: one using `Counter` and one manual accumulator.  
- Both use alpha-only tokenization (`[a-z]+`) to satisfy the “ignore punctuation and digits” constraint.  
- Designed to be streaming-safe for large input files.  
