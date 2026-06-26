def is_sorted(arr):
    # ascending order sorted
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def bubble_sort(arr):
    n = len(arr)
    is_sorted = True
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break
        print(arr)


bubble_sort([1, 2, 3, 4, 5])
