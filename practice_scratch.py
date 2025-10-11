def word_count(text):
    freq = {}
    for word in text.lower().split():
#iterates and generates the words separated, and lowercased. `.split()` creates a list
        word = ''.join(ch for ch in word if ch.isalpha())
# ''.join and "".join functionally the same. 
# ch for ch in word unpacks a list. uses a generator expression to iterate through each part of the previous list
        if not word:
            continue
#if an iteration returns blank, that means it was all special characters so word will be blank, so continue catches those cases
        freq[word] = freq.get(word, 0) + 1
#the .get(key, default) pattern, with +1 to increment the value
    return freq

#retyped and understood each part from day 8 csv writer
import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)
#take out the + to transform into counting letters instead of words

def _count(tokens):
    counts = {}
    for w in tokens:
        counts[w] = counts.get(w,0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]
#to change the way it is sorted, change the key or remove the reverse

def _write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top20.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    count = _count(token)

    assert sum(count.values) == len(token)

    top_rows = _top_items(count, top_n)
    _write_csv(top_rows, out_path)
    
    print(f"Top {top_n} words written to {out_path}.")

def smoke_tests():
    assert _tokenize("Hello! Hello, Hello!!!") == ["hello", "hello", "hello"]
    assert _count(["a","b","a"]) == {"a": 2, "b": 1}                       # Count
    assert _top_items({"x":1,"y":3,"z":2}, 2) == [("y",3), ("z",2)]        # Sort

smoke_tests()