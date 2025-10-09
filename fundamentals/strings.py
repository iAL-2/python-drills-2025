def string_lengths(words):
    out = []
    for w in words:
        out.append(len(w))
    return out

print(string_lengths(["hi", "gay", "dad", "is a homo"]))

def reverse_stirng(s):
    return s[::-1]

print(reverse_stirng("im a gay boi"))

def reverse_string(s):
    out = ""
    for ch in s:
        out = ch + out
    return out

print(reverse_string("Hi, my name is Inigo Montoya. You killed my father. Prepare to die."))

def reverse_string(s):
    result = ""
    for letter in s:
        result = letter + result #works because letter is before result
    return result


print(reverse_string("hello"))

#exercise 1
def reverseString(s):
    return s[::-1]

#strip variation removes whitespace at ends, not inside
def reverseString(text):
    return text.strip().lower()[::-1]

#variations that removes spaces and uses lowercase, good for setting up palindrome check
def reverseString(s):
    return s.replace(" ", "").lower()[::-1]

def reverseStringClean(s):
    cleaned = "".join(s.lower().split())  # remove spaces, lowercase
    return cleaned[::-1]
