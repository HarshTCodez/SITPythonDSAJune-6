arr = [2, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1]


def counting_sort(arr: list):
    number_of_zeroes = 0
    number_of_ones = 0
    number_of_twos = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            number_of_zeroes += 1
        if arr[i] == 1:
            number_of_ones += 1
        if arr[i] == 2:
            number_of_twos += 1

    res = []

    print(number_of_zeroes)
    print(number_of_ones)
    print(number_of_twos)

    for i in range(number_of_zeroes):
        res.append(0)

    for i in range(number_of_ones):
        res.append(1)

    for i in range(number_of_twos):
        res.append(2)

    print(res)


counting_sort(arr)
