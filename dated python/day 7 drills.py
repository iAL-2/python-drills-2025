def cumulative_sum(nums):
    result = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    print(f"Total sum of numbers is {total}")
    return result

assert cumulative_sum([1,2,33,4,55])[-1] == 95

print(sum([1,2,3,34,55,1]))

def fizzbuzz(n):

    for i in range(1,n+1):
        result = ""
        if i % 3 == 0 and i % 5 == 0: result = "FizzBuzz"
        elif i % 3 == 0: result = "Fizz"
        elif i % 5 == 0: result = "Buzz"
        print(result or i)

fizzbuzz(30)

def even_oddchecker(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            print(f"{x} is even")
            result.append(f"{x} is even")
        else:
            print(f"{x} is odd")
            result.append(f"{x} is odd")
    return result

print(even_oddchecker([0,2,4,5,6,7,8,9]))

while True:
    print("Enter 1 or 2. 0 to quit")

    x = int(input())

    if x == 1:
        print("Hi")
    elif x == 2:
        print("Haiiiiii <3")
    elif x == 0:
        print("Goodbyeeee")
        break
    else:
        print("Enter a valid input from 0-2")

while True:
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("0. Exit")

    try:
        choice = int(input("Input a number from 0-2 "))
    except ValueError:
        print("Enter a valid input")
        continue

    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("Goodbye")
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("Enter a valid input")

while True:
    print("1. Sum of 2 numbers")
    print("2. Multiply 2 numbers")
    print("0. Exit")

    try:
        choice = int(input("Input a number from 0-2 "))
    except ValueError:
        print("Enter a valid input")
        continue

    if choice == 1:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Sum =", sum([a,b]))
        except ValueError:
            print("❌ Please enter valid numbers.")
    elif choice == 2:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a * b)
        except ValueError:
            print("❌ Please enter valid numbers.")
    elif choice == 0:
        print("Exiting")
        break
    else:
        print("Enter a valid input")

nums = [] #initially had this in the while loop which caused it to always become blank
while True:
    print("1. Add a number to the list")
    print("2. Show all numbers")
    print("3. Show the sum of numbers")
    print("0. Exit")


    try:
        choice = int(input("Enter a number from 0-3 "))
    except ValueError:
        print("Enter a valid number")
        continue 
        #didnt add this initially, fixed by chatgpt. except valueerror needs continue
    
    if choice == 1:
        try:
            addednumber = int(input("Enter a number to add to the list "))
            nums.append(addednumber)
        except ValueError:
            print("Enter an integer")

    elif choice == 2:
        print(nums)

    elif choice == 3:
        print(sum(nums))
    
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Enter a number from 0-3")

#nested while loop
while True:
    print("1. Math Tools")
    print("2. Greetings")
    print("0. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        # do A
        while True:
                print("1. Square a Number")
                print("2. Factorial")
                print("0. Back")
                choice1 = input("Choose: ").strip()
                if choice1 == "1":
                     x = int(input("Enter a number to square: "))
                     print(f"{x} squared is {x*x}")
                elif choice1 == "2":
                     total = 1
                     x = int(input("Enter a number to get the factorial of it: "))
                     for i in range(1, x+1):
                          total *= i
                     print(f"Factorial of {x} is {total}")
                elif choice1 == "0":
                     break
                else: print("Enter a valid number.")
    elif choice == "2":
        # do B
         while True:
                print("1. Say Hello")
                print("2. Say Goodbye")
                print("0. Back")
                choice1 = input("Choose: ").strip()
                if choice1 == "1":
                   print("Hello there")
                elif choice1 == "2":
                    print("Goodbye...")
                elif choice1 == "0":
                     break
                else: print("Enter a valid number.")
    elif choice == "0":
        print("Exiting")
        break
    else:
        print("Invalid option")

## version that converts the submenus to functions, allowing them to be called
def math_menu():
    while True:
        print("1. Square a number")
        print("2. Factorial")
        print("0. Go Back")
        choice = input("Choose: ").strip()

        if choice == "1":
            x = int(input("Enter a number: "))
            print(f"The square of {x} is {x*x}")
        elif choice == "2":
            total = 1
            x = int(input("Enter a number to get the factorial of it: "))
            for i in range(1,x+1):
                total *= i
            print(f"The factorial of {x} is {total}")
        elif choice == "0":
            print("Returning to main menu")
            break
        else:
            print("Invalid option")

def greetings_menu():
    while True:
        print("1. Say Hello")
        print("2. Say Goodbye")
        print("0. Go Back")
        choice = input("Choose: ").strip()

        if choice == "1":
            print("Hello There!")
        elif choice == "2":
            print("Goodbye!!")
        elif choice == "0":
            print("Returning to main menu")
            break
        else:
            print("Invalid option")

while True:
    print("1. Math Tools")
    print("2. Greetings")
    print("0. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        math_menu()
    elif choice == "2":
        greetings_menu()
    elif choice == "0":
        print("Exiting")
        break
    else:
        print("Invalid option")
