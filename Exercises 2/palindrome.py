import re

def getstring():
    text = input("Enter a word to check for palindromes ")
    return text

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)

def originalword(token):
    return "".join(token)

def reversestring(token):
    #return "".join(token[::-1])
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def main():
    text = getstring()
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)

    if r == original:
        return True
    else:
        return False

#this version allows the user to input a string at function call of main()

def normalize(text):
    text = text.lower()
    return re.findall(r"[a-z0-9]", text)
#use r"[a-z]" if only using words not numbers

def originalword(token):
    return "".join(token)

def reversestring(token):
    #return "".join(token[::-1])
    ##optional simpler way to build
    reversedword = ""
    for w in token:
        reversedword = w + reversedword
    return reversedword

def is_palindrome(text: str) -> bool:
    token = normalize(text)
    original = originalword(token)
    r = reversestring(token)
    return r == original

##super pythonic way with the exact same logic

def is_palindrome(text: str) -> bool:
    token = "".join(re.findall(r"[a-z0-9]", text.lower()))
    return token == token[::-1]