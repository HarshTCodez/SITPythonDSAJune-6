# Day 6 — Binary Search on Structure & Answer Space

All problems today are binary search, but the array isn't always sorted in the classic sense.
The skill being built: **figure out which half to eliminate** — even when the structure is unusual.

---

## Part 1 — Trapping Rain Water

> [`trapping_rain_water.py`](trapping_rain_water.py)

**Problem:** Given an elevation map `height[]`, compute total trapped water. (LC 42) — _Homework from Day 5._

**Insight:** Water above bar `i` = `min(tallest bar to its left, tallest bar to its right) - height[i]`.
If that value is negative (bar is taller than both walls), no water sits on it.

**Approach: Prefix max + suffix max arrays**

```python
def trap(height):
    n = len(height)

    left = [] + height
    right = [] + height

    for i in range(1, n):                  # left[i] = max height from 0 to i
        left[i] = max(left[i], left[i - 1])

    for i in range(n - 2, -1, -1):         # right[i] = max height from i to n-1
        right[i] = max(right[i], right[i + 1])

    ans = 0
    for i in range(1, n - 1):              # skip the first and last bars (no walls)
        water = min(left[i - 1], right[i + 1]) - height[i]
        if water > 0:
            ans += water

    return ans
```

**Trace — `height=[0,1,0,2,1,0,1,3,2,1,2,1]`:**

```
left  = [0,1,1,2,2,2,2,3,3,3,3,3]
right = [3,3,3,3,3,3,3,3,2,2,2,1]

i=1: min(left[0]=0, right[2]=3) - 1 = 0-1 → no water
i=2: min(left[1]=1, right[3]=3) - 0 = 1   → +1
i=3: min(left[2]=1, right[4]=3) - 2 = -1  → no water
i=4: min(left[3]=2, right[5]=3) - 1 = 1   → +1
i=5: min(left[4]=2, right[6]=3) - 0 = 2   → +2
i=6: min(left[5]=2, right[7]=3) - 1 = 1   → +1
...
Total = 6 ✓
```

**Note:** `left[i-1]` is the max height **strictly to the left of i** (not including i itself). Same for `right[i+1]`. That's why we offset by 1 — the bar at i can't act as its own wall.

---

## Part 2 — Lower Bound

> [`lower_bound.py`](lower_bound.py)

**Definition:** The first index where `arr[i] >= target`. If no such index exists, return `n` (past the end).

