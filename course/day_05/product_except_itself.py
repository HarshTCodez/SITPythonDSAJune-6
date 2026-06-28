class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix = arr[i] * prefix

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * arr[i]

        return res
