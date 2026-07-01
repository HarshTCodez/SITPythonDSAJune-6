    n = len(matrix)
    m = len(matrix[0])

    result = []

    number_of_d = n + m - 1

    for d in range(number_of_d):
        if d % 2 == 0:
            for j in range(n - 1, -1, -1):
                j = d - i
                if 0 <= j < m:
                    result.append(matrix[i][j])
        else:
            for i in range(0):
                j = d - i

                if 0 <= j < m:
                    result.append(matrix[i][j])

    return result
        
