def find_prefix(arr: list):
    prefix = [] + arr
    for i in range(1, len(arr)):
        prefix[i] = prefix[i] * prefix[i - 1]
    return prefix


def find_postfix(arr: list):
    postfix = [] + arr

    for i in range(len(arr) - 2, -1, -1):
        postfix[i] = postfix[i] * postfix[i + 1]

    return postfix


class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        prefix = find_prefix(arr)
        postfix = find_postfix(arr)

        ans = [] + arr
        for i in range(len(arr)):
            if i == 0:
                left = 1
            else:
                left = prefix[i - 1]
            if i == len(arr) - 1:
                right = 1
            else:
                right = postfix[i + 1]

            ans[i] = left * right

        return ans
