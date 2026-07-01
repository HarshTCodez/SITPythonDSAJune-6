from math import ceil


def can_eat(piles: list, h: int, k: int):
    ans = 0
    for x in piles:
        ans += ceil(x / k)
    return ans <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        low = 1
        high = max_pile
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_eat(piles, h, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
