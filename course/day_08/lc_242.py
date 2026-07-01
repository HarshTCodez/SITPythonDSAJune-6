# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         freq1 = get_freq_arr(s)
#         freq2 = get_freq_arr(t)
#
#         if freq1 == freq2:
#             return True
#         else:
#             return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res = [0] * 26

        for ch in s:
            current_number = ord(ch) - ord("a")
            res[current_number] += 1

        for ch in t:
            current_number = ord(ch) - ord("a")
            if res[current_number] == 0:
                return False
            res[current_number] -= 1
        return True
