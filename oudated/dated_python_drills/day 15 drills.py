import re
import csv

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _counts(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda items:items[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word","count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.csv"
    top_n = 10

    text = _readfile(in_path)
    tokens = _tokenize(text)
    counts = _counts(tokens)

    assert sum(counts.values()) == len(tokens)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, out_path)

    print(f"Wrote top {top_n} words to {out_path}")

main()


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nums = list(range(1,21))


def buildlist():
    numbers = []
    for i in range(40,60):
        numbers.append(i)
    return numbers

nums2 = buildlist()
#2 variants of list of 20 numbers



slice1 = nums[:5] #first 5
slice2 = nums[5:] #last 15
slice2a = nums[-5:] #last 5
slice3 = nums[::3] #every third

# slices of first list in different forms

def squaredic(seq):
    squared = {}
    for n in seq:
        squared[n] = squared.get(n, n*n)
    return squared

def filterevens(dic):
    for i in dic:
        if i.value() % 2 == 0:
            continue
        else:
            del dic[i]
    return dic

import json

def writingjson(obj, path="jsontest.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def readjson(path="jsontest.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

nums = list(range(1, 21))

def build_list():
    numbers = []
    for i in range(40, 60):  # 20 numbers: 40..59
        numbers.append(i)
    return numbers

nums2 = build_list()  # second variant of 20 numbers

# slices
slice1 = nums[:5]     # first 5
slice2 = nums[-5:]    # last 5
slice3 = nums[::3]    # every 3rd

def square_dict(seq):
    out = {}
    for n in seq:
        out[n] = n * n
    return out

def filter_evens(d):
    # keep only even keys
    return {k: v for k, v in d.items() if k % 2 == 0}

import json

def write_json(obj, path="jsontest.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def read_json(path="jsontest.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# pipeline demo
sq = square_dict(nums)
even_sq = filter_evens(sq)
write_json(even_sq, "even_squares.json")
loaded = read_json("even_squares.json")

# quick checks
assert slice1 == [1, 2, 3, 4, 5]
assert slice2 == [16, 17, 18, 19, 20]
assert slice3 == [1, 4, 7, 10, 13, 16, 19]
assert loaded["2"] == 4 or loaded[2] == 4  # json keys become strings

import json


def write_json(obj, path = "jsontest.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def read_json(path = "jsontest.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    
def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def write_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f) 
    
import re
import csv

def _readfile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _counts(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items, key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.txt"
    top_n = 20

    text = _readfile(in_path)
    tokens = _tokenize(text)
    counts = _counts(tokens)

    assert sum(counts.values()) == len(tokens)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, out_path)

    print(f"Top {top_n} words printed to {out_path}")

main()
