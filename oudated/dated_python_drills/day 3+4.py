def square(n):
    print(n*n)

square(4)

def is_even(n):
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd")
    
is_even(4)
is_even(5)

def greet(name):
    print("Hello,"+name.upper())

greet("ananda")

def factorial(n):
    x=1
    for i in range(1,n+1):
        x *= i
    return x

print(factorial(5))
print(factorial(10))

def sum_list(nums):
    total=0
    for n in nums:
        total += n
    return total

print(sum_list([1,2,3,4,5,6,7,8]))

#chatgpt's cleaned up versions; made everything into pure function by using return instead

def square(n):
    return n * n

def cubed(n):
    return n * n * n

def is_even(n):
    return n % 2 == 0 # boolean result

def greet(name):
    return f"Hello, {name.upper()}"

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total

print(square(4))
print("even" if is_even(4) else "odd")
print(cubed(4))
print(factorial(5))
print(factorial(10))
print(sum_list([1,2,3,4,5,6,7,8,9,]))

#============day 4 drills=============
def is_even(n):
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"
    
print(is_even(4))
print(is_even(5))


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(5))
print(factorial(8))


#bugged out here, had to debug by looking at old working code

def sum_list(nums):
    total = 0
    for x in nums:
        #old: total += nums
        total += x
    return total

print(sum_list([3,4,5,6,7,8,9]))

def greet(name):
    return f"Hello, {name.upper()}"

print(greet("ananda"))

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
        print("Added", n, "-> total  =", total)
    return total

sum_list([1,2,3,4,5,6,7,8,9])

def sum_list(nums): #list of numbers here
    total = 0       #accumulator
    i = 0           #some kind of constant to compare the number of objects inside(nums)
    while i < len(nums): #so this loop will run until it reaches the number of objects inside nums
        total += nums[i] #not sure how nums[i] works. do the values inside nums get extracted into i each loop?
        i += 1 #seems it goes up by one manually each loop instead of using range. does that correspond to a later item in the (nums?)
    return total

#factorial that prints at each step of the factorial
#done by using "before" to snapshot "total", allowing them in the same fstring
def factorial(n):
    total = 1
    for i in range(1,n+1):
        before = total
        total *= i
        print(f"{before}*{i}={total}")
    print(f"Factorial of {n} is {total}")
    return total

factorial(5)

#factorial version that uses an fstring trick to avoid using "before"
def factorial(n):
    total = 1
    for i in range(1, n+1):
        print(f"{total}*{i}={total * i}")
        total *= i
    print(f"Factorial of {n} is {total}")
    return total

factorial(5)

#sum_list with snapshot
def sum_list(nums):
    total = 0
    for x in nums:
        before = total
        total += x
        print(f"{before} + {x} = {total}")
    print(f"Final sum is {total}")
    return total

sum_list([3, 4, 5, 6])

#sum_list with inline calculation, no snapshot
def sum_list(nums):
    total = 0
    for x in nums:
        print(f"{total} + {x} = {total + x}")
        total += x
    print(f"Final sum is {total}")
    return total

sum_list([1,2,3,4,5,6,7,8])
