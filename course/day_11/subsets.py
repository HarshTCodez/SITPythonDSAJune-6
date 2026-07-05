class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate(arr: list, start_index=0, ans=[]):
            if start_index == len(arr):
                res.append(ans.copy())
                return

            ans.append(arr[start_index])
            generate(arr, start_index + 1, ans)
            ans.pop()
            generate(arr, start_index + 1, ans)

        generate(nums, 0, [])
        return res
