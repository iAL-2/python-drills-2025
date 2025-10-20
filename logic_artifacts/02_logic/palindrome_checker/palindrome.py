import re

# --- Version 1: Original (interactive) ----------------
# Basic version that takes user input from the console.

def getstring():
    text = input("Enter a word to check for palindromes: ")
    return text

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)

def originalword(token):
    return "".join(token)

def reversestring(token):
    # return "".join(token[::-1])
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def main():
    text = getstring()
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)
    return r == original


# --- Version 2: Functional form ----------------
# Accepts text directly, no I/O inside the logic.

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)
# use r"[a-z]" if only using letters, not numbers

def originalword(token):
    return "".join(token)

def reversestring(token):
    # return "".join(token[::-1])
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def is_palindrome_v2(text: str) -> bool:
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)
    return r == original


# --- Version 3: Condensed (final) ----------------
# Same logic, but minimal and Pythonic.

def is_palindrome(text: str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]


# --- Tests / Checks ----------------
if __name__ == "__main__":
    assert is_palindrome("racecar") is True
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("") is True
    print("All tests passed.")
