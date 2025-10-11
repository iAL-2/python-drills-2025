import re
#fixed up initial logic version, this is the indicer version
def wordReverser(text):
    x = re.findall(r"[A-Za-z]+", text)
    for w in range(len(x)):
        x[w] = x[w][::-1]
    print(" ".join(x))

#list comprehension version
def wordReverser(text):
    words = text.split()
    words = [w[::-1] for w in words]
    print(" ".join(words))

#pythonic version
def wordReverser(text):
    print(" ".join([w[::-1] for w in text.split()]))

#uses map(). map(func, iterable) applies func to every element, and is a lazy iterator which saves memory
def wordReverser(text):
    print(" ".join(map(lambda w: w[::-1], text.split())))