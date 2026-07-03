DIGIT_TO_LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        def cross(curr_index, strs: list, ans=""):
            if curr_index == len(strs):
                result.append(ans)
                return
            for ch in strs[curr_index]:
                cross(curr_index + 1, strs, ans + ch)

        def gen(digits: str):
            res_strs = []
            for digit in digits:
                res_strs.append(DIGIT_TO_LETTERS[digit])
            cross(0, res_strs)

        gen(digits)
        return result
