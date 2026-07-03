# Day 10 — From Recursion to Backtracking: Counting Paths & Building Combinations

Lesson plan: [`../../day10.md`](../../day10.md). This README documents what actually landed in this folder — real files,
where they matched the plan, where they went further than planned, and one gotcha worth knowing about.

**Status:** everything in the plan got built, several parts got *more* coverage than planned (two extra maze-counting styles,
a bonus obstacles+diagonal combo, and a base-4 branching generalization). No open homework this time.

---

## Parts 1–3 — Power Function: Naive, Negative, and Half-Half — All in One

> [`lc_50.py`](lc_50.py)

The plan called for three separate passes (naive → negative → half-half). In practice they landed as one combined function:

```python
def power(x: float, n: int):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    half = power(x, n // 2)
    ans = half * half
    if n % 2 == 1:
        ans *= x
    return ans
```

Worth confirming out loud in review: `half` is computed **once** and reused for `half * half` — this is exactly the bug the
lesson plan flagged as the classic mistake (calling `power(x, n // 2)` twice, which silently degrades back to O(n)). It wasn't
made here — good sign the "compute it once" warning landed.

---

## Part 4 — Binary Search Using Recursion

> [`binary_search_recursion.py`](binary_search_recursion.py)

```python
def binary_search(arr: list, low: int, high: int, target: int):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)
```

The demo call searches for `target=1` in `[2, 3, 4, 6, 8, 10, 12, 14]` — a value that **isn't** in the array — so the first
thing this prints is the `-1` / not-found path, not a match. Good instinct to demo the negative case first rather than only
ever showing the happy path.

---

## Part 5 — Maze Paths, Diagonal Included

> [`maze.py`](maze.py) (print) · [`cout_maze.py`](cout_maze.py) & [`count_maze_1.py`](count_maze_1.py) (count, two styles) ·
> [`count_maze_2.py`](count_maze_2.py) (count + obstacles, bonus)

The plain 2-choice version from the lesson plan was skipped in favor of going straight to the diagonal-move version — which is
actually the Day 9 "add diagonal as homework" extension, done immediately instead of separately:

```python
def maze(start_row, start_col, end_row, end_col, ans=""):
    if start_row > end_row:
        return
    if start_col > end_col:
        return
    if start_row == end_row and start_col == end_col:
        print(ans)
        return
    maze(start_row + 1, start_col, end_row, end_col, ans + "D")        # down
    maze(start_row + 1, start_col + 1, end_row, end_col, ans + "S")    # diagonal
    maze(start_row, start_col + 1, end_row, end_col, ans + "R")        # right
```

Still exactly "trust me bro" style — all three moves fire unconditionally, and the two `> end_row` / `> end_col` checks are the
out-of-bounds base case doing the rejecting, no guards at the call sites. (Note the parameterization is `end_row`/`end_col`
— the actual target coordinates — rather than `n`/`m` dimensions like the plan's version; equivalent idea, just measuring the
boundary directly instead of via grid size.)

