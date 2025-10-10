#uses a generator for iterating, and uses .join() with variable assignment to keep the result
def multi_sub(n, mapping=None):
    if mapping is None:
        mapping = {2: "Two", 3: "Three", 5: "Five"}
    
    result = []
    for i in range(1, n+1):
        s = "".join(word for div,word in mapping.items() if i % div == 0)
        result.append(s or i)
    return result


#uses += to concatenate the result of iteration
def multi_sub(n, mapping=None):
    if mapping is None:
        mapping = {2: "Two", 3: "Three", 5: "Five"}
    
    result = []
    for i in range(1, n+1):
        s = ""
        for div, word in mapping.items():
            if i % div == 0:
                s += word
        result.append(s or i)
    return result

"""s += (word for div,word in mapping.items() if i % div == 0) doesn't work because:
(word for div,word in mapping.items() if i % div == 0) is a generator expression. += expects a string or number
"""

#comprehensions always involve iteration. They are explicitly about iterate over something, transform or filter it, and produce new values