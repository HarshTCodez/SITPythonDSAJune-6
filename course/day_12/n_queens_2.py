def get_matrix_size(board: list[list]) -> tuple[int, int]:
    return len(board), len(board[0])


def place_queen(board: list[list], row: int, col: int):
    board[row][col] = 1


def remove_queen(board: list[list], row: int, col: int):
    board[row][col] = 0


def check_if_safe(board: list[list], row: int, col: int) -> bool:
    n, m = get_matrix_size(board)

    for j in range(m):
        if board[row][j] == 1:
            return False

    for i in range(n):
        if board[i][col] == 1:
            return False

    # going left upwards diagnol
    temp_row = row
    temp_col = col

    while temp_row >= 0 and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col -= 1

    # going left downwards diagnol
    temp_row = row
    temp_col = col

    while temp_row < n and temp_col < m:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col += 1

    # going right upwards
    temp_row = row
    temp_col = col
    while temp_row >= 0 and temp_col < m:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col += 1

    temp_row = row
    temp_col = col
    while temp_row < n and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col -= 1

    return True


def transform_board(board: list[list]):
    ans = []
    for row in board:
        curr_str = ""
        for x in row:
            curr_str += "." if x == 0 else "Q"
        ans.append(curr_str)
    return ans


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        def find_sol(board: list[list], start_row=0):
            n, m = get_matrix_size(board)
            if start_row == n:
                ans = transform_board(board)
                res.append(ans)
                # print(ans, sep="\n")
                return

            for j in range(n):
                if check_if_safe(board, start_row, j):
                    place_queen(board, start_row, j)
                    find_sol(board, start_row + 1)
                    remove_queen(board, start_row, j)

        board = []
        for i in range(n):
            board.append([0] * n)

        find_sol(board)
        return len(res)
