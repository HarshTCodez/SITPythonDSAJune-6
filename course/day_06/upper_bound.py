def upper_bound(arr: list, target: int):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [1, 2, 3, 4, 5, 10, 20, 30, 40, 40, 40, 40, 100, 1000, 2000]
ind = upper_bound(arr, 40)
print(ind)
print(arr[ind])
