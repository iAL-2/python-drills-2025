import math
import re


def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1, 101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"Sum of evens is {sum(evens)}")
    print(f"Sum of odds is {sum(odds)}")

def evenOddSplitter():
    sumEvens = 0
    sumOdds = 0

    for i in range(1, 101):
        if i % 2 ==0:
            sumEvens += i
        else:
            sumOdds += i
    
    print(f"Sum of evens is{sumEvens}")
    print(f"Sum of odds is {sumOdds}")


def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    return(d)

import math
def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    print(sorted(d))

def wordReverser(text):
    x = re.findall(r"[A-Za-z]+", text)
    for w in range(len(x)):
        x[w] = x[w][::-1]
    print(" ".join(x))

def wordReverser(text):
    word = text.split()
    word = [w[::-1] for w in word]
    print(" ".join(word))

def wordReverser(text):
    print(" ".join([w[::-1] for w in text.split()]))


def wordReverser(text):
    print(" ".join(map(lambda w:w[::-1], text.split())))

def uniqueChars(text):
    print(set(text))

def uniqueChars(text):
    d = {}
    for ch in text:
        d[ch] = True
    print("".join(d.keys()))


import csv
from paths import DATA_DIR

def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open(DATA_DIR/"test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        for dict in d:
            writer.writerow([dict["name"], dict["age"]])
    with open(DATA_DIR/"test.csv", "r", encoding="utf-8") as f:
        return f.read()
    
def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open(DATA_DIR/"test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(d)

def csvWriter():
    d = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Carol", "age": 30},
    ]
    with open(DATA_DIR/"test.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictReader(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(d)

def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
    
def lineCounter(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())
    
def fizzBuzzBoomPop(n):
    for i in range(1, n+1):
        x = ""
        if i % 3 == 0: x+= "Fizz"
        if i % 5 == 0: x+= "Buzz"
        if i % 7 == 0: x+= "Boom"
        if i % 11 == 0: x+= "Pop"
        print(x) if x else print(i)