```python
def lower_bound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n             # default: target is larger than everything

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid   # potential answer — but a smaller index might also work
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

**Trace — `arr=[1,2,3,4,5,10,20], target=4`:**

```
low=0, high=6, mid=3(4) → 4>=4 → ans=3, high=2
low=0, high=2, mid=1(2) → 2< 4 → low=2
low=2, high=2, mid=2(3) → 3< 4 → low=3
low=3 > high=2 → return ans=3 ✓
```

**Key idea:** When `arr[mid] >= target`, record it as a candidate but keep searching left — there might be an earlier position that also satisfies the condition.

---

## Part 3 — Upper Bound

> [`upper_bound.py`](upper_bound.py)

**Definition:** The first index where `arr[i] > target`. If no such index exists, return `n`.

```python
def upper_bound(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

**Trace — `arr=[1,2,3,40,40,40,100], target=40`:**

```
low=0, high=6, mid=3(40) → 40 not > 40 → low=4
low=4, high=6, mid=5(40) → 40 not > 40 → low=6
low=6, high=6, mid=6(100) → 100>40 → ans=6, high=5
low=6 > high=5 → return ans=6 ✓
```

**The only difference from lower bound:** `>` instead of `>=`.

**Why both matter together:**

- `upper_bound(arr, x) - lower_bound(arr, x)` = count of occurrences of `x`.
- `lower_bound` gives the correct insert position to keep the array sorted.

---

## Part 4 — First and Last Occurrence

> [`first_and_last_occurance.py`](first_and_last_occurance.py)

**Problem:** Given a sorted array, return `[first_index, last_index]` of `target`. Return `[-1, -1]` if not found. (LC 34)

**Insight:** First occurrence = `lower_bound`. Last occurrence = `upper_bound - 1`.

```python
def searchRange(nums, target):
    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target)

    n = len(nums)

    if lower == n:               # lower_bound returned past-the-end → not found
        return [-1, -1]
    if nums[lower] != target:    # lower_bound landed on a bigger element → not found
        return [-1, -1]

    return [lower, upper - 1]
```

**Trace — `nums=[1,3,3,3,5,7], target=3`:**

```
lower_bound → index 1  (first position where arr[i] >= 3, and arr[1]=3 ✓)
upper_bound → index 4  (first position where arr[i] > 3)
last = upper - 1 = 3

Result: [1, 3] ✓
```

**The two guards:**

- `lower == n` — every element is smaller than target; it doesn't exist.
- `nums[lower] != target` — lower_bound landed on a larger element; target doesn't exist.

---

## Part 5 — Peak Index in a Mountain Array

> [`mountain_peak.py`](mountain_peak.py)

**Problem:** A mountain array strictly rises then strictly falls. Find the peak index. (LC 852)

**Insight:** At any `mid`, compare `arr[mid]` with `arr[mid+1]`:

- `arr[mid] > arr[mid+1]` → you're on the downslope. Peak is here or to the left.
- `arr[mid] < arr[mid+1]` → you're on the upslope. Peak is to the right.

```python
def peakIndexInMountainArray(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

**Trace — `arr=[1,3,8,5,2]`:**

```
low=0, high=4, mid=2(8) → 8>5 → ans=2, high=1
low=0, high=1, mid=0(1) → 1<3 → low=1
low=1, high=1, mid=1(3) → 3<8 → low=2
low=2 > high=1 → return ans=2 ✓
```

This is binary search on a **comparison with the neighbour**, not on the value itself — same idea the rotated array problems build on next.

---

## Part 6 — Find Minimum in Rotated Sorted Array I

> [`find_min_rotated.py`](find_min_rotated.py)

**Problem:** Find the minimum element in a rotated sorted array (no duplicates). (LC 153)

**Example:** `[4,5,6,7,0,1,2]` — the minimum `0` is at the rotation point.

**Key insight:** One of the two halves around `mid` is always fully sorted. The minimum of the fully sorted half is its leftmost element — record it, then search the _other_ half (which contains the rotation point).

```python
def findMin(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[high]:       # this whole segment is sorted
            ans = min(arr[low], ans)    # minimum must be arr[low]
            break

        if arr[low] <= arr[mid]:        # left half [low..mid] is sorted
            ans = min(arr[low], ans)    # record its minimum
            low = mid + 1              # rotation point is in the right half
        else:                           # right half has the rotation point
            ans = min(arr[mid], ans)    # arr[mid] might be the minimum
            high = mid - 1

    return ans
```

**Trace — `arr=[4,5,6,7,0,1,2]`:**

```
low=0, high=6, mid=3(7)
  arr[0]=4 > arr[6]=2 → not fully sorted
  arr[0]=4 <= arr[3]=7 → left half sorted, ans=4, low=4

low=4, high=6, mid=5(1)
  arr[4]=0 > arr[6]=2? No → arr[4]=0 <= arr[6]=2 → fully sorted, ans=min(4,0)=0, break

return 0 ✓
```

---

## Part 7 — Find Minimum in Rotated Sorted Array II (with duplicates)

> [`find_min_rotated_ii.py`](find_min_rotated_ii.py)

**Problem:** Same, but the array may contain duplicates. (LC 154)

When `arr[low] == arr[mid] == arr[high]`, you can't tell which half is sorted — shrink both ends by 1.

```python
def findMin(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if arr[low] == arr[mid] == arr[high]:
            ans = min(ans, arr[mid])    # might be the min — record before shrinking
            low += 1
            high -= 1
            continue

        if arr[low] <= arr[mid]:
            ans = min(arr[low], ans)
            low = mid + 1
        else:
            ans = min(arr[mid], ans)
            high = mid - 1

    return ans
```

---

## Part 8 — Search in Rotated Sorted Array I

> [`search_rotated.py`](search_rotated.py)

**Problem:** A sorted array has been rotated at an unknown pivot. Find the index of `target`. (LC 33)

**Same observation as find min:** one half is always sorted. Now use it to decide where the target could be.

```python
def search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:              # left half [low..mid] is sorted
            if arr[low] <= target <= arr[mid]:
                high = mid - 1               # target is in the sorted left half
            else:
                low = mid + 1                # target must be in the right half
        else:                                 # right half [mid..high] is sorted
            if arr[mid] <= target <= arr[high]:
                low = mid + 1                # target is in the sorted right half
            else:
                high = mid - 1               # target must be in the left half

    return -1
```

**Trace — `arr=[4,5,6,7,0,1,2], target=0`:**

```
low=0, high=6, mid=3(7)
  arr[0]=4 <= arr[3]=7 → left half sorted [4..7]
  0 not in [4..7] → low=4

low=4, high=6, mid=5(1)
  arr[4]=0 <= arr[5]=1 → left half sorted [0..1]
  0 in [0..1] → high=4

low=4, high=4, mid=4(0) → found! return 4 ✓
```

**Find min vs Search:** The logic for identifying the sorted half is identical. The difference is what you do with it — find min records the smallest and moves on; search checks if the target lives there.

---

## Part 9 — Search in Rotated Sorted Array II (with duplicates)

> [`search_rotated_ii.py`](search_rotated_ii.py)

**Problem:** Same as above, but with duplicates. Return `True/False`. (LC 81)

```python
def search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        if arr[low] == arr[mid] == arr[high]:   # can't determine sorted half
            low += 1
            high -= 1
            continue

        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
```

**Note:** The shrink step makes the worst case O(n) when all elements are duplicates. In practice still O(log n).

---

## Teaching Order & Summary

| #   | Problem                 | File                          | Core Idea                                         |
| --- | ----------------------- | ----------------------------- | ------------------------------------------------- |
| 1   | Trapping Rain Water     | `trapping_rain_water.py`      | Prefix max + suffix max (homework review)         |
| 2   | Lower Bound             | `lower_bound.py`              | First index ≥ target                              |
| 3   | Upper Bound             | `upper_bound.py`              | First index > target                              |
| 4   | First & Last Occurrence | `first_and_last_occurance.py` | lower_bound + upper_bound combined                |
| 5   | Mountain Peak           | `mountain_peak.py`            | Binary search on neighbour comparison             |
| 6   | Find Min Rotated I      | `find_min_rotated.py`         | Identify sorted half → min is its left end        |
| 7   | Find Min Rotated II     | `find_min_rotated_ii.py`      | Same + shrink on three-way tie                    |
| 8   | Search Rotated I        | `search_rotated.py`           | Same logic, now check if target is in sorted half |
| 9   | Search Rotated II       | `search_rotated_ii.py`        | Same + shrink on three-way tie                    |
