def maze(start_row, start_col, end_row, end_col, ans=""):
    if start_row > end_row:
        return 0
    if start_col > end_col:
        return 0
    if start_row == end_row and start_col == end_col:
        print(ans)
        return 1
    # first we go down
    down = maze(start_row + 1, start_col, end_row, end_col, ans + "D")
    diagnoally = maze(start_row + 1, start_col + 1, end_row, end_col, ans + "S")
    # then we go right
    right = maze(start_row, start_col + 1, end_row, end_col, ans + "R")

    return down + diagnoally + right


ans = maze(0, 0, 2, 2)
print(ans)
