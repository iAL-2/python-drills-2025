def countevenodd(nums):
    even = 0
    odd = 0
    for x in nums:
        if x % 2 == 0:
            even += 1
        elif x % 2 == 1:  #originally an if statement, changed to elif 
            odd += 1
    print(f"Evens: {even}, Odds: {odd}")

countevenodd([1,2,3,4,5,6])

def runningmax(nums):
    max_val = nums[0] #seeding with first element prevents breaking on negatives
    for x in nums:
        if x > max_val:
            max_val = x
        print(f"Current max after {x} = {max_val}") #had to be moved outside the if to print duplicates

runningmax([1,2,3,4,3,6])

def factorial_even(n):
    total = 1
    for i in range(2, n+1, 2): #learned how to do steps in range, otherwise was stuck
        total *= i
    return total

print(factorial_even(10))

def sum_squares(nums):
    total = 0
    for x in nums:
        total += x * x  # original form:(x * x) += total, doesnt work. accumulator
                        #needs to be on the left side of the expression
    return total

sum_squares([1,2,3,4,5,6,7])

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(30)

#string concatenation verison of fizzbuzz
def fizzbuzz(n):
    for i in range(1,n+1):
        out = ""
        if i % 3 == 0: out += "Fizz"
        if i % 5 == 0: out += "Buzz"
        if out:print(i, out)
        else: print(i)

fizzbuzz(16)

#redo of the drills for active recall =============

def countevenodd(nums):
    even = 0
    odd = 0
    for x in nums:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Evens: {even}, Odds: {odd}")

countevenodd([1,2,3,4,5,7,8,9])

def runningmax(nums):
    maxval = nums[0]
    for x in nums:
        if x > maxval:
            maxval = x
        print(f"Current max after {x} = {maxval}")

runningmax([3,4,2,1,6,8,109,1])

def evenfactorial(n):
    total = 1
    for i in range(2, n+1, 2):
        total *= i
    return total #been doing alot of inline printing so mixed it up with return value

print(evenfactorial(8))

def sumsquares(nums):
    total = 0
    for x in nums:
        total += x * x
    print(f"Total sum of the squares of the numbers is : {total}")

sumsquares([1,2,3,4])

#day 5 advanced drills
def counttype(nums):
    positives = 0
    negatives = 0
    zeroes = 0
    for x in nums:
        if x == 0:
            zeroes += 1
        elif x > 0:
            positives += 1
        elif x < 0:
            negatives += 1
    print(f"Positives: {positives}, Negatives: {negatives}, Zeroes: {zeroes}")

counttype([3, -1, 0, 5, -2, 0, 7])

def minmax(nums):
    minval = nums[0]
    maxval = nums[0]
    for x in nums:
        if x > maxval: maxval = x
        if x < minval: minval = x
    print(f"Min = {minval}, Max = {maxval}")

minmax([5, 2, 9, 1, 7])

def reverse_string(s):
    result = ""
    for letter in s:
        result = letter + result #works because letter is before result
    return result

print(reverse_string("hello"))

def cumulative_sum(nums):
    result = []
    output = 0
    for x in nums:
        output += x
        result.append(output)
    return result

print(cumulative_sum([1,2,3,4]))

def filter_evens(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    return result

print(filter_evens([1,2,3,4,5,6,7,8,9]))

def filter_odds(nums):
    result = []
    for x in nums:
        if x % 2 == 1:
            result.append(x)
    return result

print(filter_odds([1,2,3,4,5,6,7,8,9]))

def filter_odds(nums):
    result = []
    for x in nums:
        if x % 2 == 1:
            result.append(x)
    return result

print(filter_odds([1,2,3,4,5,6]))

def square_all(nums):
    result = []
    for x in nums:
        result.append(x*x)
    return result

print(square_all([1,2,3,4]))

def filter_positives(nums):
    result = []
    for x in nums:
        if x > 0:
            result.append(x)
    return result

print(filter_positives([-3, -1, 0, 2, 5]))

def doubled_evens(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x*2)
        else:
            result.append(x)
    return result

print(doubled_evens([1,2,3,4]))

def string_length(s):
    result = []
    for x in s:
        result.append(len(x)) #got stuck on this line, unfamiliar with len function
    return result

print(string_length(["hi", "python", "code"]))

def filter_long_strings(words,n):
    result = []
    for x in words:
        if len(x) > n:
            result.append(x)
    return result

print(filter_long_strings(["hi", "python", "code", "yes"], n=3))