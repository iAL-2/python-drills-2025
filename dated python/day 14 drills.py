#practice writing the csv writer
import csv
import re

def count(tokens):
    count = {}
    for w in tokens:
        count[w] = count.get(w, 0) + 1
    return count
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _readfile(text):
    with open(text, "r", encoding="utf-8") as f:
        return f.read()
    
def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def count(token):
    count = {}
    for w in token:
        count[w] = count.get(w, 0) + 1
    return count

def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _count(token):
    count = {}
    for w in token:
        count[w] = count.get(w, 0) + 1
    return count

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word,count])

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()

def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _count(token):
    count = {}
    for w in token:
        count[w] = count.get(w, 0) + 1
    return count

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda kv:kv[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word","count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.txt"
    top_n = 20

    text = _readfile(in_path)
    tokens = _tokenize(text)
    count = _count(tokens)

    assert sum(count.values()) == len(tokens)

    top_rows = _top_items(count, top_n)
    _csv_writer(top_rows, out_path)

    print(f"Top {top_n} words written out to {out_path}")

main()


#practice writing the csv writer
import csv
import re

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _counts(tokens):
    count = {}
    for w in tokens:
        count[w] = count.get(w,0) + 1
    return count

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda items:items[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.csv"
    top_n = 20

    text = _readfile(in_path)
    token = _tokenize(text)
    counts = _counts(token)

    assert sum(counts.values()) == len(token)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, out_path)

    print(f"Printed top {top_n} words to {out_path}.")

main()

def fizzbuzz(n):
    t = []
    for i in range(1,n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Boom"
        if result:
            t.append(result)
        else:
            t.append(i)
    return t

assert fizzbuzz(30)[1] == 2
result = (fizzbuzz(40))

assert result[0] == 1
assert result[1] == 2
assert result[2] == "Fizz"
assert result[4] == "Buzz"
assert result[6] == "Boom"
assert result[14] == "FizzBuzz"

import re
import csv

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _counts(tokens):
    count = {}
    for w in tokens:
        count[w] = count.get(w,0) + 1
    return count

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key = lambda items:items[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word,count in rows:
            writer.writerow([word, count])

def main():
    in_path = "sample.txt"
    out_path = "top_words.csv"
    top_n = 20

    text = _readfile(in_path)
    tokens = _tokenize(text)
    counts = _counts(tokens)

    assert sum(counts.values()) == len(tokens)

    rows = _top_items(counts, top_n)
    _csv_writer(rows, out_path)

    print(f"Printed top {top_n} words to {out_path}")

main()

def _smoke_tests():
    assert _tokenize("Hi, hi!, hi") == ["hi", "hi", "hi"]
    assert _counts(["hi", "hi", "hi"]) == {"hi":3}


_smoke_tests()

def fizzbuzz(n):
    a = []
    for i in range(1, n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Boom"
        
        if result:
            a.append(result)
        else:
            a.append(i)
    return a

test = fizzbuzz(32)

assert test[4] == "Buzz"

def fizzbuzz(n):
    a = []
    for i in range(1, n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Boom"
        
        if result:
            a.append(result)
        else:
            a.append(i)
    return a

def fizzbuzz(n):
    a = []
    for i in range(1, n+1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if i % 7 == 0:
            result += "Boom"
        if result:
            a.append(result)
        else:
            a.append(i)
    return a

for i in fizzbuzz(30):
    print(i)

nums = [0,1,2,3,4,5,6,7,8,9]

print(nums[::-1])
print(nums[::2])
print(nums[:5])
print(nums[2:7])
print(nums[5:])

import re
import csv

def _readfile(in_path):
    with open(in_path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _counts(tokens):
    count = {}
    for w in tokens:
        count[w] = count.get(w,0) + 1
    return count

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key=lambda items:items[1], reverse=True)
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
    top_n = 20

    text = _readfile(in_path)
    tokens = _tokenize(text)
    counts = _counts(tokens)

    assert sum(counts.values()) == len(tokens)

    rows = _top_items(counts, top_n)
    _csv_writer(rows,out_path)

    print(f"Printed top {top_n} words to {out_path}")