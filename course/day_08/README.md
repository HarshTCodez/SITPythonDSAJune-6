# Day 8 — String Analysis & Fundamentals + Bit Manipulation Basics

Two major themes: understanding strings at the character and frequency level, then the binary foundation for efficient algorithms.
The string problems build from basic operations → frequency analysis → pattern recognition. Bit manipulation opens the door to optimization.

---

## Part 0 — String Basics: Operations & Built-in Methods

> [`strings.py`](strings.py)

Strings in Python are sequences of characters. Common operations:

**String concatenation, splitting, and joining:**

```python
s = "hello world"
words = s.split()          # ["hello", "world"]
result = " ".join(words)   # "hello world"
```

**Case conversion and whitespace:**

```python
s = "  hello WORLD  "
s = s.strip()              # "hello WORLD"
s = s.lower()              # "hello world"
s = s.capitalize()         # "Hello world"
s = s.title()              # "Hello World"
```

**Character and substring checks:**

```python
s = "hello123"
s.isalpha()                # False (has digits)
s.isalnum()                # True (letters or digits)
s.isdigit()                # False
c = 'a'
c.isalpha()                # True
```

**Finding and replacing:**

```python
s = "hello world"
s.find("world")            # 6 (index of substring)
s.replace("world", "python")  # "hello python"
```

**Accessing characters:**

```python
s = "hello"
s[0]                       # "h"
s[-1]                      # "o"
s[1:4]                     # "ell"
s[::-1]                    # "olleh" (reverse)
```

**Key idea:** Master these operations — they are the foundation for every string problem.

---

## Part 1 — Character Frequency Analysis

> [`freq_str.py`](freq_str.py) (hashmap) · [`freq_arr.py`](freq_arr.py) (array)

Many string problems reduce to **"count how many times each character appears"**. Two main approaches:

**Approach 1: Hashmap (dictionary)**

```python
def char_frequency_map(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# "aabbc" → {'a': 2, 'b': 2, 'c': 1}
```

**Approach 2: Frequency Array (for ASCII only)**

```python
def char_frequency_array(s):
    freq = [0] * 26              # lowercase a-z only
    for char in s:
        if 'a' <= char <= 'z':
            freq[ord(char) - ord('a')] += 1
    return freq

# "aabbc" → [2, 2, 1, 0, 0, ...]  (index 0 = 'a', index 1 = 'b', etc.)
```

**ord() and chr():**

- `ord('a')` → 97 (ASCII value)
- `ord('z')` → 122
- `chr(97)` → 'a'
- `ord(char) - ord('a')` → converts 'a'→0, 'b'→1, ..., 'z'→25

**When to use which:**

- Hashmap: handles any characters (Unicode, digits, symbols), easier to read
- Array: faster for lowercase-only problems, fixed O(26) space

**Key idea:** Frequency is the _language_ of string analysis. Before you code, ask: "Do I need to count?"

---

## Part 2 — Valid Palindrome

> [`palindrome.py`](palindrome.py) (warm-up, no alnum/case handling) · [`valid_palindrome.py`](valid_palindrome.py) · [`lc_125.py`](lc_125.py) (alternate two-pointer style)

**Warm-up (`palindrome.py`):** plain two-pointer palindrome check on a clean string, no alphanumeric filtering or case-folding — the stepping stone before LC 125.

**Problem:** Given a string `s`, return `True` if it reads the same forwards and backwards, ignoring non-alphanumeric characters and case. (LC 125)

**Insight:** Two pointers from both ends, skip non-alphanumeric, compare case-insensitively.

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare case-insensitively
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

**Trace — `s="A man, a plan, a canal: Panama"`:**

```
left=0→'A', right=31→'a': 'a'=='a' ✓
left=1→' ' (skip), left=2→'m', right=30→'m': 'm'=='m' ✓
... continue until left >= right
Result: True ✓
```

**vs brute-force:** Don't build a cleaned string first. Two pointers are O(n) with O(1) space.

---

## Part 3 — Valid Anagram

> [`lc_242.py`](lc_242.py)

**Problem:** Given two strings `s` and `t`, return `True` if `t` is an anagram of `s` (same characters, different order). (LC 242)

**Approach 1: Sorting**

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

O(n log n), simple, but not optimal.

**Approach 2: Frequency Hashmap**

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_s = {}
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    for char in t:
        if char not in freq_s:
            return False
        freq_s[char] -= 1
        if freq_s[char] < 0:
            return False

    return True
```

O(n), but uses a hashmap.

**Approach 3: Frequency Array (lowercase only)**

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1

    for char in t:
        freq[ord(char) - ord('a')] -= 1
        if freq[ord(char) - ord('a')] < 0:
            return False

    return True
```

O(n) time, O(1) space (fixed array size).

**Trace — `s="listen", t="silent"`:**

```
Approach 3:
freq after s: [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
             (indices: a b c d e f g h i j k  l  m n ...)
Decrement by t: all go back to 0 → True ✓
```

