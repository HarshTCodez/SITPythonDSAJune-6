def sort(arr: list):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    arr = [5, 6, 1, 0, -2, -4]
    arr = sort(arr)
    print(arr)
