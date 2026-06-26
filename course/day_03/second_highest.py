x = [3, 4, 2, 5, 1, 0, 5]


def second_highest(arr):
    max1 = float("-inf")
    max2 = float("-inf")
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        if x != max1 and x > max2:
            max2 = x
    return max2


print(second_highest(x))
