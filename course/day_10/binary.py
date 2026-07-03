def binary_numbers(n: int, ans=""):
    if n == 0:
        print(ans)
        return

    for i in range(4):
        binary_numbers(n - 1, ans + str(i))


binary_numbers(3)
