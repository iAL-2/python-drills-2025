def from_roman(s, mapping=None):
    if mapping is None:
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    total = 0
    prev_value = 0
    for ch in reversed(s):
        value = mapping.get(ch)
        if value is None:
            return "Invalid"
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total


# ✅ Tests
assert from_roman("III") == 3
assert from_roman("IV") == 4
assert from_roman("IX") == 9
assert from_roman("LVIII") == 58
assert from_roman("MCMXCIV") == 1994
assert from_roman("MMMM") == 4000  # optionally handle as valid or Invalid
assert from_roman("XYZ") == "Invalid"


def roman_basics(s):
    mapping = {"I":1, "V":5, "X":10}
    total = 0
    prev = 0
    for ch in reversed(s):
        value = mapping.get(ch)
        if value < prev:
            total -=value
        else:
            total +=value
        prev = value
    return total