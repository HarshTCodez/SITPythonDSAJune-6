# Day 9 — Recursion: Call Stack, Base Cases & Choice Trees

Notes and lecture plan: [`../../day9.md`](../../day9.md). This README documents what actually got built in class — the files
in this folder — and calls out where a couple of live examples went off the rails, and what's still open.

**Status:** everything through the pick/not-pick subsequence pattern is done, plus more variations than originally planned
(two different accumulator styles, filtered sums, dice rolls). `pow(x, n)` and the maze paths problem were **not** reached —
they're captured in [`home_work.md`](home_work.md) as the assigned homework.

---

## Part 0 — Call Stack Basics

> [`recursion_1.py`](recursion_1.py)

Four functions (`main → c → b → a`) that just print on entry and exit, to make the stack's push/pop order visible:

```python
def a():
    print("entering a")
    print("exiting a")

def b():
    print("entering b")
    a()
    print("exiting b")
```

Output is `entering main, entering c, entering b, entering a, exiting a, exiting b, exiting c, exiting main` — the "exit" lines
unwind in the *reverse* order the "entering" lines appeared in. This is the whole call-stack mental model in eight lines.

---

## Part 1 — Order of Execution: Recurse First, Act After

> [`recursion_2.py`](recursion_2.py)

```python
def print_n(n):
    if n == 0:
        return
    print_n(n - 1)
    if n % 2 == 1:
        print(n)
```

**Nice detail worth pointing out explicitly:** `print_n(5)` prints `1, 3, 5` — in increasing order — even though the function
never sorts anything and the outer call starts at 5. That's because the recursive call happens *before* the print, so the
deepest call (`n=1`) is the first one to actually print as the stack unwinds. This is a clean, concrete follow-up to Part 0:
students can predict the output order purely from "where does the code sit relative to the recursive call," no tracing needed
once the mental model has landed.

---

## Part 2 — Factorial, With a Guard for Bad Input

> [`recursion_3.py`](recursion_3.py)

```python
def factorial(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

This is a step up from the plain textbook version: it adds `if n < 0: return` as an explicit base case for invalid input, instead
of letting a negative `n` recurse forever and blow the stack. Worth a quick note in class: `factorial(-1)` here returns `None`
silently (nothing printed, no crash) — ask students whether silently returning `None` is actually the *right* behavior, or
whether it should raise a `ValueError` instead. Either answer is defensible; the point is that "handle the invalid case in the
base case" is a deliberate design decision, not just a formality.

---

## Part 3 — Sum 1 to N, Two Different Styles

> [`recursion_3.py`](recursion_3.py) (return-based) · [`recursion_5.py`](recursion_5.py) (accumulator-based)

**Style A — build the answer on the way back up** (`recursion_3.py`):

```python
def sum_till_n(n):
    if n == 1:
        return 1
    return n + sum_till_n(n - 1)
```

**Style B — carry the answer down as a parameter, print it at the base case** (`recursion_5.py`):

```python
def sum_till_n(n: int, ans: int):
    if n == 0:
        print(ans)
        return
    sum_till_n(n - 1, ans + n)
```

This pairing is worth teaching as a deliberate contrast, even though it wasn't in the original lesson plan: Style A computes
the answer *during unwind* (nothing happens until the base case returns and the `+` chain resolves); Style B computes the
answer *on the way down* and has nothing left to do on the way back up — the base case already has the final number. Style B is
a preview of the "accumulator pattern" / tail-recursion shape that shows up constantly in later recursion and DP work.

**Known bug — good live-debugging material:** both files also have an odd-sum variant, and both are currently wrong in
different ways:

- `recursion_3.py`'s `sum_till_n_odd` recurses into `sum_till_n_even(...)` instead of `sum_till_n_odd(...)` — looks like a
  copy-paste from `sum_till_n_even` where the recursive calls didn't get renamed. `sum_till_n_odd(4)` currently returns `2`
  instead of the correct `4` (1 + 3).
- `recursion_5.py`'s `sum_till_n_odd` has the even/odd check backwards — it adds `n` to the accumulator when `n` is **even**
  and skips when `n` is **odd**, the opposite of what "sum of odd numbers" needs. `sum_till_n_odd(5, 0)` currently prints `6`
  instead of the correct `9` (1 + 3 + 5).

Left as-is for now rather than silently patched — both are genuinely useful "predict the output, then explain why it's wrong"
exercises, and `recursion_4.py`'s `sum_of_arr_odd` (below) is a working reference implementation of the same idea to compare
against once the bugs are found.

---

## Part 4 — Recursion on Arrays: Sum & Filtered Sum

> [`recursion_4.py`](recursion_4.py)

```python
def sum_of_arr(arr: list, starting_index):
    if starting_index == len(arr) - 1:
        return arr[starting_index]
    return arr[starting_index] + sum_of_arr(arr, starting_index + 1)
