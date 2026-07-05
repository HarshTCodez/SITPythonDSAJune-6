# Day 11 — Grid DFS, Tower of Hanoi, and Formal Backtracking

Lesson plan: [`../../day11.md`](../../day11.md). Same as Day 10: two passes happened here — an earlier prep pass (plain
functions, script-style) and a later pass that rewrote several problems as LeetCode-ready `Solution` classes. Where both exist
under different filenames, both are kept; where a filename collided, the later `Solution`-class version replaced the prep
version (documented below with what changed). Also added, beyond the plan: a shallow-copy exploration that turns out to
motivate half of today's `.copy()` calls in the other files.

**Status:** everything in the plan got built. A couple of small code-quality nits worth knowing about are flagged inline
rather than silently fixed — same approach as Day 9's bug callouts.

---

## Part 0 — Shallow Copy: Why `path.copy()` Matters (extra, not in the plan)

> [`test.py`](test.py)

```python
x = [1]
print(id(x))
print(id(x + [2]))
print(x)
```

Small, but worth its own callout because it's the *proof* behind a pattern used everywhere else in this folder. `x + [2]`
produces a **new** list — a different `id()` — and leaves `x` untouched. That's exactly why Day 9's `subseq`/`coin_toss`
(string concatenation, `ans + "H"`) never needed an explicit undo: every recursive call got its own fresh copy for free.

Contrast that with `path.append(...)` / `path.pop()`, used everywhere in Parts 5–8 below: `append` mutates the *same* list
object in place — no new `id()`, nothing created — which is exactly why `result.append(path.copy())` (or `path[:]`) is
mandatory at the point of recording an answer. Skip the copy, and every recorded answer is really the same list reference,
which keeps changing after the fact. Worth running `id(path)` before and after an `append` vs. before and after a `path[:]`
side by side, mirroring the `x` vs. `x + [2]` demo above.

---

## Part 1 — Lexicographical Order (Two Passes)

> [`lexicographical.py`](lexicographical.py) (prep — prints, hardcoded `n=200`) · [`lc_386.py`](lc_386.py) (final — `Solution` class)

Same algorithm both times (10-way loop-branch, `current > n` as the early-reject base case). `lc_386.py` is the LeetCode-ready
version — collects into `res` and returns it instead of printing, and loops `n` as a real parameter instead of a hardcoded
test value.

---

## Part 2 — Flood Fill (LC 733) — Two Nearly Identical Passes

> [`flood_fill.py`](flood_fill.py) (prep) · [`lc_733.py`](lc_733.py) (final)

These two are close to byte-identical — same `fill` helper (out-of-bounds check, already-new-color check, wrong-original-color
check, recolor-then-recurse-in-four-directions), just with the `new_color`/`original_color` parameters swapped in order
between the two files. Both correctly recolor **before** recursing, which is what actually prevents infinite recursion —
exactly the trap called out in the lesson plan.

---

## Part 3 — Number of Islands (LC 200)

> [`lc_200.py`](lc_200.py) — replaced an earlier prep version during organizing (see note below)

**Nice detail worth teaching explicitly:** this version doesn't write a new DFS from scratch — it reuses the *exact same*
`fill` helper from Part 2, verbatim:

```python
def fill(matrix, start_row, start_col, original_color, new_color):
    ...  # identical to flood_fill.py's fill()

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    fill(grid, i, j, "1", "2")
        return ans
```

This is worth pointing out to the class directly: **Number of Islands is just Flood Fill, called once per not-yet-visited
land cell**, "flooding" every `"1"` in the region to `"2"` so it's never counted again. Framing it this way turns two separate
LeetCode problems into one idea applied twice — a nice payoff for the "same shape, different clothes" theme running through
the whole course.

**What replaced what:** the version now in this folder is the later, root-level rewrite. The earlier prep version (not kept,
since the filename collided) used an inline closure instead of reusing `fill`, marked visited cells with `"0"` instead of
`"2"`, and had a leftover `print(f"starting from {i, j}")` debug line in the loop — functionally correct, just noisier and
without the nice Flood-Fill callback the current version has.

---

## Part 4 — Tower of Hanoi (Two Passes)

> [`tower_of_hanoi.py`](tower_of_hanoi.py) (prep, `n=3`) · [`toh.py`](toh.py) (final, `n=4`)

Identical algorithm in both — only the function name and the demo call's `n` differ. Both correctly do the "move n-1 out of
the way, move the big disk, move n-1 back" sequence with no branching search tree, matching the lesson plan exactly.

---

## Interlude — Chair Example

No file for this one — it's the conceptual pivot (choose → explore → un-choose), covered live per the lesson plan. Its
payoff shows up concretely in Part 0 above and in every `.copy()` / `.pop()` call in Parts 5–8.

---

## Part 5 — Permutations (LC 46)

> [`permutations.py`](permutations.py) — replaced an earlier prep version during organizing (see note below)

```python
class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        res = []
        path = []
        visited = [False] * n

        def generate(index: int):
            if index == n:
                res.append(path.copy())
                pass
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(arr[i])
                    generate(index + 1)
                    visited[i] = False
                    path.pop()

        generate(0)
        return res
```

