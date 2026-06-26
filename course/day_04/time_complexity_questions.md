# Time Complexity Practice Questions

For each of the following Python snippets, determine the Big-O time complexity in terms of `n`.

## Question 1
```python
def q1(n):
    return n * (n + 1) // 2
```

## Question 2
```python
def q2(n):
    for i in range(n):
        print(i)
```

## Question 3
```python
def q3(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

## Question 4
```python
def q4(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)
```

## Question 5
```python
def q5(n):
    for i in range(n):
        for j in range(10):
            print(i, j)
```

## Question 6
```python
def q6(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
```

## Question 7
```python
def q7(n):
    for i in range(n):
        print("Hello")
    for j in range(n):
        print("World")
```

## Question 8
```python
def q8(n):
    i = n
    while i > 0:
        print(i)
        i = i // 2
```

## Question 9
```python
def q9(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j = j * 2
```

## Question 10
```python
def q10(n):
    for i in range(1 << n):  # 1 << n is equivalent to 2^n
        print(i)
```

---

## Answers & Explanations

1. **$O(1)$** - Constant time. There are no loops, just mathematical arithmetic operations.
2. **$O(n)$** - Linear time. A single loop running `n` times.
3. **$O(n^2)$** - Quadratic time. Nested loops where both outer and inner loops run `n` times.
4. **$O(n^2)$** - Quadratic time. The inner loop runs `n`, `n-1`, `n-2`... times, which sums to an arithmetic progression $n(n+1)/2$. Dropping constants and lower order terms gives $O(n^2)$.
5. **$O(n)$** - Linear time. The inner loop runs a constant 10 times regardless of `n`. So it takes $10n$ operations, which simplifies to $O(n)$ when dropping the constant.
6. **$O(\log n)$** - Logarithmic time. `i` is multiplied by 2 in each step. It takes $\log_2(n)$ steps for `i` to reach `n`.
7. **$O(n)$** - Linear time. The loops run sequentially (not nested), giving $O(n) + O(n) = O(2n)$, which drops the constant to give $O(n)$.
8. **$O(\log n)$** - Logarithmic time. Similar logic to Q6, but dividing by 2 repeatedly until reaching 0.
9. **$O(n \log n)$** - Linearithmic time. The outer loop runs `n` times, and the inner loop runs $\log_2(n)$ times for each of those outer iterations.
10. **$O(2^n)$** - Exponential time. The loop directly iterates $2^n$ times (since `1 << n` shifts bits left, essentially computing $2^n$).
