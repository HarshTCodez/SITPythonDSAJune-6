# Day 1 — Logic Building, Patterns & Number Problems

Everything we covered on Day 1. The puzzles are about *thinking* — no code needed.
Then we moved on to patterns and number problems, where we wrote real Python.

> Whiteboard from the session: [`day1.excalidraw`](../../day1.excalidraw)

---

## Part 1 — Logic Puzzles (no code, just thinking)

### Q1. Two candles → measure 45 minutes

**Problem:** Two candles each burn for exactly 1 hour, but they burn *non-linearly*
(length tells you nothing about time left). Measure exactly 45 minutes.

**Logic:**
- A candle lit from **both ends** finishes in **30 minutes**, no matter how unevenly
  it burns — the two flames together consume "one hour's worth" of candle.
- At t = 0: light **Candle A at both ends** and **Candle B at one end**.
- When Candle A is fully burnt → **30 minutes** have passed.
- At that exact moment, light **Candle B's other end**. B had 30 minutes of life left,
  but now burning from both ends it finishes in **15 minutes**.
- 30 + 15 = **45 minutes**. ✅

> Idea: you only had one action — "light an end" — but using it cleverly solved it.

---

### Q2. Toffees and wrappers → answer is 74

**Problem:** You have ₹50. 1 toffee costs ₹1. The seller also gives 1 toffee in
exchange for 3 wrappers. How many toffees do you get in total?

**Logic:**
- Buy 50 toffees with ₹50. Eat them → you now hold **50 wrappers**.
- Keep exchanging while you have at least 3 wrappers:
  - 50 wrappers → 16 toffees, 2 wrappers left over → 2 + 16 = **18 wrappers**
  - 18 wrappers → 6 toffees → **6 wrappers**
  - 6 wrappers → 2 toffees → **2 wrappers** (can't exchange anymore)
- Total = 50 + 16 + 6 + 2 = **74 toffees**.

This is a **loop** — repeat "exchange" until the condition (`wrappers >= 3`) fails,
while tracking the leftover wrappers each round.

```python
money = 50
toffees = money          # buy 50 toffees with 50 rs
wrappers = toffees       # after eating them you have 50 wrappers

while wrappers >= 3:
    new = wrappers // 3            # how many toffees we can exchange for
    toffees += new                 # eat them, count them
    wrappers = wrappers % 3 + new  # leftover wrappers + the new ones

print(toffees)  # 74
```

---

### Q3. Eight coins, find the lighter one → max 2 comparisons

**Problem:** 8 identical-looking coins, 7 weigh the same, 1 is slightly lighter.
Using only a balance scale, find the odd coin in the **fewest** comparisons.

**Logic (answer = 2 comparisons):** split into groups of **3, 3, 2**.

1. **Weigh 3 vs 3.**
   - **If they balance** → the lighter coin is in the leftover group of 2.
     Weigh those 2 against each other → the lighter side is the odd coin. *(2 weighings)*
   - **If one side is lighter** → the odd coin is in that group of 3.
2. **From the lighter group of 3, weigh 1 vs 1.**
   - If one is lighter → that's it.
   - If they balance → it's the third coin you didn't weigh. *(2 weighings)*

> Idea: splitting into 3 shrinks the search faster than checking one-by-one.
> This is the seed of **binary search** and **divide & conquer** later in the course.

---

### Q4. Two eggs, 100 floors → use sqrt of the floors

**Problem:** Find the highest floor an egg can be dropped from without breaking.
You have 2 eggs. If an egg survives a floor, it survives every floor below;
if it breaks, it breaks on every floor above.

**Logic (the √n strategy):**
- √100 = 10, so drop the **first egg** every **10 floors**: 10, 20, 30, … , 100.
- The moment the first egg **breaks** (say at floor 40), the answer is somewhere in
  the previous 9 floors (31–39).
- Now use the **second egg** to test those floors **one at a time**, going up,
  until it breaks. The last safe floor is the answer.
- **Worst case** = 10 jumps (first egg) + 9 single steps (second egg) = **19 drops**.

```python
from math import floor, sqrt

floors = 100
step = floor(sqrt(floors))  # 10 -> drop first egg at 10, 20, 30, ...

first_egg_drops = list(range(step, floors + 1, step))
print(first_egg_drops)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

worst_case = floors // step + (step - 1)
print(worst_case)  # 19
```

> Idea: we are minimizing the **worst case**, trading off two strategies.
> That mindset is the start of complexity analysis.

---

## Part 2 — Pattern Printing

> See [`patterns.py`](patterns.py) for all of these as runnable functions.

### Pattern 1 — Left triangle (for given n)
```
*
**
***
```
```python
for i in range(1, n + 1):
    print("*" * i)
```

### Pattern 2 — Inverted left triangle (bottoms up)
```
***
**
*
```
```python
for i in range(n, 0, -1):
    print("*" * i)
```

### Pattern 3 — Right-aligned triangle
```
  *
 **
***
```
```python
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
```

### Pattern 4 — Pyramid
```
  *
 ***
*****
```
```python
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

### Pattern 5 — Rhombus (pyramid top + bottom combined)
```
  *
 ***
*****
 ***
  *
```
```python
for i in range(1, n + 1):                 # top half (includes middle)
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):             # bottom half
    print(" " * (n - i) + "*" * (2 * i - 1))
