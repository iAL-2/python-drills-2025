#Fizz is 3, Buzz is 5, Boom is 7
for i in range(1,106):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBoom")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzBoom")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBoom")
    elif i % 7 == 0:
        print("Boom")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#superior version
for i in range(1, 100):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if i % 7 == 0:
        result += "Boom"
    
    if result:  # if the string isn't empty
        print(result)
    else:
        print(i)


for i in range(1,100):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if i % 7 == 0:
        result += "Boom"
    
    if result: #if result:  blank is a shorthand for if result != "". It means if result is truthy no falsy
        print(result)
    else:
        print(i)

    if result != "": #explicitly written out ending
        print(result)
    else:
        print(i)

#append version
for i in range(1,100):
    result = []

    if i % 3 == 0:
        result.append("Fizz")
    if i % 5 == 0:
        result.append("Buzz")
    if i % 7 == 0:
        result.append("Boom")
    
    if result != []:
        print("".join(result)) # "text.join()" lets you add a string between each of the list items 
    else: print(i)

#shortest version, using append
for i in range(1,100):
    result = []
    if i % 3 == 0: result.append("Fizz")
    if i % 5 == 0: result.append("Buzz")
    if i % 7 == 0: result.append("Boom")
    print("".join(result) if result else i)

#even shorter versions that chatgpt tried to break my mind with
for i in range(1,100):
    print(("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) + "Boom"*(i % 7 == 0)) or i) 
#this one works using an or statement. if none of the conditions are filled, as in all the
#statements are false, then it will generate an empty string, which is falsy.

#final version chatgpt said clear and concise
def fizz_buzz_boom(start=1, stop=100):
    rules = [(3, "Fizz"), (5, "Buzz"), (7, "Boom")]
    for i in range(start, stop):
        out = "".join(word for n, word in rules if i % n == 0)
        print(out or i)

fizz_buzz_boom()

#final version chatgpt said clear and concise
def fizz_buzz_boom(start=1, stop=100):
    if start >= stop:
            return
    rules = [[3, "Fizz"], [5, "Buzz"], [7, "Boom"]]
    for i in range(start, stop):
        out = "".join(word for n, word in rules if i % n == 0)
        print(out or i)

fizz_buzz_boom()

#improved final version that flexible in changing the rules in initial argument
def fizz_buzz_boom(start=1, stop=100, rules=((3,"Fizz"), (5,"Buzz"), (7,"Boom"))):
    for i in range(start, stop):
        out = "".join(word for n, word in rules if i % n == 0)
        print(out or i)

fizz_buzz_boom()  # all defaults
fizz_buzz_boom(10, 20)  # positional: start=10, stop=20
fizz_buzz_boom(rules=[(2,"Foo"), (9,"Bar")])  # keyword: only rules changed
fizz_buzz_boom(5, rules=[(4,"Quad")])  # start=5, stop=100 (default), custom rules

def fizzbuzz_custom(start, stop, rules):
    for i in range(start, stop):
        out = ""
        for n, word in rules:
            if i % n == 0:
                out += word
        print(out or i)

def quadhex(n):
    for i in range(1, n+1):
        word = ""
        if i % 4 == 0:
            word += "Quad"
        if i % 6 == 0:
            word += "Hex"
        print(word) if word else print(i)

quadhex(50)