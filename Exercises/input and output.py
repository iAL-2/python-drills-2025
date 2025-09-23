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