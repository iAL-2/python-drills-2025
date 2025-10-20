# HTML Quote Scraper — Logic Block

**Goal**  
- Fetch a quotes page and produce a table of (quote, author). Save to CSV.

**Inputs**  
- `url: str` (e.g., "https://quotes.toscrape.com/")  
- `timeout: int` (seconds, default 10)  
- `out_path: Path` for the CSV

**Outputs**  
- CSV file with two columns: `quote, author`  
- (Internally) `list[dict]` rows: `{"quote": str, "author": str}`

**Constraints / Invariants**  
- Network requests must respect timeout.  
- Only rows with both quote and author are emitted.  
- CSV is UTF-8, with header row.  
- Parser assumes page structure compatible with CSS selectors used.

**Rules (IF/THEN)**  
- IF HTTP status != 200 OR request errors → treat as no data.  
- IF a “quote” block is missing text or author → skip that block.  
- IF `rows` length mismatches written lines → fail assertion.

**Flow**  
1. `fetch_html(url, timeout)` → HTML string or `None`.  
2. `parse_quotes(html)` → extract blocks via CSS selectors → build rows.  
3. `write_csv(rows, out_path)` → write header, then each row.  
4. Print summary.

**Edge Cases**  
- Network error / non-200 status → write empty CSV.  
- HTML structure changed → selectors find 0 blocks → empty CSV.  
- Smart quotes / punctuation → strip from text before writing.

**Tests / Checks**  
- Given sample HTML containing two quotes → returns 2 rows (`{"quote":..., "author":...}` each).  
- `fetch_html("http://bad_host")` → returns `None` (graceful handling).  
- After `write_csv(rows)`, `len(rows)` equals number of data lines (assert passes).

**Notes**  
- **Docstring vs `#` comment:** `"""Return html string or None on error."""` is a *docstring*. Put as the first statement inside a function to document it; tools/IDEs surface it. A `#` is just an inline comment for readers.  
- **BeautifulSoup’s role:** turns HTML text into a parse tree (DOM-like) so you can select elements.  
- **CSS selectors:**  
  - `soup.select("div.quote")` ⇒ all `<div class="quote">` blocks.  
  - `block.select_one("span.text")` ⇒ one `<span class="text">` inside that block.  
- **Stripping special quotes:** many sites use “smart quotes” (U+201C/U+201D). `strip("“”")` removes those from the ends so your CSV is clean.  
- **Why `list[dict]` rows:** preserves order and allows duplicate quotes if present; easier to write to CSV. You can convert to dict later if you need keyed access.  
- **`written` counter:** simple integrity check that rows written == rows in memory.
