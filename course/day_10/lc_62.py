def maze(n: int, m: int, i=0, j=0):
    if i == n or m == j:
        return 0
    if i == n - 1 and j == m - 1:
        return 1
    down = maze(n, m, i + 1, j)
    right = maze(n, m, i, j + 1)
    return down + right


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return maze(m, n)
