matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]


def row_wise_print(matrix: list[list]):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()


def col_wise_print(matrix: list[list]):
    n = len(matrix)
    m = len(matrix[0])

    for col in range(m):
        for row in range(n):
            print(matrix[row][col], end=" ")
        print()


row_wise_print(matrix)
col_wise_print(matrix)
