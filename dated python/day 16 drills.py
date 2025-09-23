import math

def is_prime(n: int) -> bool:
    # Constraints / Invariants
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n > 1e9:  # cap
        raise ValueError("Input too large")

    # Rules
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Flow: check divisibility up to sqrt(n)
    limit = int(math.isqrt(n))  # efficient integer square root
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

# Tests / Checks
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(17) == True
assert is_prime(18) == False

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
    for w in counts:
        counts[w] = counts.get(w, 0) + 1
    return counts

def _top_items(counts, n):
    pairs_sorted = sorted(counts.items(), key = lambda items:items[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(rows, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
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
    _csv_writer(rows, out_path)

main()


import math

def is_prime(n: int) -> bool:
    #constraints/invariants
    if not isinstance(n , int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n > 1e9:
        raise ValueError("Input too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(17) == True
assert is_prime(18) == False

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n > 1e9:
        raise ValueError("Input is too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n > 1e9:
        raise ValueError("Input too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("input must be integer")
    if n<0:
        raise ValueError("Input must be non-negative")
    if n>1e9:
        raise ValueError("Input too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, n+1, 2):
        if n % i:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("must be integer")
    if n <0:
        raise ValueError("must be non negative")
    if n > 1e9:
        raise ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        return TypeError("Must be integer")
    if n < 0:
        return ValueError("Must be non negative")
    if n > 1e9:
        return ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        return TypeError("must be integer")
    if n < 0:
        return ValueError("must be non negative")
    if n > 1e9:
        return ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("must be integer")
    if n < 0:
        raise ValueError("must be non negative")
    if n > 1e9:
        raise ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance:
        raise TypeError("must be integer")
    if n < 0 :
        raise ValueError("must be non negative")
    if n > 1e9:
        raise ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Must be an integer")
    if n < 0:
        raise ValueError("must be non negative")
    if n > 1e9:
        raise ValueError("too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit +1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int)->bool:
    if not isinstance(n, int):
        raise TypeError("Must be integer")
    if n < 0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("Too big")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit +1, 2):
        if n % i == 0:
            return False
    return True

def is_prime(n:int) -> bool:
    if not isinstance:
        raise TypeError("Must be an integer")
    if n < 0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("Too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

import re

def getstring():
    text = input("Enter a word to check for palindromes ")
    return text

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)

def originalword(token):
    return "".join(token)

def reversestring(token):
    #return "".join(token[::-1])
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def main():
    text = getstring()
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)

    if r == original:
        return True
    else:
        return False

#this version allows the user to input a string at function call of main()

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)
#use r"[a-z]" if only using words not numbers

def originalword(token):
    return "".join(token)

def reversestring(token):
    #return "".join(token[::-1])
    ##optional simpler way to build
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def is_palindrome(text: str) -> bool:
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)
    return r == original

##super pythonic way with the exact same logic

def is_palindrome(text: str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]

def is_prime(n:int) -> bool:
    if not isinstance:
        raise TypeError("Must be an integer")
    if n < 0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("Too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

import re

def getstring():
    text = input("Enter a word to check for palindromes: ")
    return text

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)

def originalword(token):
    return "".join(token)

def reversestring(token):
    #return "".join(token[::-1])
    r = ""
    for w in token:
        r = w + r
    return r

def main():
    text = getstring()
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)

    if r == original:
        return True
    else:
        return False
    
def normalize(text):
    return re.findall(r"a-z0-9", text.lower())

def originalword(token):
    return "".join(token)

def reversedword(token):
    #return "".join(token[::-1])
    r = ""
    for w in token:
        r = w + r
    return r

def is_palindrome(text: str) -> bool:
    token = normalize(text)
    original = originalword(token)
    r = reversedword(token)
    return r == original

def normalize(text):
    return re.findall(r"[a-z0-9]", text.lower())

def originalword(token):
    return "".join(token)

def reversedword(token):
    return "".join(token[::-1])

def is_palindrome(text:str) -> bool:
    token = normalize(text)
    original = originalword(token)
    r = reversedword(token)

    return r == original