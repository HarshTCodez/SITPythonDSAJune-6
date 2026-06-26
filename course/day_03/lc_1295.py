def count_digits(n):
    if n == 0:
        return 1
    ans = 0
    while n > 0:
        ans += 1
        n = n // 10
    return ans


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for current_number in nums:
            if count_digits(current_number) % 2 == 0:
                ans += 1
        return ans
