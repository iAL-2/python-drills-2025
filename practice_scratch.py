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

def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1, 101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

def evenOddSplitter():
    sumEvens = 0
    sumOdds = 0

    for i in range(1, 101):
        if i % 2 == 0:
            sumEvens += i
        else:
            sumOdds += i

def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1, 101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    
    sumEvens = sum(evens)
    sumOdds = sum(odds)
    return [sumEvens, sumOdds]

def evenOddSplitter():
    sumEvens = 0
    sumOdds = 0

    for i in range(1, 101):
        if i % 2 == 0:
            sumEvens += i
        else:
            sumOdds += i

def evenOddSplitter():
    evens = []
    odds = []

    for i in range(1, 101):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    
    return [sum(evens), sum(odds)]

def evenOddSplitter():
    sumEvens = 0
    sumOdds = 0

    for i in range(1, 101):
        if i % 2 == 0:
            sumEvens += i
        else:
            sumOdds += i
    return [sumEvens, sumOdds]

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

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    print(sorted(d))

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) +1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    print(sorted(d))

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    print(sorted(d))

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    print(sorted(d))

def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

def divisorFinder(n:int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    print(sorted(d))

def wordReverser(text):
    x = re.findall(r"[A-Za-z]+", text)
    for w in range(len(x)):
        x[w] = x[w][::-1]
    print(" ".join(x))

def wordReverser(text):
    x = re.findall(r"A-Za-z+", text)
    for w in range(len(x)):
        x[w] = x[w][::-1]
    print(" ".join(x))