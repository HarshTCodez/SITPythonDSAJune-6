class Solution:
    def find_next_number(self, n: int):
        new_number = 0
        while n != 0:
            curr = n % 10
            n = n // 10
            new_number += curr * curr
        return new_number

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = self.find_next_number(slow)
            fast = self.find_next_number(fast)
            fast = self.find_next_number(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False
