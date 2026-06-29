def lower_bound(arr: list, x: int):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upper_bound(arr: list, x: int):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = lower_bound(nums, target)
        upper = upper_bound(nums, target)

        n = len(nums)

        if lower == n:
            return [-1, -1]

        if nums[lower] != target:
            return [-1, -1]

        return [lower, upper - 1]
