# Number of digits in a number.  Example: 4342 -> 4
# Three methods.

from math import floor, log10

n = int(input("n: "))

# Method 1: floor division - keep dividing by 10 until 0
count = 0
temp = n
while temp > 0:
    temp = temp // 10
    count += 1
print(count)

# Method 2: log10 - floor(log10(n)) + 1
print(floor(log10(n)) + 1)

# Method 3: trick - convert to string and take its length
print(len(str(n)))
