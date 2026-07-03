def maze(matrix: list[list[int]], i=0, j=0):
    if i == len(matrix) or j == len(matrix[0]):
        return 0
    if matrix[i][j] == 1:
        return 0
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return 1

    return maze(matrix, i + 1, j) + maze(matrix, i, j + 1)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return maze(obstacleGrid)
