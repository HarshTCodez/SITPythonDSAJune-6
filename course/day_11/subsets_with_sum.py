def generate(arr: list, target: int, start_index=0, ans=[]):
    if start_index == len(arr):
        if sum(ans) > target:
            print(ans)
        return

    ans.append(arr[start_index])
    generate(arr, target, start_index + 1, ans)
    ans.pop()
    generate(arr, target, start_index + 1, ans)


generate([1, 2, 3], 3, 0)
