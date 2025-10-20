# Drill: Gradebook Aggregator

## Description
Given a list of `(student, grade)` pairs, compute the average grade per student.

## Concepts Practiced
- Mapping multiple values to a single key  
- Using a list as the value (`dict[key].append(x)`) or `defaultdict(list)`  
- Post-processing with `sum()` and `len()`

## Notes
- Both `setdefault()` and `defaultdict()` handle missing keys, but with different trade-offs:  
  - `defaultdict()` requires a setup line (`grades = defaultdict(list)`) but simplifies loops.  
  - `setdefault()` works with plain dicts but must be called in every accumulation step.  
- `.get()` is mainly for read-only lookups; it can mimic accumulation only in limited, less efficient cases.
