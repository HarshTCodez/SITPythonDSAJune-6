class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        low = 0
        high = len(arr) - 1

        while low < high:
            temp = arr[low] + arr[high]

            if temp == target:
                return [low + 1, high + 1]

            if temp < target:
                low += 1
            else:
                high -= 1

        return []
