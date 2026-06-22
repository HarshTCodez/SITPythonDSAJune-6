# Find all factors of a number.
# Loop only till sqrt(n): if i divides n, then n // i is also a factor.
# Edge case: for a perfect square, i and n // i are the same -> add it once.

from math import floor, sqrt

n = int(input("n: "))

factors = []
for i in range(1, floor(sqrt(n)) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:          # avoid duplicate for perfect squares
            factors.append(n // i)

factors.sort()
print(factors)
