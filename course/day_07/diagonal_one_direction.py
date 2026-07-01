# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def diagonal_traversal(matrix: list[list]):
    n = len(matrix)
    m = len(matrix[0])

    result = []

    number_of_d = n + m - 1

    for d in range(number_of_d):
        for i in range(n):
            j = d - i

            if 0 <= j < m:
                result.append(matrix[i][j])

    return result


res = diagonal_traversal(matrix)
print(res)
