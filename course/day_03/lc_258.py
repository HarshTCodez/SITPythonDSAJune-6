# def sum_of_digits(n):
#     ans = 0
#     while n > 0:
#         ans += n % 10
#         n = n // 10
#     return ans
#
#
# class Solution:
#     def addDigits(self, n: int) -> int:
#         while n >= 10:
#             n = sum_of_digits(n)
#         return n
#
#
# for i in range(1, 101):
#     print(f"{i} -> add digits ->", Solution().addDigits(i))


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        ans = num % 9
        if ans == 0:
            ans = 9
        return ans
