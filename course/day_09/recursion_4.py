def sum_of_arr(arr: list, starting_index):
    # sum of array starting from the index start_index
    if starting_index == len(arr) - 1:
        return arr[starting_index]
    return arr[starting_index] + sum_of_arr(arr, starting_index + 1)


def sum_of_arr_odd(arr: list, starting_index):
    # sum of array starting from the index start_index
    if starting_index == len(arr) - 1:
        if arr[starting_index] % 2 == 1:
            return arr[starting_index]
        return 0
    curr_el = arr[starting_index]
    if curr_el % 2 == 0:
        curr_el = 0
    return curr_el + sum_of_arr_odd(arr, starting_index + 1)


arr = [1, 7, 12, 13]

print(sum_of_arr(arr, 0))
print(sum_of_arr_odd(arr, 0))
