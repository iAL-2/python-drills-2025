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
