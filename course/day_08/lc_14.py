class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
        m = len(strs[0])
        for col in range(m):
            current_char = strs[0][col]
            for row in range(1, n):
                if col == len(strs[row]):
                    return ans
                if strs[row][col] != current_char:
                    return ans
            ans += current_char
        return ans
