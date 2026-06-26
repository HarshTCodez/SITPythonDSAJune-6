# Day 3 — Number Problems & Array Exercises

---

## Part 1 — Second Highest Element

> [`second_highest.py`](second_highest.py)

Find the 2nd largest value in a single pass — O(n) time, O(1) space. No sorting.

```python
def second_highest(arr):
    max1 = float("-inf")
    max2 = float("-inf")
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        if x != max1 and x > max2:
            max2 = x
    return max2
```

**Key ideas:**
- `float("-inf")` is a sentinel smaller than any real number — the first element always wins the first comparison.
- `x != max1` guard: without it, a duplicate maximum (e.g. `[5, 5, 3]`) would be mistakenly accepted as the 2nd max.
- Two variables, one pass — no sorting needed.

---

## Part 2 — Reverse a List In-Place

> [`reverese_list.py`](reverese_list.py)

```python
x = [1, 2, 3, 4, 5, 6]

for i in range(0, len(x) // 2):
    last_element_index = len(x) - i - 1
    x[i], x[last_element_index] = x[last_element_index], x[i]
```

**Key ideas:**
- `len(x) // 2` iterations are enough — each swap handles two positions at once.
- Mirror index formula: `len(x) - i - 1`.
- This is the same idea as the two-pointer approach, written with one index variable.

---

## Part 3 — LeetCode Problems

### LC 7 — Reverse Integer

> [`lc_07.py`](lc_07.py)

**Problem:** Reverse the digits of a 32-bit signed integer. Return `0` if the result overflows.

```python
MIN = -(2**31)
MAX = (2**31) - 1

def reverse_integer(n: int):
    rev = 0
    while n > 0:
        last = n % 10          # grab the last digit
        rev = rev * 10 + last  # push it onto the reversed number
        n = n // 10            # drop the last digit
    return rev

def reverse(n: int):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * (-1)
    n = reverse_integer(n)
    if is_negative:
        n = n * (-1)
    if n > MAX:
        return 0
    if n < MIN:
        return 0
    return n
```

**Key ideas:**
- `n % 10` gives the last digit; `n // 10` drops it. Same loop pattern as `sum_digits` and `count_digits` from Day 1.
- Handle the sign separately: strip it, reverse the absolute value, then restore it.
- Python integers are unbounded, so overflow must be checked manually against 32-bit limits after reversing.

---

### LC 9 — Palindrome Number

> [`lc_09.py`](lc_09.py)

**Problem:** Return `True` if an integer reads the same forwards and backwards.

```python
from lc_07 import reverse_integer

def ans(n):
    if n < 0:
        return False
    new_number = reverse_integer(n)
    return new_number == n
```

**Key ideas:**
- Negative numbers are never palindromes — the `-` sign has no mirror.
- Reuses `reverse_integer` from LC 7 — good example of writing a helper once and using it across problems.

---

### LC 258 — Add Digits

> [`lc_258.py`](lc_258.py)

**Problem:** Repeatedly sum the digits of a number until a single digit remains.
Example: `38 → 3+8=11 → 1+1=2`

**Approach 1 — Simulation (loop until single digit):**
```python
def sum_of_digits(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans

def addDigits(n: int) -> int:
    while n >= 10:
        n = sum_of_digits(n)
    return n
```

**Approach 2 — Digital root formula, O(1):**
```python
def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    ans = num % 9
    if ans == 0:
        ans = 9
    return ans
```

**Key ideas:**
- The loop is the natural solution — keep reducing until one digit remains.
- The O(1) formula uses the *digital root* pattern: repeated digit sum always equals `num % 9`. Special case: multiples of 9 return 9, not 0.

---

### LC 1295 — Find Numbers with Even Number of Digits

> [`lc_1295.py`](lc_1295.py)

**Problem:** Count how many numbers in the array have an even number of digits.

```python
def count_digits(n):
    if n == 0:
        return 1
    ans = 0
    while n > 0:
        ans += 1
        n = n // 10
    return ans

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for current_number in nums:
            if count_digits(current_number) % 2 == 0:
                ans += 1
        return ans
```

**Key ideas:**
- `count_digits` is the same floor-division loop from Day 1 — recognise and reuse patterns.
- Special case: `n == 0` has 1 digit; without the guard the loop exits immediately and returns 0.
- `% 2 == 0` selects even digit counts.
