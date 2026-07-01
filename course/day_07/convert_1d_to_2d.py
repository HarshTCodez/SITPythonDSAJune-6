class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []

        ans = []

        for i in range(m):
            ans.append([])

        for i in range(m * n):
            row_number = i // n
            ans[row_number].append(original[i])

        return ans
