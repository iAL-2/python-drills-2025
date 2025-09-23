for i in range(1,11):
    print(i*i)

while True:
    try:
        x = int(input("Enter a number from 1-3 (0 to quit): "))
    except ValueError:
        print("Invalid input, exiting...")
        break
    if x == 1:
        print("Ok")
    elif x == 2:
        print("Okk")
    elif x == 3:
        print("Okkk")
    elif x == 0:
        print("goodbye")
        break
    else:
        print("Number not in range 0-3")

def fizz_buzz(n):
    result = ""
    for i in range(1,n+1):
        if i % 3 == 0:
            result.append(f"Fizz")
        if i % 5 == 0:
            result.append(f"Buzz")
        if result: print(result)
        else: print(i)

def fizz_buzzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
        elif i % 3 == 0: print("Fizz")
        elif i % 5 == 0: print("Buzz")
        else: print(i)

fizz_buzzz(30)

def cumulative_sum(nums):
    out = []
    total = 0
    for x in nums:
        total += x
        out.append(total)
    return out

print(cumulative_sum([1,2,3,4,5,6,7,8]))

def string_lengths(words):
    out = []
    for w in words:
        out.append(len(w))
    return out

print(string_lengths(["hi", "gay", "dad", "is a homo"]))

def reverse_stirng(s):
    return s[::-1]

print(reverse_stirng("im a gay boi"))

def reverse_string(s):
    out = ""
    for ch in s:
        out = ch + out
    return out

print(reverse_string("Hi, my name is Inigo Montoya. You killed my father. Prepare to die."))