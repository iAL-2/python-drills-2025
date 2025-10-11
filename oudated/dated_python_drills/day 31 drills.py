#jump in date because i decided to account for the days i missed

def quadhex(n):
    for i in range(1, n+1):
        x = ""
        if i % 4 == 0:
            x += "Quad"
        if i % 6 == 0:
            x += "Hex"
        print(x) if x else print(i)

quadhex(26)

def fizzbuzz(n):
    for i in range(1, n+1):
        x = []
        if i % 3 == 0:
            x.append("Fizz")
        if i % 5 == 0:
            x.append("Buzz")
        if i % 7 == 0:
            x.append("Boom")
        print("".join(x)) if x else print(i)

fizzbuzz(30)

import re
import csv

def _readfile(inpath):
    with open(inpath, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    return re.findall(r"[a-z]+", text.lower())

def _counts(token):
    counts = {}
    for w in token:
        counts[w] = counts.get(w, 0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key=lambda item:item[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in rows:
            writer.writerow([word, count])

def main():
    inpath = "sample.txt"
    outpath = "top_words.csv"
    n = 20

    text = _readfile(inpath)
    token = _tokenize(text)
    counts = _counts(token)

    assert sum(counts.values()) == len(token)

    rows = _top_items(counts, n)
    _csv_writer(rows, outpath)

    print(f"Printed top {n} words to {outpath}")

def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1,101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"Sum of evens is {sum(evens)}")
    print(f"Sum of odds is {sum(odds)}")

def evenOddSplitter():
    evenSum = 0
    oddSum = 0

    for i in range(1, 101):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

import math
#optimized version with square root
def divisorFinder(n: int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    print(sorted(d))

#fixed up initial logic version, this is the indicer version
def wordReverser(text):
    x = re.findall(r"[A-Za-z]+", text)
    for w in range(len(x)):
        x[w] = x[w][::-1]
    print(" ".join(x))

#list comprehension version
def wordReverser(text):
    words = text.split()
    words = [w[::-1] for w in words]
    print(" ".join(words))

#pythonic version
def wordReverser(text):
    print(" ".join([w[::-1] for w in text.split()]))

#uses map(). map(func, iterable) applies func to every element, and is a lazy iterator which saves memory
def wordReverser(text):
    print(" ".join(map(lambda w: w[::-1], text.split())))


#using sets on a string to automatically drop duplicates. order not preserved
def uniqueChars(text):
    print(set(text))

#dictionary method, only print out the keys not the values.
def uniqueChars(text):
    d = {}
    for ch in text:
        d[ch] = True
    print("".join(d.keys()))


#csv writer with dictionaries
import csv
def csvWriter():
    d = [{"name": "Alice", "age":25}, {"name": "Bob", "age":22}, {"name": "Carol", "age":30}]
    with open("test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for dict in d:
            writer.writerow([dict["name"], dict["age"]])
    with open("test.csv", "r", encoding="utf-8") as f:
        return f.read()
    

#another version using csv.dictreader
def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open("test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictReader(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(d)

    with open("test.csv", "r", encoding="utf-8") as f:
        return f.read()
    
#line counter1
def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
    
#line counter2
#inefficient for large files since it parses each line into .readlines()
def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())
    
#fizzbuzz twist
def fizzBuzzBoomPop(n):
    for i in range(1, n+1):
        x = ""
        if i % 3 == 0: x+= "Fizz"
        if i % 5 == 0: x+= "Buzz"
        if i % 7 == 0: x+= "Boom"
        if i % 11== 0: x+= "Pop"
        print(x) if x else print(i)
