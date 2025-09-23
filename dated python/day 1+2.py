def greet(name):
    return("Hello," + name)
message = greet("Ananda")
print(message)
print(message.upper())
print(message + " - have a nice day ")
age = 30
print(f"Age: {age}")               # → Age: 30
print(f"Next year: {age + 1}")     # → Next year: 31
print(f"Name uppercased: {message.upper()}")  # → ANANDA

def high(lol):
    return("hello," + lol)

print(high("hi"))

def cubed(x):
    return x*x*x

answer = cubed(3)

print(answer)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(0))
print(factorial(5))
