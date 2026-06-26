# Day 4 — Time Complexity, Sorting & Hashing

---

## Part 1 — Time Complexity

> [`time_Complexity.py`](time_Complexity.py) | [`time_complexity_questions.md`](time_complexity_questions.md)

Big-O describes how runtime *grows* as input size `n` grows. Drop constants, keep the dominant shape.

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | index access, dict lookup |
| O(log n) | Logarithmic | halving loop |
| O(n) | Linear | single for-loop |
| O(n²) | Quadratic | nested loops |

**The key question:** "If n doubles, what happens to the runtime?"

### Halving loop — O(log n)
```python
i = 1
while i < n:
    i = i * 2   # doubles each iteration → log₂(n) steps
```

### Halving the input — O(log n)
```python
i = 1
while i < n:
    n = n // 2  # shrinks n by half each step → log₂(n) steps
```

> See [`time_complexity_questions.md`](time_complexity_questions.md) for 10 practice questions with answers.

---

## Part 2 — Selection Sort

> [`selection_sort.py`](selection_sort.py)

**Idea:** Find the minimum of the unsorted portion, swap it to the front. Repeat.

- Time: O(n²) always — scans even if already sorted, no early exit possible.
- Space: O(1)

```python
def selection_sort(arr):
    for i in range(len(arr)):
        smallest_element_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_element_index]:
                smallest_element_index = j
        arr[smallest_element_index], arr[i] = arr[i], arr[smallest_element_index]
```

**Dry run — `[6, 5, 3, 4, 1, 8]`:**
- Pass 0: min=1 at idx 4 → swap → `[1, 5, 3, 4, 6, 8]`
- Pass 1: min=3 at idx 2 → swap → `[1, 3, 5, 4, 6, 8]`
- Pass 2: min=4 at idx 3 → swap → `[1, 3, 4, 5, 6, 8]`
- Pass 3, 4, 5: already in place.

---

## Part 3 — Insertion Sort

> [`insertion_sort.py`](insertion_sort.py) | [`insertion_sort_new.py`](insertion_sort_new.py) | [`find_index.py`](find_index.py)

**Idea:** Like sorting cards in hand — pick one card and slide it left until it's in the right spot among already-sorted elements.

- Time: O(n²) worst, **O(n) best** (already sorted — no shifts needed).
- Space: O(1)

### Standard approach (shift right to make room):
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]   # shift right
            j -= 1
        arr[j + 1] = current_element
```

**Dry run — `[4, 20, 9, 7, 32]`:**
- i=1, key=20: 20 > 4 → no shift → `[4, 20, 9, 7, 32]`
- i=2, key=9: 9 < 20 → shift → `[4, 9, 20, 7, 32]`
- i=3, key=7: 7 < 20, 7 < 9 → shift both → `[4, 7, 9, 20, 32]`
- i=4, key=32: 32 > 20 → no shift → done ✓

### Alternative approach (pop and insert):
```python
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        curr = arr.pop(i)     # remove element
        j = 0
        while j < i and arr[j] < curr:
            j += 1
        arr.insert(j, curr)   # insert at correct position
```

> Same result, different mechanics — `pop` + `insert` vs shifting in-place. The shift approach is more efficient (no list reallocation).

---

## Part 4 — Bubble Sort

> [`bubble_sort.py`](bubble_sort.py)

**Idea:** Compare adjacent elements; if out of order, swap. After each full pass, the largest unsorted element "bubbles up" to its final position.

- Time: O(n²) worst, **O(n) best** (with early exit on sorted input).
- Space: O(1)

```python
def bubble_sort(arr):
    n = len(arr)
    is_sorted = True
    for i in range(n - 1):
        for j in range(n - 1 - i):   # last i elements are already sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break                     # no swaps this pass → already sorted
```

---

## Part 5 — Counting Sort (for 0s, 1s, 2s)

> [`counting_Sort.py`](counting_Sort.py) | [`counting_sort_dict.py`](counting_sort_dict.py)

**Idea:** Instead of comparing elements, count how many of each value exist, then reconstruct the sorted array. Works when the value range is small and known.

### Using separate variables:
```python
def counting_sort(arr: list):
    number_of_zeroes = 0
    number_of_ones = 0
    number_of_twos = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            number_of_zeroes += 1
        if arr[i] == 1:
            number_of_ones += 1
        if arr[i] == 2:
            number_of_twos += 1

    res = []
    for i in range(number_of_zeroes): res.append(0)
    for i in range(number_of_ones):   res.append(1)
    for i in range(number_of_twos):   res.append(2)
```

### Using a dictionary (cleaner, same idea):
```python
def counting_sort(arr: list):
    my_dict = {0: 0, 1: 0, 2: 0}
    for i in range(len(arr)):
        my_dict[arr[i]] += 1

    res = []
    for i in range(my_dict[0]): res.append(0)
    for i in range(my_dict[1]): res.append(1)
    for i in range(my_dict[2]): res.append(2)
```

- Time: O(n) — one pass to count, one pass to reconstruct.
- Space: O(1) — the dict has a fixed 3 keys regardless of input size.

---

## Part 6 — Sorting Algorithms Comparison

| Algorithm | Best | Worst | Stable? | Notes |
|-----------|------|-------|---------|-------|
| Bubble Sort | O(n) | O(n²) | Yes | Early exit on sorted input |
| Selection Sort | O(n²) | O(n²) | No | Always n(n-1)/2 comparisons |
| Insertion Sort | O(n) | O(n²) | Yes | Best for nearly-sorted data |
| Counting Sort | O(n) | O(n) | Yes | Only works on small known ranges |

**Stable** means equal elements keep their original relative order.

---

## Part 7 — Frequency Counting with Dictionaries

> [`frequency.py`](frequency.py)

Count how many times each element appears, then find the element with the highest frequency.

```python
def count_frequencies(arr: list):
    my_dict = {}
    for number in arr:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    return my_dict

def find_max_frequency(arr: list):
    freq = count_frequencies(arr)
    max_freq = 0
    for key in freq:
        if freq[key] > max_freq:
            max_freq = freq[key]
    for key in freq:
        if freq[key] == max_freq:
            print(f"element with maximum frequency is: {key}")
```

**Key idea:** `freq.get(num, 0) + 1` is a cleaner alternative to the `if number in my_dict` check — returns 0 if the key doesn't exist yet, so the first occurrence becomes 1 automatically.

---

## Part 8 — LeetCode Problems

### LC 1 — Two Sum

> [`lc_01.py`](lc_01.py)

**Problem:** Return the indices of two numbers that add up to `target`.

**Optimised — O(n) using a dictionary:**
```python
def two_sum(arr: list, target: int):
    seen = {}
    for index, value in enumerate(arr):
        diff = target - value
        if diff in seen:
            return [seen[diff], index]
        seen[value] = index
    return []
```

**Intuition:** For each number, ask *"have I already seen the number that would complete this pair?"* A dictionary answers that in O(1) — no inner loop needed.

**Trace — `arr=[2,7,11,15], target=9`:**
```
index=0, value=2, diff=7  → not in seen → seen={2:0}
index=1, value=7, diff=2  → 2 IS in seen → return [0, 1] ✓
```

---

### LC 217 — Contains Duplicate

> [`lc_217.py`](lc_217.py)

**Problem:** Return `True` if any value appears at least twice.

**Approach 1 — Sort then scan:**
```python
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```
Time: O(n log n) — sort dominates.

**Approach 2 — Set, O(n):**
```python
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
```
Converting to a set drops duplicates. If the lengths differ, a duplicate existed.
