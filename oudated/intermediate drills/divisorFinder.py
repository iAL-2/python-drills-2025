def divisorFinder(n:int):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    print(d)

import math
#optimized version with square root
def divisorFinder(n: int):
    d = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    print(sorted(d))