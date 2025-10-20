# Palindrome Checker — Logic Block

**Goal**  
- Check if a given input is a palindrome (reads the same forward and backward).

**Inputs**  
- User-inputted string.

**Outputs**  
- Boolean result — `True` if palindrome, `False` otherwise.

**Constraints / Invariants**  
- Comparison must be case-insensitive.  
- Ignore all non-alphanumeric characters.  
- Logic should stay pure (no input or print inside function).  

**Rules (IF/THEN)**  
- IF input is not a string → raise `TypeError`.  
- IF length of normalized string < 2 → return `True`.  
- ELSE compare normalized string with its reverse.  

**Flow**  
1. Receive input text.  
2. Normalize by lowercasing and removing invalid characters.  
3. Reverse the normalized text.  
4. Compare the reversed text to the original normalized text.  
5. Return boolean result.  

**Edge Cases**  
- Empty string or single character → `True`.  
- Punctuation, spaces, numbers ignored during normalization.  
- Numeric strings still valid (e.g. `"12321"`).  
- Optional: Unicode support using `casefold()` and `isalnum()`.  

**Tests / Checks**  
```python
assert is_palindrome("racecar") == True
assert is_palindrome("RaceCar") == True
assert is_palindrome("hello") == False
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("12321") == True
assert is_palindrome("") == True
