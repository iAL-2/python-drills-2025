#exercise 1
def reverseString(s):
    return s[::-1]
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
        for v in vowels:
            if l == v:
                counter += 1
    return counter

#exercise 4
def deduper(text):
    d = {}
    for ch in text:
        d[ch] = True
    return list(d.keys())

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