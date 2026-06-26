def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        curr = arr.pop(i)

        j = 0
        while j < i and arr[j] < curr:
            j += 1

        arr.insert(j, curr)

    print(arr)


print(insertion_sort([9, 8, 7, 1, 2, 3]))
