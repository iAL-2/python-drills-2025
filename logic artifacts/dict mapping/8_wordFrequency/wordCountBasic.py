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
