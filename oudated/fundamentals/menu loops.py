while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Add two numbers")
    print("3. Quit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        print("Hello 👋")
    elif choice == "2":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Sum =", a + b)
        except ValueError:
            print("❌ Please enter valid numbers.")
    elif choice == "3":
        print("Goodbye!")
        break  # exit program
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")


while True:
    print("\nMenu:")
    print("Enter a number. Any other input will exit the program")

    userinput = input("Enter number: ")

    try:
        userinput = int(userinput)
    except ValueError:
        print("goodbye")
        break

    if userinput > 100:
        print("greater than 100")
    elif userinput > 5:
        print("greater than 5 but less than 100")
    else:
        print("less than 5")

#Nested menu with helper functions, validator core logic with asserts at the end

def get_int_in_range(prompt, lo, hi):
     while True:
          s= input(prompt).strip()
          try:
               x = int(s)
               if lo <= x <= hi:
                    return x
               else:
                    print(f"Enter a number in [{lo}-{hi}].")
          except ValueError:
               print("Enter a valid integer.")

def main_choice():
      print("1. Math functions")
      print("2. Greetings")
      print("0. Exit")
      return get_int_in_range("Choose (0-2): ", 0, 2)

def math_choice():
     print("1. Square a number.")
     print("2. Get the factorial of a number.")
     print("0. Return to previous menu.")
     return get_int_in_range("Choose (0-2): ", 0, 2)

def square_number():
          x = get_int_in_range("Enter a number to get the square of it: ", -10**9, 10**9)
          total = x * x
          print(f"The square of {x} is {total}.")

def factorial():
          x = get_int_in_range("Enter a non-negative integer from 0-100: ", 0, 100)
          total = 1
          for i in range(1, x+1):
               total *= i
          print(f"The factorial of {x} is {total}.")

def greet_choice():
     print("\nGreetings:")
     print("1. Say Hello")
     print("2. Say Goodbye")
     print("0. Return to previous menu")
     return get_int_in_range("Choose (0-2): ", 0, 2)

def say_hello():
     print("Hello!")

def say_goodbye():
     print("Goodbye!")

while True:
      m = main_choice()
      if m == 1:
            while True:
                  mm = math_choice()
                  if mm == 0: break
                  elif mm == 1: square_number()
                  elif mm == 2: factorial()
      elif m == 2:
          while True:
                gm = greet_choice()
                if gm == 0 : break
                elif gm == 1: say_hello()
                elif gm == 2: say_goodbye()
      elif m == 0:
          print("Exiting")
          break
    
#validator core of get_int_in_range
def _validate_range(x, lo, hi): return lo <= x <= hi
assert _validate_range(2, 0, 3) is True
assert _validate_range(5, 0, 3) is False

#validator core of factorial()
def factorial_core(n):
      total = 1
      for i in range(1, n+1):
            total *= i
      return total
assert factorial_core(5) == 120