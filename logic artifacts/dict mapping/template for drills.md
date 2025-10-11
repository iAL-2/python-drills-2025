# Drill: Letter Frequency Counter

## Description
Count how many times each letter (a–z) appears in a given string.

## Concepts Practiced
- Character-level vs. word-level granularity  
- Membership checking within a mapping (`if ch in dict`)  
- Dictionary seeding for fixed keys

## Key Idioms
- `import string` → `string.ascii_lowercase` for alphabet generation  
- `.lower()` for normalization  
- `re.findall(r"[a-z]", text.lower())` for regex-based filtering

## Notes
- Both the regex and membership-check versions correctly ignore non-alphabetic characters.  
- The optimized version removes regex overhead and uses `if ch in count:` to skip special characters and spaces.  
- Pre-seeding ensures all 26 letters appear in the final dictionary, even if their count is zero.
