#this program prints "Hello World"
#it will also assign 2 variables, x = 7 and y = 3.
#then it will print their sum, difference, product, and quotient
""""Also it will have some multi-line strings"""

def main():
    print("Hello World")

    x = 7
    y = 3

    print(f"Sum of {x} and {y} is {x + y}")
    print(f"Difference of {x} and {y} is {x - y}")
    print(f"Product of {x} and {y} is {x*y}")
    print(f"Quotient of {x} and {y} is {x / y}") #some reason the result here is 1

main()


#conditional program, prompts user for an integer, no guards against value error

x = int(input("Enter an integer"))

if x % 2 == 0:
    print(f"{x} is even")
elif x % 5 == 0:
    print(f"{x} is odd and divisible by 5")
else:
    print(f"{x} is odd")

"""loop that prints numbers from 1-10, squaring them"""

for i in range(1,11):
    print(f"Square of {i} is {i*i}")

"""while loop that counts from 5 to 1, then prints blastoff"""

x = 5
print(x)
while x > 1:
    if x == 0:
        break
    x -= 1
    print(x)
print("Blastoff!")

#factorial and greeting functions, then calling them later
def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def greet(name):
    print(f"Hello, {name}")

print(factorial(5))
greet("Ananda")

#collections practice
"""list practice"""
fruits = ["apple","orange","banana","strawberry"]
fruits.append("mango")
del fruits[1]

for w in fruits:
    print(w)

#sets use the same curly braces as dictionaries. x = {} creates empty dictionary
"""set practice"""
num = {1,2,3,1,2,3,4,5,6,7,7,7,7}
print(num)

"""dictionary practice"""
superfruit = {}
superfruit["apple"] = 2
superfruit["banana"] = 5
print(superfruit)

"""IO practice"""
age = input("Enter your age ")
name = input("Enter your name ")
print(f"You are {age} years old, {name}")

numbers = [1,2,3,4,5,6,76]

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")

with open("numbers.txt", "r") as f:
    loaded_numbers = [int(line.strip()) for line in f]

print(loaded_numbers)

def get_int():
    try:
        x = int(input("Enter an integer: "))
        return x
    except ValueError:
        print("Error, invalid input")

"""Ran into the old problem of string joining and list appending again"""
def fizzbuzzboom(n):
    for i in range(1,n+1):
        g = ""
        if i % 3 == 0: g += "Fizz"
        if i % 5 == 0: g += "Buzz"
        if i % 7 == 0: g += "Boom"
        if g: print(g)
        else: print(i)

fizzbuzzboom(23)


"""had to look up how to get this to work. was missing the end="\t" portion"""
#also somehow forgot to put in range at first, so it was for x in (1,11)
def multiplicationtable():
    for x in range(1,11):
        for y in range(1,11):
            print(x*y, end="\t") #"why doesnt " " work instead of "\t"?
        print() #have to add this to make it add an enter after each row is done printing

multiplicationtable()

#easy menu without integer value error guard
while True:
    print("1. Say Hello")
    print("2. Add Numbers")
    print("3. Quit")

    x = int(input("Enter a number from 1-3"))
    if x == 1: print("Hello!")
    elif x == 2:
        y = int(input("Enter the first number: "))
        z = int(input("Enter a second number: "))
        print(f"The sum of {y} and {z} is {y+z}")
    elif x == 3:
        print("Goodbye")
        break
    else: print("Enter a valid number")

import re
import csv

def _readfile(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def _tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z]+", text)

def _count(tokens):
    w = {}
    for word in tokens:
        w[word] = w.get(word,0) + 1
    return w
    

def _top_items(count, n):
    pairs_sorted = sorted(count.items(), key = lambda kv: kv[1], reverse=True)
    return pairs_sorted[:n]

def _csv_writer(topitems, outpath):
    with open(outpath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word","count"])
        for word, count in topitems:
            writer.writerow([word,count])

def main():

    in_path = "sample.txt"
    out_path = "top_5.csv"
    top_n = 5

    text = _readfile(in_path)
    tokens = _tokenize(text)
    count = _count(tokens)
    topitems = _top_items(count, top_n)

    _csv_writer(topitems, out_path)
    print(f"Top {top_n} numbers printed to {out_path}")

main()