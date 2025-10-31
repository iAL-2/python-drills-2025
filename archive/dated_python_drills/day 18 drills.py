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
        counts[w] = counts.get(w, 0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    inpath = "sample.txt"
    outpath = "top_words.csv"
    top_n = 20

    text = _readfile(inpath)
    token = _tokenize(text)
    counts = _counts(token)

    assert sum(counts.values()) == len(token)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, outpath)
    print(f"Wrote top {top_n} words to {outpath}")



def quadhex(n):
    for i in range(1, n+1):
        x = ""
        if i % 4 == 0:
            x += "Quad"
        if i % 6 == 0:
            x += "Hex"
        print(x) if x else print(i)

quadhex(50)


def quadhex(n):
    for i in range(1, n+1):
        x = ""
        if i % 4 == 0:
            x += "Quad"
        if i % 6 == 0:
            x += "Hex"
        print(x) if x else print(i)

def quadhex(n):
    for i in range(1, n+1):
        x = ""
        if i % 4 == 0:
            x += "Quad"
        if i % 6 == 0:
            x += "Hex"
        print(x) if x else print(i)

def safedivide(a,b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "Undefined"
        else:
            return a / b
    except(ValueError,TypeError):
        return "invalid input"
    
def safedivide(a,b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "Undefined"
        else: 
            return a/b
    except(ValueError,TypeError):
        return "Non numeric input"
    
def safedivide(a,b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "Undefined"
        else:
            return a/b
    except(ValueError, TypeError):
        return "Non-numeric input"
    
def safedivide(a,b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "undefined"
        else: return a/b
    except(ValueError,TypeError):
        return "non-numeric input"
    
def safedivide(a,b):
    try:
        a = float(a)
        b = float(b)
        if b ==0: return "undefined"
        else: return a/b
    except(ValueError,TypeError) : return "non-numeric input"

