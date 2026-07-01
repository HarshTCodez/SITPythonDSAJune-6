# Day 7 — 2D Arrays & String Fundamentals

Two themes today: navigating a grid (row, column, diagonal, spiral) and digit-level string arithmetic.
The grid problems build on each other — each new traversal pattern is one idea added to the last.

---

## Part 0 — Homework Review: Koko Eating Bananas

> [`../day_06/koko_eating.py`](../day_06/koko_eating.py)

**Problem:** Koko can eat `k` bananas per hour. Given `piles[]` and `h` hours, find the minimum `k` such that she finishes all piles in time. (LC 875)

**Insight:** The answer is somewhere in `[1, max(piles)]`. For any candidate speed `k`, you can check feasibility in O(n) using `ceil(pile / k)` per pile. The feasibility check is monotone — if speed `k` works, any speed `> k` also works. That's the binary search signal.

**Approach: Binary search on the answer space**

```python
from math import ceil

def can_eat(piles, h, k):
    return sum(ceil(x / k) for x in piles) <= h

def minEatingSpeed(piles, h):
    low, high = 1, max(piles)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_eat(piles, h, mid):
            ans = mid       # mid works — try slower
            high = mid - 1
        else:
            low = mid + 1   # mid too slow — must eat faster

    return ans
```

**Trace — `piles=[3,6,7,11], h=8`:**

```
low=1,  high=11, mid=6:  ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6 ≤ 8  → ans=6,  high=5
low=1,  high=5,  mid=3:  1+2+3+4 = 10 > 8                                              → low=4
low=4,  high=5,  mid=4:  1+2+2+3 = 8  ≤ 8                                              → ans=4,  high=3
low=4 > high=3 → return ans=4 ✓
```

**Key idea:** The search space is the *answer domain*, not the input array. Any time you can write a monotone `can_X(value)` check, binary search on value finds the minimum/maximum.

---

## Part 1 — 2D List Basics: Row-wise & Column-wise Traversal

> [`traversal.py`](traversal.py)

A 2D list in Python is a list of rows. `matrix[i][j]` — `i` is the row index, `j` is the column index.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rows = len(matrix)       # 3
cols = len(matrix[0])    # 3
```

**Row-wise (left → right, top → bottom):**

```python
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
```

```
1 2 3
4 5 6
7 8 9
```

**Column-wise (top → bottom, left → right):**

```python
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
```

```
1 4 7
2 5 8
3 6 9
```

**Key idea:** Swap the loop order, nothing else changes. The outer loop picks *which column*, the inner loop walks *down that column*.

---

## Part 2 — Richest Customer Wealth

> [`richest_wealth.py`](richest_wealth.py)

**Problem:** `accounts[i][j]` is the money customer `i` has in bank `j`. Return the wealth of the richest customer. (LC 1672)

**Insight:** Wealth of customer `i` = sum of row `i`. Return the row-sum maximum.

```python
def maximumWealth(accounts):
    return max(sum(row) for row in accounts)
```

**Trace — `accounts=[[1,2,3],[3,2,1]]`:**

```
row 0: 1+2+3 = 6
row 1: 3+2+1 = 6
max(6, 6) = 6 ✓
```

---

## Part 3 — Convert 1D Array into 2D Array

> [`convert_1d_to_2d.py`](convert_1d_to_2d.py)

**Problem:** Reshape a 1D array `original` into an `m × n` 2D array. Return `[]` if impossible. (LC 2022)

**Insight:** Only possible when `m * n == len(original)`. Fill row by row — row `i` gets elements `[i*n .. i*n+n)`.

```python
def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []

    result = []
    for i in range(m):
        result.append(original[i * n : i * n + n])
    return result
```

**Trace — `original=[1,2,3,4], m=2, n=2`:**

```
i=0: original[0:2] = [1, 2]
i=1: original[2:4] = [3, 4]
result = [[1,2],[3,4]] ✓
```

**Key idea:** Element at flat index `k` maps to row `k // n`, column `k % n`. Slicing is just that in bulk.

---

## Part 4 — Search in a 2D Sorted Matrix

> [`search_2d_matrix.py`](search_2d_matrix.py)

Two sorted-matrix problems that look similar but need different techniques.

---

### 4a — Search a 2D Matrix (LC 74)

**Problem:** Each row is sorted left to right. The first element of each row is greater than the last element of the previous row. Return whether `target` exists.

**Insight:** The matrix is *fully* sorted — if you read it row by row it's one long sorted sequence. Treat it as a 1D array of length `m * n` and do a single binary search. Flat index `k` maps to `row = k // n`, `col = k % n`.

```python
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
```

**Trace — `matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3`:**

