from math import ceil
from typing import List


def total_time_taken_to_eat(arr: list, eating_speed: int):
    ans = 0
    for number_of_bananas in arr:
        ans += ceil(number_of_bananas / eating_speed)
    return ans


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h < len(piles):
            return -1
        lowest_speed = 1
        highest_speed = max(piles)
        ans = highest_speed

        while lowest_speed <= highest_speed:
            mid = (lowest_speed + highest_speed) // 2
            if total_time_taken_to_eat(piles, mid) <= h:
                ans = mid
                # discard all the speeds greater than mid
                highest_speed = mid - 1
            else:
                lowest_speed = mid + 1

        return ans


eating_speed = Solution().minEatingSpeed([30, 11, 23, 4, 20], 4)
print(f"The min eating speed is {eating_speed} bananas per hour.")
