arr = [4, 20, 9, 7, 32]


def insertion_sort(arr):
    n = len(arr)
    print(f"Array before sorting: {arr}")

    for i in range(1, n):
        current_element = arr[i]
        print(current_element)
        j = i - 1

        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)

        arr[j + 1] = current_element

    print(arr)

    print(f"Array After Sorting: {arr}")


def insertion_sort_ii(arr: list):
    new_arr = [arr[0]]
    arr.pop(0)

    print(new_arr)
    print(arr)

    new_arr.insert(1, arr.pop(0))

    print(new_arr)
    print(arr)

    new_arr.insert(1, arr.pop(0))

    print(new_arr)
    print(arr)

    new_arr.insert(1, arr.pop(0))

    print(new_arr)
    print(arr)

    new_arr.append(arr.pop())

    print(new_arr)
    print(arr)


insertion_sort_ii(arr)
