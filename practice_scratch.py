import re
import csv

def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def counts(token):
    count = {}
    for w in token:
        count[w] = count.get(w, 0) + 1
    return count

def top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def csvWriter(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    inpath = "sample.txt"
    outpath = "topwords.csv"
    n = 20

    with open(inpath, "r", encoding="utf-8") as f:
        token = []
        for line in f:
            token.extend(tokenize(line))
    
    count = counts(token)
    rows = top_items(count, n)
    csvWriter(rows, outpath)

    