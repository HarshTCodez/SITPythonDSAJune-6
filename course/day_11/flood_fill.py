def fill(
    matrix: list[list[int]], row: int, col: int, new_color: int, original_color: int
):
    if row < 0 or col < 0:
        return
    if row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] == new_color:
        return

    if matrix[row][col] != original_color:
        return

    matrix[row][col] = new_color

    fill(matrix, row + 1, col, new_color, original_color)
    fill(matrix, row - 1, col, new_color, original_color)
    fill(matrix, row, col + 1, new_color, original_color)
    fill(matrix, row, col - 1, new_color, original_color)


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        fill(image, sr, sc, color, image[sr][sc])
        return image
