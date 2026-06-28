def merge(arr1: list, arr2: list):
    ans = []
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < n:
        ans.append(arr1[i])
        i += 1

    while j < m:
        ans.append(arr2[j])
        j += 1

    return ans


arr = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge(arr, arr2))
