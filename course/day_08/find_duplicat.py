def solve(arr: list):
    n = len(arr) - 1
    ans = 0

    for i in range(1, n + 1):
        ans = ans ^ i

    for number in arr:
        ans = ans ^ number

    return ans


print(solve([1, 1, 3, 2]))
