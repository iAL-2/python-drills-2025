import re

def extraction(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def tokenize(text):
    return re.findall(r"\[(\w+)\]", text.upper())

def count(tokens):
    counts = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1
    return counts

def log_level_counter(filepath):
    extracted = extraction(filepath)
    tokens = tokenize(extracted)
    return count(tokens)
