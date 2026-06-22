# Reverse a number.  Example: 4342 -> 2434

n = int(input("n: "))

rev = 0
while n > 0:
    last = n % 10            # grab last digit
    rev = rev * 10 + last    # push it onto the reversed number
    n = n // 10              # drop the last digit

print(rev)
