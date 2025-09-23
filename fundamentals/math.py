def squared(x):
    return x*x

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "undefined"
        else:
            return a / b
    except (ValueError, TypeError):
        return "non-numeric"
    
print(safe_divide(6, 3))       # 2.0
print(safe_divide("7.5", 2))   # 3.75
print(safe_divide(5, 0))       # "undefined"
print(safe_divide("x", 2))     # "non-numeric"
