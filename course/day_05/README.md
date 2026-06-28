# Day 5 — Two Pointers & Binary Search

---

## Part 1 — Two Sum II (Sorted Array)

> [`lc_167.py`](lc_167.py)

**Problem:** Given a **sorted** array and a target, return the 1-based indices of the two numbers that add up to it.

**Why not the hash-map from LC 1?** The array is already sorted — we can exploit that and do it in O(1) extra space.

```python
def twoSum(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low < high:
        curr = numbers[low] + numbers[high]
        if curr == target:
            return [low + 1, high + 1]   # 1-based indices
        if curr > target:
            high -= 1    # sum too large → move right pointer left
        else:
            low += 1     # sum too small → move left pointer right

    return []
```

**Trace — `numbers=[2,7,11,15], target=9`:**
```
low=0(2),  high=3(15) → sum=17 > 9 → high--
low=0(2),  high=2(11) → sum=13 > 9 → high--
low=0(2),  high=1(7)  → sum=9 == 9 → return [1, 2] ✓
```

**Why this works:** At each step you can safely eliminate one end. If `sum < target`, moving `high` left can only make it smaller — useless. So `low` must move right. Mirror logic for `sum > target`.

---

## Part 2 — 3Sum

> [`lc_15.py`](lc_15.py)

**Problem:** Find all unique triplets that sum to zero.

**Approach:** Sort, fix one element `c`, then use Two Pointers on the rest to find pairs that sum to `-c`.

```python
def threeSum(arr):
    n = len(arr)
    ans = []
    arr.sort()

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue                          # skip duplicate fixed element

        c = arr[i]
        target = -c
        low = i + 1
        high = n - 1

        while low < high:
            curr = arr[low] + arr[high]
            if curr == target:
                ans.append([arr[i], arr[low], arr[high]])
                while low < high and arr[low] == arr[low + 1]:
                    low += 1                  # skip duplicates on the left
                low += 1
                high -= 1
            elif curr > target:
                high -= 1
            else:
                low += 1

    return ans
```

**Trace — `arr=[-4,-1,-1,0,1,2]` (after sort):**
```
i=0, c=-4, target=4:
  low=1(-1), high=5(2) → sum=1 < 4 → low++
  low=2(-1), high=5(2) → sum=1 < 4 → low++
  low=3(0),  high=5(2) → sum=2 < 4 → low++
  low=4(1),  high=5(2) → sum=3 < 4 → low++  (low not < high anymore)

i=1, c=-1, target=1:
  low=2(-1), high=5(2) → sum=1 == 1 → append [-1,-1,2]
  low=3(0),  high=4(1) → sum=1 == 1 → append [-1,0,1]

i=2: arr[2]==arr[1] → skip (duplicate)
i=3, c=0, target=0: remaining elements all positive → no valid pair

Result: [[-1,-1,2], [-1,0,1]] ✓
```

**Key ideas:**
- Sorting brings duplicates together — skipping them is a simple compare with the previous element.
- Once `arr[i] > 0`, all remaining elements are positive and can't sum to 0 — you can break early.
- Time: O(n²) — outer loop O(n), two-pointer scan O(n).

---

## Part 3 — Merge Two Sorted Arrays (New Array)

> [`merge_two_sorted.py`](merge_two_sorted.py)

**Problem:** Merge two sorted arrays into a new sorted array.

```python
def merge(arr1, arr2):
    ans = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):    # leftover from arr1
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):    # leftover from arr2
        ans.append(arr2[j])
        j += 1

    return ans
```

**Trace — `arr1=[1,3,5,7], arr2=[2,4,6,8]`:**
```
Compare 1 vs 2 → take 1
Compare 3 vs 2 → take 2
Compare 3 vs 4 → take 3
Compare 5 vs 4 → take 4
Compare 5 vs 6 → take 5
Compare 7 vs 6 → take 6
Compare 7 vs 8 → take 7
arr1 exhausted → take 8
Result: [1,2,3,4,5,6,7,8] ✓
```

Always compare the current fronts of both arrays and take the smaller one. When one array runs out, dump the rest of the other.

---

## Part 4 — Merge Sorted Array In-Place

> [`lc_88.py`](lc_88.py)

**Problem:** Merge `nums2` into `nums1` in-place. `nums1` has enough trailing zeros to hold all elements.

**Trick:** Fill from the **back** — comparing largest elements first avoids overwriting values you still need.

```python
def merge(nums1, m, nums2, n):
    i = m - 1       # last real element in nums1
    j = n - 1       # last element in nums2
    k = m + n - 1   # last slot in nums1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while i >= 0:           # leftover in nums1 (already in place, but explicit)
        nums1[k] = nums1[i]
        i -= 1
        k -= 1

    while j >= 0:           # leftover in nums2
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
```

**Trace — `nums1=[1,3,5,0,0,0] m=3, nums2=[2,4,6] n=3`:**
```
i=2(5), j=2(6), k=5 → 6>5 → nums1[5]=6, j=1, k=4
i=2(5), j=1(4), k=4 → 5>4 → nums1[4]=5, i=1, k=3
i=1(3), j=1(4), k=3 → 4>3 → nums1[3]=4, j=0, k=2
i=1(3), j=0(2), k=2 → 3>2 → nums1[2]=3, i=0, k=1
i=0(1), j=0(2), k=1 → 2>1 → nums1[1]=2, j=-1, k=0
j < 0 → loop ends, nums1[0]=1 was already there
Result: [1,2,3,4,5,6] ✓
```

