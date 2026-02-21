import re
import csv

WORD_RE = re.compile(r"[a-z]+")

def tokenize(line, *, min_len=1, stopwords=None):
    if stopwords is None:
        stopwords = set()

    tokens = WORD_RE.findall(line.lower())
    return [
        t for t in tokens
        if len(t) >= min_len and t not in stopwords
    ]


def update_counts(counts, tokens):
    for t in tokens:
        counts[t] = counts.get(t, 0) + 1


def write_csv(counts, outpath, top_n=None):
    # sort by count desc, then word asc (deterministic)
    items = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    if top_n is not None:
        items = items[:top_n]

    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(items)


def main():
    inpath = "sample.txt"
    outpath = "topitems.csv"

    min_len = 3
    stopwords = {"the", "and", "for", "with"}
    top_n = 20

    counts = {}
    total_tokens = 0

    with open(inpath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            tokens = tokenize(
                line,
                min_len=min_len,
                stopwords=stopwords
            )
            total_tokens += len(tokens)
            update_counts(counts, tokens)

    write_csv(counts, outpath, top_n)

    print(f"tokens kept: {total_tokens}")
    print(f"unique words: {len(counts)}")
    print(f"wrote {outpath}")


if __name__ == "__main__":
    main()


## mutation 1

import re
import csv
    
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

    with open(inpath, "r", encoding="utf-8") as f:
        token = []
        for line in f:
            token.extend(tokenize(line))
    count = counts(token)

    rows = top_items(count, n)
    csvWriter(rows, outpath)

    print(f"Printed top {n} words to {outpath}")

#mutation 2
import re
import csv
from paths import DATA_DIR

def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

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
    inpath = DATA_DIR / "sample.txt"
    outpath = DATA_DIR / "topwords.csv"
    n = 20

    count = {}
    with open(inpath, "r", encoding="utf-8") as f:
        for line in f:
            for w in tokenize(line):
                count[w] = count.get(w, 0) + 1

    rows = top_items(count, n)
    csvWriter(rows, outpath)

    print(f"Printed top {n} words to {outpath}")

#mutation 2 line length 
import csv

def top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return pairs_sorted[:n]

def csvWriter(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["length", "lines_with_that_length"])
        for length, freq in rows:
            writer.writerow([length, freq])

def main():
    inpath = "sample.txt"
    outpath = "line_lengths.csv"
    n = 20

    count = {}
    with open(inpath, "r", encoding="utf-8") as f:
        for line in f:
            L = len(line)
            count[L] = count.get(L, 0) + 1

    rows = top_items(count, n)
    csvWriter(rows, outpath)
    print(f"Printed top {n} lengths to {outpath}")

#mutation 2 first letter of words
import re
import csv

def tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return pairs_sorted[:n]

def csvWriter(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["first_letter", "count"])
        for letter, c in rows:
            writer.writerow([letter, c])

def main():
    inpath = "sample.txt"
    outpath = "first_letters.csv"
    n = 20

    count = {}
    with open(inpath, "r", encoding="utf-8") as f:
        for line in f:
            for w in tokenize(line):
                first = w[0]
                count[first] = count.get(first, 0) + 1

    rows = top_items(count, n)
    csvWriter(rows, outpath)
    print(f"Printed top {n} first letters to {outpath}")
