def binary_search(arr: list, low: int, high: int, target: int):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


arr = [2, 3, 4, 6, 8, 10, 12, 14]
ans = binary_search(arr, 0, len(arr) - 1, target=1)
print(ans)
