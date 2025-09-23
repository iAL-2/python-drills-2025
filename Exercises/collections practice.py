#collections practice
"""list practice"""
fruits = ["apple","orange","banana","strawberry"]
fruits.append("mango")
del fruits[1]

for w in fruits:
    print(w)


def cumulative_sum(nums):
    out = []
    total = 0
    for x in nums:
        total += x
        out.append(total)
    return out

print(cumulative_sum([1,2,3,4,5,6,7,8]))


nums = [0,1,2,3,4,5,6,7,8,9]

print(nums[2:5])     # [2,3,4] (end is exclusive)
print(nums[:4])      # [0,1,2,3] (start defaults to 0)
print(nums[6:])      # [6,7,8,9] (goes to end)
print(nums[::2])     # [0,2,4,6,8] (every 2nd element)
print(nums[::-1])    # [9,8,7,6,5,4,3,2,1,0] (reversed)

def lislicing():
    x = []
    for i in range(1, 21):
        x.append(i)
    print(x[1::2]) #prints starting at 1st index, every 2 steps
    print(x[::-1]) 
    print(x[2::3]) #prints at 2nd index, every 3 steps

lislicing()


#sets use the same curly braces as dictionaries. x = {} creates empty dictionary
"""set practice"""
num = {1,2,3,1,2,3,4,5,6,7,7,7,7}
print(num)

"""dictionary practice"""
superfruit = {}
superfruit["apple"] = 2
superfruit["banana"] = 5
print(superfruit)

d = {"a": 1, "b": 2}
print(d.keys())    # dict_keys(['a','b'])
print(d.values())  # dict_values([1,2])
print(d.items())   # dict_items([('a',1),('b',2)])




######old list practice#######
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

def filter_evens(nums):
    result = []
    for x in nums:
        if x % 2 == 0:
            result.append(x)
    return result
print(filter_evens([1,2,3,4,5,6,7,8,9]))

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