```
low=0, high=11, mid=5 → matrix[1][1]=11 > 3  → high=4
low=0, high=4,  mid=2 → matrix[0][2]=5  > 3  → high=1
low=0, high=1,  mid=0 → matrix[0][0]=1  < 3  → low=1
low=1, high=1,  mid=1 → matrix[0][1]=3  == 3 → True ✓
```

---

### 4b — Search a 2D Matrix II (LC 240)

**Problem:** Each row is sorted left to right, each column is sorted top to bottom. Rows do NOT need to connect. Return whether `target` exists.

**Insight:** Start at the **top-right corner**. From there:
- The value is the largest in its row → moving left only decreases it.
- The value is the smallest in its column → moving down only increases it.

So at each step you can eliminate an entire row or column.

```python
def searchMatrixII(matrix, target):
    r, c = 0, len(matrix[0]) - 1   # start at top-right

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1      # too big — eliminate this column
        else:
            r += 1      # too small — eliminate this row

    return False
```

**Trace — `matrix=[[1,4,7],[2,5,8],[3,6,9]], target=5`:**

```
r=0, c=2: val=7  > 5 → c=1
r=0, c=1: val=4  < 5 → r=1
r=1, c=1: val=5 == 5 → True ✓
```

**Why not binary search here?** The matrix isn't globally sorted — element `(0, n-1)` could be smaller or larger than `(1, 0)`. The staircase is O(m+n) but that's optimal for this structure.

**4a vs 4b at a glance:**

| | LC 74 | LC 240 |
|---|---|---|
| Row-to-row connection | Yes (fully sorted) | No |
| Technique | Binary search (1D view) | Staircase from top-right |
| Complexity | O(log mn) | O(m + n) |

---

## Part 5 — Diagonal Traversal (One Direction)

> [`diagonal_one_direction.py`](diagonal_one_direction.py)


**Setup:** Every cell `(i, j)` where `i + j == d` belongs to the same anti-diagonal `d`. For an `m × n` matrix there are `m + n - 1` anti-diagonals.

**Approach:** Iterate `d` from `0` to `m+n-2`. For each `d`, walk row `i` from `0` to `m-1` and compute `j = d - i`. Skip any `(i, j)` that falls outside the grid.

```python
def diagonal_traverse_one_dir(matrix):
    m, n = len(matrix), len(matrix[0])
    result = []

    for d in range(m + n - 1):
        for i in range(m):
            j = d - i
            if 0 <= j < n:
                result.append(matrix[i][j])

    return result
```

**Trace — `matrix=[[1,2,3],[4,5,6],[7,8,9]]`:**

```
d=0: (0,0)→1
d=1: (0,1)→2  (1,0)→4
d=2: (0,2)→3  (1,1)→5  (2,0)→7
d=3:           (1,2)→6  (2,1)→8
d=4:                    (2,2)→9

Result: [1, 2, 4, 3, 5, 7, 6, 8, 9]
```

**Key idea:** `i + j = d` is the grouping invariant. Holding `d` fixed and varying `i` is all you need to enumerate a diagonal. Direction within the diagonal is controlled by whether `i` runs forward or backward — next problem uses that.

---

## Part 6 — Diagonal Traverse (Alternating Direction)

> [`diagonal_traverse.py`](diagonal_traverse.py)

**Problem:** Same anti-diagonal grouping, but even diagonals go up-right and odd diagonals go down-left. (LC 498)

**Approach:** Same `d` loop. For even `d`, start at the bottom of the diagonal (`i = min(d, m-1)`) and move up (`i--`, `j++`). For odd `d`, start at the right (`j = min(d, n-1)`) and move down (`i++`, `j--`).

```python
def findDiagonalOrder(mat):
    m, n = len(mat), len(mat[0])
    result = []

    for d in range(m + n - 1):
        if d % 2 == 0:          # up-right
            i = min(d, m - 1)
            j = d - i
            while i >= 0 and j < n:
                result.append(mat[i][j])
                i -= 1
                j += 1
        else:                   # down-left
            j = min(d, n - 1)
            i = d - j
            while i < m and j >= 0:
                result.append(mat[i][j])
                i += 1
                j -= 1

    return result
```

**Trace — `mat=[[1,2,3],[4,5,6],[7,8,9]]`:**

```
d=0 (even,  ↗): (0,0)→1
d=1 (odd,   ↙): (0,1)→2  (1,0)→4
d=2 (even,  ↗): (2,0)→7  (1,1)→5  (0,2)→3
d=3 (odd,   ↙): (1,2)→6  (2,1)→8
d=4 (even,  ↗): (2,2)→9

Result: [1, 2, 4, 7, 5, 3, 6, 8, 9] ✓
```

**vs Part 5:** The only change is the starting corner and step direction inside the diagonal. The outer loop structure is identical.

---

