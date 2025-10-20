# CSV Writer — Logic Block

**Goal**  
- Write a small dataset to a CSV file with proper headers and UTF-8 encoding.

**Inputs**  
- A list of records (tuples or dictionaries).  
- Output path: `DATA_DIR / "test.csv"`.

**Outputs**  
- CSV file containing `name, age` columns with one row per record.

**Constraints / Invariants**  
- File must be UTF-8 encoded.  
- Always include header row.  
- Ensure newline handling (`newline=""`) to avoid blank lines on Windows.  
- Deterministic field order: `["name", "age"]`.

**Rules (IF/THEN)**  
- IF using tuple data → use `csv.writer`.  
- IF using dict data → use `csv.DictWriter`.  
- IF output file already exists → overwrite (no append).  
- ELSE (any I/O error) → allow exception to propagate.

**Flow**  
1. Define dataset (`list[tuple]` or `list[dict]`).  
2. Open target file with UTF-8 encoding and `newline=""`.  
3. Create writer (`csv.writer` or `csv.DictWriter`).  
4. Write header row.  
5. Iterate over records and write each line.  
6. Close file automatically via `with` context.

**Edge Cases**  
- Empty dataset → file with only header.  
- Nonexistent `DATA_DIR` → must exist or raise `FileNotFoundError`.  
- Extra fields in dict → ignored unless specified in `fieldnames`.  

**Tests / Checks**  
- Dataset of 3 rows → file with 4 lines (including header).  
- Empty list → file with only header.  
- Verify UTF-8 output opens correctly in text editor.

**Notes**  
- Demonstrates core pattern for writing structured data safely.  
- `csv.writer` is fastest for simple tuples; `csv.DictWriter` is clearer for key-based records.  
- The `newline=""` parameter avoids extra blank lines across platforms.  
