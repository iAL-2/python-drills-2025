from collections import defaultdict

data = [("Alice", 90), ("Bob", 80), ("Alice", 100)]

# defaultdict
grades_dd = defaultdict(list)
for name, score in data:
    grades_dd[name].append(score)

# setdefault
grades_sd = {}
for name, score in data:
    grades_sd.setdefault(name, []).append(score)

print(dict(grades_dd))
print(grades_sd)
# Both → {'Alice': [90, 100], 'Bob': [80]}

#setdefault is basically .get with write permissions, writes directly back into the dictionary without assignment
#must use addition instead of append since append returns None; cannot use append in assignment
grades_get = {}
for name,score in data:
    grades_get[name] = grades_get.get(name,[]) + [score]

#.append always returns none


# ASSERTs
expected = {"Alice": [90, 100], "Bob": [80]}
assert dict(grades_dd) == expected
assert grades_sd == expected
assert grades_get == expected
