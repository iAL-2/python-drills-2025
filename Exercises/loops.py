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