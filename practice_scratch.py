

def vowelCounter(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count

def countVowels(text):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

from collections import Counter

def countVowels(text):
    vowels = "aeiou"
    counts = Counter(text.lower())
    return sum(counts[v] for v in vowels)

