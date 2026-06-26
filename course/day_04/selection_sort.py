arr = [6, 5, 3, 4, 1, 8]


def selection_sort(arr):
    print(f"Orignal arr: {arr}")

    for i in range(len(arr)):
        smallest_element_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_element_index]:
                smallest_element_index = j
        arr[smallest_element_index], arr[i] = arr[i], arr[smallest_element_index]

        print(f"{i+1} smallest element bought to index {i}", arr)

    print(f"Final sorted arr: {arr}")


selection_sort(arr)
