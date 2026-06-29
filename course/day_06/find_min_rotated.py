class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        ans = float("inf")

        while low <= high:
            mid = (low + high) // 2
            if arr[low] <= arr[high]:
                ans = min(arr[low], ans)
                break

            if arr[low] <= arr[mid]:
                ans = min(arr[low], ans)
                low = mid + 1
            else:
                ans = min(arr[mid], ans)
                high = mid - 1

        return ans
