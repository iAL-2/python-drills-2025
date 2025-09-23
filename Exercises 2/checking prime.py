import math

def is_prime(n:int) -> bool:
    if not isinstance:
        raise TypeError("Must be an integer")
    if n < 0:
        raise ValueError("Must be non negative")
    if n > 1e9:
        raise ValueError("Too large")
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True