**Two different styles for "count instead of print" showed up, which is worth teaching as a deliberate pair** (same spirit as
Day 9's two sum-accumulator styles):

- `cout_maze.py` — **return-based accumulation**: each call returns an int, and the three branches are summed and returned
  (`return down + diagonally + right`).
- `count_maze_1.py` — **global side-effect counter**: a module-level `total_count` is incremented at the destination base case
  instead of anything being returned.

**Bonus, beyond the plan:** `count_maze_2.py` combines the counting maze with an obstacles grid — effectively "Unique Paths II,
but with diagonal moves and printing," built independently of the `lc_63.py` exercise below. Good extra rep of the same
"reject in the base case" idea (`if obstacles[start_row][start_col] == 1: return`) applied a second time in a different shape.

---

## Part 6 — Unique Paths (LC 62)

> [`lc_62.py`](lc_62.py)

```python
def maze(n: int, m: int, i=0, j=0):
    if i == n or m == j:
        return 0
    if i == n - 1 and j == m - 1:
        return 1
    down = maze(n, m, i + 1, j)
    right = maze(n, m, i, j + 1)
    return down + right
```

Matches the plan exactly — naive recursion, no memoization yet. Memoizing this (cache on `(i, j)`) is still the natural next
step whenever DP gets introduced.

---

## Part 7 — Unique Paths II (LC 63)

> [`lc_63.py`](lc_63.py)

```python
def maze(matrix: list[list[int]], i=0, j=0):
    if i == len(matrix) or j == len(matrix[0]):
        return 0
    if matrix[i][j] == 1:
        return 0
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return 1
    return maze(matrix, i + 1, j) + maze(matrix, i, j + 1)
```

Obstacle check is its own base case, exactly as planned — no special-casing needed for a blocked start or destination cell,
since the very first call just falls straight into that check and returns 0.

---

## Part 8 — Generate Parentheses (LC 22)

> [`lc_22.py`](lc_22.py)

```python
def generateParenthesis(self, n: int) -> List[str]:
    res = []

    def gen(n: int, open_count: int, close_count: int, ans=""):
        if close_count > open_count:
            return
        if open_count > n:
            return
        if open_count == close_count == n:
            res.append(ans)
            return
        gen(n, open_count + 1, close_count, ans + "(")
        gen(n, open_count, close_count + 1, ans + ")")

    gen(n, 0, 0)
    return res
```

Matches the plan's pruning logic precisely — `close_count > open_count` and `open_count > n` cut off invalid branches before
they're ever built, so every leaf that's reached is already a valid combination. Written as a closure over `res` rather than
threading a list parameter through — a clean way to avoid a mutable-default-argument accumulator.

---

## Part 9 — Letter Combinations of a Phone Number (LC 17)

> [`lc_17.py`](lc_17.py)

```python
def letterCombinations(self, digits: str) -> List[str]:
    result = []

    def cross(curr_index, strs: list, ans=""):
        if curr_index == len(strs):
            result.append(ans)
            return
        for ch in strs[curr_index]:
            cross(curr_index + 1, strs, ans + ch)

    def gen(digits: str):
        res_strs = []
        for digit in digits:
            res_strs.append(DIGIT_TO_LETTERS[digit])
        cross(0, res_strs)

    gen(digits)
    return result
```

Same loop-over-choices shape as Day 9's `dice_rolls`, as planned. `gen` pre-builds the list of letter-groups for the given
digit string, then `cross` does the actual index-by-index branching over whichever group is at the current position.

---

## Part 10 — Lexicographical Order (LC 386)

> [`lc_386.py`](lc_386.py)

```python
def gen(n: int, k: int = 0, res=[]):
    if k > n:
        return
    res.append(k)
    for i in range(10):
        gen(n, k * 10 + i, res)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            gen(n, i, res)
        return res
```

Sidesteps the plan's "skip appending 0" special case entirely by starting the outer loop at `1` instead of calling `gen(n, 0)`
— arguably cleaner than the version sketched in the lesson plan. Traced against `lexicalOrder(13)`, it correctly produces
`[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`.

**Worth knowing (not currently a bug):** `gen`'s `res=[]` default argument is Python's classic mutable-default-argument
gotcha — if `gen` were ever called without explicitly passing `res` (as `Solution.lexicalOrder` currently always does), the
same list would silently accumulate across calls. Correct today because every call site passes `res` explicitly; worth a
one-line mention if this pattern comes up again, since it's an easy way to introduce a hard-to-spot bug later.

---

## Extra Material Beyond the Plan

> [`binary.py`](binary.py)

```python
def binary_numbers(n: int, ans=""):
    if n == 0:
        print(ans)
        return
    for i in range(4):
        binary_numbers(n - 1, ans + str(i))
```

Despite the name, this generates base-**4** strings (digits `0`–`3`), not binary — a further generalization of Day 9's
`dice_rolls`/`binary_numbers` (2-way and 6-way) to a 4-way branch, reinforcing that the number of choices in the loop is the
only thing that changes. Good extra rep of Part 9's "loop over choices" idea; not part of the original plan.

---

## Summary

| # | Topic                              | File(s)                                          | Status |
|---|---------------------------------------|---------------------------------------------------|--------|
| 0 | Decision tree review ("ghi")        | — (board exercise)                                | Done — no file |
| 1–3 | `pow(x,n)` — naive, negative, half-half | `lc_50.py`                                    | Done — combined into one function |
| 4 | Recursive binary search             | `binary_search_recursion.py`                      | Done |
| 5 | Maze paths (print + count, +diagonal) | `maze.py`, `cout_maze.py`, `count_maze_1.py`, `count_maze_2.py` | Done — more coverage than planned |
| 6 | Unique Paths (LC 62)                | `lc_62.py`                                        | Done — memoization still open for later |
| 7 | Unique Paths II (LC 63)             | `lc_63.py`                                        | Done |
| 8 | Generate Parentheses (LC 22)        | `lc_22.py`                                        | Done |
| 9 | Phone Letters (LC 17)               | `lc_17.py`                                        | Done |
| 10 | Lexicographical Order (LC 386)     | `lc_386.py`                                       | Done |
| — | Base-4 branching generalization     | `binary.py`                                       | Bonus, beyond plan |
