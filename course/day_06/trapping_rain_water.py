class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        n = len(height)

        left = [] + height
        right = [] + height

        for i in range(1, n):
            left[i] = max(left[i], left[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1])

        for i in range(1, n - 1):
            curr_ans = min(left[i - 1], right[i + 1]) - height[i]
            if curr_ans > 0:
                ans += curr_ans

        return ans
