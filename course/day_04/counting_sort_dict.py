arr = [2, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1]


def counting_sort(arr: list):
    my_dict = {
        0: 0,
        1: 0,
        2: 0,
    }

    for i in range(len(arr)):
        # arr[i] = 0,1,2
        my_dict[arr[i]] += 1

    res = []

    print(my_dict)

    for i in range(my_dict[0]):
        res.append(0)

    for i in range(my_dict[1]):
        res.append(1)

    for i in range(my_dict[2]):
        res.append(2)

    print(res)


counting_sort(arr)
