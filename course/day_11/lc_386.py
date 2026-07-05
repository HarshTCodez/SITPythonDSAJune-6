class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def generate(n: int, current_number: int):
            if current_number > n:
                return

            res.append(current_number)
            for i in range(10):
                generate(n, current_number * 10 + i)

        for i in range(1, 10):
            generate(n, i)
        return res