**Key idea:** Anagrams have _identical character counts_. The structure of the string doesn't matter.

---

## Part 4 — Group Anagrams

> [`lc_49.py`](lc_49.py)

**Problem:** Given an array of strings, group the anagrams together. (LC 49)

**Insight:** Anagrams share the same sorted form — use it as a hashmap key.

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
```

`lc_49.py` also keeps a commented-out `get_freq_arr`/`convert_freq_arr_to_str` pair (build the key from a frequency array instead of `sorted()`) — same idea, O(n) key construction instead of O(n log n).

**Key idea:** Anagram grouping is the "compare character frequencies" idea from Part 3, generalized to a hashmap of buckets.

---

## Part 5 — Longest Common Prefix

> [`lc_14.py`](lc_14.py)

**Problem:** Given an array of strings `strs`, return the longest common prefix. Return `""` if no common prefix. (LC 14)

**Insight:** Compare characters at the same position across all strings.

**Approach 1: Vertical Scan (simple)**

```python
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]
```

O(S) where S is the sum of all characters. Early exit on mismatch.

**Approach 2: Binary Search (when prefix matters)**

```python
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    def is_common_prefix(length):
        prefix = strs[0][:length]
        for s in strs[1:]:
            if not s.startswith(prefix):
                return False
        return True

    low, high = 0, len(strs[0])
    while low < high:
        mid = (low + high + 1) // 2
        if is_common_prefix(mid):
            low = mid
        else:
            high = mid - 1

    return strs[0][:low]
```

O(S log L) where L is the length of the shortest string. Overkill for most cases.

**Trace — `strs=["flower","flow","flight"]`:**

```
i=0: char='f', all have 'f' ✓
i=1: char='l', all have 'l' ✓
i=2: char='o', "flight"[2]='i' ✗ → return "fl" ✓
```

**Key idea:** Vertical scan is almost always sufficient. Binary search is a pattern to recognize, not a requirement here.

---

## Part 6 — Reverse Words in a String

> [`reverse_words.py`](reverse_words.py)

**Problem:** Given a string `s`, reverse the order of words. Words are separated by spaces. (LC 151)

**Insight:** `split()` handles multiple spaces, reverse the list, `join()` them back.

```python
def reverseWords(s: str) -> str:
    words = s.split()              # ["the", "sky", "is", "blue"]
    return " ".join(words[::-1])   # "blue is sky the"
```

**Without built-ins (two-pointer approach):**

```python
def reverseWords(s: str) -> str:
    # Convert to list for in-place manipulation
    s_list = s.split()
    left, right = 0, len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return " ".join(s_list)
```

**Trace — `s="the sky is blue"`:**

```
After split: ["the", "sky", "is", "blue"]
After reverse: ["blue", "is", "sky", "the"]
After join: "blue is sky the" ✓
```

**Key idea:** `split()` is your friend — it handles the "multiple spaces" problem automatically. The rest is just reversing.

---

## Part 7 — Length of Last Word

> [`length_of_last_word.py`](length_of_last_word.py)

**Problem:** Given a string `s`, return the length of the **last word**. A word is a maximal substring consisting of non-space characters. (LC 58)

**Approach 1: Split and return**

```python
def lengthOfLastWord(s: str) -> int:
    words = s.split()
    return len(words[-1]) if words else 0
```

Simple and O(n).

**Approach 2: Two-pointer from the right (interview optimization)**

```python
def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count the word length
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
```

O(n) time, O(1) space. Shows understanding of the pointer pattern.

**Trace — `s="luffy is still joyboy"`:**

```
Approach 1: words=["luffy", "is", "still", "joyboy"], len(words[-1])=7 ✓
Approach 2: i=20 ('y'), skip nothing, count backwards: j→o→y→b→o→y=7 ✓
```

**Key idea:** Split works. But pointers from the right show you understand the pattern — useful in interviews.

---

## Part 8 — Bit Manipulation Basics

> Concepts only — no dedicated file in this folder; `binary.py` picks up from here with population count.

Binary is how computers think. Bit operations are the foundation for optimization and clever tricks.

**Binary representation:**

```python
bin(5)      # '0b101'
bin(10)     # '0b1010'
int('0b101', 2)  # 5 (parse from binary string)
```

**Bitwise AND (`&`)** — 1 only if both bits are 1:

```python
5 & 3       # 0b101 & 0b011 = 0b001 = 1
6 & 3       # 0b110 & 0b011 = 0b010 = 2
```

**Bitwise OR (`|`)** — 1 if either bit is 1:

```python
5 | 3       # 0b101 | 0b011 = 0b111 = 7
4 | 2       # 0b100 | 0b010 = 0b110 = 6
```

**Bitwise XOR (`^`)** — 1 if bits differ:

```python
5 ^ 3       # 0b101 ^ 0b011 = 0b110 = 6
5 ^ 5       # 0b101 ^ 0b101 = 0b000 = 0  (any number XOR itself is 0)
```

**Bitwise NOT (`~`)** — flip all bits (in Python, includes sign):

```python
~5          # -(5+1) = -6  (two's complement)
```

**Left shift (`<<`)** — multiply by powers of 2:

```python
5 << 1      # 0b101 << 1 = 0b1010 = 10  (5 * 2)
5 << 2      # 0b101 << 2 = 0b10100 = 20  (5 * 4)
```

**Right shift (`>>`)** — divide by powers of 2 (integer division):

```python
5 >> 1      # 0b101 >> 1 = 0b10 = 2  (5 // 2)
10 >> 2     # 0b1010 >> 2 = 0b10 = 2  (10 // 4)
```

**Key idea:** Bits are binary. Shifts are _multiply/divide by powers of 2_ without the overhead.

---

## Part 9 — Bit Manipulation Problems

> [`binary.py`](binary.py) (population count) · [`lc_136.py`](lc_136.py) (LC 136 Single Number) · [`find_duplicat.py`](find_duplicat.py) (XOR missing-element trick)

**Count significant bits — population count (`binary.py`), Brian Kernighan's trick:**

```python
def count_bits(n: int):
    count = 0
    while n > 0:
        n = n & (n - 1)   # drops the lowest set bit each time
        count += 1
    return count

