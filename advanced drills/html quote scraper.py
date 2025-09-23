#html quote scraper
import csv
import requests
from bs4 import BeautifulSoup

def fetch_html(url, timeout=10):
    """Return html string or None on error.""" #what is this? if this is a note why doesnt it use #
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code !=200:
            print(f"HTTP {r.status_code} for {url}")
            return None
        return r.text
    except Exception as e:
        print(f"Request failed: {e}")
        return None
#this function tries to get the string from a URL. im guessing status code 200 means its working, anything else will fail
#covers both a status code violation and if an Exception is raised
#so it uses a request toolbox. im guessing .get is part of that toolbox
    
def parse_quotes(html):
        """Return list of {'quote':str, 'author':str}."""
        soup = BeautifulSoup(html, "html.parser")
        rows = []
        for block in soup.select("div.quote"):
             text_el = block.select_one("span.text")
             auth_el = block.select_one("small.author")
             if not (text_el and auth_el):
                  continue
             quote = text_el.get_text(strip=True).strip("“”")
             author = auth_el.get_text(strip=True)
             if quote and author:
                  rows.append({"quote": quote, "author": author})
        return rows
#dont quite understand the role of the beautiful soup here. right now, you have a big text dump, a long string right?
#so you make a list to print. same as the word frequency program, it needs to be tuples
#how does it separate those using .select and .select_one()?
#why does it need to strip the special quotations that i cant even type
#this is what i think the goal is: strip the quote and the author of that quote, using some method
#get a list of them as a dictionary? why not just dictionary and turn into list later like in the word frequency program
#the variable assignments and the if checks, essentially it needs to pass some checks to be registered as a quote and author dictionary


def write_csv(rows, out_path):
     with open(out_path, "w", newline="", encoding="utf-8") as f:
          w = csv.writer(f)
          w.writerow(["quote", "author"])
          written = 0
          for r in rows:
               w.writerow([r["quote"], r["author"]])
               written += 1
     assert written == len(rows)
#the format here for this write_csv is similar to the one for the word frequency so i can kind of read it. instead of writer you put w
#not sure what the point of written is. is it just for an assert check?

def main():
     url = "https://quotes.toscrape.com/"
     outcsv = "quotes.csv"
     html = fetch_html(url)
     if not html:
          write_csv([], outcsv)
          print("No data written.")
          return
     rows = parse_quotes(html)
     write_csv(rows, outcsv)
     print(f"Wrote {len(rows)} rows to {outcsv}")
#main loop. put in the url and output path. if html doesnt pass it will catch it and print a message
#then process it with parse_quotes, assign it to rows so it can pass it to write_csv as an argument
#print the result

main()