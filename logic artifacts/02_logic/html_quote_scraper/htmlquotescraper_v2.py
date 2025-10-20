from paths import DATA_DIR
import csv
import requests
from bs4 import BeautifulSoup

def fetch_html(url, timeout=10):
    """Return HTML string or None on error."""
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code != 200:
            return None
        return r.text
    except Exception:
        return None

def parse_quotes(html):
    """Return list of {'quote': str, 'author': str}."""
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for block in soup.select("div.quote"):
        text_el = block.select_one("span.text")
        auth_el = block.select_one("small.author")
        if not (text_el and auth_el):
            continue
        quote = text_el.get_text(strip=True).strip("“”\"'")
        author = auth_el.get_text(strip=True)
        if quote and author:
            rows.append({"quote": quote, "author": author})
    return rows

def write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["quote", "author"])
        written = 0
        for r in rows:
            w.writerow([r["quote"], r["author"]])
            written += 1
    assert written == len(rows)

def main():
    url = "https://quotes.toscrape.com/"
    outcsv = DATA_DIR / "quotes.csv"
    html = fetch_html(url)
    if not html:
        write_csv([], outcsv)
        print("No data written.")
        return
    rows = parse_quotes(html)
    write_csv(rows, outcsv)
    print(f"Wrote {len(rows)} rows to {outcsv}")

if __name__ == "__main__":
    main()
