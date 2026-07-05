def generate(remaining_target: int, start_index, arr: list, ans: list = []):
    if remaining_target < 0:
        return
    if remaining_target == 0:
        print(ans)
        return

    for i in range(start_index, len(arr)):
        ans.append(arr[i])
        generate(remaining_target - arr[i], i, arr, ans)
        ans.pop()


generate(7, 0, [2, 3, 6, 7])
