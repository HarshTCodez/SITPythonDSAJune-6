MIN = -(2**31)
MAX = (2**31) - 1


def reverse_integer(n: int):
    rev = 0
    while n > 0:
        last = n % 10  # grab last digit
        rev = rev * 10 + last  # push it onto the reversed number
        n = n // 10  # drop the last digit
    return rev


def reverse(n: int):
    is_negative = False
    if n < 0:
        is_negative = True
        n = n * (-1)
    n = reverse_integer(n)
    if is_negative:
        n = n * (-1)
    if n > MAX:
        return 0
    if n < MIN:
        return 0
    return n


if __name__ == "__main__":
    print(reverse(-123))