```

### Pattern 6 — Hollow rectangle (n rows × m columns)
Only the border is `*`, the inside is blank.
```
*****
*   *
*****
```
```python
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

---

## Part 3 — Swapping Two Numbers

> See [`swapping.py`](swapping.py).

**Method 1 — using an extra variable**
```python
temp = a
a = b
b = temp
```

**Method 2 — arithmetic (no extra variable)**
```python
a = a + b
b = a - b
a = a - b
```

**Method 3 — XOR (no extra variable)**
```python
a = a ^ b
b = a ^ b
a = a ^ b
```

**Method 4 — tuple unpacking (the Pythonic way)**
```python
a, b = b, a
```

---

## Part 4 — `range()`

`range(start, stop, step)` generates numbers from `start` up to **but not including** `stop`.

- `range(5)` → 0, 1, 2, 3, 4  *(start defaults to 0)*
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(1, 10, 2)` → 1, 3, 5, 7, 9  *(step = 2)*
- `range(5, 0, -1)` → 5, 4, 3, 2, 1  *(counting down)*

This is why a factorial loop is `range(1, n + 1)` — to actually include `n`.

---

## Part 5 — Number Problems

### Q. Sum of all natural numbers till n
> [`sum_natural.py`](sum_natural.py)
```python
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# or directly:  n * (n + 1) // 2
```

### Q. Factorial of n
> [`factorial.py`](factorial.py)
```python
ans = 1
for i in range(1, n + 1):
    ans = ans * i
print(ans)
```

### Q. Number of digits — 3 methods
> [`count_digits.py`](count_digits.py). Example: `4342 → 4`

```python
from math import floor, log10

# Method 1: floor division
count = 0
temp = n
while temp > 0:
    temp = temp // 10
    count += 1

# Method 2: log10
floor(log10(n)) + 1

# Method 3: trick
len(str(n))
```

### Q. Sum of all digits
> [`sum_digits.py`](sum_digits.py). Example: `4342 → 13`
```python
total = 0
while n > 0:
    total += n % 10   # last digit
    n = n // 10       # drop the last digit
print(total)
```

### Q. Reverse the number
> [`reverse_number.py`](reverse_number.py). Example: `4342 → 2434`
```python
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)
```

### Q. Strong number
> [`strong_number.py`](strong_number.py). A number whose digits' factorials sum to itself.
> Example: `145 = 1! + 4! + 5! = 1 + 24 + 120 = 145`
```python
total = 0
while n > 0:
    digit = n % 10
    total += factorial(digit)
    n = n // 10
# strong if total == original number
```

### Q. Prime number check
> [`prime_check.py`](prime_check.py). Only loop till `sqrt(n)`:
> if `n = a * b`, one of `a` or `b` must be `<= sqrt(n)`, so checking up to
> `sqrt(n)` is enough.
```python
from math import floor, sqrt

is_prime = n >= 2
for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break
```

### Q. All factors of a number
> [`factors.py`](factors.py). Loop till `sqrt(n)`: if `i` divides `n`, then `n // i`
> is also a factor. Edge case: for a **perfect square**, `i` and `n // i` are equal,
> so add it only once.
```python
from math import floor, sqrt

factors = []
for i in range(1, floor(sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:          # avoid duplicate for perfect squares
            factors.append(n // i)
factors.sort()
```
