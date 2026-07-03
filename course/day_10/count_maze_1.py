total_count = 0


def maze(start_row, start_col, end_row, end_col, ans=""):
    if start_row > end_row:
        return
    if start_col > end_col:
        return
    if start_row == end_row and start_col == end_col:
        print(ans)
        global total_count
        total_count += 1
        return
    # first we go down
    maze(start_row + 1, start_col, end_row, end_col, ans + "D")
    maze(start_row + 1, start_col + 1, end_row, end_col, ans + "S")
    # then we go right
    maze(start_row, start_col + 1, end_row, end_col, ans + "R")


maze(0, 0, 2, 2)
print(total_count)