## Part 7 — Spiral Matrix

> [`spiral_matrix.py`](spiral_matrix.py)

**Problem:** Return all elements of an `m × n` matrix in spiral order (clockwise from the top-left). (LC 54)

**Approach: Shrinking boundary** — maintain four pointers `top`, `bottom`, `left`, `right`. Each pass peels one layer: go right along top, down along right, left along bottom, up along left. Shrink the corresponding boundary after each pass.

```python
def spiralOrder(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):        # → along top row
            result.append(matrix[top][j])
        top += 1

        for i in range(top, bottom + 1):        # ↓ along right column
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:                        # ← along bottom row (guard: still rows left)
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:                        # ↑ along left column (guard: still cols left)
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

**Trace — `matrix=[[1,2,3],[4,5,6],[7,8,9]]`:**

```
top=0,bottom=2,left=0,right=2
→ top row:    1 2 3   (top → 1)
↓ right col:  6 9     (right → 1)
← bottom row: 8 7     (bottom → 1)
↑ left col:   4       (left → 1)

top=1,bottom=1,left=1,right=1
→ top row:    5       (top → 2)
top(2) > bottom(1) → stop

Result: [1, 2, 3, 6, 9, 8, 7, 4, 5] ✓
```

**Why the guards?** After shrinking `top` and `right`, you might have consumed all rows or columns. Without the guards, the bottom-row and left-column passes would double-count corner elements.

---

## Part 8 — String Basics: Palindrome Check

> [`palindrome.py`](palindrome.py)

**Problem:** Return `True` if a string reads the same forwards and backwards.

**Approach: Two pointers** — one at each end, walk inward. If they ever disagree, return `False`.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Trace — `s="racecar"`:**

```
l=0,r=6: 'r'=='r' ✓
l=1,r=5: 'a'=='a' ✓
l=2,r=4: 'c'=='c' ✓
l=3,r=3: left >= right → True ✓
```

**Key idea:** You never need to build the reversed string. The two-pointer pattern checks agreement from the outside in, stopping as soon as there's a mismatch.

---

## Part 9 — Add Strings

> [`add_strings.py`](add_strings.py)

**Problem:** Given two non-negative integers as strings `num1` and `num2`, return their sum as a string — without converting to `int`. (LC 415)

**Insight:** Simulate column addition right-to-left. Extract digit values with `ord(ch) - ord('0')`. Track carry. Collect digits in a list and reverse at the end.

```python
def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        a = ord(num1[i]) - ord('0') if i >= 0 else 0
        b = ord(num2[j]) - ord('0') if j >= 0 else 0
        total = a + b + carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1

    return ''.join(reversed(result))
```

**Trace — `num1="11", num2="123"`:**

```
i=1, j=2: a=1, b=3, total=4, carry=0 → result=['4']
i=0, j=1: a=1, b=2, total=3, carry=0 → result=['4','3']
i=-1,j=0: a=0, b=1, total=1, carry=0 → result=['4','3','1']
i=-1,j=-1, carry=0 → stop

reversed → ['1','3','4'] → "134" ✓
```

**Why `ord(ch) - ord('0')`?** ASCII value of `'0'` is 48, `'9'` is 57. Subtracting `ord('0')` converts the character to its integer digit without using `int()`.

---

## Teaching Order & Summary

| #   | Problem                     | File                        | Core Idea                                          |
| --- | --------------------------- | --------------------------- | -------------------------------------------------- |
| 0   | Koko Eating Bananas         | `../day_06/koko_eating.py`  | Binary search on answer space (homework review)    |
| 1   | 2D Traversal Basics         | `traversal.py`              | Row-wise vs column-wise — swap loop order          |
| 2   | Richest Customer Wealth     | `richest_wealth.py`         | Sum each row, take max                             |
| 3   | Convert 1D Array to 2D      | `convert_1d_to_2d.py`       | Flat index k → row k//n, col k%n                  |
| 4a  | Search a 2D Matrix          | `search_2d_matrix.py`       | Fully sorted → binary search (1D view)             |
| 4b  | Search a 2D Matrix II       | `search_2d_matrix.py`       | Row+col sorted → staircase from top-right          |
| 5   | Diagonal Traversal (1 dir)  | `diagonal_one_direction.py` | Group by i+j=d, always walk i forward              |
| 6   | Diagonal Traverse (LC 498)  | `diagonal_traverse.py`      | Same grouping, flip direction per diagonal         |
| 7   | Spiral Matrix               | `spiral_matrix.py`          | Shrinking boundary — peel one layer per iteration  |
| 8   | Palindrome Check            | `palindrome.py`             | Two pointers from both ends                        |
| 9   | Add Strings                 | `add_strings.py`            | Column addition with carry, ord() for digit value  |
