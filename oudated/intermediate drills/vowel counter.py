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
