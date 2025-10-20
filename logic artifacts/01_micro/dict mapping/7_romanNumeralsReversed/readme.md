# Drill: <Roman Numerals Reversed>

## Description
Take a roman numeral and convert it into an integer

## Concept Practiced
- Reading and iterating in reverse using a map

## Key Idioms
- `dict.get(key)` for safe lookup  
- reading a string in reverse with `reversed()`

## Notes
- Complicated feeling function. Because of how roman numeral works with exceptions such as IV and IX, you must read it in reverse to properly get the integer equivalent.
- 2 ways to do that, either use `reversed(s)` or `s[::-1]`
- Cover invalid inputs by checking against the map. Attempt variable assignment with `.get()`, if the value doesn't exist the variable will be assigned `None`. Use an if statement to cover that and return `"Invalid"`
- Always have 2 variables, in order to compare current vs previous roman numeral values. To cover IV and IX, if the current value is lower than the previous value, subtract the current value(usually I=1) instead of adding it. That logic will fulfill the special rule of roman numerals
- Otherwise by reading in reverse, if the next value is >=, just add the new value.