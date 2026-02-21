import csv
from paths import DATA_DIR

def top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def csvWriter(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["length", "count"])
        for length, count in rows:
            writer.writerow([length, count])

def main():
    inpath = DATA_DIR / "sample.txt"
    outpath = DATA_DIR / "linelengthcount.csv"
    n = 20

    count = {}
    with open(inpath, "r", encoding="utf-8") as f:
        for line in f:
            length = len(line)
            count[length] = count.get(length, 0) + 1

    rows = top_items(count, n)
    csvWriter(rows, outpath)
    print(f"Printed top {n} lengths to {outpath}")

if __name__ == "__main__":
    main()