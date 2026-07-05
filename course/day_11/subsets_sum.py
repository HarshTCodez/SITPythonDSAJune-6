def subsets(arr: list, target: int):
    res = []

    def gen(index: int, ans: list):
        if index == len(arr):
            if sum(ans) >= target:
                res.append(ans[:])
            return

        ans.append(arr[index])
        gen(index + 1, ans)
        ans.pop()
        gen(index + 1, ans)

    gen(0, [])
    return res


all = subsets([2, 3, 4, -1, -2], 8)
print(all)
