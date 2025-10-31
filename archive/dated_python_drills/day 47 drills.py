#exercise 1
def reverseString(s):
    return s[::-1]

#strip variation removes whitespace at ends, not inside
def reverseString(text):
    return text.strip().lower()[::-1]

#variations that removes spaces and uses lowercase, good for setting up palindrome check
def reverseString(s):
    return s.replace(" ", "").lower()[::-1]

def reverseStringClean(s):
    cleaned = "".join(s.lower().split())  # remove spaces, lowercase
    return cleaned[::-1]


#to modify this, need to use either re.findall, or something like text.split()
#check with chatgpt after finishing the rest

#exercise 2
def reverseList(x):
    newlist = []
    for n in x:
        if n % 2 == 0:
            newlist.append(n)
    reverselist = newlist[::-1]
    return reverselist, newlist

#exercise 3
def vowelCounter(input):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for l in input:
        for v in vowels: #double for loop, explicit but inefficient
            if l == v:
                counter += 1
    return counter

def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}  # set for fast lookup
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

def vowelCounter(text):
    vowels = set("aeiou") #faster set writeup
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

def count_vowels(text):
    vowels = "aeiou" #string version works but is less efficient when using 'if x in'
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

def count_vowels(text): 
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels) #returns numbers separated by commas

from collections import Counter

def count_vowels(text):
    vowels = "aeiou"
    counts = Counter(text.lower()) #creates a dictionary with values of counts
    return sum(counts[v] for v in vowels)

#exercise 4
def deduper(text):
    d = {}
    for ch in text:
        d[ch] = True
    return list(d.keys())

#stable deduper for older python versions
def deduper(text):
    seen = set()
    result = []
    for item in text:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#exercise 4.2
def textDict(text):
    d = {}
    for l in text:
        d[l] = d.get(l, 0) + 1
    return d

#exercise 5
def listWriter():
    l = ['apple','banana','strawberry']
    with open("text.txt", "w", newline="", encoding="utf-8") as f:
        for word in l:
            f.write(word + "\n")

    with open("text.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip().upper())

