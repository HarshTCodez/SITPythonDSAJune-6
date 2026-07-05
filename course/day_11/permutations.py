class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        res = []
        path = []
        visited = [False] * n

        def generate(index: int):
            if index == n:
                res.append(path.copy())
                pass
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(arr[i])
                    generate(index + 1)
                    # backtracking
                    visited[i] = False
                    path.pop()

        generate(0)
        return res
