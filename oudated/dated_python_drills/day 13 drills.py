def get_int(prompt):
    try:
        x = int(input(prompt))
        return x
    except ValueError:
        print("Enter a valid number")
        return None

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    total = 1
    for i in range(1, n+1):
        total *= i
    return total



def menu_loop():
    while True:
        print("Menu:")
        print("1. Square a number")
        print("2. Get the factorial of a number")
        print("3. Exit program")
        
        choice = get_int("Enter a number from 1-3: ")

        if choice == 1:
            x = get_int("Enter a number to square: ")
            if x is not None:
                print(f"The square of {x} is {x*x}")
            else: continue

        elif choice == 2:
            x = get_int("Enter a number to get the factorial of it: ")
            if x is not None:
                print(f"The factorial of {x} is {factorial(x)}")
            else: continue

        elif choice == 3:
            print("Exiting")
            break

        else:
            print("Invalid number. Enter a number from 1-3 ")

#menu_loop()


def fizzbuzzboom(n):
    results = []
    for i in range(1, n+1):
        s = []
        if i % 3 == 0: s.append("Fizz")
        if i % 5 == 0: s.append("Buzz")
        if i % 7 == 0: s.append("Boom")
        if s: results.append("".join(s))
        else: results.append(i)
    return results
# hard to test because it prints. better to turn it into a list and check elements, then print separately
out = fizzbuzzboom(31)
assert out[0] == 1
assert out[2] == "Fizz"

def get_table_size():
    while True:
        try:
            n = int(input("Enter a number from 10-20 for table size: "))
            if 10 <= n <= 20:
                return n
            else:
                print("Invalid input, try again")
        except ValueError:
            print("Enter a valid integer")

def multiplicationtable(n):
        for x in range(1,n+1):
            for y in range(1,n+1):
                print(x*y, end="\t")
            print()
#m = get_table_size()            
#multiplicationtable(m)

assert factorial(5) == 120

d = {"a":1, "b":2}
print(d.keys())
print(d.values())
print(d.items())

with open("test.txt", "w") as f:
    f.write("hello")
with open("test.txt", "r") as f:
    print(f.read())

from utils import square
print(square(5))