```

Same shape as Part 3, but reducing an **array index** instead of a plain integer — this is the array-recursion pattern that
Day 10 builds on directly. `sum_of_arr_odd` extends it by zeroing out even elements before adding — and, unlike the two buggy
`sum_till_n_odd` variants in Part 3, this one is correct: `sum_of_arr_odd([1, 7, 12, 13], 0)` correctly returns `21` (1+7+13).
Use it as the answer key when debugging Part 3's bugs.

---

## Part 5 — Fibonacci

> [`fibonacci.py`](fibonacci.py)

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)
```

Plain naive recursive version, matches the lesson plan's recursion-tree discussion (see `day9.md` Part 5 for the full tree
diagram and the overlapping-subproblem discussion). **Not yet done:** the memoized version — still a good next exercise before
moving on to Day 11, since the naive tree here visibly slows down for `fib(30)`+.

---

## Part 6 — Branching Choice Trees: Coin Toss, Binary Strings, Dice Rolls

> [`coin_toss.py`](coin_toss.py)

Three back-to-back variations on "two (or more) choices at every step," all in the same file — this is more than the original
plan called for and it's a good progression:

```python
def coin_toss(n: int, ans=""):
    if n == 0:
        print(ans)
        return
    coin_toss(n - 1, ans + "H")
    coin_toss(n - 1, ans + "T")

def binary_numbers(n: int, ans=""):
    ...
    binary_numbers(n - 1, ans + "0")
    binary_numbers(n - 1, ans + "1")

def dice_rolls(n: int, ans=""):
    ...
    for i in range(1, 7):
        dice_rolls(n - 1, ans + str(i))
```

`binary_numbers` is literally `coin_toss` relabeled (H/T → 0/1) — a good one to point out is "the same function, new alphabet."
`dice_rolls` is the natural generalization from 2-way to 6-way branching using a loop instead of two hardcoded calls, which is
itself worth a beat: "when the number of choices is fixed at 2, write two calls; when it varies, loop over the choices." That's
the bridge from hardcoded pick/not-pick into the general backtracking-with-a-loop shape used from Day 12 onward.

---

## Part 7 — Pick / Not-Pick: Subsequences

> [`coin_toss.py`](coin_toss.py) — `subseq`

```python
def subseq(myStr: str, start_index=0, ans=""):
    if start_index == len(myStr):
        print(ans)
        return
    subseq(myStr, start_index + 1, ans + myStr[start_index])
    subseq(myStr, start_index + 1, ans)
```

Run as `subseq("abc")`. Same tree shape as `coin_toss` one more time — "pick" is heads, "don't pick" is tails — worth drawing
the two trees side by side once so the connection is unmissable. `home_work.md` (q3) asks students to draw the decision tree
for `"ghi"` by hand — same code, just re-labelled letters, to confirm the pattern really did transfer and wasn't just memorized
for `"abc"`.

---

## Not Yet Done — Homework

> [`home_work.md`](home_work.md)

Two problems from the lesson plan didn't get covered in class and are assigned as homework instead:

1. **`x^n`** — e.g. `2^5 = 32`. Naive recursive version (`x * pow(x, n-1)`) is the expected first pass; see `day9.md` Part 7
   for the divide-and-conquer follow-up (`pow(x, n//2)^2`) if you want to push further once the naive version works.
2. **`x^n` with negative `n`** — e.g. `2^(-2) = 0.25`. Reduces to problem 1 plus one extra base case: compute the positive
   power, then return `1 / result`.
3. **Decision tree for `subseq("ghi")`** — draw it by hand (see Part 7 above); this is a "did the pattern actually transfer"
   check, not new code.

**Maze paths** (all paths from `(0,0)` to `(n-1, m-1)`, right/down moves only) also wasn't reached this session — see `day9.md`
Part 9 for the planned "trust me bro" approach (recurse unconditionally, reject invalid paths in an out-of-bounds base case
rather than guarding the call sites). Worth doing first thing next time, before it's forgotten — it's the last new *shape*
(fixed 2-way choice + boundary base case) before Day 12's backtracking builds directly on it.

---

## Summary

| # | Topic                              | File(s)                          | Status |
|---|--------------------------------------|-----------------------------------|--------|
| 0 | Call stack                          | `recursion_1.py`                  | Done |
| 1 | Print order via recursion           | `recursion_2.py`                  | Done |
| 2 | Factorial (+ invalid input guard)   | `recursion_3.py`                  | Done |
| 3 | Sum 1 to N — return vs. accumulator | `recursion_3.py`, `recursion_5.py` | Done — 2 known bugs in the odd-sum variants, see Part 3 |
| 4 | Recursion on arrays (sum, filtered) | `recursion_4.py`                  | Done |
| 5 | Fibonacci (naive)                   | `fibonacci.py`                    | Done — memoized version still pending |
| 6 | Coin toss / binary strings / dice   | `coin_toss.py`                    | Done — extra material beyond the original plan |
| 7 | Pick/not-pick subsequences          | `coin_toss.py` (`subseq`)         | Done |
| 8 | `pow(x, n)`, incl. negative `n`     | —                                  | **Homework** — see `home_work.md` |
| 9 | Maze paths                          | —                                  | **Not reached** — do next session |
