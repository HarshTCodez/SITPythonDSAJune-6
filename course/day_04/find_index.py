def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        current = arr.pop(i)

        j = 0
        while j < i and arr[j] < current:
            j += 1

        arr.insert(j, current)

    return arr


print(insertion_sort([5, 4, 3, 2, 1, 99, -1, -2, -3]))
