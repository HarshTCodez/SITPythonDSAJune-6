def bubble_sort(arr):
    n = len(arr)
    is_sorted = True
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            break


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bubble_sort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False
        return True
