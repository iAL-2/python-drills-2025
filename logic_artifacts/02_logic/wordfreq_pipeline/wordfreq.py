# --- VERSION 1: Counter-based pipeline -------------------

import re
from collections import Counter
import csv

def tokenize(text):
    return re.findall(r"\w+", text.lower())

def wordfreq_pipeline(filepath, export_csv=None):
    counter = Counter()
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            counter.update(tokenize(line))
    if export_csv:
        with open(export_csv, "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(["word", "count"])
            writer.writerows(counter.items())
    return counter


# --- VERSION 2: Manual dictionary pipeline ---------------
import re
import csv

def readfile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def counts(token):
    count = {}
    for w in token:
        count[w] = count.get(w, 0) + 1
    return count

def top_items(counts,n):
    pairs_sorted = sorted(counts.items(), key=lambda item:item[1], reverse = True)
    return pairs_sorted[:n]

def csvWriter(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    inpath = "sample.txt"
    outpath = "topword.csv"
    n = 20

    text = readfile(inpath)
    token = tokenize(text)
    count = counts(token)

    rows = top_items(count)
    csvWriter(rows, outpath)

    print(f"Printed top {n} words to {outpath}")

