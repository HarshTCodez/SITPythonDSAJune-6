# Prime number check.
# Only loop till sqrt(n): if n = a * b, then one of a, b must be <= sqrt(n).
# So if no divisor is found up to sqrt(n), there is none at all.

from math import floor, sqrt

n = int(input("n: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not prime")
