def power(x: float, n: int):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    half = power(x, n // 2)
    ans = half * half
    if n % 2 == 1:
        ans *= x
    return ans


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return power(x, n)
