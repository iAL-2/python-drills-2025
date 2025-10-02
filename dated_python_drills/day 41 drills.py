import re
import csv

def readFile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def counts(token):
    counts = {}
    for w in token:
        counts[w] = counts.get(w, 0) + 1
    return counts

def topItems(counts, n):
    pairs_sorted = sorted(counts.items(), key = lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def writeCsv(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    inpath = "sample.txt"
    outpath = "top_words.csv"
    n = 20

    text = readFile(inpath)
    token = tokenize(text)
    count = counts(token)

    assert sum(count.values()) == len(token)

    rows = topItems(count, n)
    writeCsv(rows, outpath)

#fizzbuzz that returns list for asserts
def fizzBuzzBazz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0: result.append("Fizz")
        if i % 5 == 0: result.append("Buzz")
        if i % 7 == 0: result.append("Bazz")
        else: result.append(i)
    return result

#deduper that keeps first occurence order

def deduper(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
