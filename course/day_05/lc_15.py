class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        ans = []
        arr.sort()

        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            c = arr[i]
            target = -c
            low = i + 1
            high = n - 1

            while low < high:
                curr = arr[low] + arr[high]
                if curr == target:
                    ans.append([arr[i], arr[low], arr[high]])
                    while low < high and arr[low] == arr[low + 1]:
                        low += 1
                    low += 1
                    high -= 1
                elif curr > target:
                    high -= 1
                else:
                    low += 1

        return ans
