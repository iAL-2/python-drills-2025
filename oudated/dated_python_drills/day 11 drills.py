def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Enter a valid number. ")
        return None
    
def squared(x):
    return x*x

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

while True:
    print("\nMenu:")
    print("1. Square a number")
    print("2. Factorial of a number")
    print("3. Exit program")

    choice = get_int("Enter a number from 1-3: ")

    if choice == None : continue

    elif choice == 1:
        n = get_int("Enter a number to square: ")
        if n is not None:
            print(f"{n} squared is {n*n}.")
    elif choice == 2:
        n = get_int("Enter a number to get the factorial of it: ")
        if n is not None:
            print(f"Factorial of {n} is {factorial(n)}.")


    elif choice == 3:
        print("Exiting")
        break

    else:
        print("Invalid option, please choose 1-3.")


#retyped and understood each part from day 8 csv writer
import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#take out the + to transform into counting letters instead of words

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]
#to change the way it is sorted, change the key or remove the reverse

def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top20.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    count = _count(token)

    assert sum(count.values) == len(token)

    top_rows = _top_items(count, top_n)
    _write_csv(top_rows, out_path)
    
    print(f"Top {top_n} words written to {out_path}.")

def smoke_tests():
    assert _tokenize("Hello! Hello, Hello!!!") == ["hello", "hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("y",3), ("z",2)]        # Sort

smoke_tests()


#transformed word count, ascending order, with flag to choose between text file or multistring
import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#take out the + to transform into counting letters instead of words

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv:kv[1])
    return pairs_sorted[:n]
#to change the way it is sorted, change the key or remove the reverse

def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top20.csv"
    top_n = 20


    USE_FILE = True
    text = _readfile(in_path) if USE_FILE else """your multiline string..."""
    token = _tokenize(text)
    count = _count(token)

    assert sum(count.values()) == len(token)

    top_rows = _top_items(count, top_n)
    _write_csv(top_rows, out_path)
    
    print(f"Top {top_n} words written to {out_path}.")

def smoke_tests():
    assert _tokenize("Hello! Hello, Hello!!!") == ["hello", "hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("x",1), ("z",2)]        # Sort

smoke_tests()

main()

#modified version with letters, dictionary seeds all 26

import re
import csv
import string

def _read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
#now you have a bigasss string, next tokenize it and normalize it

def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]", text)

#a list of all letters has been created, all normalized as lowercase

def _counts(tokens):
    count = {letter: 0 for letter in string.ascii_lowercase}
    for w in tokens:
        count[w] = count.get(w, 0) + 1
    return count

def _top_items(count):
    pairs_sorted = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
    return pairs_sorted

def _write_csv(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["letter", "count"])
        for letter, count in rows:
            writer.writerow([letter,count])

def main():

    stringinput = False
    inpath = "sample.txt" if not stringinput else "insert hardcode string here"
    outpath = "letters_sorted.csv"

    text = _read_text(inpath)
    token = _tokenize(text)
    count = _counts(token)

    assert sum(count.values()) == len(token)

    sortedlist = _top_items(count)
    _write_csv(sortedlist, outpath)

    print(f"List of number of times letters occured printed to {outpath}")

main()

def smoke_tests():
    assert _tokenize("Asshole") == ["a","s","s","h","o","l","e"]
    counts = _counts(["a","s","s","h","o","l","e"])
    assert counts["a"] == 1
    assert sum(counts.values()) == len("asshole")

smoke_tests()


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