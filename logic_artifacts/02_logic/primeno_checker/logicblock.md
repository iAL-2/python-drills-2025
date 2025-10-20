# Prime Number Checker — Logic Block

**Goal**  
- Check whether a number is prime or not.

**Inputs**  
- Any integer.

**Outputs**  
- Boolean result — `True` if prime, `False` otherwise.

**Constraints / Invariants**  
- No floats, no negatives.  
- Input capped at around 1e9 for efficiency and safety.  

**Rules (IF/THEN)**  
- IF input is not an integer → raise `TypeError`.  
- IF input < 0 → raise `ValueError`.  
- IF input ≤ 1 → return `False`.  
- IF input == 2 → return `True`.  
- IF input > 2 and even → return `False`.  
- ELSE loop through odd divisors up to the square root of the number;  
  IF any divisor found → return `False`;  
  ELSE return `True`.  

**Flow**  
1. Validate type and range.  
2. Handle small numbers and even cases early.  
3. Compute integer square root limit.  
4. Loop through odd divisors from 3 to √n.  
5. Return result based on whether any divisors were found.  

**Edge Cases**  
- Input 0 or 1 → `False` (not prime).  
- Negative numbers → raise `ValueError`.  
- Input larger than 1e9 → raise `ValueError` for performance cap.  

**Tests / Checks**  
  ```python
  assert is_prime(2) == True
  assert is_prime(3) == True
  assert is_prime(4) == False
  assert is_prime(29) == True
  assert is_prime(1) == False
  assert is_prime(0) == False
```

**Notes**

- **Type hints (`n: int -> bool`)**  
  - Make the function’s contract explicit and help IDEs or static checkers catch mistakes early.  
  - They don’t affect runtime but improve readability and maintainability.

- **Error choices**  
  - `TypeError`: wrong data type (not an integer).  
  - `ValueError`: invalid integer (negative or too large).  
  - Distinguishes type errors from value errors, following Python conventions.

- **Prime-checking logic**  
  - A prime has no divisors other than 1 and itself.  
  - If `n` has a factor, one of the factors must be ≤ √n — so checking past that is redundant.  
  - `math.isqrt(n)` safely computes the integer square root without floating-point issues.  
  - We skip even numbers since any even `n > 2` is composite; thus, we start at 3 and step by 2.  
  - This reduces time complexity to roughly O(√n/2).

