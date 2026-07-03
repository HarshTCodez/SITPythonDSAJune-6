class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen(n: int, open_count: int, close_count: int, ans=""):
            if close_count > open_count:
                return
            if open_count > n:
                return
            if open_count == close_count == n:
                res.append(ans)
                return
            gen(n, open_count + 1, close_count, ans + "(")
            gen(n, open_count, close_count + 1, ans + ")")

        gen(n, 0, 0)
        return res