Correct output — the chair template (`used[i]` / `visited[i]` marks + explicit `pop()`/un-mark) is right, and `path.copy()` is
present, so answers aren't aliased (see Part 0). **One thing worth knowing:** the `if index == n:` branch appends but has no
`return` (just a stray `pass`) — it happens to be harmless here, because when `index == n` every element is already marked
`visited`, so the `for` loop right below it can't do anything (`if not visited[i]` is false for all `i`) and the function just
falls through. Still fragile — an easy thing to trip on if this gets refactored later, since nothing stops a future edit from
breaking that implicit invariant. The earlier prep version (not kept, filename collided) had an explicit `return` in the same
spot and is the safer pattern to point to if this comes up again.

---

## Part 6 — Subsets (LC 78)

> [`subsets.py`](subsets.py) — replaced an earlier prep version during organizing (see note below)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate(arr: list, start_index=0, ans=[]):
            if start_index == len(arr):
                res.append(ans.copy())
                return
            ans.append(arr[start_index])
            generate(arr, start_index + 1, ans)
            ans.pop()
            generate(arr, start_index + 1, ans)

        generate(nums, 0, [])
        return res
```

Matches the plan exactly — pick branch appends/pops, don't-pick branch does neither, which is a good one to point at directly
if anyone's still unsure why the second recursive call doesn't need its own undo (nothing was chosen on that branch).

**Worth knowing:** `generate`'s `ans=[]` default is the same mutable-default-argument pattern flagged in Day 10's
`lc_386.py`. Harmless here too, since the very first call (`generate(nums, 0, [])`) always passes an explicit empty list —
same "not a bug today, would be if called differently" caveat as before.

---

## Part 7 — Subset Sum

> [`subsets_sum.py`](subsets_sum.py) (prep — includes negative numbers) · [`subsets_with_sum.py`](subsets_with_sum.py) (later exploration)

Two different explorations here, worth treating as a pair rather than a straightforward "prep vs. final":

```python
# subsets_sum.py — tests [2, 3, 4, -1, -2] against target 8, keeps subsets with sum(ans) >= target
# subsets_with_sum.py — tests [1, 2, 3] against target 3, prints subsets with sum(ans) > target
```

**Worth flagging, not silently fixing:** the lesson plan's Part 7 asks for subsets whose sum **equals** the target, but both
files here check `>=` / `>` instead of `==`. `subsets_sum.py`'s use of a **negative-number** test array is a great catch,
though — it's a direct, hands-on version of the plan's own extra-practice question ("what changes if the array has negative
numbers?"), since the value-based pruning trick from the plan doesn't apply once numbers can be negative (a running sum can
overshoot and still come back down). Worth confirming next session whether the `>`/`>=` checks were intentional (e.g., "at
least target") or should be tightened to `==` — an easy one-line fix once the intent is confirmed.

---

## Part 8 — Combination Sum (LC 39)

> [`combination_sum.py`](combination_sum.py) — replaced an earlier prep version during organizing (see note below)

```python
class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(arr)

        def gen(curr_index: int, remaining_target: int, ans: list):
            if remaining_target < 0:
                return
            if remaining_target == 0:
                res.append(ans.copy())
                return
            for i in range(curr_index, n):
                ans.append(arr[i])
                gen(i, remaining_target - arr[i], ans)
                ans.pop()

        gen(0, target, [])
        return res
```

Different shape from the lesson plan's version, and arguably a cleaner one: instead of an explicit binary
"pick-and-stay-on-index" / "skip-and-advance-index" pair of recursive calls, this loops `for i in range(curr_index, n)` and
recurses with `gen(i, ...)` (not `i + 1`) — the loop itself naturally handles "try every remaining candidate, and allow
reusing the current one," without needing a separate skip-branch. Same reuse trick as the plan (recurse on `i`, not `i + 1`,
to allow picking the same number again), just expressed with a loop instead of two hardcoded calls — worth showing both
side by side, since it's the same "loop vs. two hardcoded branches" choice that came up with Day 9's `dice_rolls`.

---

## Summary

| # | Topic                          | File(s)                                      | Status |
|---|----------------------------------|-------------------------------------------------|--------|
| 0 | Shallow copy demo (extra)       | `test.py`                                       | Extra, beyond plan |
| 1 | Lexicographical Order (recap)   | `lexicographical.py`, `lc_386.py`               | Done — 2 passes |
| 2 | Flood Fill (LC 733)             | `flood_fill.py`, `lc_733.py`                    | Done — 2 passes, near-identical |
| 3 | Number of Islands (LC 200)      | `lc_200.py`                                     | Done — reuses Part 2's `fill` directly |
| 4 | Tower of Hanoi                  | `tower_of_hanoi.py`, `toh.py`                   | Done — 2 passes |
| 5 | Permutations (LC 46)            | `permutations.py`                               | Done — fragile missing `return`, see note |
| 6 | Subsets (LC 78)                 | `subsets.py`                                    | Done |
| 7 | Subset Sum                      | `subsets_sum.py`, `subsets_with_sum.py`         | Done — confirm `==` vs `>`/`>=` intent |
| 8 | Combination Sum (LC 39)         | `combination_sum.py`                            | Done — loop-based reuse instead of binary pick/skip |
