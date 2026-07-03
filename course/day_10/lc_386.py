def gen(n: int, k: int = 0, res=[]):
    if k > n:
        return

    res.append(k)
    for i in range(10):
        gen(n, k * 10 + i, res)


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            gen(n, i, res)
        return res
