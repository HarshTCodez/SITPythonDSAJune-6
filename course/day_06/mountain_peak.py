class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        ans = n - 1

        while low <= high:
            mid = (low + high) // 2
            # print(f"{mid=}")
            # print(f"{arr[mid]=}")
            if arr[mid] > arr[mid + 1]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
