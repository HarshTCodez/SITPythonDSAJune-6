from math import floor, sqrt


# default argument (number_of_dashes) + keyword arguments when calling
def line_break(use_asterix, number_of_dashes=40):
    if use_asterix:
        print("*" * number_of_dashes)
    else:
        print("-" * number_of_dashes)


line_break(use_asterix=True)
print("line a")
line_break(use_asterix=True)
print("line b")
line_break(use_asterix=False, number_of_dashes=45)
print("line c")
line_break(use_asterix=True)


def sum_two_numbers(a, b):
    print("a+b")
    return a + b
    print("done")  # unreachable: code after `return` never runs


c = sum_two_numbers(10, 15)
print(c)


def is_prime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        return None
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans


def power(a, b):
    return a ** b


def sum_of_squares(a, b):
    if a > b:
        return None
    ans = 0
    for i in range(a, b + 1):
        ans += i ** 2
    return ans


print(is_prime(7))
print(is_prime(9))
print(factorial(5))
print(factorial(-5))
print(sum_of_squares(1, 5))
