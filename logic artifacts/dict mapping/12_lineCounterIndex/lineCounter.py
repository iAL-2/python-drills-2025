import re
from collections import defaultdict

def extraction(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

def tokenize_and_index(lines):
    index = defaultdict(set)
    for lineno, line in enumerate(lines, start=1):
        for word in re.findall(r"\w+", line.lower()):
            index[word].add(lineno)
    return index


result = tokenize_and_index(extraction("text.txt"))
print(result)
