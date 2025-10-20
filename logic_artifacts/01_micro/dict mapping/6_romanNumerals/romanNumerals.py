def to_roman(n, mapping=None):
    if mapping==None:
        mapping = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}
    return mapping.get(n, "Invalid")
    
assert to_roman(1) == "I"
assert to_roman(4) == "IV"
assert to_roman(10) == "X"
assert to_roman(11) == "Invalid"


def to_roman(n, mapping=None):
    if mapping is None:
        # Ordered from largest to smallest value
        mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

    if not (1 <= n <= 3999):
        return "Invalid"

    result = ""
    for value, symbol in mapping.items():
        # Determine how many times this symbol fits into n
        count, n = divmod(n, value)
        result += symbol * count  # Append repeated symbols if needed
    return result

#divmod(x,y) returns 2 numbers: 1. integer quotient (a//b) 2. the remainder(a%b)
#q, r = divmod(58, 10)
#q = 5, r = 8


# ✅ Tests
assert to_roman(1) == "I"
assert to_roman(4) == "IV"
assert to_roman(9) == "IX"
assert to_roman(58) == "LVIII"       # 50 + 5 + 3
assert to_roman(1994) == "MCMXCIV"   # 1000 + 900 + 90 + 4
assert to_roman(3999) == "MMMCMXCIX"
assert to_roman(4000) == "Invalid"