# n=7  (0b0111): 3 set bits
# n=8  (0b1000): 1 set bit
# n=15 (0b1111): 4 set bits
# n=16 (0b10000): 1 set bit
```

`n & (n - 1)` clears the lowest set bit — looping until `n` hits 0 counts exactly the set bits, in `O(popcount)` iterations instead of `O(bit-width)`. This is also the same trick behind a power-of-2 check: `n & (n - 1) == 0` means `n` has exactly one set bit.

**Python shorthand:** `bin(5).count('1')` gives the same answer without the loop.

**Single Number — XOR cancels pairs (`lc_136.py`, LC 136):**

Every number appears twice except one — find it in O(1) space.

```python
def singleNumber(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans

# a^a = 0 for any a, and XOR is commutative/associative,
# so every paired number cancels out and only the lone one survives.
```

**Find the missing number — XOR against the full range (`find_duplicat.py`):**

```python
def solve(arr: list):
    n = len(arr) - 1
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for number in arr:
        ans ^= number
    return ans
```

XOR every value `1..n` together, then XOR every value actually present in `arr` — matching values cancel out, leaving the one that's missing.

**Key idea:** XOR-based tricks solve "find the odd one out" problems in O(n) time, O(1) space — no hashmap needed.

---

## Part 10 — Hexadecimal & Binary Conversion Homework

> Concepts only — no dedicated file in this folder.

**Decimal to binary:**

```python
bin(13)        # '0b1101'
format(13, 'b')  # '1101'
```

**Decimal to hexadecimal:**

```python
hex(255)       # '0xff'
format(255, 'x')  # 'ff'
format(255, 'X')  # 'FF'
```

**Binary to decimal:**

```python
int('1101', 2)   # 13
int('0b1101', 2)  # 13
```

**Hexadecimal to decimal:**

```python
int('ff', 16)    # 255
int('0xff', 16)  # 255
```

**Why hex?** Easier to read than binary, compact representation (1 hex digit = 4 bits).

---

## Teaching Order & Summary

| #   | Problem                 | File                                                | Core Idea                                                  |
| --- | ----------------------- | ---------------------------------------------------- | ----------------------------------------------------------- |
| 0   | String Basics           | `strings.py`                                        | split, join, strip, replace, slicing                        |
| 1   | Frequency Analysis      | `freq_str.py`, `freq_arr.py`                        | Hashmap vs array for character counts                        |
| 2   | Valid Palindrome        | `palindrome.py`, `valid_palindrome.py`, `lc_125.py` | Two pointers, skip non-alphanumeric, case-insensitive        |
| 3   | Valid Anagram           | `lc_242.py`                                         | Compare character frequencies                                |
| 4   | Group Anagrams          | `lc_49.py`                                          | Bucket by sorted (or frequency-array) key                    |
| 5   | Longest Common Prefix   | `lc_14.py`                                          | Vertical scan, early exit on mismatch                        |
| 6   | Reverse Words           | `reverse_words.py`                                  | split(), reverse list, join()                                |
| 7   | Length of Last Word     | `length_of_last_word.py`                            | Two-pointer from right or simple split                       |
| 8   | Bit Basics              | _(concepts only)_                                   | AND, OR, XOR, shifts; binary representation                  |
| 9   | Bit Problems            | `binary.py`, `lc_136.py`, `find_duplicat.py`        | Population count, XOR cancel-pairs, XOR missing-element       |
| 10  | Hex & Binary Conversion | _(concepts only)_                                   | bin(), hex(), int(x, base) for conversions                   |
