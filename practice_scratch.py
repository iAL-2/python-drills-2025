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
    items = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    if top_n is not None:
        items = items[:top_n]

    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerow(items)

    