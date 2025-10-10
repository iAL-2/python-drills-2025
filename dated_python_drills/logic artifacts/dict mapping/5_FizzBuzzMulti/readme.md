# Drill: <FizzBuzzMapping>

## Description
Similar to fizzbuzz, go through a list of numbers starting from 1 to n, replace the numbers dividable within the dictionary/map

## Concept Practiced
- Dictionary/Mapping
- mapping.items()
- Generator expressions vs loop statements; exploration of iterating logic
- String concatenation

## Key Idioms
- mapping.items()
- (x for y in z if 'blank')
- .join() vs +=
- for i in range()
- .append

## Notes
This is essentially fizzbuzz logic exploration. Ran into a tricky part about iterating, comprehension, and loop statements.

## Initial understanding: Both forms are comprehension
Both formats appear to be comprehensions. the key difference is how its stored into memory. since by default, a comprehension doesnt store to memory. they are both string concatenation using comprehension. but the difference is at which step does it become stored into memory? the 'lazy' version uses a generator expression, allowing the whole thing to iterate first, make a temporary collection, then modify it with .join() and store it into a variable. whereas the += version interjects itself in the middle of the comprehension and stores the result AS IT ITERATES. this results in requiring more processing power, but the result is technically the same. every other part of the two versions are the same

## Refined understanding
They are not both comprehension statements.
They are both constructs that iterate. While the key point is indeed where and when they store to memory, comprehension generator expressions and loop statements are just classed differently. 

- Loop statements must have an action while iterating, it's mandatory
- Comprehension/generator expressions iterates according to the comprehension logic. 
- They act in very similar ways but if not following those rules the code will break.

Both ultimately iterate and concatenate strings, but Python classifies them differently at the language level
Loop statements require an explicit action, while comprehension expressions yield values according to their comprehension logic 
They behave similarly but operate in distinct grammatical systems — one procedural, one declarative