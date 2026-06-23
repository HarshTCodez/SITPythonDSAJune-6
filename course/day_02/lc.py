def next_number(n):
    ans = 0

    while n > 0:
        curr_digit = n % 10
        ans += curr_digit * curr_digit
        n = n // 10

    return ans


class Solution:

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = next_number(slow)
            fast = next_number(fast)
            fast = next_number(fast)
            print(f"slow={slow}")
            print(f"fast={fast}")
            if slow == fast:
                break
        if slow == 1:
            return True
        return False
