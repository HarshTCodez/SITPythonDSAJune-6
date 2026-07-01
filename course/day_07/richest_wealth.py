class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        m = len(accounts[0])
        max_sum = float("-inf")

        for i in range(n):
            current_sum = 0
            for j in range(m):
                current_sum += accounts[i][j]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
