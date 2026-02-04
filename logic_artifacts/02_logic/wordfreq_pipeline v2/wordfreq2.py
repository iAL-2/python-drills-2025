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
