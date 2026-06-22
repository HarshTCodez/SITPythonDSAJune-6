# Sum of all digits of a number.  Example: 4342 -> 4+3+4+2 = 13

n = int(input("n: "))

total = 0
while n > 0:
    total += n % 10   # last digit
    n = n // 10       # drop the last digit

print(total)
