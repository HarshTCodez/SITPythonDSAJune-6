from lc_07 import reverse_integer


def ans(n):
    if n < 0:
        return False
    new_number = reverse_integer(n)
    return new_number == n
