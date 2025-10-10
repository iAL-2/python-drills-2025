# Drill: <Roman Numerals>

## Description
Uses a map of roman numerals and their values. Input the number, get back the roman numeral equivalent. 
Advanced version goes up to 3999

## Concept Practiced
- dict mapping
- loop statements
- ordered iteration and accumulation

## Key Idioms
- `dict.get(key, default)` for safe lookup  
- `divmod(a, b)`
- `"string" * i`

## Notes
Had trouble understanding the `divmod(`) variant at first, the point is to loop starting from the largest numbers and slowly iterate through the list, with each large number's roman equivalent being appended onto the result. `divmod()` keeps taking the remainder and uses that for the next part of the map, updating each time. The main difficulty is in understanding the way to set this up so it respects the roman numeral structure. `"string" * integer` was also not explored before this drill. 