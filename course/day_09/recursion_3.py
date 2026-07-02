def factorial(n):
    if n < 0:
        return
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def sum_till_n(n):
    if n == 1:
        return 1
    return n + sum_till_n(n - 1)


def sum_till_n_even(n):
    if n == 1 or n == 0:
        return 0
    if n % 2 == 1:
        return sum_till_n_even(n - 1)
    return n + sum_till_n_even(n - 2)


def sum_till_n_odd(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return sum_till_n_even(n - 1)
    return n + sum_till_n_even(n - 2)


ans = factorial(-1)
print(ans)
