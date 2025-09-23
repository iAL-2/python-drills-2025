import math
import re

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Must be an integer")
    if n <0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("Too large")
    
    if n < 2:
        raise False
    if n == 2:
        raise True
    if n % 2 == 0:
        raise False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int)->bool:
    if not isinstance(n, int):
        raise TypeError("Must be an integer")
    if n < 0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("TOoo large")
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit +1, 2):
        if n % i == 0:
            return False
    return True

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)

def originalword(token):
    return "".join(token)

def reversedword(token):
    r = ""
    for w in token:
        r = w + r
    return r

def is_palindrome(text:str)->bool:
    token = normalize(text)
    original = originalword(token)
    r = reversedword(token)
    return r == original

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

import re
import csv

def _readfile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def _counts(token):
    counts = {}
    for w in token:
        counts = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    counts = _counts(token)

    assert sum(counts.values) == len(token)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, top_n)

    print(f"Wrote top {top_n} words to {out_path}")

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def is_palindrome(text:str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def quadhex(n):
    for i in range(1, n+1):
        word = ""
        if i % 4 == 0:
            word += "Quad"
        if i % 6 == 0:
            word += "Hex"
        print(word) if word else print(i)

quadhex(50)

import re
import csv

def _readfile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def _counts(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w, 0) +1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda items:items[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word","count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    counts = _counts(token)

    assert sum(counts.values()) == len(token)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, out_path)

    print(f"Wrote top {top_n} words to {out_path}")

main()

def csvmini():
    ash = [("Alice", 25), ("Bob", 30), ("Carol", 22)]
    with open("test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for name, age in ash:
            writer.writerow([name,age])

csvmini()

def lislicing():
    x = []
    for i in range(1, 21):
        x.append(i)
    print(x[1::2])
    print(x[::-1])
    print(x[2::3])

lislicing()

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "undefined"
        else:
            return a / b
    except (ValueError, TypeError):
        return "non-numeric"
    
print(safe_divide(6, 3))       # 2.0
print(safe_divide("7.5", 2))   # 3.75
print(safe_divide(5, 0))       # "undefined"
print(safe_divide("x", 2))     # "non-numeric"
