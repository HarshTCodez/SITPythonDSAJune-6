def _sum_till_n(n: int):
    if n == 0:
        return 0
    return n + _sum_till_n(n - 1)


def sum_till_n(n: int, ans: int):
    if n == 0:
        print(ans)
        return

    sum_till_n(n - 1, ans + n)


def sum_till_n_odd(n: int, ans: int):
    if n == 0:
        print(ans)
        return

    if n % 2 == 0:
        sum_till_n_odd(n - 1, ans + n)
    else:
        sum_till_n_odd(n - 1, ans)


sum_till_n(5, 0)