Writing to slot `k` from the right never overwrites an element you haven't processed yet.

---

## Part 5 — Product of Array Except Itself

> [`lc_238.py`](lc_238.py)

**Problem:** Return an array where `output[i]` = product of all elements except `nums[i]`. No division, O(n). (LC 238)

**Approach:** Build a `prefix` array (left products) and a `postfix` array (right products), then combine.

```python
def find_prefix(arr):
    prefix = [] + arr
    for i in range(1, len(arr)):
        prefix[i] = prefix[i] * prefix[i - 1]
    return prefix

def find_postfix(arr):
    postfix = [] + arr
    for i in range(len(arr) - 2, -1, -1):
        postfix[i] = postfix[i] * postfix[i + 1]
    return postfix

def productExceptSelf(arr):
    prefix = find_prefix(arr)
    postfix = find_postfix(arr)

    ans = [] + arr
    for i in range(len(arr)):
        left  = prefix[i - 1]  if i > 0           else 1
        right = postfix[i + 1] if i < len(arr) - 1 else 1
        ans[i] = left * right

    return ans
```

**Trace — `arr=[1,2,3,4]`:**
```
prefix:  [1, 2,  6, 24]   (prefix[i] = product of arr[0..i])
postfix: [24, 24, 12, 4]  (postfix[i] = product of arr[i..n-1])

i=0: left=1 (none),      right=postfix[1]=24  → ans[0]=24
i=1: left=prefix[0]=1,   right=postfix[2]=12  → ans[1]=12
i=2: left=prefix[1]=2,   right=postfix[3]=4   → ans[2]=8
i=3: left=prefix[2]=6,   right=1 (none)       → ans[3]=6

Result: [24, 12, 8, 6] ✓
```

**Intuition:** `ans[i]` = (product of everything left of i) × (product of everything right of i). The prefix array gives the left half; the postfix array gives the right half.

---

## Part 6 — Kadane's Algorithm (Maximum Subarray)

> [`lc_53.py`](lc_53.py)

**Problem:** Find the contiguous subarray with the largest sum. (LC 53)

Two ways to think about the same decision:

### Approach 1 — Conditional reset
```python
def maxSubArray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]   # previous sum is a drag — restart
        else:
            current_sum += arr[i]  # still positive — keep extending

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
```

### Approach 2 — `max()` one-liner (same logic, cleaner)
```python
def maxSubArray(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(current_sum, max_sum)
    return max_sum
```

**Trace — `arr=[-2,1,-3,4,-1,2,1,-5,4]`:**
```
i=1: current=max(1,  -2+1)=1,   max=1
i=2: current=max(-3, 1-3)=-2,   max=1
i=3: current=max(4,  -2+4)=4,   max=4
i=4: current=max(-1, 4-1)=3,    max=4
i=5: current=max(2,  3+2)=5,    max=5
i=6: current=max(1,  5+1)=6,    max=6
i=7: current=max(-5, 6-5)=1,    max=6
i=8: current=max(4,  1+4)=5,    max=6

Result: 6  (subarray [4,-1,2,1]) ✓
```

**The key decision:** Should I extend the previous subarray, or start fresh?
- `max(arr[i], current_sum + arr[i])` answers exactly that — whichever is larger wins.
- If `current_sum` was negative, adding it only makes things worse, so `arr[i]` alone wins.

---

## Part 7 — Binary Search

> [`lc_704.py`](lc_704.py)

**Problem:** Find the index of `target` in a sorted array. Return `-1` if not found. (LC 704)

```python
def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1    # target is in the left half
        else:
            low = mid + 1     # target is in the right half

    return -1
```

**Trace — `nums=[1,3,5,7,9,11], target=7`:**
```
low=0, high=5, mid=2(5)  → 5 < 7  → low=3
low=3, high=5, mid=4(9)  → 9 > 7  → high=3
low=3, high=3, mid=3(7)  → found! → return 3 ✓
```

**Why `low <= high`?** The `=` handles the case where the answer is the single last remaining element. With `<`, you'd exit before checking it.

**Time: O(log n)** — search space halves every iteration.

---

## Part 8 — Square Root of X

> [`lc_69.py`](lc_69.py)

**Problem:** Return the integer (floor) square root of `x`. No `sqrt()` allowed. (LC 69)

**Approach:** Binary search for the largest `mid` where `mid² ≤ x`.

```python
def mySqrt(x):
    if x < 2:
        return x

    low = 1
    high = x - 1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        if mid * mid > x:
            high = mid - 1
        else:
            low = mid + 1

    return high    # floor of sqrt(x)
```

**Trace — `x=8`:**
```
low=1, high=7, mid=4 → 16 > 8 → high=3
low=1, high=3, mid=2 → 4  < 8 → low=3
low=3, high=3, mid=3 → 9  > 8 → high=2
low=3 > high=2 → exit, return high=2 ✓  (√8 ≈ 2.82, floor=2)
```

**Why return `high`?** When the loop exits without an exact match, `high` is the last position where `mid² ≤ x` — that's the floor.

---

## Homework

### LC 42 — Trapping Rain Water

**Problem:** Given an elevation map, compute how much water it can trap after rain.

**Hint:** Water above bar `i` = `min(max_left, max_right) - height[i]`, where `max_left` and `max_right` are the tallest bars to its left and right.

Try a two-pass O(n) approach first (build a prefix-max array and a suffix-max array), then see if you can do it with two pointers in O(1) space.
