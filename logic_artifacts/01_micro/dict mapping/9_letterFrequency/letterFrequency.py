#initial solution
import string
import re

def letterFreqCount(text):
    count = {letter: 0 for letter in string.ascii_lowercase}
    for ch in re.findall(r"[a-z]", text.lower()):
        count[ch] = count.get(ch, 0) + 1
    return count



#micro-optimization that checks membership using dictionary and `if ch in count`
#special characters and spaces are discarded because they are not in count, which is designed to only have the 26 letters
def letterFreqCount(text):
    count = {letter: 0 for letter in string.ascii_lowercase}
    for ch in text.lower():
        if ch in count:
            count[ch] += 1
    return count
