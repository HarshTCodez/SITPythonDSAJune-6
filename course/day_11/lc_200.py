def fill(matrix: list[list[int]], start_row, start_col, original_color, new_color):
    # out of bounds
    if start_row < 0 or start_col < 0:
        return
    # out of bounds
    if start_row >= len(matrix) or start_col >= len(matrix[0]):
        return
    # already filled the color
    if matrix[start_row][start_col] == new_color:
        return
    # not the original_color
    if matrix[start_row][start_col] != original_color:
        return

    # make it new color
    matrix[start_row][start_col] = new_color

    # traverse down -> up -> right -> left
    fill(matrix, start_row + 1, start_col, original_color, new_color)
    fill(matrix, start_row - 1, start_col, original_color, new_color)
    fill(matrix, start_row, start_col + 1, original_color, new_color)
    fill(matrix, start_row, start_col - 1, original_color, new_color)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    fill(grid, i, j, "1", "2")
        return ans
